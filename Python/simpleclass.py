class Dog:
    # Class attributes defined outside def just below the first line, is used to define attributes /
    # that have the same value for every instance
    species = "Canis familiaris"

    # Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # Another Instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)
