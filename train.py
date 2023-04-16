""" from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score """


""" 
    feature_names = ["Glucose","BloodPressure","SkinThickness","Insulin"]
    target_variable = 'Outcome'
    
    dataframe = pd.read_csv('diabetes.csv')
    
    X = dataframe[feature_names].values
    y = dataframe[target_variable].values
    
    test_size=0.2
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    
    clf = LogisticRegression()
    # Fit the model to the training data
    clf.fit(X_train, y_train)
    # Evaluate the model on the testing data
    y_pred = clf.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print("Accuracy: {:.2f}%".format(accuracy * 100)) """