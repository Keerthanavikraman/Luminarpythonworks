#data structures....store data

#stack ....  like a bucket
#stack operations
#1 push....adddings elements to stack
#2 pop....removing elements from stack

#initially empty stack
#last in first out....LIFO

#create stack using list

stack1=[]
size=int(input("enter the size"))
top=0
n=0
def push():
    global top,size
    if(top>=size):
        print("stack is full")
    else:
        p=int(input("enter the element want to push"))
        stack1.append(p)
        top=top+1
def pop():
    global top,size
    if(top<=0):
        print("stack is empty")
    else:

        stack1.pop()
        top=top-1
def display():
    print(stack1)

while(n!=1):
    print("enter the operation want to perform")
    opt=int(input("press 1)push 2)pop 3)display"))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
n=int(input("do you want to continue press1 for exit"))