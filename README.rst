Classless
=============

Get all the benefits of making your functions methods on a class
without actually having define them methods on a class! 

**Classless** allows you, instead,
to pass a list of functions to `gen_class`
and curry them on the specified attributes.

Example:

```
from classless import gen_class

def fun_stuff(db, name, x):
    q = db.get(name)
    return int(q) + x

def cool_stuff(q, z, name, y, db):
    db.insert(name, (q, z, y))

def awesome_adventure(w, name):
    if w > 5:
        return name
    else:
        raise Exception("I don't approve of the name {}".format(name))


MyPretendClass = gen_class(methods=(fun_stuff,
                                    cool_stuff,
				    awesome_adventure),
		           init_attrs=['db', 'name'])

```
and then we use ```MyPretendClass``` just like any regular class:

```
obj = MyPretendClass(name='NiceName', db=some_connection)
obj.awesome_adventure(25) # Calls awesome_adventure with name='NiceName'
                          # and w=25

obj.cool_stuff(1,2,3) # == cool_stuff(1, 2, 'NiceName', 3, some_connection

    
obj.fun_stuff('Dr. X') # == fun_stuff(x='Dr. X')
```
where ```obj``` just holds the list of ```methods``` curried on the ```init_attrs```.

We could have defined ```MyRealClass``` as so and get identical behaviour:

```
class MyRealClass(object):
    def __init__(self, db, name):
        self.db = db
	self.name = name

    def fun_stuff(x):
        q = self.db.get(self.name)
        return int(q) + x
    
    def cool_stuff(q, z, y):
        self.db.insert(self.name, (q, z, y))
    
    def awesome_adventure(w):
        if w > 5:
            return self.name
        else:
            raise Exception("I don't approve of the name {}".format(self.name))

```

But, then every one of those methods is tied down to a given class, and can't be used as regular functions, without first constructing ```MyRealClass```.


