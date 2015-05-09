def fizz_buzz(num_list):
    result = []
    for num in num_list:
        output = ''
        fizz = (num % 3 == 0)
        buzz = (num % 5 == 0)
        if fizz:
            output += "Fizz"

        if buzz:
            output += "Buzz"

        if not fizz and not buzz:
            output = num

        result.append(output)
        
    return result

print fizz_buzz(range(0,101))
