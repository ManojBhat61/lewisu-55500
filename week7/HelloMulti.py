import multiprocessing
from  multiprocessing import Process
import os.path
import time

print("Number of cpu : ", multiprocessing.cpu_count())

def parallelFunc(file_path):
    procNo = multiprocessing.current_process().pid
    print(' Process ' + str(procNo) + ' is running and waiting ....')
    while not os.path.exists(file_path):
        time.sleep(1)
    print(' Process ' + str(procNo) + ' is terminating  ....', procNo)


if __name__ == "__main__":  # confirms that the code is under main function
    names = ['/tmp/p1.txt', '/tmp/p2.txt', '/tmp/p3.txt']
    procs = []

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=parallelFunc, args=(name, ))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
		
		