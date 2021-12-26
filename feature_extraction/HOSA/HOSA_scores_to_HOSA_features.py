import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
import glob
all_files = glob.glob('HOSA_scores/*.pkl')

import pickle
j=-1
for file_name in all_files:
    
    with open(file_name,'rb') as f:
        HOSA_scores = pickle.load(f)
        
    min_vid_scores  = np.min(HOSA_scores)
    max_vid_scores  = np.max(HOSA_scores)
    mean_vid_scores = np.mean(HOSA_scores)    
    std_vid_scores  = np.std(HOSA_scores)    
    kurt_vid_scores = kurtosis(np.asarray(HOSA_scores))
    skew_vid_scores = skew(np.asarray(HOSA_scores))
    
    HOSA_features = [min_vid_scores, 
                     max_vid_scores,
                     mean_vid_scores,
                     std_vid_scores,
                     kurt_vid_scores,
                     skew_vid_scores]
    
    with open('HOSA_features/'+file_name[12:-8]+'.pkl','wb') as f:
        pickle.dump(HOSA_features, f)