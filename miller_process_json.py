"""
Process a JSON file to bike stations by their region ID and save the result.

JSON file is in the format where stations is a list of dictionaries with numerous keys regarding the NYC CitiBike program.

{
    "data": {
        "stations": [
            {
                "external_id": "0f98907a-d4cc-45e0-b174-7d9dfda74106",
                "eightd_has_key_dispenser": false,
                "short_name": "6711.13",
                "lat": 40.75905795418586,
                "capacity": 32,
                "rental_uris": {
                    "ios": "https://bkn.lft.to/lastmile_qr_scan",
                    "android": "https://bkn.lft.to/lastmile_qr_scan"
                },
                "station_type": "classic",
                "has_kiosk": true,
                "name": "Steinway St & Broadway",
                "electric_bike_surcharge_waiver": false,
                "station_id": "0f98907a-d4cc-45e0-b174-7d9dfda74106",
                "rental_methods": [
                    "KEY",
                    "CREDITCARD"
                ],
                "region_id": "71",
                "eightd_station_services": [],
                "lon": -73.91897544264793
            }
        ]
    }
    "last_updated": 1738005142,
    "ttl": 60,
    "version": "1.1"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import json

# Import from local project modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

fetched_folder_name: str = "data"
processed_folder_name: str = "data_processed"

#####################################
# Define Functions
#####################################

def count_stations_by_region_id(file_path: pathlib.Path) -> dict:
    """Count the number of stations with each region ID from a JSON file."""
    try:
        with file_path.open('r') as file:
            # Use the json module load() function 
            # to read data file into a Python dictionary
            station_dictionary = json.load(file)  
            # initialize an empty dictionary to store the counts
            station_counts_dictionary = {}
            # stations is a list of dictionaries in the JSON file
            station_list: list = station_dictionary.get("data", {}).get("stations", [])
            for bike_dictionary in station_list:  
                region = bike_dictionary.get("region_id", "Unknown")
                station_counts_dictionary[region] = station_counts_dictionary.get(region, 0) + 1
            return station_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {}

def process_json_file():
    """Read a JSON file, count stations by region ID, and save the result."""
    input_file: pathlib.Path = pathlib.Path(fetched_folder_name, "NYCbike.json")
    output_file: pathlib.Path = pathlib.Path(processed_folder_name, "bike_regions.txt")
    
    region_counts = count_stations_by_region_id(input_file)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    with output_file.open('w') as file:
        file.write("Bike Stations by Region ID:\n")
        for region, count in region_counts.items():
            file.write(f"{region}: {count}\n")
    
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")