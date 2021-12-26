function VBLINDS_features = get_VBLINDS_features(vidfilename)
% This is the implementation of Video BLIINDS as described in:
% M.A. Saad, A.C. Bovik, and C. Charrier, "Blind Prediction of Natural Video Quality", IEEE Transactions on Image Processing, Vol. 23, no. 3, pp. 1352-1365, March 2014.

% First off, all frames are read and then using different functions the
% features described in the paper are extracted.

frames = read_all_frames(vidfilename);

niqe_features = compute_niqe_features(frames);
dt_dc_measure1 = temporal_dc_variation_feature_extraction(frames);
[dt_dc_measure2, geo_ratio_features] = NSS_spectral_ratios_feature_extraction(frames);
[mean_Coh10x10, G] = motion_feature_extraction(frames);

VBLINDS_features = [niqe_features log(1+dt_dc_measure1) log(1+dt_dc_measure2) log(1+geo_ratio_features) log(1+mean_Coh10x10) log(1+G)];
end
%% READ ALL FRAMES
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