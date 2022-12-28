# Naive Bayes Theorm and Probability Calculator using the 
# titanic.csv data set found at https://www.kaggle.com/competitions/titanic/data?select=train.csv
# This program can find 
# 1. The total number of passengers fitting a feature,
# 2. The probabillity of any given passenger possessing a certain quality
# 3. The probability of an event given another event
# 
# Created By Karl Poulson, Dec 26 2022

import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the file and convert to a pandas data frame
df = pd.read_csv('train.csv')

# Probability of a feature happening (rarity) takes the mean
def P(feature0, condition0, denominator):
    i = 0
    for index, person in df.iterrows():
        try:
            if (person[feature0] == condition0):
                i = i + 1
        except:
            print("error")
    return i / denominator

# Probability of feature A and feature B happening
# Takes the Union. Inputs a feature dataset like Survived[]
# and for each person, compares if Suvived[] == condition (like 0 or 1)
# Set denominator to 1 to get the number of a certain condition
def pAandB(featureA, conditionA, featureB, conditionB, denominator):
    i = 0
    for index, person in df.iterrows():
        try:
            if (person[featureA] == conditionA) and (person[featureB] == conditionB):
                i = i + 1
        except:
            print("error")
    return i / denominator

def bayes(A, B, BA):
    return (A * BA) / B


# Total Probabilities
totalPassengers = len(df)
totalSurvivors = P("Survived", 1, 1)


print("Survival given a Sex:")
print("Probability of Survival given Female: %s" % 
    bayes( P("Survived", 1, totalPassengers), 
    P("Sex", "female", totalPassengers), 
    pAandB("Survived", 1, "Sex", "female", totalSurvivors)))

print("Probability of Surviving given Male: %s" %
    bayes( P("Survived", 1, totalPassengers),
    P("Sex", "male", totalPassengers),
    pAandB("Survived", 1, "Sex", "male", totalSurvivors)))


print("Survival given a Class: ")
print("Probabiliy of Survival given First Class: %s" %
    bayes( P("Survived", 1, totalPassengers),
    P("Pclass", 1, totalPassengers),
    pAandB("Survived", 1, "Pclass", 1, totalSurvivors)))

print("Probabiliy of Survival given First Class: %s" %
    bayes( P("Survived", 1, totalPassengers),
    P("Pclass", 2, totalPassengers),
    pAandB("Survived", 1, "Pclass", 2, totalSurvivors)))

print("Probabiliy of Survival given First Class: %s" %
    bayes( P("Survived", 1, totalPassengers),
    P("Pclass", 3, totalPassengers),
    pAandB("Survived", 1, "Pclass", 3, totalSurvivors)))


