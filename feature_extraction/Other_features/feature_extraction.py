# In this file, several functions are defined each one to extract differente features.
# Using the compute_fetures(video_file) function all features are calculated and returned.
# Just notice that you should give video address as the input for each of the functions.
# Note: In some of the functions opencv library for python is used (cv2). 
#		To install Opencv in Ubuntu or Debian, use the bash file at this link to quick install
#		link: http://milq.github.io/install-opencv-ubuntu-debian/
# Note: In some of the functions matlab engine is used. To use the MATLAB engine you need to 
#		first install the MATLAB(2017b or latter) on Linux. Next, you should install its 
#		engine for python. To do so, fisrt off, find the path to the MATLAB folder. Start MATLAB
#		and type matlabroot in the command window. Copy the path returned by matlabroot.
#		Then, on Mac or Linux systems run:
#		cd "matlabroot/extern/engines/python"
#		sudo python setup.py install
# Note: In compute_BRISQUE_fetures(), compute_VBLINDS_fetures() and compute_VIIDEO_fetures() functions
#		some user-defined MATLAB functions are used. You should add thier directory to MATLAB path in 
#		MATLAB program (in set path).

import cv2
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
import math
import matlab.engine 

#------------------------------------------------------------------------------

def test_videofile(video_file):
    cap = cv2.VideoCapture(video_file)
    if (cap.isOpened() == False): 
        print("Unable to read the file:" + video_file)
        return False
    else:
        return True

#------------------------------------------------------------------------------

def get_resolution(video_file):
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("readerobj = VideoReader(vidfilename, 'tag', 'myreader1');",nargout=0)
    eng.eval("width  = readerobj.Width;",nargout=0)
    eng.eval("height = readerobj.height;",nargout=0)
    
    width = eng.workspace['width'] 
    height = eng.workspace['height'] 
    
    eng.quit()
    
    resolution_fetures = [width, height, width*height]
    
    return resolution_fetures

#------------------------------------------------------------------------------ 

def get_frameRate(video_file):
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("readerobj = VideoReader(vidfilename, 'tag', 'myreader1');",nargout=0)
    eng.eval("frameRate  = readerobj.FrameRate;",nargout=0)
        
    frameRate = eng.workspace['frameRate'] 
        
    eng.quit()
        
    return [frameRate]

#------------------------------------------------------------------------------   
    
def compute_sobel_features(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    means_x = []
    stds_x  = []

    means_y = []
    stds_y  = []
    
    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            sobel_x = cv2.Sobel(frame_YUV[:,:,0],cv2.CV_64F,1,0,ksize=5)#frame_YUV[:,:,0] sobel from "Y"
            sobel_y = cv2.Sobel(frame_YUV[:,:,0],cv2.CV_64F,0,1,ksize=5)
            
            sobel_x = abs(sobel_x)
            sobel_y = abs(sobel_y)
            
            means_x.append(np.mean(sobel_x))
            stds_x.append(np.std(sobel_x))

            means_y.append(np.mean(sobel_y))
            stds_y.append(np.std(sobel_y))
            
        # Break the loop
        else:
            break 
            
    min_means_x  = np.min(np.asarray(means_x))
    max_means_x  = np.max(np.asarray(means_x))
    mean_means_x = np.mean(np.asarray(means_x))
    std_means_x  = np.std(np.asarray(means_x))
    kurt_means_x = kurtosis(np.asarray(means_x))
    skew_means_x = skew(np.asarray(means_x))
    
    min_stds_x   = np.min(np.asarray(stds_x))
    max_stds_x   = np.max(np.asarray(stds_x))
    mean_stds_x  = np.mean(np.asarray(stds_x))
    std_stds_x   = np.std(np.asarray(stds_x))
    kurt_stds_x  = kurtosis(np.asarray(stds_x))
    skew_stds_x  = skew(np.asarray(stds_x))
        
    
    min_means_y  = np.min(np.asarray(means_y))
    max_means_y  = np.max(np.asarray(means_y))
    mean_means_y = np.mean(np.asarray(means_y))
    std_means_y  = np.std(np.asarray(means_y))
    kurt_means_y = kurtosis(np.asarray(means_y))
    skew_means_y = skew(np.asarray(means_y))
    
    min_stds_y   = np.min(np.asarray(stds_y))
    max_stds_y   = np.max(np.asarray(stds_y))
    mean_stds_y  = np.mean(np.asarray(stds_y))
    std_stds_y   = np.std(np.asarray(stds_y))
    kurt_stds_y  = kurtosis(np.asarray(stds_y))
    skew_stds_y  = skew(np.asarray(stds_y))
    
     
    features = [min_means_x,max_means_x,mean_means_x,std_means_x,kurt_means_x,skew_means_x,
                min_stds_x,max_stds_x,mean_stds_x,std_stds_x,kurt_stds_x,skew_stds_x,
                
                min_means_y,max_means_y,mean_means_y,std_means_y,kurt_means_y,skew_means_y,
                min_stds_y,max_stds_y,mean_stds_y,std_stds_y,kurt_stds_y,skew_stds_y,
                ]#24 featres
    
    return features#list

#------------------------------------------------------------------------------
   
def compute_laplacian_features(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    means_laplacian = []
    stds_laplacian  = []

    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            laplacian = cv2.Laplacian(frame_YUV[:,:,0], cv2.CV_64F, ksize=5)#frame_YUV[:,:,0] sobel from "Y"
            
            laplacian = abs(laplacian)
            
            means_laplacian.append(np.mean(laplacian))
            stds_laplacian.append(np.std(laplacian))
            
        # Break the loop
        else:
            break 
            
    min_means_laplacian = np.min(np.asarray(means_laplacian))
    max_means_laplacian = np.max(np.asarray(means_laplacian))
    mean_means_laplacian = np.mean(np.asarray(means_laplacian))
    std_means_laplacian  = np.std(np.asarray(means_laplacian))
    kurt_means_laplacian = kurtosis(np.asarray(means_laplacian))
    skew_means_laplacian = skew(np.asarray(means_laplacian))
    
    min_stds_laplacian = np.min(np.asarray(stds_laplacian))
    max_stds_laplacian = np.max(np.asarray(stds_laplacian))
    mean_stds_laplacian = np.mean(np.asarray(stds_laplacian))
    std_stds_laplacian  = np.std(np.asarray(stds_laplacian))
    kurt_stds_laplacian = kurtosis(np.asarray(stds_laplacian))
    skew_stds_laplacian = skew(np.asarray(stds_laplacian))
    
         
    features = [min_means_laplacian,max_means_laplacian,mean_means_laplacian, std_means_laplacian, kurt_means_laplacian, skew_means_laplacian,
                min_stds_laplacian,max_stds_laplacian,mean_stds_laplacian,  std_stds_laplacian,  kurt_stds_laplacian,  skew_stds_laplacian,
                ]#12 featres
    
    return features#list

#------------------------------------------------------------------------------
    
def compute_SI_features(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    kernel_size = 5
    #p_threshold = 12
    
    means_R = []
    stds_R  = []  
    
    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            sobel_x = cv2.Sobel(frame_YUV[:,:,0], cv2.CV_64F, 1, 0, ksize=kernel_size)#frame_YUV[:,:,0] sobel from "Y"
            sobel_y = cv2.Sobel(frame_YUV[:,:,0], cv2.CV_64F, 0, 1, ksize=kernel_size)
            
            R = np.zeros(sobel_x.shape)
            #theta = np.zeros(sobel_x.shape)
            
            for i in range(sobel_x.shape[0]):
                for j in range(sobel_x.shape[1]):
                    R[i,j] = math.sqrt(sobel_x[i,j]**2 + sobel_y[i,j]**2)
                    #theta[i,j] = math.atan2(sobel_x[i,j], sobel_y[i,j])
            
            means_R.append(np.mean(R))
            stds_R.append(np.std(R))
            
        # Break the loop
        else:
            break 
            
    min_means_R = np.min(np.asarray(means_R))
    max_means_R = np.max(np.asarray(means_R))
    mean_means_R = np.mean(np.asarray(means_R))
    std_means_R  = np.std(np.asarray(means_R))
    kurt_means_R = kurtosis(np.asarray(means_R))
    skew_means_R = skew(np.asarray(means_R))
    
    min_stds_R  = np.min(np.asarray(stds_R))
    max_stds_R  = np.max(np.asarray(stds_R))
    mean_stds_R  = np.mean(np.asarray(stds_R))
    std_stds_R   = np.std(np.asarray(stds_R))
    kurt_stds_R  = kurtosis(np.asarray(stds_R))
    skew_stds_R  = skew(np.asarray(stds_R))
     
    features = [min_means_R,max_means_R,mean_means_R,std_means_R,kurt_means_R,skew_means_R,
                min_stds_R,max_stds_R,mean_stds_R,std_stds_R,kurt_stds_R,skew_stds_R,
                ]#12 featres
    
    return features#list

#------------------------------------------------------------------------------
    
def compute_HV13_features(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    kernel_size = 13
    rmin = 20
    delta_theta = 0.225
    p_threshold = 3
    
    all_HV13s = []
    
    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            sobel_x = cv2.Sobel(frame_YUV[:,:,0], cv2.CV_64F, 1, 0, ksize=kernel_size)#frame_YUV[:,:,0] sobel from "Y"
            sobel_y = cv2.Sobel(frame_YUV[:,:,0], cv2.CV_64F, 0, 1, ksize=kernel_size)
            
            #R = np.zeros(sobel_x.shape)
            #theta = np.zeros(sobel_x.shape)
            HV = np.zeros(sobel_x.shape)
            HV_ = np.zeros(sobel_x.shape)
            
            for i in range(sobel_x.shape[0]):
                for j in range(sobel_x.shape[1]):
                    R = math.sqrt(sobel_x[i,j]**2 + sobel_y[i,j]**2)
                    theta = math.atan2(sobel_x[i,j], sobel_y[i,j])
                    
                    if R<rmin:
                        HV[i,j]  = 0
                        HV_[i,j] = 0
                    elif abs(theta)< (delta_theta) :
                        HV[i,j]  = R
                        HV_[i,j] = 0
                    elif (math.pi-abs(theta))< (delta_theta) :
                        HV[i,j]  = R
                        HV_[i,j] = 0
                    elif (math.pi/2 - delta_theta)<abs(theta) and abs(theta)< (math.pi/2 + delta_theta) :
                        HV[i,j]  = R
                        HV_[i,j] = 0
                    else:
                        HV[i,j]  = 0
                        HV_[i,j] = R
            
            mean_HV  = np.mean(HV)
            mean_HV_ = np.mean(HV_)
            
            if mean_HV < p_threshold:
                mean_HV = p_threshold
            if mean_HV_ < p_threshold:
                mean_HV_ = p_threshold
            
            HV13 = mean_HV/float(mean_HV_)
            #NOte: feature_HV13 is a simple means to include  variations in the 
            #      sensitivity of the human visual system with respect to angular orientation

            all_HV13s.append(np.mean(HV13))
            
        # Break the loop
        else:
            break 
            
    min_all_HV13s  = np.min(np.asarray(all_HV13s))
    max_all_HV13s  = np.max(np.asarray(all_HV13s))
    mean_all_HV13s = np.mean(np.asarray(all_HV13s))
    std_all_HV13s  = np.std(np.asarray(all_HV13s))
    kurt_all_HV13s = kurtosis(np.asarray(all_HV13s))
    skew_all_HV13s = skew(np.asarray(all_HV13s))
    
     
    features = [min_all_HV13s,
                max_all_HV13s,
                mean_all_HV13s,
                std_all_HV13s,
                kurt_all_HV13s,
                skew_all_HV13s
                ]#6 featres
    
    return features#list

#------------------------------------------------------------------------------
   
def compute_contrast_info(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    means_contrast = []
    stds_contrast  = []

    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            Y = frame_YUV[:,:,0] #frame_YUV[:,:,0] sobel from "Y"

            means_contrast.append(np.mean(Y))
            stds_contrast.append(np.std(Y))
            
        # Break the loop
        else:
            break 
            
    min_means_contrast  = np.min(np.asarray(means_contrast))
    max_means_contrast  = np.max(np.asarray(means_contrast))
    mean_means_contrast = np.mean(np.asarray(means_contrast))
    std_means_contrast  = np.std(np.asarray(means_contrast))
    kurt_means_contrast = kurtosis(np.asarray(means_contrast))
    skew_means_contrast = skew(np.asarray(means_contrast))
    
    min_stds_contrast  = np.min(np.asarray(stds_contrast))
    max_stds_contrast  = np.max(np.asarray(stds_contrast))
    mean_stds_contrast = np.mean(np.asarray(stds_contrast))
    std_stds_contrast  = np.std(np.asarray(stds_contrast))
    kurt_stds_contrast = kurtosis(np.asarray(stds_contrast))
    skew_stds_contrast = skew(np.asarray(stds_contrast))
    
         
    features = [min_means_contrast, max_means_contrast, mean_means_contrast, std_means_contrast, kurt_means_contrast, skew_means_contrast,
                min_stds_contrast, max_stds_contrast, mean_stds_contrast,  std_stds_contrast,  kurt_stds_contrast,  skew_stds_contrast,
                ]#12 featres
    
    return features#list

#------------------------------------------------------------------------------
   
def compute_chrominance_info(video_file):
    
    cap = cv2.VideoCapture(video_file)
    
    means_U = []
    stds_U  = []
    
    means_V = []
    stds_V  = []    

    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
            
            U = frame_YUV[:,:,1] #frame_YUV[:,:,1] sobel from "U"
            V = frame_YUV[:,:,2] #frame_YUV[:,:,2] sobel from "V"

            means_U.append(np.mean(U))
            stds_U.append(np.std(U))
            
            means_V.append(np.mean(V))
            stds_V.append(np.std(V))
            
        # Break the loop
        else:
            break 
            
    min_means_U  = np.min(np.asarray(means_U))
    max_means_U  = np.max(np.asarray(means_U))
    mean_means_U = np.mean(np.asarray(means_U))
    std_means_U  = np.std(np.asarray(means_U))
    kurt_means_U = kurtosis(np.asarray(means_U))
    skew_means_U = skew(np.asarray(means_U))
    
    min_stds_U  = np.min(np.asarray(stds_U))
    max_stds_U  = np.max(np.asarray(stds_U))
    mean_stds_U = np.mean(np.asarray(stds_U))
    std_stds_U  = np.std(np.asarray(stds_U))
    kurt_stds_U = kurtosis(np.asarray(stds_U))
    skew_stds_U = skew(np.asarray(stds_U))
    

    min_means_V  = np.min(np.asarray(means_V))
    max_means_V  = np.max(np.asarray(means_V))
    mean_means_V = np.mean(np.asarray(means_V))
    std_means_V  = np.std(np.asarray(means_V))
    kurt_means_V = kurtosis(np.asarray(means_V))
    skew_means_V = skew(np.asarray(means_V))
    
    min_stds_V  = np.min(np.asarray(stds_V))
    max_stds_V  = np.max(np.asarray(stds_V))
    mean_stds_V = np.mean(np.asarray(stds_V))
    std_stds_V  = np.std(np.asarray(stds_V))
    kurt_stds_V = kurtosis(np.asarray(stds_V))
    skew_stds_V = skew(np.asarray(stds_V))    
    
         
    features = [min_means_U, max_means_U, mean_means_U, std_means_U, kurt_means_U, skew_means_U,
                min_stds_U, max_stds_U, mean_stds_U,  std_stds_U,  kurt_stds_U,  skew_stds_U,
                
                min_means_V, max_means_V, mean_means_V, std_means_V, kurt_means_V, skew_means_V,
                min_stds_V, max_stds_V, mean_stds_V,  std_stds_V,  kurt_stds_V,  skew_stds_V,
                ]#24 featres
    
    return features#list

#------------------------------------------------------------------------------
    
def compute_colorfulness_features(video_file):

    cap = cv2.VideoCapture(video_file)
    

    means_rg = []
    stds_rg  = []

    means_yb = []
    stds_yb  = []

    means_rgyb = []
    stds_rgyb  = []

    all_colorfulness = []

    while(True):
        ret, frame = cap.read()
        if ret == True: 
            #BGR
            B = frame[:,:,0]#Blue
            G = frame[:,:,1]#Green
            R = frame[:,:,2]#Red
            
            rg = np.array(R) - np.array(G)
            yb = 0.5*(np.array(R)*np.array(G)) - np.array(B)
            
            mean_rg = np.mean(rg)
            std_rg = np.std(rg)
            
            mean_yb = np.mean(yb)
            std_yb = np.std(yb)
            
            mean_rgyb = math.sqrt(mean_rg**2 + mean_yb**2)
            std_rgyb = math.sqrt(std_rg**2 + std_yb**2)
            
            colorfulness = std_rgyb + 0.3*mean_rgyb
            
            
            means_rg.append(mean_rg)
            stds_rg.append(std_rg)
            means_yb.append(mean_yb)
            stds_yb.append(std_yb)
            means_rgyb.append(mean_rgyb)
            stds_rgyb.append(std_rgyb) 
            all_colorfulness.append(colorfulness)
            
        # Break the loop
        else:
            break 
        
    min_means_rg  = np.min(np.asarray(means_rg))
    max_means_rg  = np.max(np.asarray(means_rg))
    mean_means_rg = np.mean(np.asarray(means_rg))
    std_means_rg  = np.std(np.asarray(means_rg))
    kurt_means_rg = kurtosis(np.asarray(means_rg))
    skew_means_rg = skew(np.asarray(means_rg))
        
    min_stds_rg  = np.min(np.asarray(stds_rg))
    max_stds_rg  = np.max(np.asarray(stds_rg))
    mean_stds_rg = np.mean(np.asarray(stds_rg))
    std_stds_rg  = np.std(np.asarray(stds_rg))
    kurt_stds_rg = kurtosis(np.asarray(stds_rg))
    skew_stds_rg = skew(np.asarray(stds_rg))
        
    min_means_yb  = np.min(np.asarray(means_yb))
    max_means_yb  = np.max(np.asarray(means_yb))
    mean_means_yb = np.mean(np.asarray(means_yb))
    std_means_yb  = np.std(np.asarray(means_yb))
    kurt_means_yb = kurtosis(np.asarray(means_yb))
    skew_means_yb = skew(np.asarray(means_yb))
        
    min_stds_yb  = np.min(np.asarray(stds_yb))
    max_stds_yb  = np.max(np.asarray(stds_yb))
    mean_stds_yb = np.mean(np.asarray(stds_yb))
    std_stds_yb  = np.std(np.asarray(stds_yb))
    kurt_stds_yb = kurtosis(np.asarray(stds_yb))
    skew_stds_yb = skew(np.asarray(stds_yb))

    min_means_rgyb  = np.min(np.asarray(means_rgyb))
    max_means_rgyb  = np.max(np.asarray(means_rgyb))
    mean_means_rgyb = np.mean(np.asarray(means_rgyb))
    std_means_rgyb  = np.std(np.asarray(means_rgyb))
    kurt_means_rgyb = kurtosis(np.asarray(means_rgyb))
    skew_means_rgyb = skew(np.asarray(means_rgyb))
        
    min_stds_rgyb  = np.min(np.asarray(stds_rgyb))
    max_stds_rgyb  = np.max(np.asarray(stds_rgyb))
    mean_stds_rgyb = np.mean(np.asarray(stds_rgyb))
    std_stds_rgyb  = np.std(np.asarray(stds_rgyb))
    kurt_stds_rgyb = kurtosis(np.asarray(stds_rgyb))
    skew_stds_rgyb = skew(np.asarray(stds_rgyb))

    min_all_colorfulness  = np.min(np.asarray(all_colorfulness))
    max_all_colorfulness  = np.max(np.asarray(all_colorfulness))
    mean_all_colorfulness = np.mean(np.asarray(all_colorfulness))
    std_all_colorfulness  = np.std(np.asarray(all_colorfulness))
    kurt_all_colorfulness = kurtosis(np.asarray(all_colorfulness))
    skew_all_colorfulness = skew(np.asarray(all_colorfulness))
    

    features = [min_means_rg, max_means_rg, mean_means_rg, std_means_rg, kurt_means_rg, skew_means_rg,
                min_stds_rg, max_stds_rg, mean_stds_rg, std_stds_rg, kurt_stds_rg, skew_stds_rg,
                
                min_means_yb, max_means_yb, mean_means_yb, std_means_yb, kurt_means_yb, skew_means_yb,
                min_stds_yb, max_stds_yb, mean_stds_yb, std_stds_yb, kurt_stds_yb, skew_stds_yb,
                
                min_means_rgyb, max_means_rgyb, mean_means_rgyb, std_means_rgyb, kurt_means_rgyb, skew_means_rgyb,
                min_stds_rgyb, max_stds_rgyb, mean_stds_rgyb, std_stds_rgyb, kurt_stds_rgyb, skew_stds_rgyb,
                
                min_all_colorfulness, max_all_colorfulness, mean_all_colorfulness, std_all_colorfulness, kurt_all_colorfulness, skew_all_colorfulness,
                ]#6*7=42 featres
    
    return features#list

#------------------------------------------------------------------------------
    
def compute_temporal_features(video_file):
    cap = cv2.VideoCapture(video_file)
    
    means_diff = []
    stds_diff  = []    
    
    ret, frame_old = cap.read()
    while(True):
        ret, frame_new = cap.read()
        if ret == True: 
            frame_new_YUV = cv2.cvtColor(frame_new, cv2.COLOR_BGR2YUV)
            frame_old_YUV = cv2.cvtColor(frame_old, cv2.COLOR_BGR2YUV)
            
            Y_new = frame_new_YUV[:,:,0] #frame_YUV[:,:,0] sobel from "Y"
            Y_old = frame_old_YUV[:,:,0] #frame_YUV[:,:,0] sobel from "Y"
            
            Y_new = np.array(Y_new)
            Y_old = np.array(Y_old)
            
            diff  = Y_new - Y_old
            
            diff  = abs(diff)
            
            means_diff.append(np.mean(diff))
            stds_diff.append(np.std(diff))
           
            frame_old = frame_new
        # Break the loop
        else:
            break 
        
    min_means_diff  = np.min(np.asarray(means_diff))
    max_means_diff  = np.max(np.asarray(means_diff))
    mean_means_diff = np.mean(np.asarray(means_diff))
    std_means_diff  = np.std(np.asarray(means_diff))
    kurt_means_diff = kurtosis(np.asarray(means_diff))
    skew_means_diff = skew(np.asarray(means_diff))
    
    min_stds_diff  = np.min(np.asarray(stds_diff))
    max_stds_diff  = np.max(np.asarray(stds_diff))
    mean_stds_diff = np.mean(np.asarray(stds_diff))
    std_stds_diff  = np.std(np.asarray(stds_diff))
    kurt_stds_diff = kurtosis(np.asarray(stds_diff))
    skew_stds_diff = skew(np.asarray(stds_diff))
    
         
    features = [min_means_diff, max_means_diff, mean_means_diff, std_means_diff, kurt_means_diff, skew_means_diff,
                min_stds_diff, max_stds_diff, mean_stds_diff,  std_stds_diff,  kurt_stds_diff,  skew_stds_diff,
                ]#12 featres
    
    return features#list

#------------------------------------------------------------------------------
def compute_BRISQUE_features(video_file):
    # This function works with MATLAB 
    # All the codes are writte in MATLAB and are called here using matlab engine
    # *** Note: Please, note that the MATLAB m-files [functions] should be in a directory
    #           which its address is added in the path in MATLAB. Unless, please set the 
    #           path in MATLAB.
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("all_BRISQUE_features = get_BRISQUE_features(vidfilename);",nargout=0)
    eng.eval("min_feat = nanmin(all_BRISQUE_features);",nargout=0)
    eng.eval("max_feat = nanmax(all_BRISQUE_features);",nargout=0)
    eng.eval("mean_feat = nanmean(all_BRISQUE_features);",nargout=0)
    eng.eval("std_feat  = nanstd(all_BRISQUE_features);",nargout=0)
    eng.eval("kurtosis_feat = kurtosis(all_BRISQUE_features);",nargout=0)
    eng.eval("skewness_feat = skewness(all_BRISQUE_features);",nargout=0)
    
    min_feat      = eng.workspace['min_feat'] 
    max_feat      = eng.workspace['max_feat'] 
    mean_feat     = eng.workspace['mean_feat'] 
    std_feat      = eng.workspace['std_feat'] 
    kurtosis_feat = eng.workspace['kurtosis_feat'] 
    skewness_feat = eng.workspace['skewness_feat'] 
    
    eng.quit()
    
    min_feat      = np.asarray(min_feat)
    max_feat      = np.asarray(max_feat)
    mean_feat     = np.asarray(mean_feat)
    std_feat      = np.asarray(std_feat)
    kurtosis_feat = np.asarray(kurtosis_feat)
    skewness_feat = np.asarray(skewness_feat)
    
    all_stat = [min_feat,
                max_feat,
                mean_feat,
                std_feat,
                kurtosis_feat,
                skewness_feat,
                ]
    
    all_stat = np.hstack(all_stat)
    
    features = all_stat.tolist()
    
    features = features[0]#to make a list in one dim
    
    return features#6*36=216 features 

#------------------------------------------------------------------------------
def compute_BRISQUE_scores(video_file):
    # This function works with MATLAB 2017b (using brisque() function pre-defined in MATLAB 2017b)
    # All the codes are writte in MATLAB and are called here using matlab engine
    # *** Note: Please, note that the MATLAB m-files [functions] should be in a directory
    #           which its address is added in the path in MATLAB. Unless, please set the 
    #           path in MATLAB.
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("all_BRISQUE_scores = get_BRISQUE_scores(vidfilename);",nargout=0)
    eng.eval("min_scores = nanmin(all_BRISQUE_scores);",nargout=0)
    eng.eval("max_scores = nanmax(all_BRISQUE_scores);",nargout=0)
    eng.eval("mean_scores = nanmean(all_BRISQUE_scores);",nargout=0)
    eng.eval("std_scores  = nanstd(all_BRISQUE_scores);",nargout=0)
    eng.eval("kurtosis_scores = kurtosis(all_BRISQUE_scores);",nargout=0)
    eng.eval("skewness_scores = skewness(all_BRISQUE_scores);",nargout=0)
    
    min_scores      = eng.workspace['min_scores'] 
    max_scores      = eng.workspace['max_scores'] 
    mean_scores     = eng.workspace['mean_scores'] 
    std_scores      = eng.workspace['std_scores'] 
    kurtosis_scores = eng.workspace['kurtosis_scores'] 
    skewness_scores = eng.workspace['skewness_scores'] 
    
    eng.quit()
    
    all_statistics = [min_scores,
                     max_scores,
                     mean_scores,
                     std_scores,
                     kurtosis_scores,
                     skewness_scores,
                     ]
    
    return all_statistics#6 features

#------------------------------------------------------------------------------
def compute_VBLINDS_features(video_file):
    # This function works with MATLAB 
    # All the codes are writte in MATLAB and are called here using matlab engine
    # *** Note: Please, note that the MATLAB m-files [functions] should be in a directory
    #           which its address is added in the path in MATLAB. Unless, please set the 
    #           path in MATLAB.
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("VBLINDS_features = get_VBLINDS_features(vidfilename);",nargout=0)
    
    VBLINDS_features = eng.workspace['VBLINDS_features'] 
    
    eng.quit()
    
    VBLINDS_features = np.asarray(VBLINDS_features)
    
    VBLINDS_features = VBLINDS_features.tolist()
    VBLINDS_features = VBLINDS_features[0]
    
    return VBLINDS_features#46 features

#------------------------------------------------------------------------------
def compute_VIIDEO_features(video_file):
    # This function works with MATLAB 
    # All the codes are writte in MATLAB and are called here using matlab engine
    # *** Note: Please, note that the MATLAB m-files [functions] should be in a directory
    #           which its address is added in the path in MATLAB. Unless, please set the 
    #           path in MATLAB.
    
    eng = matlab.engine.start_matlab()
    eng.workspace['vidfilename'] =video_file
    eng.eval("VIIDEO_features = get_VIIDEO_features(vidfilename);",nargout=0)
    
    eng.eval("min_VIIDEO_features       = nanmin(VIIDEO_features);",nargout=0)
    eng.eval("max_VIIDEO_features       = nanmax(VIIDEO_features);",nargout=0)
    eng.eval("mean_VIIDEO_features      = nanmean(VIIDEO_features);",nargout=0)
    eng.eval("std_VIIDEO_features       = std(VIIDEO_features);",nargout=0)
    eng.eval("kurtosis_VIIDEO_features  = kurtosis(VIIDEO_features);",nargout=0)
    eng.eval("skewness_VIIDEO_features  = skewness(VIIDEO_features);",nargout=0)
    
    min_feat      = eng.workspace['min_VIIDEO_features'] 
    max_feat      = eng.workspace['max_VIIDEO_features'] 
    mean_feat     = eng.workspace['mean_VIIDEO_features'] 
    std_feat      = eng.workspace['std_VIIDEO_features'] 
    kurtosis_feat = eng.workspace['kurtosis_VIIDEO_features'] 
    skewness_feat = eng.workspace['skewness_VIIDEO_features'] 
    
    eng.quit()
    
    min_feat      = np.asarray(min_feat)
    max_feat      = np.asarray(max_feat)
    mean_feat     = np.asarray(mean_feat)
    std_feat      = np.asarray(std_feat)
    kurtosis_feat = np.asarray(kurtosis_feat)
    skewness_feat = np.asarray(skewness_feat)
    
    all_stat = [min_feat,
                max_feat,
                mean_feat,
                std_feat,
                kurtosis_feat,
                skewness_feat,
                ]
    
    all_stat = np.hstack(all_stat)
    
    features = all_stat.tolist()
    
    features = features[0]#to make a list in one dim
    
    return features#6*12=72 features 

#------------------------------------------------------------------------------
import time
def compute_fetures(video_file):
# In this file, several functions are defined each one to extract differente features.
# Using the compute_fetures(video_file) function all features are calculated and returned.
# Just notice that you should give video address as the input for each of the functions.
# Note: In some of the functions opencv library for python is used (cv2). 
#		To install Opencv in Ubuntu or Debian, use the bash file at this link to quick install
#		link: http://milq.github.io/install-opencv-ubuntu-debian/
# Note: In some of the functions matlab engine is used. To use the MATLAB engine you need to 
#		first install the MATLAB(2017b or latter) on Linux. Next, you should install its 
#		engine for python. To do so, fisrt off, find the path to the MATLAB folder. Start MATLAB
#		and type matlabroot in the command window. Copy the path returned by matlabroot.
#		Then, on Mac or Linux systems run:
#		cd "matlabroot/extern/engines/python"
#		sudo python setup.py install
# Note: In compute_BRISQUE_fetures(), compute_VBLINDS_fetures() and compute_VIIDEO_fetures() functions
#		some user-defined MATLAB functions are used. You should add thier directory to MATLAB path in 
#		MATLAB program (in set path).
        
    test_videofile(video_file)#test whether python can read the file
    print "video test is OK."
	
    t0 = time.time()
    resolution_features = get_resolution(video_file)                  #   3 featres
    t1 = time.time()
    print "video resolution features are extracted"
    frameRate_feature   = get_frameRate(video_file)                   #   1 featres
    t2 = time.time()
    print "video frame rate is extracted"
    
    #Spatial information
    sobel_features = compute_sobel_features(video_file)               #  24 featres  -- Ref. #9
    t3 = time.time()
    print "video sobel features are extracted"
    laplacian_features = compute_laplacian_features(video_file)       #  12 featres  -- Ref. #9
    t4 = time.time()
    print "video laplacian features are extracted"
    SI_features = compute_SI_features(video_file)                     #  12 featres
    t5 = time.time()
    print "video SI features are extracted"
    HV13_features  = compute_HV13_features(video_file)                #   6 featres  -- Ref. #9
    t6 = time.time()
    print "video HV13 features are extracted"
    contrast_info = compute_contrast_info(video_file)                 #  12 featres  -- Ref. #9
    t7 = time.time()
    print "video contrast_info features are extracted"
    chrominance_info = compute_chrominance_info(video_file)           #  24 featres  -- Ref. #9
    t8 = time.time()
    print "video chrominance_info features are extracted"
    colorfulness_features = compute_colorfulness_features(video_file) #  42 featres  -- Ref. #10
    t9 = time.time()
    print "video colorfulness features are extracted"
    
    #Temporal information
    temporal_features = compute_temporal_features(video_file)         #  12 featres  -- Ref. #9
    t10 = time.time()
    print "video temporal features are extracted"


    # NR-IQA metrics (features + scores)
    BRISQUE_features = compute_BRISQUE_features(video_file)           # 216 featres  -- Ref.
    t11 = time.time()
    BRISQUE_scores  = compute_BRISQUE_scores(video_file)              #   6 featres  -- Ref.
    t12 = time.time()
    print "video BRISQUE features are extracted"
    
    # NR-VQA metrics (features + scores)
    VBLINDS_features = compute_VBLINDS_features(video_file)           #  46 featres  -- Ref.
    t13 = time.time()
    print "video VBLINDS features are extracted"
    VIIDEO_features  = compute_VIIDEO_features(video_file)            #  72 featres  -- Ref.
    t14 = time.time()
    print "video VIIDEO features are extracted"
    
    features = [resolution_features,
                frameRate_feature,
                sobel_features,
                laplacian_features,
                SI_features,
                HV13_features,
                contrast_info,
                chrominance_info,
                temporal_features,
                colorfulness_features,
                BRISQUE_features,
                BRISQUE_scores,
                VBLINDS_features,
                VIIDEO_features,
                ]
    exe_times = [t1-t0,		#resolution_features
				t2-t1,		#frameRate_feature
				t3-t2,		#sobel_features
				t4-t3,		#laplacian_features
				t5-t4,		#SI_features
				t6-t5,		#HV13_features
				t7-t6,		#contrast_info
				t8-t7,		#chrominance_info
				t9-t8,		#temporal_features
				t10-t9,		#colorfulness_features
				t11-t10,	#BRISQUE_features
				t12-t11,	#BRISQUE_scores
				t13-t12,	#VBLINDS_features
				t14-t13,	#VIIDEO_features
				]
    features = np.hstack(features)
    return [exe_times,features]