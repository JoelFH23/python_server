from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import pickle

def train_model() -> None:
    try:
        feature_names = ["age","anaemia","diabetes","high_blood_pressure","sex","smoking"]
        target_variable = 'DEATH_EVENT'
        
        dataframe = pd.read_csv('datasets/heart_failure.csv')
        
        X = dataframe[feature_names].values
        y = dataframe[target_variable].values
        
        test_size=0.2
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        accuracy = accuracy_score(y_test, y_pred)
        print("Accuracy: {:.2f}%".format(accuracy * 100))
        
        # New prediction
        """ new_pred = [[ 46, 1, 1, 0, 0 ]]
        y_pr = random_forest.predict(new_pred)
        print(f"New predict: {y_pr}") """
       
        with open('random_forest_clf.pkl', "wb") as f:
            pickle.dump(model, f)
    
    except Exception as ex:
        print(ex)

train_model()