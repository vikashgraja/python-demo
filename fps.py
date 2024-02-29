import multiprocessing as mp

def executer(arg):
    func , para = arg
    func(*para)


def tes(a):
    pool = mp.Pool(processes=mp.cpu_count())
    r = zip(*pool.map(executer,[i for i in a]))
    pool.close()
    pool.join()
    return r
