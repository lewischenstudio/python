# Variables and Mememory
import sys
import ctypes
import gc
# gc is the garbage collector

class Variable():

    def __init__(self, myvar):
        self.myvar = myvar

    @property
    def myvar(self):
        return self._myvar

    @myvar.setter
    def myvar(self, myvar):
        self._myvar = myvar
    
    def id(self):
        # id is the memory address of myvar stored in the memory
        return id(self.myvar)

    def hex(self):
        # hex is the hex version of id
        return hex(id(self.myvar))

    def getrefcount(self):
        # passing myvar to getrefcount() creates an extra reference
        return sys.getrefcount(self.myvar)

    def ctypescount(self):
        # we just pass the memory address an integer -- not a reference --
        # which does not affect the reference count
        return ctypes.c_long.from_address(id(self.myvar)).value

    def type(self):
        return type(self.myvar)
        
    def ismutable(self):
        if type(self.myvar) == list or type(self.myvar) == set or type(self.myvar) == dict:
            return True
        else:
            return False

    def append(self, newvar):
        if type(self.myvar) == list:
            try:
                new_list = self.myvar
                new_list.append(newvar)
                self.myvar = new_list
                return self.myvar
            except Exception as e:
                raise ValueError('Error -- %s' % e.args)
        elif type(self.myvar) == dict:
            if type(newvar) == dict:
                try:
                    new_dict = self.myvar
                    key_list = []
                    val_list = []
                    for key in newvar.keys():
                        key_list.append(key)
                    for val in newvar.values():
                        val_list.append(val)
                    for index in range(len(key_list)):
                        new_dict[key_list[index]] = val_list[index]
                    self.myvar = new_dict
                    return self.myvar
                except Exception as e:
                    raise ValueError('Error -- %s' % e.args)
            else:
                raise ValueError('Input must be type %s' % type(self.myvar))
        elif type(self.myvar) == set:
            try:
                new_set = self.myvar
                new_set.add(newvar)
                self.myvar = new_set
                return self.myvar
            except Exception as e:
                    raise ValueError('Error -- %s' % e.args)
        else:
            raise ValueError('%s is immutable' % type(self.myvar))
    
    def __str__(self):
        return '%s' % self.myvar
    
    def __repr__(self):
        return 'Variable {0} with type {1}'.format(self.myvar, type(self.myvar))

    ## For Garbage Collector, don't use it unless absolutely necessary required to debug
    def ref_count(myvar):
        return ctypes.c_long.from_address(myvar).value


    def object_by_id(myvar):
        for obj in gc.get_objects():
            if id(obj) == myvar:
                return "Object exists"
        return "Not Found"

class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b: {1}'.format(hex(id(self)), hex(id(self.b))))

class B:
    def __init__(self, a):
        self.a = a
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))



if __name__ == "__main__":
    from variable import Variable
    Variable("hello")