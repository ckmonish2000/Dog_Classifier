import torch
from os import listdir
import classifier
path='pet_images/'


# print(listdir(path))
with open('dognames.txt','r') as f:
    file=f.read()
    dognames=file.split()  
# print(dognames)

model='vgg'
files=listdir(path)

for i in files:
    result=classifier(f'{path}i',model)
    print(f"the result for {i} is {result}")











