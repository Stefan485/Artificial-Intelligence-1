# Exercises 10

In this exercises we are solving the problem of binary classification on the Titanic dataset. We use knowledge that we acquaired from previous exercises to preprocess the data and create the data splits that are needed to properly train and test the models. We train and test the same algorithms that we used in the previous exercises and compare their performance. For better representability of the results we use k-fold cross validation. After choosing one of the algorithms we use hyperparater tuning to extract the best possible rersults, which we are measuring with standard metrics for classification tasks (accuracy, precision, recall, f1 score). Then, finally, we are using the trained model to make predictions on the test set and submit them to the Kaggle competition.

This dataset is available on Kaggle as a part of Kaggle competition [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic/overview). There you can submit all of your generated predictions on the test set and see your score on the world leaderboard. I encourage you to try to further improve results from the exercises and submit them to the competition.

## Files

- `titanic_template.ipynb` - notebook with the template for this exercises
- `titanic_solution.ipynb` - notebook with the solution for this exercises (still not fully completed - we will finish it in the next exercises)
- `titanic_dataset/` - folder with the dataset for this exercises