from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

def train_model() -> None:
    try:
        feature_names = ["age","high_blood_pressure","sex","smoking"]
        target_variable = 'DEATH_EVENT'
        
        dataframe = pd.read_csv('datasets/heart_failure.csv')
        
        X = dataframe[feature_names].values
        y = dataframe[target_variable].values
        
        test_size=0.2
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        
        logistic_regression = LogisticRegression()
        # Fit the model to the training data
        logistic_regression.fit(X_train, y_train)
        # Evaluate the model on the testing data
        y_pred = logistic_regression.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy * 100))
        
        with open("logistic_regression.pkl", "wb") as f:
            pickle.dump(logistic_regression, f)
    
    except Exception as ex:
        print(ex)

train_model()