
import streamlit as st
from src.predict import load_model, predict_price

st.set_page_config(
    page_title="NYC Airbnb Price Predictor",
    page_icon="🏠",
    layout="centered"
)

@st.cache_resource
def get_model():
    return load_model()

model = get_model()

st.title("🏠 NYC Airbnb Price Predictor")
st.write("Predict the estimated nightly price of an Airbnb listing in NYC.")

st.subheader("Listing Details")

borough = st.selectbox(
    "Borough",
    ["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]
)

room_type = st.selectbox(
    "Room Type",
    ["Entire home/apt", "Private room", "Shared room"]
)

neighbourhood = st.text_input(
    "Neighbourhood",
    value="Midtown"
)

col1, col2 = st.columns(2)

with col1:
    latitude = st.number_input(
        "Latitude",
        min_value=40.4,
        max_value=41.0,
        value=40.75,
        format="%.6f"
    )

with col2:
    longitude = st.number_input(
        "Longitude",
        min_value=-74.3,
        max_value=-73.6,
        value=-73.98,
        format="%.6f"
    )

minimum_nights = st.number_input(
    "Minimum Nights",
    min_value=1,
    value=1
)

number_of_reviews = st.number_input(
    "Number of Reviews",
    min_value=0,
    value=10
)

reviews_per_month = st.number_input(
    "Reviews per Month",
    min_value=0.0,
    value=1.0
)

host_listings = st.number_input(
    "Host Listing Count",
    min_value=1,
    value=1
)

availability = st.slider(
    "Availability (Days per Year)",
    min_value=0,
    max_value=365,
    value=180
)

if st.button("Predict Price", type="primary"):
    listing = {
        "neighbourhood_group": borough,
        "neighbourhood": neighbourhood,
        "room_type": room_type,
        "latitude": latitude,
        "longitude": longitude,
        "minimum_nights": minimum_nights,
        "number_of_reviews": number_of_reviews,
        "reviews_per_month": reviews_per_month,
        "calculated_host_listings_count": host_listings,
        "availability_365": availability
    }

    try:
        price = predict_price(model, listing)

        st.success(f"Estimated nightly price: ${price:.2f}")
        st.caption(
            "This is a model estimate, not a guaranteed Airbnb price."
        )

    except Exception as error:
        st.error(f"Prediction failed: {error}")

