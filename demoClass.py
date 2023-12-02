class Student:
    __slots__ = ["__first_name", "__last_name"] #SLOTS -> FOR PRE-DEFINING THE VARIABLES
    def __init__(self, f_name, l_name): #Initializes the Class Object
        self.__first_name = f_name # first_name is instance variable >>> Encapsulation (Private)
        self.__last_name = l_name   # Encapsulation

    # BY DEFAULT MAKE GET AND SET FUNCTIONS
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
    
    ## Represents
    def __repr__(self):
        return str(self.__class__) + "( " + self.get_first_name() + " " + self.get_last_name() + " )"
    
    ## checks if objects are equal (call this by just doing st1==st2)
    def __eq__(self, otherStudent): 
        # return type(self) == type(otherStudent) and (self.__last_name == otherStudent.__last_name)
        return isinstance(otherStudent, self.__class__) and (self.get_last_name() == otherStudent.get_last_name()) and (self.get_first_name() == otherStudent.get_first_name())
    
    ## check if not equal (call this by doing st1 != st2)
    def __ne__(self, otherStudent):
        return not self.__eq__(otherStudent)
    
    ## Optimising eqality check
    def __hash__(self):
        return hash(self.get_last_name())
    
    def __lt__(self, otherStudent):
        return (self.get_first_name() < otherStudent.get_first_name())
    
    def __ge__(self, otherStudent):
        return self.get_first_name() >= otherStudent.get_first_name()
    
    def __gt__(self, otherStudent):
        return self.get_first_name() > otherStudent.get_first_name()
    
    def __le__(self, otherStudent):
        return self.get_first_name() <= otherStudent.get_first_name()


st1 = Student("Nihar", "Gandhi") # Constructor
st2 = Student("Ashitha", "Gandhi")

# print(st1)

print(st1)
print(st1 <= st2)

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


## -- -- -- -- QUEUE RIT METHOD -- -- -- -- ##
class CircularQueue:
    def __init__(self, size):
        self.__tail = -1  # Rear of Queue
        self.__front = -1  # Front of Queue
        # if size = 5 -> [None, None, None, None, None]
        self.__queue = [None] * size
        self.__size = size

    def isEmpty(self):
        return self.__front == -1

    def isFull(self):
        return (self.__tail + 1) % self.__size == self.__front

    def getQueue(self):
        return self.__queue

    def enQueue(self, data):  # Add data to queue
        if self.isFull():
            print("Queue full")
            return

        if self.isEmpty():
            self.__front = self.__tail = 0
        else:
            self.__tail = (self.__tail + 1) % self.__size

        self.__queue[self.__tail] = data

    def deQueue(self):  # Remove data from queue
        if self.isEmpty():
            print("Queue empty")
            return None

        if self.__front == self.__tail:
            self.__front = -1
            self.__queue[self.__front] = None

        else:
            self.__queue[self.__front] = None
            self.__front = (self.__front + 1) % self.__size

        return self.__queue


FIFO = 'FIRST IN FIRST OUT'
"""
[None, None, None, None, None]
[0, 1, 2, 3, 4]
[None, 1, 2, 3, 4]
[None, None, 2, 3, 4]
[None, None, None, 3, 4]
[None, None, None, None, 4]
[None, None, None, None, None]
"""


capacity = 5
my_circular_queue = CircularQueue(capacity)

my_circular_queue.enQueue(1)
my_circular_queue.enQueue(2)
my_circular_queue.enQueue(3)
# print("Circular queue", my_circular_queue.getQueue())

# print("Size of the queue:", my_circular_queue.size())

# print("Dequeue:", my_circular_queue.deQueue())
# print("Dequeue:", my_circular_queue.deQueue())

my_circular_queue.enQueue(4)
my_circular_queue.enQueue(5)
# print("Circular queue", my_circular_queue.getQueue())


# print("Dequeue:", my_circular_queue.deQueue())
# print("Dequeue:", my_circular_queue.deQueue())
# print("Dequeue:", my_circular_queue.deQueue())
