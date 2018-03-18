import random
import csv
import os.path as path

datasets_num = 5
datasets_size = 1000

if path.exists('datasets.csv'):
    path.remove('datasets.csv')

with open('datasets.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    outfile.write("A,B,C,D,E\n")
    for col in range(datasets_size):
        rlist = [random.randint(1,1000) for col in range(datasets_num)]
        values = ",".join(str(i) for i in rlist)
        outfile.write(values + "\n")