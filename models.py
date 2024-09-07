import pandas as pd

# Load CSV data into a DataFrame and convert to dictionary
def load_data(csv_file_path):
    df = pd.read_csv(csv_file_path)
    data = df.to_dict(orient='records')
    return data, df

# Function to filter data based on parameters
def filter_data(df, filters):
    filtered_data = df.copy()

    # Apply filters if provided
    if filters['temp']:
        filtered_data = filtered_data[filtered_data['Temperature'] == float(filters['temp'])]
    if filters['ph']:
        filtered_data = filtered_data[filtered_data['pH'] == float(filters['ph'])]
    if filters['conductivity']:
        filtered_data = filtered_data[filtered_data['Conductivity'] == float(filters['conductivity'])]
    if filters['bod']:
        filtered_data = filtered_data[filtered_data['BOD'] == float(filters['bod'])]
    if filters['coliform']:
        filtered_data = filtered_data[filtered_data['Coliform'] == float(filters['coliform'])]
    if filters['fluoride']:
        filtered_data = filtered_data[filtered_data['Fluoride'] == float(filters['fluoride'])]
    if filters['arsenic']:
        filtered_data = filtered_data[filtered_data['Arsenic'] == float(filters['arsenic'])]

    return filtered_data.to_dict(orient='records')
