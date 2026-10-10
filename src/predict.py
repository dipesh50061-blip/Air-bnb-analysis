
import joblib
import numpy as np
import pandas as pd
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Saved model path
MODEL_PATH = PROJECT_ROOT / "models" / "airbnb_price_model.pkl"


def load_model():
    """Load the trained Airbnb price prediction model."""
    return joblib.load(MODEL_PATH)


def predict_price(model, listing_data):
    """
    Predict Airbnb nightly price in dollars.

    listing_data must contain the same feature columns
    used during model training.
    """
    if isinstance(listing_data, dict):
        listing_data = pd.DataFrame([listing_data])

    log_price = model.predict(listing_data)
    predicted_price = np.expm1(log_price)

    return max(0.0, float(predicted_price[0]))


if __name__ == "__main__":
    model = load_model()

    sample_listing = {
        "neighbourhood_group": "Manhattan",
        "neighbourhood": "Midtown",
        "room_type": "Entire home/apt",
        "latitude": 40.75,
        "longitude": -73.98,
        "minimum_nights": 1,
        "number_of_reviews": 10,
        "reviews_per_month": 1.0,
        "calculated_host_listings_count": 1,
        "availability_365": 180
    }

    price = predict_price(model, sample_listing)
    print(f"Predicted nightly price: ${price:.2f}")
