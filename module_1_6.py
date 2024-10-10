my_dict = {'Max': 1997, 'Anna': 2012, 'Alex': 1987}
print(my_dict)
print(my_dict['Anna'])
print(my_dict.get('Sasha'))
my_dict.update({'Peter': 2018, 'Mike': 1993})
print(my_dict)
a = my_dict.pop('Alex')
print(my_dict)
print(a)
#множества
my_set = {2022, 2023, 'Python', 2022, (2+3)}
print(my_set)
my_set.update({2024, 'pycharm'})
print(my_set)
my_set.discard((2+3))
print(my_set)