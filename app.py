import csv
import io

from flask import Flask, jsonify, request
from models import load_data

app = Flask(__name__)

# Load the CSV data when the app starts
data, df = load_data("data.csv")
df = df.dropna(how="all", axis=0)


@app.route("/")
def home():
    return "Water Body Monitoring API"


# API route to fetch all data
@app.route("/api/data/fetch_all", methods=["GET"])
def get_all_data():
    return jsonify(data)


@app.route("/api/data/write", methods=["POST"])
def upload_csv():
    # Check if 'csv_data' is present in the request (this assumes 'csv_data' is a POST parameter)
    csv_data = request.form.get("csv_data")

    if not csv_data:
        return jsonify({"error": "No CSV data provided"}), 400

    try:
        # Use io.StringIO to treat the CSV string as a file-like object
        csv_reader = csv.reader(io.StringIO(csv_data))

        # Append the parsed CSV data to the local CSV file
        with open("data.csv", mode="a", newline="") as f:
            writer = csv.writer(f)
            for row in csv_reader:
                writer.writerow(row)

        return jsonify({"message": "CSV data processed and stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
