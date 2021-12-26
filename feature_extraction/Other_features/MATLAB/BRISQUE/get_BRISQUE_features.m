function all_BRISQUE_features = get_BRISQUE_features(vidfilename)
% This code get video filename and returns BRISQUE features for all frames.
% First off, using read_all_frames(vidfilename) which is defined next all the frames are 
%      extracted and then  BRISQUE features for each frame is computed using the function
%      computeBRISQUEFeatures() which is defined at the end of this code.
% Note: computeBRISQUEFeatures() was used from brisqueModel.m file in MATLAB 2017b which is located at toolbox/images/images/+images/+internal

    frames = read_all_frames(vidfilename);
    
    num_features = 18;
    num_scales = 2;
    framenumber = size(frames,3);%framenumber
    all_BRISQUE_features = zeros(framenumber,num_features*num_scales);
    for f=1:framenumber
        im = frames(:,:,f);
        all_BRISQUE_features(f,:) = computeBRISQUEFeatures(im);
    end
end

function I=read_all_frames(vidfilename)
    readerobj = VideoReader(vidfilename, 'tag', 'myreader1');
    F = get(readerobj, 'numberOfFrames');
    frame = single(read(readerobj,1));
    I = zeros(size(frame,1),size(frame,2));
    k=0;
    video=VideoReader(vidfilename);
    while hasFrame(video)
        k = k+1;
        vidFrame = readFrame(video);
        im = vidFrame;
        if(size(im,3)==3)
            if isa(im,'int16')
                % Since rgb2gray does not support int16
                im = im2double(im);
            end
            im = rgb2gray(im);
        end

        im = round(255*im2double(im));

        I(:,:,k) = im;
    end
end

function full_NSSfeatures = computeBRISQUEFeatures(im)
% computeBRISQUEFeatures computes the Natural Scene Statistics based
%   BRISQUE features which are used for predicting the BRISQUE score and
%   training the SVR model

% Copyright 2016 The MathWorks, Inc.

    num_features = 18;
    num_scales = 2;

    full_NSSfeatures = zeros(num_features*num_scales,1);

    for i = 1:num_scales

        % Normalize image to zero mean and ~unit std
        immean = imgaussfilt(im,7/6,'FilterSize',7,'Padding','replicate');
        imstd = sqrt(abs(imgaussfilt(im.*im,7/6,'FilterSize',7,'Padding','replicate') - immean.*immean));
        imnorm = (im-immean)./(imstd+1);

        % Compute the AGGD parameters
        NSSfeats = images.internal.computeNSSFeatures(imnorm);
        full_NSSfeatures((i-1)*num_features+1:i*num_features) = NSSfeats';

        im =imresize(im,0.5);
    end
end
