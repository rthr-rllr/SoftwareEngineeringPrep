# OOP


- Attributes
	- static vs. non static: which is defined at the class level vs. proper to one instance; public vs. protected vs. private: accessible to outside world vs. accessible to the class only ([ref](https://stackoverflow.com/questions/1020749/what-are-public-private-and-protected-in-object-oriented-programming))
		- In `Python`, there is no actual implementation of this, instead use *managed attributes*: the [property](http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_classes/classes.html#proprietes) functionality, as examplified [here](https://www.smallsurething.com/private-methods-and-attributes-in-python/) and summarised in the code of this [question](https://stackoverflow.com/questions/4555932/public-or-private-attribute-in-python-what-is-the-best-way).
		- In `Python`, attributes can be added to objects at any moment by default (even if not present in `__init__`). A possible [workaround](https://stackoverflow.com/questions/3603502/prevent-creating-new-attributes-outside-init) is  to rewrite `__setattr__` so as to restrict it to `__dict__` defined in `__init__.

		

- Encapsulation – an object contains (encapsulates) both (1) data and (2) the relevant processing instructions, as we have seen. Once an object has been created, it can be reused in other programs.
- Inheritance – once you have created an object, you can use it as the foundation for similar objects that have the same behavior and characteristics.
- Polymorphism – generics, the presence of "many shapes." In object-oriented programming, polymorphism means that a message (generalized request) produces different results based on the object that it is sent to.

## Design Patterns Examples

### Creation

- Factory
- Builder
- Singleton

### Composition (Structural)

- Adapter
- Facade
- Decorator
- Proxy

### Behavioral

- Chain of responsibility
- Command
- Iterator
- Visitor
