# Q.2 Program to perform operations on a Linear Queue

queue = []
queue2 = []


# 1. Enqueue an element into the queue
def enqueue():
    element = input("Enter element to enqueue: ")
    queue.append(element)
    print("Element inserted successfully!")
    print("Queue:", queue)
enqueue()

# 2. Dequeue an element from the queue
def dequeue():
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        element = queue.pop(0)
        print("Dequeued element:", element)
        print("Queue:", queue)

# 3. Display the queue
def display():
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        print("Queue elements (Front to Rear):", queue)

display()
# 4. Reverse the queue using a stack
def reverse_queue():
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        stack = []

        while len(queue) > 0:
            stack.append(queue.pop(0))

        while len(stack) > 0:
            queue.append(stack.pop())

        print("Queue reversed successfully!")
        print("Queue:", queue)
reverse_queue()

# 5. Merge two queues into one
def merge_queues():
    global queue, queue2

    queue2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        queue2.append(element)

    merged_queue = queue + queue2

    print("First Queue:", queue)
    print("Second Queue:", queue2)
    print("Merged Queue:", merged_queue)


# 6. Check if two queues are identical
def identical_queues():
    global queue2

    queue2 = []

    n = int(input("Enter number of elements in second queue: "))

    for i in range(n):
        element = input("Enter element: ")
        queue2.append(element)

    print("First Queue:", queue)
    print("Second Queue:", queue2)

    if queue == queue2:
        print("Both queues are identical.")
    else:
        print("Both queues are not identical.")

identical_queues()

