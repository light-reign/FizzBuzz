def output_list(my_list):
    for item in my_list:
        print item,

def fizz_buzz(fizz, buzz, num_list):
    result = []
    for num in num_list:
        output = ''
        should_fizz = (num % fizz == 0)
        should_buzz = (num % buzz == 0)
        if should_fizz:
            output += "Fizz"

        if should_buzz:
            output += "Buzz"

        if not should_fizz and not should_buzz:
            output = num

        result.append(output)
        
    return result

output_list(fizz_buzz(3, 5, range(0,101)))
