from fake_math import divide as f_divide
from true_math import divide as t_divide


result1 = f_divide(69, 3)
result2 = f_divide(3, 0)
result3 = t_divide(49, 7)
result4 = t_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
