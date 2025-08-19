#Loops
#1. For Loop
for i in range(1,10):#Excludes 10
    print(i)
for i in range(1,20,2):# 1 -> start 20 -> end 2 -> step-size
    print(i)
#2.While loop
i=0
while(i<10):
    print(i)
    i+=1
#3. Nested loops
for i in range(1,5):
    for j in range(1,5):
        print(i,j)
i=0
j=0
while(i<5 and j<5):
    print(i,j)
    i+=1
    j+=1
#4. Loop Control Statements break continue pass
#1. Break
for i in range(1,10):
    if(i==5):
        break # Exits loop after 5
    print(i)
#2. Continue
for i in range(1,10):
    if(i==5):
        continue # Skips 5 and continues till the loop terminates
    print(i)
#5. Enumerate
#1. Enumerate
fruits=['apple','banana','cherry']
for i,fruit in enumerate(fruits):
    print(i,fruit)
#6. Zip
fruits=['apple','banana','cherry']
colors=['red','yellow','pink']
for fruit,color in zip(fruits,colors):
    print(fruit,color)
