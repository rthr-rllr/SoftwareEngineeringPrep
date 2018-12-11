
# create an object which does not accept
# new attribute definitions outside __init__

#%%

class OnlyOneAttribute:
  
  def __init__(self, a):
    # cannot write self.a = a because of __setattr__
    self.__dict__['a'] = a
  
  def __setattr__(self, attribute, value):
    if not attribute in self.__dict__:
        raise ValueError('cannot set attribute {}'.format(attribute))
    else:
        self.__dict__[attribute] = value
        
        
foo = OnlyOneAttribute(2)
print(foo.__dict__)

foo.a = 3
print(foo.__dict__)

foo.b = 'no way'
print(foo.__dict__)