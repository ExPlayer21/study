a = str(input("Введите натуральное число: "))
for i in range(len(a)):    
    for n in range(i ++ 1, len(a)):
        if a[i] == a[n]:
            print('да')
            exit()        
print('нет')