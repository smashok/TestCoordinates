from geopy.distance import geodesic

current_coord = (50.603694,30.650625)

distance_west_meters = 93.53
bearing_west = 270  #западное направление

distance_south_meters = 13.36
bearing_south = 180  #южное направление

new_coord_west = geodesic(kilometers=distance_west_meters / 1000).destination(current_coord, bearing_west)
new_coord_final = geodesic(kilometers=distance_south_meters / 1000).destination(new_coord_west, bearing_south)

print("Новые координаты:", new_coord_final.latitude, new_coord_final.longitude)