def F(n):
    count = 0
    step = 0
    m = n
    for i in range(0,51,25):
        for j in range(0,21):
            if(i == 0 and j == 0):
                continue
            for k in range(1,4):
                if  (m - k*j) < 0 or (m - i)<0:
                    continue
                else:   
                    if i == 0:
                        m = m - k*j
                    elif j == 0:
                        m = m - i
          
                    step = step + 1
                    if step > 11:
                        m = n
                        step = 0
                    if m == 0:
                        m = n
                        count = count + 1
                
    return count
    
n = input("Enter n:")
print(F(int(n)))




