import mingus.containers as ms
import random

class Note:
    def __init__(self,noteString: str,duration: int,octave: int)-> None:
        self.noteString = noteString
        self.ocatave=octave
        if noteString == "pause" :
            self.notereturn = noteString
            self.hasNoteObject = False
            self.hasRest = True
        else:
            self.noteObject = ms.Note(noteString,octave)
            self.hasNoteObject = True
            self.hasRest = False
            self.notereturn = self.formatReturnNote()
        
        self.duration = duration


    def __str__(self):
        return f"{self.notereturn} duration: {self.duration} beats" 
    def getDuration(self):
        return self.duration
    def getOctave(self):
        if(self.hasNoteObject):
            return self.noteObject.octave
        return 0
    def changePitch(self,noteString):
        if(noteString == "pause"):
            self.noteObject = None
            self.hasNoteObject = False
            self.noteReturn = noteString
        else:
            self.hasNoteObject = True
            self.noteObject = ms.Note(noteString,random.randint(4,5)) 
        self.notereturn = self.formatReturnNote()
    def getNote(self):
        return self.notereturn
    def changeDuration(self):
        self.duration = random.randint(1,4)
    def getNoteNoOctave(self):
        if(self.hasNoteObject):
            return self.noteObject.name
        return self.noteString
    def formatReturnNote(self):
        if(self.hasNoteObject):
            note_string_pre_format = list(self.noteObject.name)
            if(len(note_string_pre_format) > 1):
                note_string_post_format = note_string_pre_format[0] +str(self.noteObject.octave) + note_string_pre_format[1]
            else:
                note_string_post_format =note_string_pre_format[0] +str(self.noteObject.octave)
            return note_string_post_format
        else:
            return self.noteString
