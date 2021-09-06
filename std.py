import csv
import math

with open('data.csv', newline='') as f:
    reader= csv.reader(f)
    file_data= list(reader)

data= file_data[0]

def mean(data):
    total= 0
    n = len(data)
    for m in data:
        total+= int(m)
        mean=total/n 
        return mean

square=[]
for num in data:
    a= int(num)- mean(data)
    a= a**2
    square.append(a)

sum=0
for z in square:
    sum=sum+z

result=sum/(len(data)-1)
s=math.sqrt(result)
print(s)