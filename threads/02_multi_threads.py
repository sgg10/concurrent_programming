import threading

def executor_a(id=0):
    for x in range(10):
        print(f"Hi, I'm Thread {id} - iteration {x}")

def executor_b(id=0):
    for x in range(10):
        print(f"Hi, I'm Thread {id} - iteration {x}")

def executor_c(id=0):
    for x in range(10):
        print(f"Hi, I'm Thread {id} - iteration {x}")

thread_a = threading.Thread(target=executor_a, args=[1])
thread_b = threading.Thread(target=executor_b, args=(2,)) # Tuple is the most recommended way
thread_c = threading.Thread(target=executor_c, kwargs={"id": 3})

thread_a.start()
thread_b.start()
thread_c.start()