# Bengaluru House Price Predictor

This is a Machine Learning-based web application that predicts the price of houses in Bengaluru, India, based on user inputs such as location, square footage, number of bedrooms (BHK), and number of bathrooms. The model is trained on real estate data and deployed with a user-friendly web interface.

## Features

- Predict house prices instantly based on input features
- Trained on real-world Bengaluru house pricing dataset
- Lightweight front-end built with HTML, CSS, and JavaScript
- Python backend using Flask (served via REST API)
- Deployed on AWS (via EC2 or similar)
- Includes Jupyter Notebook for training and experimentation

## Web App Screenshot

![House Price Predictor Screenshot](screenshot.png)

## Dataset

The dataset used for training this model is publicly available and can be downloaded from:

**[Bengaluru House Price Data - Kaggle](https://www.kaggle.com/datasets/amitabhajoy/bengaluru-house-price-data)**

## Project Structure

```
HousePricePredictor/
├── client/                          # Frontend files (HTML, CSS, JS)
│   ├── app.html
│   ├── app.css
│   └── app.js
│
├── model/                           # ML model and artifacts
│   └── Bengaluru_House_Data.pickle
│
├── notebook/                        # Jupyter Notebook for training and EDA
│   └── bhp.ipynb
│
├── server.py                        # Flask backend script
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Files to ignore in version control
├── README.md                        # Project documentation
└── screenshot.png                   # Web UI screenshot
```

## How it Works

1. User inputs the location, square footage, BHK, and number of bathrooms.
2. The frontend sends this data to the backend via an API call.
3. The backend uses a trained machine learning model to predict the house price.
4. The predicted price is returned and displayed to the user.

## Installation (Local)

```bash
git clone git@github.com:Faizan-Ali-Memon/House-price-predictor.git
cd HousePricePredictor
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

## Deployment

To deploy this project on AWS:

- Set up an EC2 instance or use AWS Elastic Beanstalk
- Install required packages
- Upload your project and run `server.py`
- Open necessary ports
- Use public IP or domain to access the application

## Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas, NumPy
- HTML/CSS/JavaScript
- Jupyter Notebook
- AWS (EC2)

**Author:** Faizan Ali Memon
