data=[8,50,6,48,23]

for i in range(5):
    t=data[i]
    for j in range(i-1, 0, -1):
        if data[j]>t:
            data[j+1]=data[j]
            data[j]=t
        else:
            data[j+1]=t
print(data)