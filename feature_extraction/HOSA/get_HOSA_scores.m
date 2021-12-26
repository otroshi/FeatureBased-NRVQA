function HOSA_scores = get_HOSA_scores(video_filename)

% main
load('whitening_param.mat', 'M', 'P');
load('codebook_hosa', 'codebook_hosa');
load('hosa_live_model');
BS = 7; % patch size
power = 0.2; % signed power normalizaiton param

v = VideoReader(video_filename);
i=0;
while hasFrame(v)
    i = i+1;
    
    img = readFrame(v);
    %img = rgb2gray(img);
    frame_HOSA_feats = hosa_feature_extraction(codebook_hosa.centroid_cb, codebook_hosa.variance_cb, ...
    codebook_hosa.skewness_cb, M, P, BS, power, img);
    
    frame_HOSA_feats = sparse(frame_HOSA_feats);
    frame_score = liblinearpredict(1, frame_HOSA_feats', hosa_live_model);

    if i==1
        HOSA_scores = frame_score;
    else
        HOSA_scores(i,:)= frame_score;
    end
end

end
