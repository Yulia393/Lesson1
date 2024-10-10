immutable_var = (1, 2, "bear", True)
print(immutable_var)
#immutable_var [1] = 70
#print(immutable_var)
#Кортеж является неизменяемым обЪектом, поэтому значение элемента [1] не изменяется на 70.
mutable_list = ['head', 'eyes', 'nose', 'ears']
print(mutable_list)
mutable_list.append('legs')
print(mutable_list)
mutable_list.extend(['arms', 'back'])
print(mutable_list)
mutable_list.remove('nose')
print(mutable_list)