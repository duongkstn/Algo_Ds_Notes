'''
Circular Queue is based on FIFO (First In First Out) principle and the last position 
is connected back to the first position to make a circle.
'''

class Circular_Queue:
    def __init__(self, size=5):
        self.front = -1
        self.rear = -1
        self.size = size
        self.queue = [None] * size

    def insert(self, value):
        if (self.front == 0 and self.rear == self.size - 1):
            print("Queue is full")
            return
        if (self.front == -1): #do not have any element
            self.front = self.rear = 0
        elif (self.rear == self.size - 1 and self.front != 0): #rear out of range
            self.rear = 0
        else:
            self.rear += 1
        self.queue[self.rear] = value
    def delete(self):#delete an element
        if (self.front == -1):
            print("Queue Underflow")
            return
        print("Element deleted from queue is : %s" % self.queue[self.front])
        if (self.front == self.rear):
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
    def display(self):
        if (self.front == -1):
            print("Queue is Empty")
            return
        print("Circular Queue elements are: ") 
        if (self.front <= self.rear):
            real_arr = self.queue[self.front: self.rear + 1]   
        else:
            real_arr = self.queue[self.front:] + self.queue[:self.rear + 1]
        print(', '.join([str(x) for x in real_arr]))


def main():
    print("1.Insert")
    print("2.Delete")
    print("3.Display")
    my_queue = Circular_Queue(size = 5)

    while True:
        choice = int(input("Enter choice: "))
        if choice == 1:
            value = int(input("Enter the value: "))
            my_queue.insert(value=value)
        elif choice == 2:
            my_queue.delete()
        else:
            my_queue.display()
            break
if __name__ == '__main__':
    main()
    
