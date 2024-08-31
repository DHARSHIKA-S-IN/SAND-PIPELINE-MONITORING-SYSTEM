import matplotlib.pyplot as plt 
import librosa.display
import numpy as np
import os
from matplotlib import pyplot as plt
import cv2
import random
import pickle


file_list = []
class_list = []
x = [] 
y = [] 
rt=0
i=0
DATADIR1 = "dataset"
DATADIR2 = "data"
# All the categories you want your neural network to detect
CATEGORIES=["FAULT","NORMAL"]

for category in CATEGORIES :
    path = os.path.join(DATADIR1, category)
    path2 = os.path.join(DATADIR2, category)
    for im in os.listdir(path):
        pyo=path+str("/")+im
        for line in open(pyo, 'r'):
            rt=rt+1
            lines = [i for i in line.split()]
            x.append(float(lines[0])) 
            y.append(float(lines[1]))
            if rt==200:
                rt=0
                print(len(y))

                import math
                import numpy as np
                import matplotlib.pyplot as plt

                Time_difference = 0.0001

                Time_Array = np.linspace(0, 5, math.ceil(5 / Time_difference))

                plt.specgram(y, Fs=10, cmap="rainbow")

                #plt.title("Spectrogram Using matplotlib.pyplot")
                #plt.xlabel("DATA")
                #plt.ylabel("TIME")
                i=i+1
                p=str(path2)+"/"+str(i)+"out.png"
                plt.savefig(p)
                x=[]
                y=[]
                #plt.show()

