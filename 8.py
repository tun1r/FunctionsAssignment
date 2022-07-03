#Find the output for these lines of code:
def Changelist():
    L = []
    L1 = []
    L2 = []
    for i in range(1,10):
        L.append(i)
    for i in range(10,1,-2):
        L1.append(i)
    for i in range(len(L1)):
        L2.append(L1[i] + L[i])
    L2.append(len(L) - len(L1))
    print(len(L))
    print(len(L1))
    print(L2)
Changelist()


'''Output:
9
5
[11, 10, 9, 8, 7, 4]
```
