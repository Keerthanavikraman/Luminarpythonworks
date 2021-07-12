#queue
#consists of insertion and deletion
#enqueue...insertion
#dequeue...deletion
#display operation
#first in first out...FIFO

queue1=[]
size=int(input("enter the size"))
front=0
rear=0
n=0
def insert():
    global front,rear,size,queue1
    if(rear>=size):
        print("queue is full")
    else:
        p=int(input("enter the element want to insert"))
        queue1.insert(rear,p)
        rear=rear+1

        for i in range(front,rear):
            print(queue1[i])
def delete():
    global front,rear,size,queue1
    if(rear==front):
        print("queue is empty")
    else:
        front=front+1
        for i in range(front,rear):
            print(queue1[i])

while(n!=1):
    print("enter the operation want to perform")
    opt=int(input("press \n1)enqueue \n2)dequeu\n"))
    if(opt==1):
        insert()
    elif(opt==2):
        delete()

n=int(input("do you want to continue press1 for exit"))