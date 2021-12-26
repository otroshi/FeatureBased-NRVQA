This is the code for extraction of CORNIA[1] scores, NR-IQA algorithm, for all frames of each video in the KonVid-k database[2].
We used the original implementation of CORNIA[1] from its authors. 

To Run the code:
1. First, run `VidReader_to_mat.m` to prepare videos in mat format.
2. Second, run `Extract_CORNIA_from_KonVid1k.m` to Extract CORNIA scores from every frames. This code will save the result as a mat-file in `CORNIA_scores.mat`.
3. Finally, run `python mat_to_pickle.py` to convert `CORNIA_scores.mat` to pickle files (stored at `/CORNIA_features`).

[1] Ye, Peng, Jayant Kumar, Le Kang, and David Doermann. "Unsupervised feature learning framework for no-reference image quality assessment." In 2012 IEEE Conference on Computer Vision and Pattern Recognition, pp. 1098-1105. IEEE, 2012.
[2] Hosu, Vlad, Franz Hahn, Mohsen Jenadeleh, Hanhe Lin, Hui Men, Tamás Szirányi, Shujun Li, and Dietmar Saupe. "The Konstanz natural video database (KoNViD-1k)." In 2017 Ninth International Conference on Quality of Multimedia Experience (QoMEX), pp. 1-6. IEEE, 2017.