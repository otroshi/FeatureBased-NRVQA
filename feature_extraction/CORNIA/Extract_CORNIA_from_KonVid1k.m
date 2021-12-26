%clc;
clear all;
rand('seed',1);

% read list of video files
csv=readtable('KoNViD_1k_attributes.csv');

% load codebook
load('CSIQ_codebook_BS7.mat','codebook0');
load('LIVE_soft_svm_model.mat','soft_model','soft_scale_param');

% load whitening parameter
load('CSIQ_whitening_param.mat','M','P');

svm_model = soft_model;
svm_scale = soft_scale_param;


% V-CORNIA paramter
alpha=0.2;

CORNIA_scores= -ones(1200,260);
parfor i=1:1200
    filename = char(csv(i,3).file_name);
    filedir  = strcat('mat\',filename(1:end-4),'mat');
    mat_file = load(filedir)
    vid_frames = mat_file.vid_frames;
    
    for frame=1:vid_frames(1,1,260)
        img = vid_frames(:,:,frame)
        score = CORNIA(img, codebook0, 'soft', svm_model, svm_scale, M, P);
        
        if frame==1
            CORNIA_frames_scores = score;
        else
            CORNIA_frames_scores(frame)= score;
        end
    end
    

    CORNIA_frames_scores(260)=vid_frames(1,1,260);%frame MOS     
    CORNIA_frames_scores(259)=vid_frames(1,2,260);%frame Num
    CORNIA_frames_scores(258)=vid_frames(1,3,260);%Frame Rate 
    CORNIA_frames_scores(257)=vid_frames(1,4,260);%Duration
        
    CORNIA_scores(i,:)=CORNIA_frames_scores;
    
    
end

save("CORNIA_scores",'CORNIA_scores');