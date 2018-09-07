import numpy as np
import pandas as pd

def accuracy_score(truth, pred):
  """ Returns accuracy score for input truth and predictions. """

  # Ensure that the number of predictions matches number of outcomes
  if len(truth) == len(pred):

    print((truth == pred))
    print((truth == pred).mean())

    # Calculate and return the accuracy as a percent
    return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

  else:
    return "Number of predictions does not match number of outcomes!"

def predictions_1(data):
  """ Model with one feature:
          - Predict a passenger survived if they are female. """

  predictions = []
  for _, passenger in data.iterrows():
    if passenger['Sex'] == 'female':
      predictions.append(1)
    else:
      predictions.append(0)

  # Return our predictions
  return pd.Series(predictions)

def main():
  in_file = 'titanic_data.csv'
  full_data = pd.read_csv(in_file)
  print(full_data.head())

  outcomes = full_data['Survived']
  data = full_data.drop('Survived', axis = 1)

  predictions = predictions_1(data)

main()