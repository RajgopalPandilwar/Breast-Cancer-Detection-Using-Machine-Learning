import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load the pre-trained breast cancer classification model
# This model.pkl was created locally from trusted training data, so pickle deserialization is safe
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/')
def home():
    """Render the home page with the input form for cell features."""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict breast cancer malignancy based on submitted cell features.
    Returns 'yes.html' if malignant (output == 4), 'no.html' if benign.
    """
    # Extract integer values from the submitted form
    input_features = [int(x) for x in request.form.values()]
    features_value = [np.array(input_features)]

    # Define feature names matching the model's training data
    features_name = ['clump_thickness', 'uniform_cell_size', 'uniform_cell_shape',
                     'marginal_adhesion', 'single_epithelial_size', 'bare_nuclei',
                     'bland_chromatin', 'normal_nucleoli', 'mitoses']

    # Create DataFrame with proper column names for model prediction
    df = pd.DataFrame(features_value, columns=features_name)

    # Make prediction using the loaded model
    output = model.predict(df)

    # Classify result: 4 = Malignant, otherwise Benign
    if output == 4:
        return render_template('yes.html')   # Malignant (cancerous)
    else:
        return render_template('no.html')    # Benign (non-cancerous)


if __name__ == "__main__":
    app.run()
