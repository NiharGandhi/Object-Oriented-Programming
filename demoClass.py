class Student:
    __slots__ = ["__first_name", "__last_name"]
    def __init__(self, f_name, l_name):
        self.__first_name = f_name # first_name is instance variable
        self.__last_name = l_name   # Encapsulation

    ## accessor or getter
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    ## mutator or setter
    def set_first_name(self, first_name):
        self.__first_name = first_name
    
    def set_last_name(self, last_name):
        self.__last_name = last_name
    
    ## Prints
    def __str__(self):
        return "My Name is " + self.__first_name + " and Family name is " + self.__last_name
    
    ## Represnts
    def __repr__(self):
        return str(self.__class__) + "( " + self.get_first_name() + " " + self.get_last_name() + " )"
    
    ## checks if objects are equal
    def __eq__(self, otherStudent): 
        # return type(self) == type(otherStudent) and (self.__last_name == otherStudent.__last_name)
        return isinstance(otherStudent, self.__class__) and (self.get_last_name() == otherStudent.get_last_name()) and (self.get_first_name() == otherStudent.get_first_name())
    
    ## check if not equal
    def __ne__(self, otherStudent):
        return not self.__eq__(otherStudent)
    
    ## OPtimising eqality check
    def __hash__(self):
        return hash(self.get_first_name())
    
    def __it__(self, otherStudent):
        return self.get_first_name() < otherStudent.get_first_name()
    
    def __go__(self, otherStudent):
        return self.get_first_name() >= otherStudent.get_first_name()


st1 = Student("Nihar", "Gandhi") # Constructor
# st2 = Student("Nihar", "Gandhi")
# st3 = st1

# print(st1)
# st1.__first_name = "Gandhi"


# print(repr(st1))

# print(st1.get_first_name(), st1.get_last_name())
# st1.set_first_name('Faiz')
# st1.set_last_name('Ahamed')
# print(st1)


# comparer if 2 objects are equal
# if st1.get_first_name() == st2.get_first_name():
#     print("Hello, world!")

# # ----- OR ------ # Calls the __eq__ function.
# if st1 == st2:
#     print("Hello, world!")


## EXAMPLE 2
class Car:
    __slots__ = ["__brand", "__color"]
    def __init__(self, brand_name, color): # Initialize
        self.__brand = brand_name   # Encapsulation -> 
        self.__color = color
    

c1 = Car("Ford", "Black") # Constructor c1 -> object -> type Car
c1.__brand = "Cadillac"



## EXAMPLE 3
class Node:
    __slots__ = ["__data" "__next"]

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self, data):
        self.__data = data

    def set_next(self, next):
        self.__next = next

    def str(self):
        return "data= " + str(self.get_data()) + "next= " + str(self.get_next())


class Stack:
    def __init__(self): # Initialization
        self.__head = None # Last element or position of STACK
        self.__size = 0 # SIZE of STACK (0 means empty)

    def push(self, data):
        new_node = Node(data)
        if self.__head is None:
            self.__head = new_node
        else:
            new_node.__next = self.__head
            self.__head = new_node
        self.__size += 1

    def pop(self):
        if self.__size == 0:
            return None
        else:
            data = self.__head.data
            self.__head = self.__head.__next
            self.__size -= 1
            return data

"""
PUSH
1. Node(1) >>> [1]
2. [None] or [data]
3. [None] >>> [[1]] >>> [1] -> head
4. [data] >>> [[1], [head(None)]] -> [[1], [2]]
5. size = size + 1

POP
1. [] is Empty or not
2. Not empty
3. data -> last element [[1], [2]] >>> data = [2]
4. head (2) >>> head.__next -> [None] ==> [2] -> [None]
5. size = size - 1
"""


LIFO = 'Last In - First Out'
