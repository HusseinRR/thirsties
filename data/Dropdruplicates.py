import pandas as pd

train = pd.read_csv('X_train_Hi5.csv', sep = ';')

train = train.drop_duplicates()

train.to_csv('train-data.csv', sep = ';', index = False)
