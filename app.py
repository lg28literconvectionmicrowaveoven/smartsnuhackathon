import csv
import io

<<<<<<< HEAD
from flask import Flask, jsonify, request
from models import load_data
=======
from flask import Flask,jsonify, render_template, request, redirect, url_for
from models import filter_data, load_data
>>>>>>> 2d4b516 (add webpage)

app = Flask(__name__)

# Load the CSV data when the app starts
data, df = load_data("data.csv")
<<<<<<< HEAD
df = df.dropna(how="all", axis=0)
=======
print(df)
>>>>>>> 2d4b516 (add webpage)


@app.route("/")
def index():
    # Convert DataFrame to HTML table with Tailwind classes
    html_table = df.to_html(classes='min-w-full divide-y divide-gray-200', index=False)
    
    # Render the table in the HTML template
    return render_template('index.html', table=html_table)


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
