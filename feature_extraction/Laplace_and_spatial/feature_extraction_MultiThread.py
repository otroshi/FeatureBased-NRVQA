#----------------------- Preparing data Add. ----------------------------------
import glob
videos_add=glob.glob("KoNViD_1k_videos/*")
# e.g. videos_add[1] is 'KoNViD_1k_videos/6947112934_original_centercrop_960x540_8s.mp4'
import csv
csvfile = open('KoNViD_1k_attributes.csv', 'rb')
reader=csv.reader(csvfile)

i=0
dic_file_to_MOS={}
for row in reader:
    i +=1
    if i>1:
        file_name = row[2]
        MOS = float(row[3])
        dic_file_to_MOS[file_name] = MOS
csvfile.close()
#----------------------- End of Preparing data Add. ---------------------------

import feature_extraction_mp

import multiprocessing as mp
import time

start_time = time.time()

pool   = mp.Pool(mp.cpu_count())
result = pool.map(feature_extraction_mp.calc_and_save_features,videos_add)

exe_time = time.time() - start_time

print exe_time