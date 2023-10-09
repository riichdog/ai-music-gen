from note import Note
import musical_scales as scales
import random
from melody import Melody
from typing import List
from scale import Scales as ScaleMachine
import numpy as np
import musicalbeeps
import copy
scale_machine = ScaleMachine()
population=[]
BARS = 8
GENERATIONS = 500
POPULATION_SIZE =100
IND_MUTATION_RATE = 0.3

functionProbabilities = {"CROSSOVER" :0.7,
                        "MUTATION":0.5}
def calculateFitness(melody:Melody,scale:str):
    #! Punish Lack of variety in melody
    freq = [x.getNote() for x in melody.getMelody()]
    values, counts = np.unique(freq, return_counts=True)
    variety = len(counts) /(BARS*1.125) 
    #Punish no holds
    #Punish too many holds
    #Check for interesting swing?
    #$ SCALE CHECK
    for i in range(melody.getLengthOfArrangement()):
        rootNote = melody.getMelody()[i].getNoteNoOctave()
        if(rootNote!="pause"):
            break
    else:
        return 0
    # print(str(melody))
    scaleItems = scale_machine.getScale(scale,rootNote)
    rightNoteCount = 0
    for note in melody.getMelody():
        if(note.getNoteNoOctave() in scaleItems) or (note.getNoteNoOctave() =="pause"):
            rightNoteCount+=1
    noteRightPercentage = rightNoteCount/melody.getLengthOfArrangement()
    #$SIZE PUNISHMENT
    totalBeats = BARS * 4
    actualBeats = melody.getTotalBeats()
    differneceInBeats = abs(totalBeats-actualBeats)*5
    fitness = ((1*(noteRightPercentage**3))/(differneceInBeats+1))*variety
    # print(fitness)
    return fitness


allNotes= {"C","D","E","F","G","A","B","C#","D#","F#","G#","A#","Bb","Db","Eb","Gb","Ab"}

def generatePopulation(size: int,lengthOfMelody):
    population = []
    for index in range(size):
        melody = Melody(lengthOfMelody)
        population.append(melody)
    return population

def mutate(melody: Melody ):
    ram = copy.deepcopy(melody)
    if ram.elite:
        return ram
    ram.changeRandomNote(IND_MUTATION_RATE)

    return ram

def getRankedPopulation(population,scale):
    n = len(population)
    rankedFitness =[]
    rankedPopulation = []
    rank_sum = n * (n + 1) / 2
    for i in population:
        rankedFitness.append([i,calculateFitness(i,scale)])
    for rank, item in enumerate(sorted(rankedFitness,key=lambda x: x[1]),1):
        ranked = (float(rank)/rank_sum)
        rankedPopulation.append([item[0],item[1],ranked])

    # for i,x in enumerate(rankedPopulation,1):
    #     print(f"Melody {i}")
    #     print(f"Fitness: {x[1]}")
    #     print(f"Rank: {x[2]}\n")
        
    
    return rankedPopulation
def rankedSelection(population,scale)->List[Melody]:
    rankedList = getRankedPopulation(population,scale)
    pop = [x[0] for x in rankedList]
    p = [x[2] for x in rankedList]
    choices = (random.choices(population=pop,weights=p,k=2))
    
    return choices
#? HOW SHOULD I MAKE SURE THEY GRAB EVERYTHING
def crossover(melody1: Melody, melody2: Melody)->Melody:
    randomCrossoverPoint1 = random.randint(1,melody1.getLengthOfArrangement()-2)
    randomCrossoverPoint2 = random.randint(1,melody2.getLengthOfArrangement()-2)
    randomMelodyFrom1 = random.choices(population=melody1.arrangement,k=randomCrossoverPoint1)
    randomMelodyFrom2 = random.choices(population=melody2.arrangement,k=randomCrossoverPoint2)

    combinedMelody = randomMelodyFrom1 + randomMelodyFrom2
  
    random.shuffle(combinedMelody)
    melodyChild = Melody(combinedMelody)
    # print(f"\nMelody 1: {melody1}\n")
    # print(f"Melody 2: {melody2}\n")
    # print(f"Melody Child: {str(melodyChild)}\n")
    return melodyChild


if __name__ == "__main__":
    # mel =Melody(4)
    # print(mel)
    # print(calculateFitness(mel,"aeolian"))    
    #$GENERATE POPULATION
    population: List[Melody]= generatePopulation(POPULATION_SIZE ,BARS)
    scale_used = "aeolian"
    #$GENERATION LOOP
    bestMelody = None
    maxFitnessVal=0
    generation_i =0
    best_fitness =0
    while(best_fitness<0.9):
        generation_i += 1
    
    # for generation_i in range(GENERATIONS):
        #$ GET BEST
        population = sorted(population,reverse=True,key= lambda x: calculateFitness(x,scale_used))
        for count,mel in enumerate(population,0):
            if(count==0):
                mel.setElite(True)
                best_fitness = calculateFitness(mel,scale_used)
            else:
                mel.setElite(False)
        print(f"Generation: {generation_i} -- Best Fitness: {best_fitness}")

        #$ CROSSOVER
        choice = random.choices(population=list(functionProbabilities.keys()),weights=list(functionProbabilities.values()),k=1)[0]
        if(choice=="CROSSOVER"):
            print("CROSSOVER")
            parent1 = rankedSelection(population,scale_used)[0]
            parent2 = rankedSelection(population,scale_used)[1]
            fitness1 = calculateFitness(parent1,scale_used)
            fitness2 = calculateFitness(parent2,scale_used)
            child = crossover(parent1,parent2)
            # print(f"parent1: {fitness1} parent2: {fitness2} child fitness { calculateFitness(child,scale_used)}")
            population.append(child)

        #$ MUTATION        
        choice = random.choices(population=list(functionProbabilities.keys()),weights=list(functionProbabilities.values()),k=1)[0]
        if(choice =="MUTATION"):
            print("MUTATION")

            parent = rankedSelection(population,scale_used)[random.randint(0,1)]
            # while(parent.elite):
            #     parent = rankedSelection(population,scale_used)[random.randint(0,1)]
            if not parent.elite:
                # print(f" maxFit: {best_fitness} parent fitness: {calculateFitness(parent,scale_used)}")
                print("MUTATING")
                population.remove(parent)
                population.append(mutate(parent))
        
        #$ CREATE NEW POPULATION
        population = sorted(population,reverse=True,key= lambda x: calculateFitness(x,scale_used))
        newPop = []
        for count,mel in enumerate(population):
            if(count<POPULATION_SIZE):
                # print(f"{count} is ELITE: {mel.elite} parent fitness: {calculateFitness(mel,scale_used)}")
                newPop.append(mel)
        population = newPop

    bestMelody = population[0]
    print(f"BEST MELODY FITNESS {calculateFitness(bestMelody,scale_used)}")
    print(str(bestMelody))
    player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)
    
    
    for note in bestMelody.getMelody():
        player.play_note(note.getNote(), note.getDuration()*0.5)
        
    