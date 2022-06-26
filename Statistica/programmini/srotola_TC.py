print("welcom mettere lanci")
a = input()
arrayIniz =[]
temp = []
t = 'T'
c = 'C'
a = int(a)
for el in range(a):
    arrayIniz.append(t)
for i in range(a):
    temp = arrayIniz
    for g in range(1,a):
        temp[a-g] = c
        print(temp)
