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

import os
def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)
#----------------------- Feature Extraction -----------------------------------
import feature_extraction
import time
#feature_extraction.calc_features(vid_address)

csvfiles_directory = "csv_files/"
ensure_dir(csvfiles_directory)


error_csvfile_dir = csvfiles_directory + "error.csv"
error_csvfile = open(error_csvfile_dir, 'wb') #csv file to write the errors


data={}
i=0
for video_file in videos_add:
    
    i=i+1
    try:
        print "----------------------------"
        print "video#: " + str(i)
        print video_file[17:]
        
        start_time = time.time()
        features  = feature_extraction.calc_features(vid_address=video_file)
        exe_time = time.time() - start_time
        
        print "***** The feature extraction is completed *****" 
        print "Exe. time: " + str(exe_time) + " seconds"
        
        file_name = video_file[17:]
        MOS = dic_file_to_MOS[file_name]
        
        data[file_name] = [MOS,features]
        
        
    except:
        print "----------------------------"
        print "video#: " + str(i)
        print video_file[17:]
		
        print "ERORR in the Feature Extraction Process!"
		
        file_name = video_file[17:]
        new_row = file_name + "\n"
        error_csvfile.write(new_row)
        pass    
    
    
error_csvfile.close()

import pickle
with open('featurs.pkl','w') as f:
    pickle.dump(data,f)
#----------------------- End of Feature Extraction ----------------------------
#feature_extraction_time;
#file_name;
#MOS;
#features;