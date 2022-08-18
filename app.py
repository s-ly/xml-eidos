import re

file_name = input('Введите имя файла: ')

list = []
# file = open("data.xml", "r") 
file = open(file_name, "r") 

for i in file:

    dop = ''    
    prob = 0
    tab = 0

    # В этом блоке вычисляем количество пробелов и табов в начале строки.
    for j in i:
        if j == ' ':
            prob = prob + 1
        elif j == '\t':
            tab = tab + 1
        else: break
    print(str(prob), str(tab))
    dop = ((' ') * prob) + (('\t') * tab)


    if len(i) >= 100:
        while True:
            substr = re.search(r'" \w', i)        
            if substr != None:
                s_str = substr.group()
                i = re.sub(s_str, s_str[0:1] + '\n' + dop + s_str[-1], i)
            else:
                break


    list.append(i)
file.close()

file = open(file_name, "w") 
file.writelines(list)
file.close()

# strip(): удаляет начальные и конечные пробелы из строки
# rstrip(): удаляет конечные пробелы из строки