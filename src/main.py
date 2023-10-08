import mingus.core.notes as notes
import mingus.core.scales as scales
import mingus.core.keys as keys 
import mingus.midi as midi
import time
from mingus.containers import Note
from mingus.containers import NoteContainer
from mingus.midi import fluidsynth
from mingus.midi import pyfluidsynth


if __name__ == "__main__":
    c = Note("C")
    c.velocity =100
    c.channel =5
    fluidsynth.init("My_flutes_and_My_voice.sf2")   
    fluidsynth.play_NoteContainer(NoteContainer(['C', 'E', 'G']))
    time.sleep(10)