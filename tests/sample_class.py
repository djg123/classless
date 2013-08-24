class Klass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def different_arguments(self,a,b,c,d):
        return a * b * c * d

    def no_arguments(self):
        return 27

    def times_3(self):
        return self.x * 3
    
    def plus_2(self):
        return self.x + 2
    
    def times(self):
        return self.x * self.y
    
    def plus(self):
        return self.x + self.y
    
    def comma_string(self,z):
        return '{},{},{}'.format(self.x,self.y,z)
    
    def a_is_b(self, z):
        return 'x is {}, y is {}, z is {}'.format(
            self.x, self.y, z)
    
    def second_instance_arg_only(self):
        return self.y * 100
    
    def second_instance_arg_and_extras(self, a,d):
        return {'a': a,
                'y': self.y,
                'd': d}
