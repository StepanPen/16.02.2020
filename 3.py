inp = input('Введите строку:')
fnd = input('Введите символ:')

i = 0
cnt = 0

while(True):
    i = inp.find(fnd, i)
    if i == -1 or i == (len(inp)-1):
        if i == (len(inp)-1):
            cnt +=1
            break
        else:
            break
    else:
        cnt += 1
        i = inp.find(fnd, i+1)
print('В строке было найдено:', format(cnt), 'символа')