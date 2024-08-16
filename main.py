import time
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(n,0,-1):
    for j in range(i):
        time.sleep(0.6)
        print(i,end=" ")
    print()