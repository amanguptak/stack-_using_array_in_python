class stack:

    def __init__(self):
        self.__data=[]


    def push(self,data):
        if data==-1:
            print("ok bye")
        else:self.__data.append(data)

        return
    def pop(self):
        if len( self.__data)==0:
            print("stadk is empty")
        else:
            print(f"{self.__data.pop()} this is poped element")

    def isempty(self):
        if len(self.__data)==0:
            print("stack is empty")

        else :
            print(f"stack has -> {len(self.__data)} elemnt")

    def top(self):
        if(len(self.__data)==0):
            print("stack is empty")

        else:
            print("top is ", self.__data[-1])
        return
    def Stack(self):
       for i in self.__data:
           print(i)

       return



sk=stack()

l=[5,0,9,8,6,76,987,898,6.08,8 ,"hey",9]
for i in l:
 sk.push(i)
sk.pop()
sk.Stack()
sk.isempty()
