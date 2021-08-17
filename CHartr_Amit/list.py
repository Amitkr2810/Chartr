stand=[]
for i in range(20):
    stand.append(i)
    if len(stand)==4:
        print('---------')
        print(stand)
        
temp = str(stand)
print(temp)
print(type(temp))