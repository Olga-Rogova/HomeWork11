def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = 45.32, 'Papka', False
values_dict = {'a':231, 'b':'Maska', 'c':666}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = 55, 'Lampa'

print_params(*values_list_2, 42)