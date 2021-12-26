import csv
import pickle
import math
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.model_selection import KFold
import scipy as scy
import numpy as np

#----------------------- Needed Functions -------------------------------------
def strlist2floatlist(the_list):
    # This function receives a list and return the similar list which its
    # items became string.
    to_float = []
    for item in the_list:
        to_float.append(float(item))
    return to_float


def MSE(seq1, seq2, length):
    sum_square_error = 0
    for i in range(length):
        sum_square_error += (seq1[i]-seq2[i])**2
        
    mean_square_error = sum_square_error/length
    return mean_square_error

def MAE(seq1, seq2, length):
    sum_abs_error = 0
    for i in range(length):
        sum_abs_error += abs(seq1[i]-seq2[i])
        
    mean_abs_error = sum_abs_error/length
    return mean_abs_error

#----------------------- End of Needed Functions ------------------------------
def train_and_save_results(seq_counter):
    print seq_counter,"/",2**21
    the_seq = '{0:022b}'.format(seq_counter)
        
    f1  = int(the_seq[-1])
    f2  = int(the_seq[-2])
    f3  = int(the_seq[-3])
    f4  = int(the_seq[-4])
    f5  = int(the_seq[-5])
    f6  = int(the_seq[-6])
    f7  = int(the_seq[-7])
    f8  = int(the_seq[-8])
    f9 = int(the_seq[-9])
    f10 = int(the_seq[-10])
    f11 = int(the_seq[-11])
    f12 = int(the_seq[-12])
    f13 = int(the_seq[-13])
    f14 = int(the_seq[-14])
    f15 = int(the_seq[-15])
    f16 = int(the_seq[-16])
    f17 = int(the_seq[-17])    
    f18 = int(the_seq[-18])    
    f19 = int(the_seq[-19])    
    f20 = int(the_seq[-20])    
    f21 = int(the_seq[-21])    
    
    csvfile = open('csv_files (final)/collection.csv', 'rb')
    reader=csv.reader(csvfile)
    i=0
    dic_file_to_MOS={}
    for row in reader:
        i +=1
        if i>1:
            file_name             = row[1]
            MOS                   = float(row[2])
            
            resolution_features   = row[3  :3+3  ]
            frameRate_feature     = row[6  :6+1  ]
    
            Luma_info             = row[61 :61+12]
            chrominance_info      = row[73 :73+24]
            temporal_features     = row[97 :97+12]
            colorfulness_features = row[109:109+42 ]
            BRISQUE_features      = row[151:151+216]
            BRISQUE_scores        = row[367:367+6  ]
            
            VBLINDS_features      = row[373:373+46 ]
            
            VIIDEO_features       = row[419:419+72 ]
            
            
            resolution_features   = strlist2floatlist(resolution_features)
            frameRate_feature     = strlist2floatlist(frameRate_feature)
    
            Luma_info             = strlist2floatlist(Luma_info)
            chrominance_info      = strlist2floatlist(chrominance_info)
            temporal_features     = strlist2floatlist(temporal_features)
            colorfulness_features = strlist2floatlist(colorfulness_features)
            BRISQUE_features      = strlist2floatlist(BRISQUE_features)
            BRISQUE_scores        = strlist2floatlist(BRISQUE_scores)
            VBLINDS_features      = strlist2floatlist(VBLINDS_features)
            VIIDEO_features       = strlist2floatlist(VIIDEO_features)
            
            
            with open('Laplace_and_sobel/'+file_name[:-4]+'.pkl','rb') as f:
                ST_feats = pickle.load(f)
                
            try:
                [features_grad_amp_0, features_grad_ang_0, features_sobel_0, features_laplacian_0,
                 features_grad_amp_1, features_grad_ang_1, features_sobel_1, features_laplacian_1,
                 features_grad_amp_2, features_grad_ang_2, features_sobel_2, features_laplacian_2
                 ] = ST_feats
            except:
                continue
             
            #        HOSA
            with open('HOSA_features/'+file_name[:-4]+'.pkl','rb') as f:
                HOSA_scores = pickle.load(f)
             
            #        CORNIA
            with open('CORNIA_features/'+file_name[:-4]+'.pkl','rb') as f:
                CORNIA_scores = pickle.load(f)
             
            
            dic_file_to_MOS[file_name] = MOS
            
            
            selected_features     = [MOS] # ---> selected_features = [MOS,features]
            
            
            if f1==1:
                for feature in frameRate_feature:#1
                    selected_features.append(feature)
                    
            if f2  == 1:        
                for feature in features_sobel_0:#24
                    selected_features.append(feature)
                    
            if f3  == 1:        
                for feature in features_sobel_1:#24
                    selected_features.append(feature)
                for feature in features_sobel_2:#24
                    selected_features.append(feature)
                    
            if f4  == 1:        
                for feature in features_laplacian_0:#8
                    selected_features.append(feature)
                    
            if f5  == 1:        
                for feature in features_laplacian_1:#8
                    selected_features.append(feature)
                for feature in features_laplacian_2:#8
                    selected_features.append(feature)
                    
            if f6  == 1:        
                for feature in features_grad_amp_0:#8
                    selected_features.append(feature)
                    
            if f7  == 1:        
                for feature in features_grad_amp_1:#8
                    selected_features.append(feature)
                for feature in features_grad_amp_2:#8
                    selected_features.append(feature)
                    
            if f8  == 1:        
                for feature in features_grad_ang_0:#8
                    selected_features.append(feature)
                    
            if f9  == 1:        
                for feature in features_grad_ang_1:#8
                    selected_features.append(feature)
                for feature in features_grad_ang_2:#
                    selected_features.append(feature)
                    
            if f10 == 1:        
                for feature in Luma_info:#12
                    selected_features.append(feature)
                                    
            if f11 == 1:        
                for feature in chrominance_info:#24
                    selected_features.append(feature)
                    
            if f12 == 1:        
                for feature in temporal_features:#12
                    selected_features.append(feature)
                    
            if f13 == 1:        
                for feature in colorfulness_features:#42
                    selected_features.append(feature)
                    
            if f14 == 1:        
                for feature in BRISQUE_features:#216
                    selected_features.append(feature)
                    
            if f15 == 1:        
                for feature in BRISQUE_scores:#6
                    selected_features.append(feature)
                    
            if f16 == 1:        
                for feature in VBLINDS_features[:-9]:#37
                    selected_features.append(feature)
                    
            if f17 == 1:        
                for feature in VBLINDS_features[-9:-2]:#7
                    selected_features.append(feature)
                    
            if f18 == 1:        
                for feature in VBLINDS_features[-2:]:#2
                    selected_features.append(feature)
            if f19 == 1:      
                for feature in VIIDEO_features:#72
                    selected_features.append(feature)
                    if math.isnan(feature):
                        flag_NaN = 1
                    
            if f20 == 1:        
                for feature in HOSA_scores:#6
                    selected_features.append(feature)
                    
            if f21 == 1:        
                for feature in CORNIA_scores:#6
                    selected_features.append(feature)
                                                    
                            
                    
            flag_NaN = 0  
            for feature in selected_features:            
                if math.isnan(feature):
                    flag_NaN = 1
            if flag_NaN == 0 :
                selected_features = np.asarray(selected_features)
                selected_features = np.reshape(selected_features,(1,-1))
                
                if i==2:
                    all_selected_features = selected_features
                else:
                    all_selected_features = np.append(all_selected_features,selected_features,axis=0)
    
    
    csvfile.close()


    regr = ExtraTreesRegressor(n_estimators=100,random_state=1)


    sum_spearmanr_train = sum_pearsonr_train = sum_kendalltau_train =  sum_MSE_train = sum_MAE_train = 0
    sum_spearmanr_test  = sum_pearsonr_test  = sum_kendalltau_test  =  sum_MSE_test  = sum_MAE_test  = 0
    num_folds = 5
    k=0
    kf = KFold(n_splits=num_folds,random_state=1)
    for train, test in kf.split(all_selected_features):
        all_features_train, all_MOS_train = [all_selected_features[train,1:], all_selected_features[train,0]/5.0]
        all_features_test,  all_MOS_test  = [all_selected_features[test,1:],  all_selected_features[test,0]/5.0 ]
        
        train_num = all_features_train.shape[0]
        test_num  = all_features_test.shape[0]
        
        list_features_train = []
        list_features_test  = []
        
        list_MOS_train = []
        list_MOS_test  = []
        
        for i in range(train_num):
            list_features_train.append(all_features_train[i,:])
            list_MOS_train.append(all_MOS_train[i])
        
        for i in range(test_num):
            list_features_test.append(all_features_test[i,:])
            list_MOS_test.append(all_MOS_test[i])
        
        regr = regr.fit(list_features_train, list_MOS_train)
        
        ##---------------------------------------
        k+=1
        #print"------------- train ",k,"/",num_folds,"-------------"
        MOS_pred = regr.predict(list_features_train)
        
        spearmanr_train=scy.stats.spearmanr(list_MOS_train,MOS_pred)        
        pearsonr_train=scy.stats.pearsonr(list_MOS_train,MOS_pred)
        kendalltau_train=scy.stats.kendalltau(list_MOS_train,MOS_pred)
        MSE_train=MSE(list_MOS_train,MOS_pred,len(list_MOS_train))
        MAE_train=MAE(list_MOS_train,MOS_pred,len(list_MOS_train))
        
        ##---------------------------------------
        #print"------------- test -------------"
        
        MOS_pred = regr.predict(list_features_test)
        
        spearmanr_test=scy.stats.spearmanr(list_MOS_test,MOS_pred)
        pearsonr_test=scy.stats.pearsonr(list_MOS_test,MOS_pred)
        kendalltau_test=scy.stats.kendalltau(list_MOS_test,MOS_pred)
        MSE_test=MSE(list_MOS_test,MOS_pred,len(list_MOS_test))
        MAE_test=MAE(list_MOS_test,MOS_pred,len(list_MOS_test))


        sum_spearmanr_train += spearmanr_train[0]
        sum_pearsonr_train  += pearsonr_train[0]
        sum_kendalltau_train+= kendalltau_train[0]
        sum_MSE_train += MSE_train 
        sum_MAE_train += MAE_train 
        
        sum_spearmanr_test += spearmanr_test[0]
        sum_pearsonr_test  += pearsonr_test[0]
        sum_kendalltau_test+= kendalltau_test[0]
        sum_MSE_test += MSE_test 
        sum_MAE_test += MAE_test 
    

    mean_spearmanr_train = sum_spearmanr_train/float(num_folds)
    mean_pearsonr_train  = sum_pearsonr_train/float(num_folds)  
    mean_kendalltau_train= sum_kendalltau_train/float(num_folds)
    mean_MSE_train = sum_MSE_train /float(num_folds)
    mean_MAE_train = sum_MAE_train /float(num_folds)
    
    mean_spearmanr_test = sum_spearmanr_test/float(num_folds)
    mean_pearsonr_test  = sum_pearsonr_test/float(num_folds)  
    mean_kendalltau_test= sum_kendalltau_test/float(num_folds)
    mean_MSE_test = sum_MSE_test /float(num_folds)
    mean_MAE_test = sum_MAE_test /float(num_folds)
    
    flags   = [f1,
               f2,
               f3,
               f4,
               f5,
               f6,
               f7,
               f8,
               f9,
               f10,
               f11,
               f12,
               f13,
               f14,
               f15,
               f16,
               f17,
               f18,
               f19,
               f20,
               f21
               ]
    
    results = [mean_spearmanr_train, mean_pearsonr_train, mean_kendalltau_train, mean_MSE_train, mean_MAE_train,
               mean_spearmanr_test, mean_pearsonr_test, mean_kendalltau_test, mean_MSE_test, mean_MAE_test]
    with open('results/'+str(seq_counter)+'.pkl','wb') as f:
        pickle.dump([flags, results], f)