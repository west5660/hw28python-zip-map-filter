
student = ['Ivanov','Petrov', 'Smith']
mark = [5,4,3]
pet = ['cat','cat','turtle']

# student.remove('Petrov')
for i in range(len(student)):
    print(student[i], '--', mark[i])

newzip = zip(student,mark,pet)                                 #скрепили 3 списка в один
newzip  = list(newzip)                                         # преобразовали в список
print(newzip)
newzip.pop(1)                                                  #удалили одного человека
print(newzip)

newstudent, newmark, newpet = zip(*newzip)                     # разделили зип обратно на 3 новых саиска
print(newstudent, newmark,newpet)

# zip  скрепляет списки в один
# map применяет к списку функцию и получает новый список
# filter фильтруеет список через функцию и создает новый список


pets = [('cat','lion'), ('dog','fox'), ('turtle',['don','raf','mike','leo'])]
print(pets[2][1][0])

nums = [1,2,3,4,5]
nums3 = []
def f1():
    for i in nums:
        nums3.append(i*3)
f1()
print(nums3)
print('################################')
nums = [1,2,3,4,5]
nums3 = []
def f2(i):
    return i*3
for i in nums:
    res=f2(i)
    nums3.append(i*3)
print(nums3)
print('################################')
nums3 = list(map(f2,nums))
print(nums3)

a = [2,4,6,8]
b = []
def f3(i):
    return i+100
for i in a:
    res=f3(i)
    b.append(i+100)
print(b)

auto = ['bmw','vaz','zil','zaz','kamaz']
ear = [2005,1990,2022,1989,2014]
number = ['qw34','bg456','gb567','fv456','cd123']
c = zip(auto,ear,number)
for auto1,ear1,number1 in c:
    print(auto1,'--',ear1,'--',number1)

# print(*c, sep='\n')
nums11 = [15,22,33,5]

def f11(i):
    # if i%5==0:
        return i%5==0
newnums11 = list(filter(f11,nums11))
print(newnums11)