# Rest API Python ML

API to predict if a person has heart disease.

---

## Dependencies

-   Python 3.9 or Higher

Make sure that you have all of the required dependencies installed before running the script. You can install the required dependencies by running the following command:

```python
pip install -r requirements.txt
```

## Usage

To train the model run the following command (only if the pkl files do not exist):

```python
python model.py
```

To start the server run the following command:

```python
python app.py
```

## To make a new prediction

The API only accepts the POST method.

You can use Postman or Insomnia REST to make a prediction.

The base URL:

```
localhost:3000/v1/predict
```

To make a new predict with JS:

```javascript
const data = [
    {
        age: 49,
        diabetes: 0,
        high_blood_pressure: 1,
        sex: 0,
        smoking: 0,
    },
];

fetch("http://localhost:3000/v1/predict", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
})
    .then((response) => response.json())
    .then((response) => console.log(response))
    .catch((err) => console.error(err));
```

The server will return the following:

```javascript
[
    {
        Prediction: 1,
    },
];
```
