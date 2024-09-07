import csv
import io
import os

from flask import Flask, jsonify, request
from models import filter_data, load_data

app = Flask(__name__)

# Load the CSV data when the app starts
data, df = load_data("NWMP_DATA_2022-12-14.csv")


@app.route("/")
def home():
    return "Water Body Monitoring API"


# API route to fetch all data
@app.route("/api/data/fetch_all", methods=["GET"])
def get_all_data():
    return jsonify(data)


# API route to filter data by parameters (temp, ph, conductivity, etc.)
@app.route("/api/data/filter", methods=["GET"])
def filter_by_params():
    # Get query params
    filters = {
        'station_code': request.args.get('station-code'),
        'location': request.args.get('location'),
        'temperature_min': request.args.get('temperature-min'),
        'temperature_max': request.args.get('temperature-max'),
        'ph_min': request.args.get('ph-min'),
        'ph_max': request.args.get('ph-max'),
        'conductivity_min': request.args.get('conductivity-min'),
        'conductivity_max': request.args.get('conductivity-max'),
        'coliform_min': request.args.get('coliform-min'),
        'coliform_max': request.args.get('coliform-max'),
        'dissolved_solids_min': request.args.get('dissolved-solids-min'),
        'dissolved_solids_max': request.args.get('dissolved-solids-max'),
        'fluoride_min': request.args.get('fluoride-min'),
        'fluoride_max': request.args.get('fluoride-max'),
        'arsenic_min': request.args.get('arsenic-min'),
        'arsenic_max': request.args.get('arsenic-max'),
    }

    # Filter data using the model's function
    filtered_data = filter_data(df, filters)

    return jsonify(filtered_data)


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
        with open("NWMP_DATA_2022-12-14.csv", mode="a", newline="") as f:
            writer = csv.writer(f)
            for row in csv_reader:
                writer.writerow(row)

        return jsonify({"message": "CSV data processed and stored successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
