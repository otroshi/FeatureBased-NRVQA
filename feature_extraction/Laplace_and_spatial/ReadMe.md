This is the code for extraction of Laplacian and spatial filters for all frames of each video in the KonVid-k database[1].

To Run the code:
- Either, run `feature_extraction_singleThread.py` to calculate Laplacian and spatial features for each video in the KonVid-k database[1] using *single thread* processing.
```
$ python feature_extraction_singleThread.py
```
- Or,   run `feature_extraction_MultiThread.py` to calculate Laplacian and spatial features for each video in the KonVid-k database[1] using *multi-thread* processing.
```
$ python feature_extraction_MultiThread.py
```

[1] Hosu, Vlad, Franz Hahn, Mohsen Jenadeleh, Hanhe Lin, Hui Men, Tam�s Szir�nyi, Shujun Li, and Dietmar Saupe. "The Konstanz natural video database (KoNViD-1k)." In 2017 Ninth International Conference on Quality of Multimedia Experience (QoMEX), pp. 1-6. IEEE, 2017.
