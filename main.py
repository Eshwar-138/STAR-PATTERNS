import time
n=5
for i in range(n):
    for j in range(i+1):
        time.sleep(0.78)
        print("*",end=" ")
    print()
