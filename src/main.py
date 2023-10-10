import mingus.core.notes as notes
import mingus.core.scales as scales
import mingus.core.keys as keys 
import mingus.midi as midi
import time
from mingus.containers import Note
from mingus.containers import NoteContainer
import musicalbeeps
from note import Note
import mga
from typing import List
from melody import Melody
import midiutil as mu

def playMelody(melody:Melody):
    player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)
    for note in melody.getMelody():
        player.play_note(note.getNote(), note.getDuration()*0.25)

def exportMidi(melody:Melody,index:int):
    midi = mu.MIDIFile(1)
    track    = 0
    channel  = 0
    time     = 0   # In beats
    tempo    = 120  # In BPM
    volume   = 100
    midi.addTempo(track,time, tempo)

    for note in melody.getMelody():
        if(note.getNote() != "pause"):
            midi.addNote(track, channel, note.getMidi(), time, note.getDuration(), volume)
        time = time + note.getDuration()

    with open(f"midi_exports/evolved_melody{index}.mid", "wb") as output_file:
        midi.writeFile(output_file)

    return

if __name__ == "__main__":
    for i in range(10):
        evolvedMelody = mga.evolve(scale_used = "aeolian",indy=i,barCount=8)
    # playMelody(melody=evolvedMelody)
        exportMidi(melody=evolvedMelody,index=i)

    
    
        
    
    