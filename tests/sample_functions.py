def different_arguments(a,b,c,d):
    return a * b * c * d

def no_arguments():
    return 27

def times_3(x):
    return x * 3

def plus_2(x):
    return x + 2

def times(x,y):
    return x * y

def plus(x,y):
    return x + y

def comma_string(x,y,z):
    return '{},{},{}'.format(x,y,z)

def a_is_b(z,y,x):
    return 'x is {}, y is {}, z is {}'.format(x,y,z)

def second_instance_arg_only(y):
    return y * 100

def second_instance_arg_and_extras(a,y,d):
    return {'a': a,
            'y': y,
            'd': d}
