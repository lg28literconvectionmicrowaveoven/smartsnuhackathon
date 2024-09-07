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
    if filters['station_code']:
        filtered_data = filtered_data[filtered_data['Station Code'] == filters['station_code']]
    
    if filters['location']:
        filtered_data = filtered_data[filtered_data['Location'].str.contains(filters['location'], case=False, na=False)]

    # Temperature filter (min/max)
    if filters['temperature_min']:
        filtered_data = filtered_data[filtered_data['Temperature'] >= float(filters['temperature_min'])]
    if filters['temperature_max']:
        filtered_data = filtered_data[filtered_data['Temperature'] <= float(filters['temperature_max'])]

    # pH filter (min/max)
    if filters['ph_min']:
        filtered_data = filtered_data[filtered_data['pH'] >= float(filters['ph_min'])]
    if filters['ph_max']:
        filtered_data = filtered_data[filtered_data['pH'] <= float(filters['ph_max'])]

    # Conductivity filter (min/max)
    if filters['conductivity_min']:
        filtered_data = filtered_data[filtered_data['Conductivity'] >= float(filters['conductivity_min'])]
    if filters['conductivity_max']:
        filtered_data = filtered_data[filtered_data['Conductivity'] <= float(filters['conductivity_max'])]

    # Coliform filter (min/max)
    if filters['coliform_min']:
        filtered_data = filtered_data[filtered_data['Coliform'] >= float(filters['coliform_min'])]
    if filters['coliform_max']:
        filtered_data = filtered_data[filtered_data['Coliform'] <= float(filters['coliform_max'])]

    # Dissolved Solids filter (min/max)
    if filters['dissolved_solids_min']:
        filtered_data = filtered_data[filtered_data['Dissolved Solids'] >= float(filters['dissolved_solids_min'])]
    if filters['dissolved_solids_max']:
        filtered_data = filtered_data[filtered_data['Dissolved Solids'] <= float(filters['dissolved_solids_max'])]

    # Fluoride filter (min/max)
    if filters['fluoride_min']:
        filtered_data = filtered_data[filtered_data['Fluoride'] >= float(filters['fluoride_min'])]
    if filters['fluoride_max']:
        filtered_data = filtered_data[filtered_data['Fluoride'] <= float(filters['fluoride_max'])]

    # Arsenic filter (min/max)
    if filters['arsenic_min']:
        filtered_data = filtered_data[filtered_data['Arsenic'] >= float(filters['arsenic_min'])]
    if filters['arsenic_max']:
        filtered_data = filtered_data[filtered_data['Arsenic'] <= float(filters['arsenic_max'])]

    return filtered_data.to_dict(orient='records')
