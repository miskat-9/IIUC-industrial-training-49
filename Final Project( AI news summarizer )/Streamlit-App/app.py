import streamlit as st
import requests

# Base URL of your FastAPI app
BASE_URL = "http://localhost:8001"

# Function to fetch data from FastAPI
def fetch_data(endpoint, params=None):
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None

def post_data(endpoint, json_data):
    try:
        response = requests.post(f"{BASE_URL}{endpoint}", json=json_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error posting data: {e}")
        return None

# Streamlit app
st.title("News Management System")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = ["Home", "Add News", "View Categories", "View News", "Get News Summary"]
choice = st.sidebar.selectbox("Choose an option", options)

if choice == "Home":
    st.write("Welcome to the News Management System!")
    st.write("Use the sidebar to navigate through the options.")

elif choice == "Add News":
    st.header("Add News Article")
    url = st.text_input("Enter the news URL")
    if st.button("Submit"):
        response = post_data("/news/", {"url": url})
        if response:
            st.success(f"News article successfully posted. ID: {response['news_id']}")
        else:
            st.error("Failed to post news article.")

elif choice == "View Categories":
    st.header("Categories")
    categories = fetch_data("/categories/")
    if categories:
        st.write(categories)
    else:
        st.error("Failed to retrieve categories.")

elif choice == "View News":
    st.header("News Articles")
    news = fetch_data("/news/")
    if news:
        st.write(news)
    else:
        st.error("Failed to retrieve news articles.")

elif choice == "Get News Summary":
    st.header("Get News Summary")
    news_id = st.number_input("Enter the News ID", min_value=1)
    if st.button("Get Summary"):
        summary = fetch_data(f"/news/{news_id}/summary")
        if summary:
            st.write(f"Summary for News ID {news_id}:")
            st.write(summary['summary'])
        else:
            st.error("Failed to retrieve summary.")
