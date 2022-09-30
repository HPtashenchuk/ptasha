import random

rnlist =[]
while True:
    try:
        qnumber =int(input("Введіть розігрувану кількість чисел: "))
        maxnumber=int(input("Введіть максимальне розігруване число: "))
        if qnumber>maxnumber:
            print("Ви ввели некоректне число, повторіть введення.")
            continue #пропуск
        if qnumber < 1 or maxnumber < 1:
            print("Ви ввели некоректне число, повторіть введення.")
            continue 
        break
    except ValueError:
        print("Ви ввели некоректне число, повторіть введення: ")
  

i=0

while i < qnumber:
    rnumber=random.randint(1,maxnumber)
    if rnlist.count(rnumber)==0:
      rnlist.append(rnumber)
      i=i+1

pnumber=[]
s=0
while s<qnumber:
    print("Спроба №", s+1)
    
    while True:
        try:
            savenumber=int(input("Введіть числo: "))
            break
        except ValueError:
            print("Ви ввели некоректне число, повторіть введення: ")

    if pnumber.count(savenumber)==0 and 0<savenumber<maxnumber+1:
        pnumber.append(savenumber)
        s=s+1
      
#print(pnumber)
rnlist.sort()
pnumber.sort()
correct_number = set(rnlist) & set(pnumber)
print ("Розігруванні числа:", rnlist)
if correct_number:
    print("Числа які співпали:", correct_number)
    print("Кількість співпадінь:", len(correct_number))
else:
    print("Нажаль, Ви не вгадали. Пощастить наступного разу.")
