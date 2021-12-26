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


all_PLCCs = np.zeros([21,21])
all_SROCCs = np.zeros([21,21])
for i in range(21):
    for j in range(21):
                
        for k in range(all_pkl_data.shape[0]):
            if np.sum(all_pkl_data[k,:21])<3:
                if all_pkl_data[k,i]+all_pkl_data[k,j]==2:
                    print(i,j,k,all_pkl_data[k,-4],all_pkl_data[k,-5])
                    all_PLCCs[i,j]  = round(all_pkl_data[k,-4],2)
                    all_SROCCs[i,j] = round(all_pkl_data[k,-5],2)
                    break


print(all_PLCCs)



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
            
import itertools
import numpy as np
import matplotlib.pyplot as plt

def plot_the_table(cm, features,
                          title='Pearson Linear Correlation Coefficient',
                          cmap=plt.cm.Greens):
    plt.figure(figsize=(15,15))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=18)
    plt.colorbar()
    tick_marks = np.arange(len(features))
    plt.xticks(tick_marks, features, rotation=90, fontsize=14)
    plt.yticks(tick_marks, features, fontsize=14)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black", fontsize=12)

    plt.tight_layout()
#    plt.ylabel('True label')
#    plt.xlabel('Predicted label')

#import pickle
#with open("2by2_PLCC.pkl","wb") as f:
#    pickle.dump(PCC,f)
#with open("2by2_SROCC.pkl","wb") as f:
#    pickle.dump(SROCC,f)
	
plot_the_table(all_PLCCs, features,title='Pearson Linear Correlation Coefficient (PLCC)')    
plt.savefig('2by2_PLCC.png',dpi=200)   # save the figure to file
plot_the_table(all_SROCCs, features,title='Spearman Order Correlation Coefficient (SROCC)')    
plt.savefig('2by2_SROCC.png',dpi=200)   # save the figure to file
plt.show()



