def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    return inner_function()

inner_function() #Вызов функци выдает ошибку
# мы не можем доставать значения
# внутри функции

test_function()