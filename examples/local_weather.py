from pprint import pprint

import bomapi

# Find a location
results = bomapi.location_search("Wollongong")
result = results[0]
pprint(result)

# Create a location instance and query local info
location = bomapi.Location(result)
pprint(location.info())
pprint(location.warnings())
pprint(location.observations())
pprint(location.forcast_daily())
pprint(location.forcast_3_hourly())
