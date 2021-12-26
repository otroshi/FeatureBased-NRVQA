import numpy as np
import scipy.io
from scipy.stats import kurtosis
from scipy.stats import skew

mat = scipy.io.loadmat('CORNIA_scores.mat')
CORNIA_scores = mat['CORNIA_scores']


import os
os.makedirs("CORNIA_features", exist_ok=True) 

import csv
csvfile = open('KoNViD_1k_attributes.csv', 'rb')
reader=csv.reader(csvfile)

import pickle
i=0
j=-1
for row in reader:
    i +=1
    if i>1:
        j +=1
        file_name = row[2]
        
        num_frames = int(CORNIA_scores[j,258])
        CORNIA_scores_for_the_video = CORNIA_scores[j, : num_frames]/100.0
        
        min_vid_scores  = np.min(CORNIA_scores_for_the_video)
        max_vid_scores  = np.max(CORNIA_scores_for_the_video)
        mean_vid_scores = np.mean(CORNIA_scores_for_the_video)    
        std_vid_scores  = np.std(CORNIA_scores_for_the_video)    
        kurt_vid_scores = kurtosis(np.asarray(CORNIA_scores_for_the_video))
        skew_vid_scores = skew(np.asarray(CORNIA_scores_for_the_video))
        
        CORNIA_features = [min_vid_scores, 
                           max_vid_scores,
                           mean_vid_scores,
                           std_vid_scores,
                           kurt_vid_scores,
                           skew_vid_scores]
        
        with open('CORNIA_featurse/'+file_name[:-4]+'.pkl','wb') as f:
            pickle.dump(CORNIA_features,f)