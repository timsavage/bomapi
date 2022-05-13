from pprint import pprint

from pybomapi import LocationResult, Location

# print(location_search("Cordeaux Heights"))
l = LocationResult(
    geohash="r3gk01s",
    id="Cordeaux Heights-r3gk01s",
    name="Cordeaux Heights",
    postcode="2526",
    state="NSW",
)
location = Location(l)
pprint(location.info())
pprint(location.warnings())
pprint(location.observations())
pprint(location.forcast_daily())
pprint(location.forcast_3_hourly())
