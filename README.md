# NYC Airbnb Price Prediction

A Machine Learning project that analyzes Airbnb listings in New York City and predicts estimated nightly prices using listing characteristics and location data.

## Project Overview

This project uses the Airbnb NYC 2019 dataset to explore pricing patterns, perform exploratory data analysis (EDA), train regression models, and build an interactive Streamlit application for price prediction.

## Objectives

- Analyze Airbnb listing prices and distributions.
- Explore relationships between price, location, room type, and listing characteristics.
- Train and compare regression models.
- Evaluate predictions using MAE, RMSE, and R².
- Deploy an interactive price prediction application.

## Dataset

**Dataset:** Airbnb NYC 2019

The dataset contains 48,895 listings and 16 columns, including:

- Neighbourhood group and neighbourhood
- Latitude and longitude
- Room type
- Price
- Minimum nights
- Number of reviews
- Reviews per month
- Host listing count
- Availability throughout the year

## Tech Stack

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Streamlit
- Joblib
- Pytest

## Machine Learning Models

The following models were evaluated:

1. Linear Regression
2. Random Forest Regressor
3. Random Forest with a log-transformed target

### Model Comparison

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | $70.70 | $186.05 | 0.135 |
| Random Forest | $64.77 | $182.71 | 0.166 |
| Random Forest (Log Target) | $55.63 | $177.25 | 0.215 |

The Random Forest model trained on log-transformed prices achieved the best results among these experiments.

## Project Structure

```text
airbnb-nyc-mlops/
├── data/
├── models/
├── notebooks/
├── src/
│   ├── __init__.py
│   └── predict.py
├── tests/
│   └── test_pipeline.py
├── app.py
├── requirements.txt
└── README.md
```

## Installation

Clone or download this repository, then navigate to the project directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

## Run Tests

Execute the automated tests:

```bash
python -m pytest tests/test_pipeline.py -v
```

## Key Findings

- Location coordinates were among the most important features in the Random Forest model.
- Room type and neighbourhood information helped capture pricing differences.
- Airbnb prices were right-skewed, with some very expensive listings.
- The log-target experiment improved the observed test-set metrics compared with the initial models.

## Limitations

The best model achieved an R² of 0.215 on the test set, so its predictive performance remains limited. Predictions are estimates, not guaranteed market prices. Results may be affected by extreme prices, missing information, and the limitations of the 2019 dataset.

## Future Improvements

- Tune model hyperparameters.
- Perform cross-validation.
- Improve feature engineering.
- Add prediction monitoring and experiment tracking.
- Deploy the application online.

## Disclaimer

This project is for educational and portfolio purposes. The dataset represents Airbnb listings from 2019 and may not reflect current market prices.