a = str(input("Введите фамилию, имя и отчество: "))
fio = a.split()
a = fio[0] + " " + fio[0][0] + "." + fio[1][0] + "."
print ( a )
