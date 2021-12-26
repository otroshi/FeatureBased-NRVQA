function all_scores = get_BRISQUE_scores(vidfilename)
% This code use brisque() function which is pre-defined in MATLAB 2017b.
% This finction[-->get_BRISQUE_scores(vidfilename)] returns BRISQUE score(a NR-IQA)
%      for each frame all in an array in sequence.

    video=VideoReader(vidfilename);
    f=0;
    while hasFrame(video)
        f = f+1;
        vidFrame = readFrame(video);
        score = brisque(vidFrame);

        all_scores(f) = score;
    end
 
end
