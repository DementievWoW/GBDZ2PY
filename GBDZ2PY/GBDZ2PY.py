##задание 1
#N = int(input('N: '))
#value = 1
#nums = []
#for i in range(1, N + 1):
#    nums.append(value)
#    value *= i + 1
#print(nums)
###задание 2
#tmp=0
#nums = [0,0,0]
#while True:
#    nums
#    tmp=(1-(nums.[0]*y))+z
#    print(tmp)
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
n = int(input())
a = input().split()
for _ in range(n):
    aa = []
    for i in range(len(a) - 1):
        aa.append(a[i + 1])
    aa.append(a[0])
    a = aa
print(a)
