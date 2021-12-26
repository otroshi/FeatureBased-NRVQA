import pickle
with open('results/1.pkl','r')as f:
    data = pickle.load(f)
    
import glob
pkl_files=glob.glob('results/*.pkl')

import numpy as np
all_pkl_data = np.zeros([2**21-1, len(data[0])+len(data[1])])
for i in range(1,2**21):
    
    with open('results/'+str(i)+'.pkl','r')as f:
        data = pickle.load(f)
    data_array = np.zeros(31)
    data_array[:21]=data[0]
    data_array[21:]=data[1]
    all_pkl_data[i-1,:] = data_array

#prsn_thr  = 0.747
#sprmn_thr = 0.745
#counter = 0
#happened_feats_both = np.zeros(21)
#for i in range(all_pkl_data.shape[0]):
#    if all_pkl_data[i,-5]>prsn_thr:
#        if all_pkl_data[i,-4]>sprmn_thr:
#            counter 


spearmanr_ET = 0.767
pearsonr_ET  = 0.771

happened_feats_both = np.zeros(21)
n_both= 0
happened_feats_spearman = np.zeros(21)
n_spearman= 0
happened_feats_pearsonr = np.zeros(21)
n_pearsonr= 0

for i in range(all_pkl_data.shape[0]):
    reg = all_pkl_data[i,:]

    feats     = reg[:21]
    spearmanr = reg[-5]
    pearsonr  = reg[-4]
    
    if spearmanr>spearmanr_ET:
#        print('yes')
        happened_feats_spearman +=feats
        n_spearman +=1
        
    if pearsonr>pearsonr_ET:
        happened_feats_pearsonr +=feats
        n_pearsonr +=1
        
        if spearmanr>spearmanr_ET:
            happened_feats_both +=feats
            n_both +=1

features = ["#1" ,
            "#2" ,
            "#3" ,
            "#4" ,
            "#5" ,
            "#6" ,
            "#7" ,
            "#8" ,
            "#9" ,
            "#10" ,
            "#11" ,
            "#12" ,
            "#13" ,
            "#14" ,
            "#15",
#            "#16",
            "#16_NSS",
            "#16_NVS",
            "#16_Motion",
            "#17",
            "#18",
            "#19"
            ]
import matplotlib.pyplot as plt
plt.figure(figsize=(10,5))
plt.bar(features,happened_feats_both)
plt.xticks(features, rotation=90, fontsize=12)
plt.yticks( fontsize=12)
plt.savefig('hist.png',dpi=200)   # save the figure to file