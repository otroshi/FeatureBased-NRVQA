function result = smooth_with_memory(a,framerate,window_time)
    window_size = framerate * window_time;
    std= (2*window_size-1)/12;
    
    filter=0;
    for i=1:window_size
       filter(i)=exp(-(i^2/(2*std^2)));
    end
    
    b=0;
    for i=1:size(a)
        
        sum_scores = 0;
        sum_weights=0;
        
        if (i-window_size)<1
            aa=a(1:i);
        else
            aa=a(i-window_size:i);
        end
        aa=flip(sort(aa));
        
        for j=1:size(aa,2)
            sum_scores = sum_scores + aa(j)*filter(j);
            sum_weights = sum_weights + filter(j);
            if (i-j)==1
                break
            end
        end
        
        score = sum_scores/sum_weights;
        b(i) =score;
    end
    result=b;
end