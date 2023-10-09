from note import Note
import random
from typing import List
class Melody:
    
    def __init__(self,*args) -> None:
        self.allNotes = {"C","D","E","F","G","A","B","C#","D#","F#","G#","A#","Bb","Db","Eb","Gb","Ab","pause"}
        self.elite = False
        if isinstance(args[0],int):
            bars = args[0]
            self.bars = bars
            #$ 2SECOND: 4beats: 1 Bar
            #$ 120bpm: 0.5sec
            #! ^ May Change How Duration Work ^
            
            arrangements = []
            totalBeats = bars*4
            while(totalBeats>0):
                endpoint = 4 if totalBeats >3 else totalBeats
                #Create note
                duration = random.randint(1,endpoint)
                note_string = random.choice(tuple(self.allNotes))
                octave = random.randint(4,5)
                #append note
                arrangements.append(Note(note_string,duration,octave))
                totalBeats = totalBeats - duration
            self.arrangement = arrangements
        else:
            arrangement = args[0]
            self.bars = sum(note.getDuration() for note in arrangement)/4
            self.arrangement = arrangement


    def __str__(self):
        return f"Melody:\n"+"\n".join(map(str,self.arrangement))
    def getLengthOfArrangement(self):
        return len(self.arrangement)
    def getTotalBeats(self):
        return self.bars*4
    def getBars(self):
        return self.bars
    def getMelody(self) ->List[Note]:
        return self.arrangement
    def setMelody(self,arrangement):
        self.arrangement = arrangement
    def setElite(self,bool):
        self.elite = bool
    def changeRandomNote(self,mutation_rate):
        for count,note in enumerate(self.arrangement):
            if(random.random() < mutation_rate):
                if( 0.6 > random.random() > 0.0):
                    #$PTICH
                    note.changePitch(random.choice(tuple(self.allNotes)))
                elif(0.9 > random.random() > 0.6 ):
                    #$DURATION
                    note.changeDuration()
                else:
                    
                    duration = random.randint(1,4)
                    note_string = random.choice(tuple(self.allNotes))
                    octave = random.randint(4,5)
                #append note
                    self.arrangement.insert(count,Note(note_string,duration,octave))
        
