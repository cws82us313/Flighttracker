import json
import requests

def track_plane(flight_number):
    """
    This function takes a flight number as input and returns information
    about the current location of the plane.
    """

    # Replace 'XXX' with your own API key
    API_KEY = 'XXX'

    # Set the base URL for the API endpoint
    API_URL = 'https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/'

    # Set the parameters for the API request
    params = {
        'appId': API_KEY,
        'flightId': flight_number,
        'utc': True,
        'numHours': 1
    }

    # Make the API request and store the response
    response = requests.get(API_URL, params=params)

    # Parse the JSON data from the response
    data = json.loads(response.text)

    # Get the current latitude and longitude of the plane
    latitude = data['flightStatus']['position']['latitude']
    longitude = data['flightStatus']['position']['longitude']

    # Return the latitude and longitude of the plane
    return latitude, longitude

# Example: track flight AA123
lat, lon = track_plane('AA123')
print('Latitude:', lat)
print('Longitude:', lon)