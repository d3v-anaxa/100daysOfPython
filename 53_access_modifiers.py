class default:
    def __init__(self):
        self.public_variable = "public_variable"
        self._protected_variable = "_protected_variable"
        # Name mangling in Python is a technique used to protect class-private and superclass-private attributes from being accidentally overwritten by subclasses.
        self.__private_variable = "__private_variable"


object = default()
print(object.public_variable)
print(object._protected_variable)
print(object._default__private_variable)  # can be accessed like this
