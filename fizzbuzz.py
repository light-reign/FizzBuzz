def fizz_buzz(params, num):
    # params is a list of rule dictionaries Ex. params[0] = {'Fizz' : lambda bool function}
    output = ''
    for order in params:
        for rule in order:
            if order[rule](num):
                output += rule
    if (output == ''):
        output = num

    return output

params = [{'Fizz' : (lambda i: (i % 3) == 0)}
        , {'Buzz' : (lambda i: (i % 5) == 0)}
        , {'Zazz' : (lambda i: (i < 10))}
        ]

for num in range(1, 21):
    print fizz_buzz_v2(params, num)
