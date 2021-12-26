# Feature-based No-Reference Video Quality Assessment using Extra Trees
This repository contains the source code to reproduce the  paper **Feature-based No-Reference Video Quality Assessment using Extra Trees**.

## 1. Feature Extraction
The source code to extract features from video files are available at [`./feature_extraction`](feature_extraction) folder. Please check the instruction in [`./feature_extraction/ReadMe.md`](feature_extraction/ReadMe.md) to extract features from video files.
As mentioned in that instruction, after running the files, you will eventually have the following folders containing all extracted features:
- `CORNIA_features`
- `HOSA_features`
- `Laplace_and_sobel`
- `csv_files (final)`

**Note:** In some of the functions (e.g., [`./feature_extraction/Other_features/feature_extraction.py`](feature_extraction/Other_features/feature_extraction.py)),  matlab engine is used. To use the MATLAB engine you need to
		first install the MATLAB(2017b or latter) on Linux. Next, you should install its
		engine for python. To do so, fisrt off, find the path to the MATLAB folder. Start MATLAB
		and type matlabroot in the command window. Copy the path returned by matlabroot.
		Then, on Mac or Linux systems run:

```
$ cd "matlabroot/extern/engines/python"
$ sudo python setup.py install
```
## 2. Merge features
To merge the features please check the instruction in [`./merge_features`](merge_features). After running the code, you will have two files:
- `tags.npy`: which indicates each of the feature belongs to which group of feature as reported in the paper.
- `all_selected_features.npy`: which includes all 611 features and the ground-truth MOS.

## 3. Experiments
Experiments are completely described in [`./Experiments`](Experiments), including:
1. Different Regressors
2. [Extra Trees] All Combination of Feature
3. [Extra Trees] performance of model with up to two subsets of features
4. [Extra Trees] frequency of appearance in top models
5. [Extra Trees] MDI Feature Importance


## Citation
If you found this repository helpful, please don't forget to cite our paper:
```
H. Otroshi-Shahreza, A. Amini, H. Behroozi, "Feature-based No-Reference Video Quality Assessment using Extra Trees", IET Image Processing.
```
In case of any question, please feel free to contact Hatef Otroshi ([hatef.otroshi@epfl.ch](mailto:hatef.otroshi@epfl.ch)).