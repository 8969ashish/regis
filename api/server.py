from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)

# Function to load data from the GitHub raw URL
def load_data():
    try:
        # Replace with your GitHub raw URL
        url = "https://raw.githubusercontent.com/8969ashish/flask-data/refs/heads/main/data.json"
        response = requests.get(url)
        response.raise_for_status()  # Raise error if request fails
        return response.json()  # Parse JSON response
    except Exception as e:
        print(f"Error loading data: {e}")
        return []  # Return an empty list if there's an error

# Load data when the application starts
data = load_data()

# Current index tracker
current_index = 0

@app.route('/data', methods=['GET'])
def get_data():
    global current_index
    if not data:
        return jsonify({"error": "No data available"}), 404  # If data is empty or failed to load

    # Return data of the current index
    response_data = data[current_index]

    # Increment index and reset if it exceeds data length
    current_index = (current_index + 1) % len(data)

    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True, port=3000)
