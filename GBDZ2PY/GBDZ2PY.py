##задание 1
#N = int(input('N: '))
#value = 1
#nums = []
#for i in range(1, N + 1):
#    nums.append(value)
#    value *= i + 1
#print(nums)
####задание 2

##for x in range(0,2):
##    for y in range(0,2):
##        for z in range(0,2):
##            print(f'{x}|{y}|{z}|{not (x and y) or z}')

##задание 3
#count = 0
#a = str(input('1: '))
#b=str(input('2: '))
#def search_counter(search_string, searchme):
#    count = 0
#    for x in search_string:
#        for y in searchme:
#            if x == y:
#                count = count + 1
#    return count
#i=0
#while i<len(b):
#    tmp= search_counter(a,b[i])
#    print(tmp)
#    i+=1
#Задание 4
step=1
N= int(input('vvedite N: '))
listN=list(range(-N,N+1))
while step <=2:
    n=listN[-step:] + listN[:-step]
    print(n)
    step+=1

