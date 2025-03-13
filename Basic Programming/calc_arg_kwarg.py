def calculate_numbers(*args, **kwargs):
    if not args:
        return "No number provided!"
    
    operation = kwargs.get('operation', 'add')
    if operation == 'add':
        return sum(args)
    elif operation == 'subtract':
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    elif operation == 'multiply':
        result = 1
        for num in args:
            result *= num
        return result
    elif operation == 'divide':
        result = args[0]
        for num in args[1:]:
            result /= num
        return result
    elif operation == 'average':
        return (sum(args)/len(args))


print(calculate_numbers(4, 5, 6 , 4,
                        operation = 'average'))