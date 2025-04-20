ML API with FastAPI

This project demonstrates how to build a simple Machine Learning API using FastAPI, scikit-learn, and a pre-trained model. The API allows to send data for predictions based on Iris dataset.

Here is how it works - 
1. This API wraps a logistic regression model trained on the Iris dataset (from sklearn).
2. The model is exposed as a prediction API through FastAPI.
3. Users can POST data to the /predict endpoint to receive model predictions.


