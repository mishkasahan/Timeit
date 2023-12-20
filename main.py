from time import time,sleep

def timeit(func):
    def inner():
        print("Start")
        t1 = time()
        func()
        print("Finish")
        t2 = time()
        print(f"Час виконання функції - {t2 - t1}")
    return inner

@timeit
def fd():
    for i in range(10):
        print(i*i)
    sleep(2)

fd()
