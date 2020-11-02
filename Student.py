class Person:
    def __init__(self, name, gender, dob):
        #intialize person attributes
        self._name = name       #a single _ implies the variable is private
        self._dob=dob
        self.__gender = gender  #a double __ means it can not be overwritten outside this class
        self._is_public = True 

    def setPrivate(self):
        self._is_public = False

    # The __ prefix results in an actual method name of _Person__getInfo
    # Thus, this method can not be overwritten in another class.
    # Attempting to do so would result in a method called _NewClass__getInfo
    def __getInfo(self):
        return  "Name: " + self._name + " DOB: " + self._dob + " Gender: " + self.__gender

    # getName can be called from any other class 
    def getName(self):
        return self._name

    # Only print all info when is_public is True    
    def __str__(self):
        if self._is_public:
            # This works because the call to __getInfo is in the same class
            # it actually returns self._Person__getInfo()
            return self.__getInfo() 
        else:
            return self.getName()

class Student(Person):
    def __init__(self, name, gender, dob, idnumber):
        Person.__init__(self, name, gender, dob) # calls parent's constructor 
        self._idnumber = idnumber  # add specialization
        
        #gender attribute is not needed, but it's here to shows you canNOT
        #  inadvertantly overwrite _Person__gender attribute, try it
        self.__gender = "x" 

    def __str__(self):
        if self._is_public:
            # return self.__getInfo() will return an error, try it
            return Person.__str__(self) + " Student ID #: " + str(self._idnumber)
        else:
            return self.getName()
    
def main():
    print("Creating two people... and using their behavior.")
    person1 = Person("Mary", "female", "03-06-1995")
    person2 = Person("Marvin","male","04-04-1994")
    print(person1)
    print("Setting info to private, and reprinting...")
    person1.setPrivate()
    print(person1)
    print(person2)
    # let's put the people in a list
    list_of_people = [person1,person2]
    
    print("\nCreating Students..., which are people")
    # add each Student to the list of people
    jane = Student("Jane", "female", "03-06-1999",1671)
    list_of_people.append(jane)
    
    jack = Student("Jack","male","02-02-1997",1234)
    list_of_people.append(jack)
    
    jill = Student("Jill","female","06-22-1989",1112)
    list_of_people.append(jill)

    # set some info to private
    jill.setPrivate()
    person1.setPrivate()

    print("Printing everyone's information")
    for person in list_of_people:
        print(person)

    # attempt to udpates Jane's class private gender attribute
    jane.__gender="unknown"
    print(jane)
    print(jane.__gender)
        
if __name__=="__main__":
    main()
