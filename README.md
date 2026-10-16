# Breast Cancer Detection Using Machine Learning

A machine learning web application that predicts breast cancer malignancy based on cell features using a pre-trained classification model.

## Overview

This project uses a trained ML model to classify breast cancer tumors as benign or malignant based on 9 key cell features. Built with Flask for the web interface.

### Youtube Explanation : https://youtu.be/TzkyqZhNCEo?si=hUnDeC1UAWyQylKN

## Features

- Web-based input form for cell feature values
- Real-time prediction using pre-trained ML model
- Clean, responsive UI with separate result pages
- 9 feature classification (clump thickness, cell size, cell shape, etc.)

## Tech Stack

- **Backend**: Flask (Python)
- **ML Model**: Pre-trained classifier (pickle format)
- **Frontend**: HTML templates
- **Libraries**: NumPy, Pandas, scikit-learn

## Installation

```bash
pip install -r requirements.txt
python app.py
```

## Usage

1. Run the application: `python app.py`
2. Open browser at `http://127.0.0.1:5000/`
3. Enter the 9 cell feature values
4. Submit to get prediction (Benign or Malignant)

## Project Structure

```
├── app.py                  # Main Flask application with prediction logic
├── model.pkl               # Pre-trained ML model
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html          # Input form
│   ├── yes.html            # Malignant result page
│   └── no.html             # Benign result page
└── README.md               # This file
```

## Model Features

The model uses the following 9 features for prediction:

1. Clump Thickness
2. Uniform Cell Size
3. Uniform Cell Shape
4. Marginal Adhesion
5. Single Epithelial Cell Size
6. Bare Nuclei
7. Bland Chromatin
8. Normal Nucleoli
9. Mitoses

## Prediction Output

- **Output = 4**: Malignant (cancerous) - renders `yes.html`
- **Output ≠ 4**: Benign (non-cancerous) - renders `no.html`

---

## Credits


Maintained by **Rajgopal Pandilwar**.
