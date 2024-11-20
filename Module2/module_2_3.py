my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while index < len(my_list):
     elem = my_list[index]
     index += 1
     if elem == 0:
          continue
     elif elem < 0:
          break
     else:
          print(elem)







