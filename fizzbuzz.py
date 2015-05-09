def fizz_buzz(param_dict, num_list):
    # param in format 'Fizz' : lambda bool function
    result = []
    for num in num_list:
        output = ''
        for key in param_dict:
            if param_dict[key](num):
                output += key
        if output == '':
            output = num

        result.append(output)
    return result

params = {
            'Fizz' : (lambda i: (i % 3) == 0)
            , 'Buzz' : (lambda i: (i % 5) == 0)
            , 'Zazz' : (lambda i: (i < 10))
         }

for value in fizz_buzz(params, range(1, 101)):
    print value,
