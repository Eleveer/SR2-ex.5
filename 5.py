n = int(input('Введите n: '))
for x in range(1,n+1):
    if x == 1:
        print('1'*n, end ='\n')
    if x>1:
        print('1','0'*(n-2),'1',sep='', end = '\n')
    if x == n:
        print('1'*n)
a = int(input('Какой столбец вас интересует? - '))
if a == 1:
    print(n)
if a > 1 and a!=n:
    print('2')
if a == n:
    print(n)
        
