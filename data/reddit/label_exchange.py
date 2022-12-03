import numpy as np
import pickle
import random

path = 'reddit_labels.txt'
result = 'reddit_label.txt'
label = []
for i in range(0,50000):
    label.append(0)
maxi = 0
with open(path,'r') as f:
    for i in f:
        x,y = i.strip().split(" ")
        maxi = max(maxi,int(x))
        if label[int(x)] == 0 :
            label[int(x)] = int(y)
f.close()
with open(result,'w') as output:
    for i in range(0,maxi+1):
        #for j in label[i]:
        output.write(str(i)+" "+str(label[i])+"\n")
output.close()
