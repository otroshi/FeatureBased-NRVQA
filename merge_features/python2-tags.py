#----------------------- Preparing data Add. ----------------------------------
import csv
csvfile = open('csv_files (final)/collection.csv', 'rb')
reader=csv.reader(csvfile)
import pickle

#----------------------- Needed Functions -------------------------------------
def strlist2floatlist(the_list):
    # This function receives a list and return the similar list which its
    # items became string.
    to_float = []
    for item in the_list:
        to_float.append(float(item))
    return to_float
#----------------------- End of Needed Functions ------------------------------
import numpy as np
print("pls wait!")
import math
f1 = f2 = f3 = f4 = f5 = f6 = f7 = f8 = f9 = f10 = f11 = f12 = f13 = f14 = f15 = f16 = f17 = f18 = f19 = f20 = f21 = 1
i=0
dic_file_to_MOS={}
for row in reader:
    i +=1
    if i>1:
        #exe_time              = float(row[0])
        file_name             = row[1]
        MOS                   = float(row[2])

#10 Luma Information 12
#11 Chroma Information 24
#12 Temporal Information 12
#13 Colorfulness 18
#14 LMSCN Statistics 216
#15 BRISQUE Scores 6
#16 V.BLINDS 46
#(16 NVS) (5)
#(16 NSS) (37)
#(16 Motion) (4)
#17 VIIDEO features 72
#18 HOSA Scores 6
#19 CORNIA Scores

#        sobel_features        = row[7  :7+24 ]
#        laplacian_features    = row[31 :31+12]
#        SI_features           = row[43 :43+12]
#        HV13_features         = row[55 :55+6 ]

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
#        sobel_features        = strlist2floatlist(sobel_features)
#        laplacian_features    = strlist2floatlist(laplacian_features)
#        SI_features           = strlist2floatlist(SI_features)
#        HV13_features         = strlist2floatlist(HV13_features)
        Luma_info             = strlist2floatlist(Luma_info)
        chrominance_info      = strlist2floatlist(chrominance_info)
        temporal_features     = strlist2floatlist(temporal_features)
        colorfulness_features = strlist2floatlist(colorfulness_features)
        BRISQUE_features      = strlist2floatlist(BRISQUE_features)
        BRISQUE_scores        = strlist2floatlist(BRISQUE_scores)
        VBLINDS_features      = strlist2floatlist(VBLINDS_features)
        VIIDEO_features       = strlist2floatlist(VIIDEO_features)



        #2 Spatial Gradient 24
        #3 Spatiotemporal Gradient 48
        #4 Spatial Laplacian 12
        #5 Spatiotempral Laplacian 24
        #6 Spatial Gradient Amplitude 12
        #7 Laplacian Gradient Amplitude 24
        #8 Spatial Angular Information 8
        #9 Spatiotempral Angular Information 16

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

        tags=[]
        if f1==1:
            for feature in frameRate_feature:#1
                selected_features.append(feature)
                tags.append(1)

        if f2  == 1:
            for feature in features_sobel_0:#16**************************24
                selected_features.append(feature)
                tags.append(2)

        if f3  == 1:
            for feature in features_sobel_1:#16**************************24
                selected_features.append(feature)
                tags.append(3)
            for feature in features_sobel_2:#16**************************24
                selected_features.append(feature)
                tags.append(3)

        if f4  == 1:
            for feature in features_laplacian_0:#8***********************12
                selected_features.append(feature)
                tags.append(4)
        if f5  == 1:
            for feature in features_laplacian_1:#8***********************12
                selected_features.append(feature)
                tags.append(5)
            for feature in features_laplacian_2:#8***********************12
                selected_features.append(feature)
                tags.append(5)
        if f6  == 1:
            for feature in features_grad_amp_0:#8***********************12
                selected_features.append(feature)
                tags.append(6)
        if f7  == 1:
            for feature in features_grad_amp_1:#8***********************12
                selected_features.append(feature)
                tags.append(7)
            for feature in features_grad_amp_2:#8***********************12
                selected_features.append(feature)
                tags.append(7)
        if f8  == 1:
            for feature in features_grad_ang_0:#8
                selected_features.append(feature)
                tags.append(8)
        if f9  == 1:
            for feature in features_grad_ang_1:#8
                selected_features.append(feature)
                tags.append(9)
            for feature in features_grad_ang_2:#
                selected_features.append(feature)
                tags.append(9)
        if f10 == 1:
            for feature in Luma_info:#12
                selected_features.append(feature)
                tags.append(10)

        if f11 == 1:
            for feature in chrominance_info:#24
                selected_features.append(feature)
                tags.append(11)
        if f12 == 1:
            for feature in temporal_features:#12
                selected_features.append(feature)
                tags.append(12)
        if f13 == 1:
            for feature in colorfulness_features:#42
                selected_features.append(feature)
                tags.append(13)
        if f14 == 1:
            for feature in BRISQUE_features:#216
                selected_features.append(feature)
                tags.append(14)
        if f15 == 1:
            for feature in BRISQUE_scores:#6
                selected_features.append(feature)
                tags.append(15)
        if f16 == 1:
            for feature in VBLINDS_features[:-9]:#37
                selected_features.append(feature)
                tags.append(16)
        if f17 == 1:
            for feature in VBLINDS_features[-9:-2]:#7
                selected_features.append(feature)
                tags.append(17)
        if f18 == 1:
            for feature in VBLINDS_features[-2:]:#2
                selected_features.append(feature)
                tags.append(18)
        if f19 == 1:
            for feature in VIIDEO_features:#72
                selected_features.append(feature)
                tags.append(19)
                if math.isnan(feature):
                    flag_NaN = 1

        if f20 == 1:
            for feature in HOSA_scores:#6
                selected_features.append(feature)
                tags.append(20)
        if f21 == 1:
            for feature in CORNIA_scores:#6
                selected_features.append(feature)
                tags.append(21)


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
        break

csvfile.close()



np.save('tags.npy',np.array(tags))
print(tags)
