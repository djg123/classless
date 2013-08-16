import inspect
from types import MethodType

########
def times_3(x):
    return x * 3

def plus_2(x):
    return x + 2

def times(x,y):
    return x * y

def plus(x,y):
    return x + y

def three(x,y,z):
    print '{},{},{}'.format(x,y,z)

def cows_eat_sheep(z,y,x):
    return 'x is {}, y is {}, z is {}'.format(x,y,z)

def try_something():
    Klass = gen_class(methods=(times_3, plus_2, times, plus, three,
                               cows_eat_sheep),
                      init_attrs=['x','y'])
    k = Klass(1,2)
    print k.plus()
    #print k.times()
    print k.three(z='hello')
    print k.cows_eat_sheep(z=2)

def make_free_args(f, init_attrs):
    f_args = inspect.getargs(f.func_code)
    
    def func(self, *args, **kwargs):
        my_kwargs = {}
        for attr in init_attrs:
            my_kwargs[attr] = getattr(self, attr)
        print len(args)
        leftover_args = compute_leftover_args(f_args.args, args, my_kwargs)
        print my_kwargs
        print leftover_args
        print kwargs
        kw_from_positional_args = dict(zip(leftover_args, args))
        if set(leftover_args) != set(kwargs.keys()):
            raise Exception('Wrong argument list')
        if set(my_kwargs.keys()) & set(kwargs.keys()) != set([]):
            raise('Cannot override instance variables')
        my_kwargs.update(kwargs)
        my_kwargs.update(kw_from_positional_args)
        return f(**my_kwargs)
    func.func_name = f.func_name
    return func

def compute_leftover_args(func_args, args, kwargs):
    #return func_args[len(my_kwargs) + len(args) :]
    return list(set(func_args) - set(kwargs.keys()))
    

def gen_class(methods, init_attrs, class_name='Generated Class'):
    new_methods = [make_free_args(f, init_attrs) for f in methods]

    def init(*args, **kwargs):
        if len(args) + len(kwargs) > len(init_attrs):
            raise Exception("Too many arguments")
        elif len(args) + len(kwargs) < len(init_attrs):
            raise Exception("Too few arguments")
        else:
            obj = type(class_name, (object,), {})
            leftover_args = init_attrs[len(args):]
            print 'Init leftover arguments:'
            print leftover_args
            if set(leftover_args) != set(kwargs):
                raise Exception("Wrong keyword arguments")
            for attr, arg in zip(init_attrs, args):
                setattr(obj, attr, arg)
            for k,v in kwargs.iteritems():
                setattr(obj, k, v)
            attach_methods(obj, new_methods, class_name)
        return obj
        
    return init

def attach_methods(obj, methods, class_name):
    for method in methods:
        setattr(obj, method.func_name, MethodType(method, obj, class_name))
