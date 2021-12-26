import multiprocessing as mp
import train_kfold
import time

start_time = time.time()

pool   = mp.Pool(mp.cpu_count())
result = pool.map(train_kfold.train_and_save_results,range(1,2**21))

exe_time = time.time() - start_time

print exe_time
