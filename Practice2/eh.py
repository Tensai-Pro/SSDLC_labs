import multiprocessing
import time

def heavy(n, i, proc):
    for x in range(1, n):
        for y in range(1, n):
            x**y
    print(f"Cycle № {i} kernel {proc}")

def sequential(calc, proc):
    print(f"New thread № {proc}")
    for i in range(calc):    
        heavy(500, i, proc)
    print(f"{calc} cycles finished. CPU № {proc}")
    
    
def processesed(procs, calc):
    # procs - количество ядер
    # calc - количество операций на ядро
    
    processes = []
    
    # делим вычисления на количество ядер
    for proc in range(procs):
        p = multiprocessing.Process(target=sequential, args=(calc, proc))
        processes.append(p)
        p.start()

    # Ждем, пока все ядра 
    # завершат свою работу.
    for p in processes:
        p.join()

if __name__ == "__main__":
    start = time.time()
    # узнаем количество ядер у процессора
    n_proc = multiprocessing.cpu_count()
    # вычисляем сколько циклов вычислений будет приходится
    # на 1 ядро, что бы в сумме получилось 80 или чуть больше
    calc = 80 // n_proc + 1
    processesed(n_proc, calc)
    end = time.time()
    print(f"Total {n_proc} kernels")
    print(f"On each kernel there were {calc} cycles")
    print(f"Total cycles: {n_proc*calc} in time: ", end - start)