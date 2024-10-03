import pandas as pd
from pyproj import Proj, transform

# Load the CSV file
file_path = 'Traffic Count Locations.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Define the Vicgrid projection (EPSG: 7899) and WGS84 projection (EPSG: 4326)
vicgrid_proj = Proj(init='EPSG:7899')
wgs84_proj = Proj(init='EPSG:4326')


# Function to convert coordinates
def convert_coordinates(row):
    x = row['X']
    y = row['Y']
    longitude, latitude = transform(vicgrid_proj, wgs84_proj, x, y)
    return pd.Series({'latitude': latitude, 'longitude': longitude})

# Apply the conversion to each row in the DataFrame
data[['latitude', 'longitude']] = data.apply(lambda x: convert_coordinates(x), axis=1)

# Drop the original x and y columns (optional)
data = data.drop(columns=['X', 'Y'])

# Save the updated DataFrame back to CSV
data.to_csv('updated_file.csv', index=False)  # Replace with the desired output file name