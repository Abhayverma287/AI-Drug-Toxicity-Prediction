import joblib

# Load trained model
model = joblib.load("models/target_model.pkl")

def predict_disease(score, gene_code):

    features = [[score, gene_code]]

    prediction = model.predict(features)

    return prediction[0]