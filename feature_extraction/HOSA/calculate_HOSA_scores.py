#----------------------- Preparing data Add. ----------------------------------
import glob
videos_add=glob.glob("KoNViD_1k_videos/*")
# e.g. videos_add[1] is 'KoNViD_1k_videos/6947112934_original_centercrop_960x540_8s.mp4'

#----------------------- End of Preparing data Add. ---------------------------

#----------------------- Needed Functions -------------------------------------
import os
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
#----------------------- End of Needed Functions ------------------------------

#----------------------- Feature Extraction -----------------------------------
import time
import pickle 

import matlab.engine 
eng = matlab.engine.start_matlab()

ensure_dir("csv_files/")
ensure_dir("HOSA_scores/")

error_csvfile_dir = "csv_files/" + "error.csv"
error_csvfile = open(error_csvfile_dir, 'wb') #csv file to write the errors

exe_tmie_csvfile_dir = "csv_files/" + "exe_tmie.csv"
exe_tmie_csvfile = open(exe_tmie_csvfile_dir, 'wb') #csv file to write the exe times

HOSA_feats_csvfile_dir = "csv_files/" + "HOSA_feats.csv"
HOSA_feats_csvfile = open(HOSA_feats_csvfile_dir, 'wb') #csv file to write the exe times

import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
i=0
for video_file in videos_add:
    
    i=i+1
    try:
        print "----------------------------"
        print "video#: " + str(i)
        file_name = video_file[17:]        
        print file_name
        
        start_time = time.time()
        eng.workspace['vidfilename'] =video_file
        eng.eval("HOSA_scores   = get_HOSA_scores(vidfilename);",nargout=0)
        exe_time = time.time() - start_time

        HOSA_scores   = eng.workspace['HOSA_scores'] 
        HOSA_scores = np.asarray(HOSA_scores)/100.0

        print "***** The feature extraction is completed *****" 
        print "Exe. time HOSA   : " + str(exe_time) + "seconds"

        new_row = file_name + "," + str(exe_time)+ "\n"
        exe_tmie_csvfile.write(new_row)
            
        with open("HOSA_scores/"+video_file[17:]+".pkl",'wb') as f:
            pickle.dump(HOSA_scores,f)

        min_HOSA_scores = np.min(HOSA_scores)
        max_HOSA_scores = np.max(HOSA_scores)
        mean_HOSA_scores = np.mean(HOSA_scores)
        std_HOSA_scores  = np.std(HOSA_scores)
        kurt_HOSA_scores = kurtosis(HOSA_scores)
        skew_HOSA_scores = skew(HOSA_scores)
        
        HOSA_scores_feats = [min_HOSA_scores,
                             max_HOSA_scores,
                             mean_HOSA_scores,
                             std_HOSA_scores,
                             kurt_HOSA_scores,
                             skew_HOSA_scores]
                             
        new_row = file_name 
        for feat in HOSA_scores_feats:
            new_row = new_row + "," + str(feat)
        new_row = new_row + "\n"

        HOSA_feats_csvfile.write(new_row)
    except:
        print "----------------------------"
        print "video#: " + str(i)
        print video_file[17:]
		
        print "ERORR in the Feature Extraction Process!"
		
        #file_name = video_file[17:]
        new_row = file_name + "\n"
        error_csvfile.write(new_row)
        pass    
HOSA_feats_csvfile.close()
error_csvfile.close()
