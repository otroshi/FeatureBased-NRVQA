import cv2
import math
import numpy as np
from scipy.stats import kurtosis
from scipy.stats import skew
#------------------------------------------------------------------------------

def test_videofile(video_file):
    cap = cv2.VideoCapture(video_file)
    if (cap.isOpened() == False): 
        print("Unable to read the file:" + video_file)
        return False
    else:
        return True
    
def calc_sobel_laplacian_features(video_cube,axis):
    
    means_sobel_x = []
    stds_sobel_x  = []

    means_sobel_y = []
    stds_sobel_y  = []
    
    means_grad_amp = []
    stds_grad_amp  = []
    
    means_grad_ang = []
    stds_grad_ang  = []
    
    means_laplacian = []
    stds_laplacian  = []
    
    for i in range(video_cube.shape[axis]):
        if axis==0:
            slice_ = video_cube[i,:,:]
        elif axis==1:
            slice_ = video_cube[:,i,:]
        elif axis==2:
            slice_ = video_cube[:,:,i]
            
        sobel_x = cv2.Sobel(slice_, cv2.CV_64F, 1,0, ksize=3)#frame_YUV[:,:,0] sobel from "Y"
        sobel_y = cv2.Sobel(slice_, cv2.CV_64F, 0,1, ksize=3)
        
        all_amps = []
        all_angs = []
        for x in range(slice_.shape[0]):
            for y in range(slice_.shape[1]):
                grad_x = sobel_x[x,y]
                grad_y = sobel_y[x,y]
                amp = math.sqrt(grad_x**2+grad_y**2)                
                all_amps.append(amp)
                if amp>20 :
                    try:
                        ang = math.atan2(grad_y,grad_x)
                        all_angs.append(ang)
                    except:
                        pass
                    
        means_grad_amp.append(np.mean(all_amps))
        stds_grad_amp.append(np.std(all_amps))
        
        means_grad_ang.append(np.mean(all_angs))
        stds_grad_ang.append(np.std(all_angs))
        
        sobel_x = np.abs(sobel_x)
        sobel_y = np.abs(sobel_y)

    
        means_sobel_x.append(np.mean(sobel_x))
        stds_sobel_x.append(np.std(sobel_x))

        means_sobel_y.append(np.mean(sobel_y))
        stds_sobel_y.append(np.std(sobel_y))
        
        
        laplacian = cv2.Laplacian(slice_, cv2.CV_64F, ksize=5)
        laplacian= np.abs(laplacian)        
        
        means_laplacian.append(np.mean(laplacian))
        stds_laplacian.append(np.std(laplacian))
        
    
    
    min_means_grad_amp  = np.min(np.asarray(means_grad_amp))
    max_means_grad_amp  = np.max(np.asarray(means_grad_amp))
    mean_means_grad_amp = np.mean(np.asarray(means_grad_amp))
    std_means_grad_amp  = np.std(np.asarray(means_grad_amp))
    kurt_means_grad_amp = kurtosis(np.asarray(means_grad_amp))
    skew_means_grad_amp = skew(np.asarray(means_grad_amp))
    
    min_stds_grad_amp  = np.min(np.asarray(stds_grad_amp))
    max_stds_grad_amp  = np.max(np.asarray(stds_grad_amp))
    mean_stds_grad_amp = np.mean(np.asarray(stds_grad_amp))
    std_stds_grad_amp  = np.std(np.asarray(stds_grad_amp))
    kurt_stds_grad_amp = kurtosis(np.asarray(stds_grad_amp))
    skew_stds_grad_amp = skew(np.asarray(stds_grad_amp))
    
    features_grad_amp = [min_means_grad_amp, max_means_grad_amp, mean_means_grad_amp,std_means_grad_amp,kurt_means_grad_amp,skew_means_grad_amp,
                         min_stds_grad_amp, max_stds_grad_amp, mean_stds_grad_amp, std_stds_grad_amp, kurt_stds_grad_amp ,skew_stds_grad_amp
                         ]#12 featres
    
    
    
    mean_means_grad_ang = np.mean(np.asarray(means_grad_ang))
    std_means_grad_ang  = np.std(np.asarray(means_grad_ang))
    kurt_means_grad_ang = kurtosis(np.asarray(means_grad_ang))
    skew_means_grad_ang = skew(np.asarray(means_grad_ang))
    
    mean_stds_grad_ang = np.mean(np.asarray(stds_grad_ang))
    std_stds_grad_ang  = np.std(np.asarray(stds_grad_ang))
    kurt_stds_grad_ang = kurtosis(np.asarray(stds_grad_ang))
    skew_stds_grad_ang = skew(np.asarray(stds_grad_ang))
    
    features_grad_ang = [mean_means_grad_ang,std_means_grad_ang,kurt_means_grad_ang,skew_means_grad_ang,
                         mean_stds_grad_ang, std_stds_grad_ang, kurt_stds_grad_ang ,skew_stds_grad_ang
                         ]#12 featres
    
    
    
    min_means_x  = np.min(np.asarray(means_sobel_x))
    max_means_x  = np.max(np.asarray(means_sobel_x))
    mean_means_x = np.mean(np.asarray(means_sobel_x))
    std_means_x  = np.std(np.asarray(means_sobel_x))
    kurt_means_x = kurtosis(np.asarray(means_sobel_x))
    skew_means_x = skew(np.asarray(means_sobel_x))
    
    min_stds_x  = np.min(np.asarray(stds_sobel_x))
    max_stds_x  = np.max(np.asarray(stds_sobel_x))
    mean_stds_x = np.mean(np.asarray(stds_sobel_x))
    std_stds_x  = np.std(np.asarray(stds_sobel_x))
    kurt_stds_x = kurtosis(np.asarray(stds_sobel_x))
    skew_stds_x = skew(np.asarray(stds_sobel_x))
   
    
    min_means_y  = np.min(np.asarray(means_sobel_y))
    max_means_y  = np.max(np.asarray(means_sobel_y))
    mean_means_y = np.mean(np.asarray(means_sobel_y))
    std_means_y  = np.std(np.asarray(means_sobel_y))
    kurt_means_y = kurtosis(np.asarray(means_sobel_y))
    skew_means_y = skew(np.asarray(means_sobel_y))
    
    min_stds_y  = np.min(np.asarray(stds_sobel_y))
    max_stds_y  = np.max(np.asarray(stds_sobel_y))
    mean_stds_y = np.mean(np.asarray(stds_sobel_y))
    std_stds_y  = np.std(np.asarray(stds_sobel_y))
    kurt_stds_y = kurtosis(np.asarray(stds_sobel_y))
    skew_stds_y = skew(np.asarray(stds_sobel_y))
    
    features_sobel = [min_means_x,max_means_x,mean_means_x,std_means_x,kurt_means_x,skew_means_x,
                      min_stds_x,max_stds_x,mean_stds_x,std_stds_x,kurt_stds_x,skew_stds_x,
                
                      min_means_y,max_means_y,mean_means_y,std_means_y,kurt_means_y,skew_means_y,
                      min_stds_y,max_stds_y,mean_stds_y,std_stds_y,kurt_stds_y,skew_stds_y,
                      ]#24 featres
    
    
    
    min_means_laplacian = np.min(np.asarray(means_laplacian))
    max_means_laplacian  = np.max(np.asarray(means_laplacian))
    mean_means_laplacian = np.mean(np.asarray(means_laplacian))
    std_means_laplacian  = np.std(np.asarray(means_laplacian))
    kurt_means_laplacian = kurtosis(np.asarray(means_laplacian))
    skew_means_laplacian = skew(np.asarray(means_laplacian))
    
    min_stds_laplacian = np.min(np.asarray(stds_laplacian))
    max_stds_laplacian  = np.max(np.asarray(stds_laplacian))
    mean_stds_laplacian = np.mean(np.asarray(stds_laplacian))
    std_stds_laplacian  = np.std(np.asarray(stds_laplacian))
    kurt_stds_laplacian = kurtosis(np.asarray(stds_laplacian))
    skew_stds_laplacian = skew(np.asarray(stds_laplacian))
    
    features_laplacian = [min_means_laplacian, max_means_laplacian, mean_means_laplacian, std_means_laplacian, kurt_means_laplacian, skew_means_laplacian,
                          min_stds_laplacian, max_stds_laplacian, mean_stds_laplacian,  std_stds_laplacian,  kurt_stds_laplacian,  skew_stds_laplacian,
                          ]#12 featres


    return features_grad_amp, features_grad_ang, features_sobel,features_laplacian

def vid2cube(vid_address):

    cap = cv2.VideoCapture(vid_address)
    i=0
    while(True):
        ret, frame = cap.read()
        if ret == True: 
            frame_YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)            
            frame_y = frame_YUV[:,:,0]
            
            try:
                frame_y = np.reshape(frame_y, (frame_y.shape[0], frame_y.shape[1], 1) )
                cube    = np.append(cube,frame_y,axis=2)
            except:
                cube = np.reshape(frame_y, (frame_y.shape[0], frame_y.shape[1], 1) )
                pass
            i +=1
            #print i
        else:
            break
    return cube


def calc_features(vid_address):
    features = 0
    if test_videofile(vid_address):
        video_cube = vid2cube(vid_address)
        [features_grad_amp_0, features_grad_ang_0, features_sobel_0, features_laplacian_0] = calc_sobel_laplacian_features(video_cube, axis=0)
        [features_grad_amp_1, features_grad_ang_1, features_sobel_1, features_laplacian_1] = calc_sobel_laplacian_features(video_cube, axis=1)
        [features_grad_amp_2, features_grad_ang_2, features_sobel_2, features_laplacian_2] = calc_sobel_laplacian_features(video_cube, axis=2)
        
        features = [features_grad_amp_0, features_grad_ang_0, features_sobel_0, features_laplacian_0,
                    features_grad_amp_1, features_grad_ang_1, features_sobel_1, features_laplacian_1,
                    features_grad_amp_2, features_grad_ang_2, features_sobel_2, features_laplacian_2
                    ]
    return features
