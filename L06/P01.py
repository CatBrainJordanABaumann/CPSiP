def strip_string(b_function):
    def wrapper():
        func = b_function()
        strip_string = func.strip('-')
        return strip_string
    return wrapper

def uppercase_decorator(some_function):
    def a_wrapper():
        func = some_function()
        make_uppercase = func.upper()
        return make_uppercase
    return a_wrapper

@strip_string
@uppercase_decorator
def clli_code():
    print('The Florida router clli ode is', end = '')
    return '---tpaflxacg19'

print(clli_code())