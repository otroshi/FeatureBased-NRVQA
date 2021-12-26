This is the code for extraction of HOSA[1] scores, NR-IQA algorithm, for all frames of each video in the KonVid-k database[2].
We used the original implementation of HOSA[1] from its authors. 

To Run the code:
1. First, run `calculate_HOSA_scores.py` to calculate HOSA scores for all frames of each video in the KonVid-k database[2].
2. Second, run `HOSA_scores_to_HOSA_features.m` to calculate 6 features for each video from the frame-level HOSA scores. This code will save the result as pickle files in `/HOSA_features` directory.

[1] Xu, Jingtao, Peng Ye, Qiaohong Li, Haiqing Du, Yong Liu, and David Doermann. "Blind image quality assessment based on high order statistics aggregation." IEEE Transactions on Image Processing 25, no. 9 (2016): 4444-4457.
[2] Hosu, Vlad, Franz Hahn, Mohsen Jenadeleh, Hanhe Lin, Hui Men, Tamás Szirányi, Shujun Li, and Dietmar Saupe. "The Konstanz natural video database (KoNViD-1k)." In 2017 Ninth International Conference on Quality of Multimedia Experience (QoMEX), pp. 1-6. IEEE, 2017.