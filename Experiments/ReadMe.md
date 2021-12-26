## Experiments
[1. Different Regressors](Different_Regressors)
This experiment investigate the effect of type of regressor on the performance of VQA model.

[2. [Extra Trees] All Combination of Feature ](ExtraTrees_allCombinationFeatures)
In this experiment, we use Extra Trees regressor and evaluate the performance of all possible  feature groups selection.

[3. [Extra Trees] performance of model with up to two subsets of features](ExtraTrees_SoloPairCombination)
In this experiment, we find the performance of Extra Trees regressor model with up to two subsets of features.

[4. [Extra Trees] frequency of appearance in top models ](ExtraTrees_FreqApearanceBetterThanFull)
In this experiment, we find the frequency of appearance of each feature group in Extra Trees regressor models which have better performance than full-feature setup.


[5. [Extra Trees] MDI Feature Importance](ExtraTrees_MDI_FeatureImportance)
In another experiment, we train an Extra Trees regressor with all
the extracted features and find the importance of each feature according to the number of splits in the trees. For this end, we calculate the
mean decrease impurity (MDI) score  over all trees in the trained
regressor.
