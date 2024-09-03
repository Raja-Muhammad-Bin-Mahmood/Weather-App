import streamlit as st
import requests

# OpenWeatherMap API configuration
api_key = "ec5dff3620be8d025f51f648826a4ada"  # Replace with your actual OpenWeatherMap API key
lat = 32.6970
lon = 73.3252
url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

# Fetch weather data
response = requests.get(url)
data = response.json()

# Streamlit app
st.set_page_config(page_title="Weather Dashboard for PD Khan", page_icon=":sunny:", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to right, #000000, #004d00); /* Jet black to green gradient */
            color: #00ff00; /* Bright green text */
        }
        .stTitle {
            color: #00ff00; /* Bright green title */
            font-size: 2.5em; /* Larger title size */
            font-family: 'Arial', sans-serif; /* Font for the title */
        }
        .stMarkdown {
            color: #00ff00; /* Bright green text */
            font-family: 'Arial', sans-serif; /* Font for the content */
        }
        .stTable {
            color: #00ff00; /* Bright green table text */
            background: rgba(0, 0, 0, 0.7); /* Slightly transparent black background */
            border-radius: 8px; /* Rounded corners */
            padding: 10px; /* Padding inside table */
        }
        .stCode {
            color: #00ff00; /* Bright green code text */
            background: rgba(0, 0, 0, 0.5); /* Slightly transparent black background */
            border-radius: 4px; /* Rounded corners */
            padding: 5px; /* Padding inside code block */
            font-family: 'Courier New', monospace; /* Font for the code */
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #00ff00; /* Green border */
        }
        th {
            background-color: #003300; /* Darker green for header */
        }
        tr:nth-child(even) {
            background-color: #000000; /* Black for even rows */
        }
        tr:nth-child(odd) {
            background-color: #002200; /* Dark green for odd rows */
        }
    </style>
""", unsafe_allow_html=True)

st.title("Weather Dashboard for PD Khan")
st.write("Live weather data from OpenWeatherMap API")

# Check if data is retrieved successfully
if 'main' in data:
    current_temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    humidity = data['main']['humidity']

    table = f"""
    <table>
        <tr><th>Parameter</th><th>Value</th></tr>
        <tr><td>Temperature</td><td>{current_temp}°C</td></tr>
        <tr><td>Feels like</td><td>{feels_like}°C</td></tr>
        <tr><td>Minimum Temperature</td><td>{min_temp}°C</td></tr>
        <tr><td>Maximum Temperature</td><td>{max_temp}°C</td></tr>
        <tr><td>Humidity</td><td>{humidity}%</td></tr>
    </table>
    """
    st.markdown(table, unsafe_allow_html=True)
else:
    st.error(f"Error: {data.get('message', 'Unexpected error occurred')}")
