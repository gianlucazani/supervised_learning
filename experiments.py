import queue

import pandas as pd

from assignment2.classifiers.k_nearest_neighbours import classify_nn
from assignment2.classifiers.naive_bayes import classify_nb
from assignment2.stratified_folds_generation.stratified_cross_selection import generate_stratified_folds
from classes.ReverseFixedSizePriorityQueue import ReverseFixedSizePriorityQueue
from assignment2.classifiers import k_nearest_neighbours, naive_bayes
# import time

training_set = pd.read_csv("data/pima-indians-diabetes.csv", header=None)
testing_set = pd.read_csv("data/test_set_knn.csv", header=None)
# print(classify_nn(training_set, testing_set, 10))
print(classify_nb(training_set, testing_set))
# print(naive_bayes.classify_nb("data/pima-indians-diabetes.csv", "data/test_set_knn.csv"))
# data_set = pd.read_csv("./data/test_stratified_folds.csv", header=None)
# generate_stratified_folds(data_set, 2)
