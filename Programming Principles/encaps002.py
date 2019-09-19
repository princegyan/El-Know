class MyEncapsulation:

    #Hidden variable or member of class MyEncapsulations
    __secretNumber = 10

    #function "adder" created 
    def adder(self,increment):
        self.__secretNumber += increment
        print(self.__secretNumber)

myObject = MyEncapsulation()
myObject.adder(2)
myObject.adder(8)

#This Line Causes an error
print(myObject._MyEncapsulation__secretNumber)