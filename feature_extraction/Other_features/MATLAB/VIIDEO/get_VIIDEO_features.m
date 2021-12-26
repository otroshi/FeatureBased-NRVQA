function [VIIDEO_features]=  get_VIIDEO_features(vidfilename)

blocksizerow     = 18;
blocksizecol     = 18;
filtlength1      = 7;
filtlength2      = 7;
filtlength       = [filtlength1 filtlength2];
blockrowoverlap  = 8;
blockcoloverlap  = 8;

readerobj = VideoReader(vidfilename, 'tag', 'myreader1');

framenumber = get(readerobj, 'numberOfFrames');

width  = readerobj.Width;
height = readerobj.height;

VIIDEO_features_corrs   =  compute_VIIDEO_features(vidfilename,height,width, ...
                     	   	framenumber,blocksizerow,blocksizecol,...
                     		blockrowoverlap,blockcoloverlap,filtlength);

VIIDEO_features = VIIDEO_features_corrs';

end
