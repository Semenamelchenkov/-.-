immutable_var=tuple([1,2,3,4,5])
print(immutable_var)
immutable_var[0]=1
Ошибка 'tuple' object does not support item assignment появляется поскольку элементы кортежа не могут быть изменены
mutable_list=[1,2,3,4,5]
print(mutable_list)
mutable_list.append('number')
print(mutable_list)
