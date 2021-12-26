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

#----------------------- Needed Functions -------------------------------------
def list2strlist(the_list):
    # This function receives a list and return the similar list which its
    # items became string.
    to_string = []
    for item in the_list:
        to_string.append(str(item))
    return to_string

import os
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
#----------------------- End of Needed Functions ------------------------------

#----------------------- Feature Extraction -----------------------------------
import feature_extraction
import time

csvfiles_directory = "csv_files (final)/"
ensure_dir(csvfiles_directory)

collection_csvfile_dir = csvfiles_directory + "collection.csv"
collection_csvfile = open(collection_csvfile_dir, 'wb') #csv file to write all the features

header_exe_time = "Exe_time,File_name,MOS" + "\n"
collection_csvfile.write(header_exe_time)


exe_time_csvfile_dir = csvfiles_directory + "exe_time.csv"
exe_time_csvfile = open(exe_time_csvfile_dir, 'wb') #csv file to write all the feature extarction times

header_exe_time = "File_name,exe_time,resolution_features,frameRate_feature,sobel_features,laplacian_features,SI_features,HV13_features,contrast_info,chrominance_info,temporal_features,colorfulness_features,BRISQUE_features,BRISQUE_scores,VBLINDS_features,VIIDEO_features" + "\n"
exe_time_csvfile.write(header_exe_time)


error_csvfile_dir = csvfiles_directory + "error.csv"
error_csvfile = open(error_csvfile_dir, 'wb') #csv file to write the errors
i=1100
for video_file in videos_add:
    
    i=i+1
    try:
        print "----------------------------"
        print "video#: " + str(i)
        print video_file[17:]
        
        start_time = time.time()
        [exe_times, features]  = feature_extraction.compute_fetures(video_file=video_file)
        exe_time = time.time() - start_time
        
        print "***** The feature extraction is completed *****" 
        print "Exe. time: " + str(exe_time/60) + "minutes"
        
        file_name = video_file[17:]
        MOS = dic_file_to_MOS[file_name]
        
        exe_time_srt = str(exe_time)
        exe_times_str= list2strlist(exe_times)
        features_str = list2strlist(features)
        MOS_str = str(MOS)
        
        
        new_row = [exe_time_srt,file_name,MOS_str]
        for feat in features_str:
            new_row.append(feat)
            
        new_row = ','.join(new_row)
        new_row = new_row + "\n"
        
        csv_file_dir = csvfiles_directory + file_name[:-4] + ".csv"
        with open(csv_file_dir, 'wb') as csvfile:
            csvfile.write(new_row)
            
            
        collection_csvfile.write(new_row)
        
        
        new_row_exe_time = [file_name,exe_time_srt]
        for t in exe_times_str:
            new_row_exe_time.append(t)
        
        new_row_exe_time = ','.join(new_row_exe_time)
        new_row_exe_time = new_row_exe_time + "\n"
        exe_time_csvfile.write(new_row_exe_time)
        
        
    except:
        print "----------------------------"
        print "video#: " + str(i)
        print video_file[17:]
		
        print "ERORR in the Feature Extraction Process!"
		
        file_name = video_file[17:]
        new_row = file_name + "\n"
        error_csvfile.write(new_row)
        pass    
    
collection_csvfile.close()
exe_time_csvfile.close()
error_csvfile.close()
    
#----------------------- End of Feature Extraction ----------------------------
