import pandas as pd
from math import radians, sin, cos, sqrt, atan2


def haversine_distance(lat1, lon1, lat2, lon2):

    earth_radius = 6371

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    a = (
        sin(delta_lat / 2) ** 2
        +
        cos(lat1)
        *
        cos(lat2)
        *
        sin(delta_lon / 2) ** 2
    )

    c = 2 * atan2(
        sqrt(a),
        sqrt(1 - a)
    )

    return earth_radius * c


settlements = pd.read_csv(
    "data/settlements.csv"
)

sites = pd.read_csv(
    "data/site.csv"
)


distance_records = []


for _, settlement in settlements.iterrows():

    for _, site in sites.iterrows():

        straight_line_distance = haversine_distance(
            settlement["latitude"],
            settlement["longitude"],
            site["latitude"],
            site["longitude"]
        )

        # Mock road distance.
        # Later replace this with actual routing.
        road_distance = (
            straight_line_distance * 1.35
        )

        # Mock travel time assuming ~35 km/h average.
        travel_time = (
            road_distance / 35
        ) * 60

        distance_records.append({

            "settlement_id":
                settlement["settlement_id"],

            "site_id":
                site["site_id"],

            "straight_line_distance_km":
                round(straight_line_distance, 2),

            "road_distance_km":
                round(road_distance, 2),

            "estimated_travel_time_minutes":
                round(travel_time, 0)

        })


distances = pd.DataFrame(
    distance_records
)


distances.to_csv(
    "data/distances.csv",
    index=False
)


print("distances.csv generated successfully.")

print(distances.head())