
import pandas as pd
import pytest

from src.predict import load_model, predict_price


@pytest.fixture
def model():
    return load_model()


@pytest.fixture
def sample_listing():
    return {
        "neighbourhood_group": "Manhattan",
        "neighbourhood": "Midtown",
        "room_type": "Entire home/apt",
        "latitude": 40.75,
        "longitude": -73.98,
        "minimum_nights": 1,
        "number_of_reviews": 10,
        "reviews_per_month": 1.0,
        "calculated_host_listings_count": 1,
        "availability_365": 180,
    }


def test_model_loads(model):
    assert model is not None


def test_prediction_is_numeric(model, sample_listing):
    price = predict_price(model, sample_listing)

    assert isinstance(price, float)


def test_prediction_is_finite(model, sample_listing):
    import math

    price = predict_price(model, sample_listing)

    assert math.isfinite(price)


def test_prediction_is_non_negative(model, sample_listing):
    price = predict_price(model, sample_listing)

    assert price >= 0


def test_prediction_accepts_dataframe(model, sample_listing):
    listing_df = pd.DataFrame([sample_listing])

    price = predict_price(model, listing_df)

    assert isinstance(price, float)
