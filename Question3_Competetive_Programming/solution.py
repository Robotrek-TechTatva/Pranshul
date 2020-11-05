import pandas as pd 

def F(n):
    data = pd.read_csv(n)
    data = data.to_numpy()[:,1:]
    count = 0
    for i in range(0,data.shape[0]):
        area = (data[i,0]*(data[i,3] - data[i,5]) + data[i,2]*(data[i,5] - data[i,1]) + data[i,4]*(data[i,1] - data[i,3]))/2
        area1 = (data[i,2]*(data[i,5] ) + data[i,4]*(0-data[i,3]))/2
        area2 = (data[i,0]*(0 - data[i,5]) + data[i,4]*(data[i,1] - 0))/2
        area3 = (data[i,0]*(data[i,3]) + data[i,2]*(0 - data[i,1]) )/2
        if area == area1 + area2 + area3:
            count = count + 1
    return count
n = input("Enter Location of the csv file:")
print(F(n))
