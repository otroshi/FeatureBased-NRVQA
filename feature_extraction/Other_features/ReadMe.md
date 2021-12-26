This is the code for extraction of several features for each video in the KonVid-k database.

To Run the code:
You only need to run the `main.py` as follows:
```
python main.py
```
The results are stored in `/csv_files (final)` directory.

**Note:** In some of the functions matlab engine is used. To use the MATLAB engine you need to 
		first install the MATLAB(2017b or latter) on Linux. Next, you should install its 
		engine for python. To do so, fisrt off, find the path to the MATLAB folder. Start MATLAB
		and type `matlabroot` in the command window. Copy the path returned by `matlabroot`.
		Then, on Mac or Linux systems run:
		```
		cd "matlabroot/extern/engines/python"
		sudo python setup.py install
		```
**Note:** In `compute_BRISQUE_fetures()`, `compute_VBLINDS_fetures()` and `compute_VIIDEO_fetures()` functions (in `feature_extraction.py`)
	some user-defined MATLAB functions are used. You should add thier directory to MATLAB path in 
	MATLAB program (in set path).
	
	
**Note:** For the MATLAB implementations of BRISQUE, VBLINDS, and VIIDEO, we used the corresponding codes from their authers.

