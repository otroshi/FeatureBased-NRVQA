## Experiment 5: [Extra Trees] MDI Feature Importance
In another experiment, we train an Extra Trees regressor with all
the extracted features and find the importance of each feature according to the number of splits in the trees. For this end, we calculate the
mean decrease impurity (MDI) score  over all trees in the trained
regressor.

To run this experiment, you can use the notebook available in this directory.


**Note:** To run this experiment, you need the merged features (`tags.npy` and  `all_selected_features.npy`) as described in [Merge Features](../../merge_features).
