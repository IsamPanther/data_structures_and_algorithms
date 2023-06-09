class Queue:
    def __init__(self):

        self.stack_1 = list()

        self.stack_2 = list()

    def enqueue(self,item):

        self.stack_1.append(item)
    

    def dequeue(self):

        if len(self.stack_1) == 0 and len(self.stack_2) == 0:

            print("The Queue is Empty")

        elif len(self.stack_1) > 0 and len(self.stack_2) == 0:

            while len(self.stack_1):

                element = self.stack_1.pop()

                self.stack_2.append(element)

            print(self.stack_2.pop())

        else:
            print(self.stack_2.pop())


if __name__ == "__main__":
    
    my_queue = Queue()
    my_queue.enqueue(89)
    my_queue.enqueue(12)
    my_queue.enqueue(1)


    my_queue.dequeue()
    my_queue.dequeue()
    my_queue.dequeue() 
    my_queue.dequeue()                           


