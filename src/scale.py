import musical_scales as ms
import random
from melody import Melody
from typing import List
class Scales:

    def __init__(self)->None:
        return
    def getScale(self,scale:str,note:str):
        # print(f"{note} <----")
        scale_temp = str(ms.scale(note,scale))
        # print(scale_temp)
        scale_final = ''.join([i for i in scale_temp if not i.isdigit()]).replace(",","").removeprefix("[").removesuffix("]")
        scale_final =scale_final.split()
        # print(str(scale_final))
        return scale_final
