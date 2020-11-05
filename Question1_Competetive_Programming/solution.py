def F(n):
    count = 0
    for i in range(2,n):
        for j in range(2,n):
            if  i < pow(j,3):
                break
            for k in range(2,n):
                if i == pow(j,2) * pow(k,3):
                    count = count + 1
                if  i < pow(j,2) * pow(k,3):
                    break
    return count
n = input("Enter n: ")
print(F(int(n)))
