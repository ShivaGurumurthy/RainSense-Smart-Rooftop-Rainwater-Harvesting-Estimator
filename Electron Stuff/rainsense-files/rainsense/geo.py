from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="rainsense_project")

def get_district_state(location_name):
    try:
        location = geolocator.geocode(location_name, addressdetails=True, language="en")
        if not location or "address" not in location.raw:
            return None, None

        address = location.raw["address"]

        # Extract district
        district = (address.get("county") or
                    address.get("state_district") or
                    address.get("city") or
                    address.get("region"))
        state = address.get("state")

        # Corrections (custom mapping)
        corrections = {
            "Alandur": "Chennai",
            "Tambaram": "Chennai",
            "Poonamallee": "Tiruvallur",
            "Thane": "Mumbai Suburban"
        }
        if district in corrections:
            district = corrections[district]

        return district, state
    except Exception as e:
        print("Error during geocoding:", e)
        return None, None
