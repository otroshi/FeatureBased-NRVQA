## Merge features
To merge the features,
you need to have all extracted features in separate folders:
- `CORNIA_features`
- `HOSA_features`
- `Laplace_and_sobel`
- `csv_files (final)`

Then, you can run the following code to merge the features:
```
python python2-convert.py
python python2-tags.py
```

 After running the code, you will have two files:
- `tags.npy`: which indicates each of the feature belongs to which group of feature reported in the paper.
- `all_selected_features.npy`: which includes all 611 features and the ground-truth MOS.
