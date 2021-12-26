clear all

csv=readtable('KoNViD_1k_attributes.csv');

for i=1:1200
    i
    filename = char(csv(i,3).file_name);
    filedir  = strcat('KoNViD_1k_videos\',filename);
    v = VideoReader(filedir);
    
    vid_frames = -ones(540,960,260);
    
    frame=0;
    while hasFrame(v)
        frame = frame+1;
        img = readFrame(v);
        img = rgb2gray(img);
        if size(img,2)==540
            img = reshape(img,[540,960]);
        end
        vid_frames(:,:,frame)=img;
    end
    
    vid_frames(1,1,260) = csv(i,4).MOS;
    vid_frames(1,2,260) = frame;
    vid_frames(1,3,260) = v.FrameRate;
    vid_frames(1,4,260) = v.Duration;
    
    save(strcat('mat\',filename(1:end-4)),'vid_frames');
end