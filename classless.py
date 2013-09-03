import itertools
import inspect
from types import MethodType

########
def _make_free_args(f, init_attrs):
    '''
    Takes a function and a list of the instance attributes (as strings.)

    Returns a function intended to be turned into a method on the new
    class. The method will access all of its arguments that it took as
    a parameter in its prior life as a function from self, assuming
    the attributes are in init_args.
    '''
    f_args = inspect.getargs(f.func_code)
    
    def func(self, *args, **kwargs):
        print 'Inside func'
        my_kwargs = {}
        for attr in init_attrs:
            my_kwargs[attr] = getattr(self, attr)
        
        leftover_args = _compute_leftover_args(f_args.args, args, my_kwargs)
        print 'f_args: {}'.format(f_args)
        print 'args: {}'.format(args)
        print 'my_kwargs: {}'.format(my_kwargs)
        print 'leftover_args: {}'.format(leftover_args)
        print 'kwargs:  {}'.format(kwargs)
        kw_from_positional_args = dict(zip(leftover_args, args))
        print 'kw_from_positional_args: {}'.format(kw_from_positional_args)
        if set(my_kwargs.keys()) & set(kwargs.keys()) != set([]):
            raise('Cannot override instance variables')
        my_kwargs.update(kwargs)
        my_kwargs.update(kw_from_positional_args)

        # Remove args in my_kwargs that are not in f_args.args
        for k,v in my_kwargs.copy().iteritems():
            if not k in f_args.args:
                my_kwargs.pop(k)
        print 'Final my_kwargs: {}'.format(my_kwargs)
        return f(**my_kwargs)
    func.func_name = f.func_name
    return func

def _compute_leftover_args(func_args, args, my_kwargs):
    #return func_args[len(my_kwargs) + len(args) :]
    func_args_set = set(func_args)
    print 'func_args_set {}'.format(set(func_args))
    my_kwargs_keys_set = set(my_kwargs.keys())
    print 'my_kwargs_keys_set {}'.format(set(my_kwargs.keys()))
    leftover_args_set = func_args_set - my_kwargs_keys_set
    # set loses the order, this way we make sure the leftover
    # args are in the same order as the original func_args
    return [x for x in func_args if x in leftover_args_set]
    

def gen_class(methods, init_attrs, class_name='Generated Class'):
    new_methods = [_make_free_args(f, init_attrs) for f in methods]

    def __init__(*args, **kwargs):
        len_args = len(args)
        len_kwargs = len(kwargs)
        len_init_attrs = len(init_attrs)
        if len_args + len_kwargs != len_init_attrs:
            raise TypeError("__init__() takes exactly {} arguments ({} given)".format(
                len_init_attrs + 1,
                len_args + len_kwargs + 1))
        else:
            obj = type(class_name, (object,), {})
            leftover_args = init_attrs[len(args):]
            #print 'Init leftover arguments:'
            #print leftover_args
            if set(leftover_args) != set(kwargs):
                wrong_arguments = set(kwargs) - set(leftover_args)
                dic = dict(zip(wrong_arguments,
                                            itertools.cycle([0])))
                bad_key = iter(dic).next()
                raise TypeError("__init__() got an unexpected keyword "
                                "argument '{}'".format(
                                    bad_key))
            for attr, arg in zip(init_attrs, args):
                setattr(obj, attr, arg)
            for k,v in kwargs.iteritems():
                setattr(obj, k, v)
            _attach_methods(obj, new_methods, class_name)
        return obj
        
    return __init__

def _attach_methods(obj, methods, class_name):
    for method in methods:
        setattr(obj, method.func_name, MethodType(method, obj, class_name))
