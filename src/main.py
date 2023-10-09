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

if __name__ == "__main__":
    player = musicalbeeps.Player(volume = 0.3,
                            mute_output = False)
    
    melody = Melody(4)
    for note in melody.getMelody():
        player.play_note(note.getNote(), note.getDuration()*0.5)
        
    
    