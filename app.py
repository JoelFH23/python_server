from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Page Not Found</h1>", 404

@app.route('/v1/predict', methods=['POST'])
def predict():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        try:
            with open('logistic_regression.pkl', 'rb') as f:
                random_forest = pickle.load(f)
            
            data = request.json
            
            if not isinstance(data, list):
                raise TypeError("Data must be a list.")
            
            if not len(data) == 1:
                raise ValueError("Data must be equal to 1")
            
            data = data[0]
            
            if not all(isinstance(value, int) and value >= 0 for value in data.values()):
                raise TypeError("The dictionary values must be non-negative integers")
            
            specific_keys = ["age","diabetes","high_blood_pressure","sex","smoking"]
            if not all(key in data for key in specific_keys):
                raise ValueError("The dictionary does not contain all the specific keys")
            
            if not all( specific_keys[i] == key for i, key in enumerate(data.keys())):
                raise ValueError("The dictionary does not contains the keys in the specified order")
            
            new_data = [ value for value in data.values() ]
            pred = random_forest.predict(pd.DataFrame([new_data]))
            
            return [{ "Prediction": int(pred[0]) }], 200
        
        except ValueError as ve:
            return jsonify([{ "error": str(ve) }]), 400
        except TypeError as te:
            return jsonify([{ "error": str(te) }]), 400
        except Exception as ex:
            print(ex)
            return "An error occurred. Please try again later!", 400
    else:
        return "Content type is not supported.", 400

if __name__ == "__main__":
    app.run(port=3000, debug=True)
