from flask import Flask, jsonify, request
from models import load_data, filter_data

app = Flask(__name__)

# Load the CSV data when the app starts
data, df = load_data('NWMP_DATA_2022-12-14.csv')

@app.route('/')
def home():
    return "Water Body Monitoring API"

# API route to fetch all data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    return jsonify(data)

# API route to filter data by parameters (temp, ph, conductivity, etc.)
@app.route('/api/data/filter', methods=['GET'])
def filter_by_params():
    # Get query params
    filters = {
        'temp': request.args.get('temp'),
        'ph': request.args.get('ph'),
        'conductivity': request.args.get('conductivity'),
        'bod': request.args.get('bod'),
        'coliform': request.args.get('coliform'),
        'fluoride': request.args.get('fluoride'),
        'arsenic': request.args.get('arsenic')
    }

    # Filter data using the model's function
    filtered_data = filter_data(df, filters)

    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
