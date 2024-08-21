immutable_var = 1, 2, 'true', 'string'
print("Незменяемый объект 'Кортеж':", immutable_var)
print(immutable_var)
print(immutable_var[0])
immutable_var[0] = 8 #кортеж не поддерживает обращение по элементам.



mutable_list = ['открой','глаза', 1 , 2]
print(mutable_list)
mutable_list[0] ='1'
mutable_list[1] = '2'
mutable_list[3] = 'peach'
print("Измененный Список:", mutable_list)

