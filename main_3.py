base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):

    global total_trip

    total_trip = total_trip + 1

    trip_price = base_rate + (distance_km * price_per_km)

    return trip_price
