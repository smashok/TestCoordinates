import math
from geopy.distance import geodesic
from geopy import Point

# Координаты контрольной точки
Lat1 = 50.603694
Lon1 = 30.650625
point_x_center = 558
point_y_center = 328

# Координаты центра изображения
center_x = 320
center_y = 256

# Азимут и количество метров в пикселе
azimut = 335
pixel_coefficient = 0.38

# Ищем расстояние между точками
big_leg = abs(point_x_center - center_x) * pixel_coefficient
small_leg = abs(point_y_center - center_y) * pixel_coefficient
hypotenuse = math.sqrt(big_leg ** 2 + small_leg ** 2)

# Ищем угол между направлением движения дрона и отрезком
cosine_value = small_leg / hypotenuse
angle_rad = math.acos(cosine_value)
angle_deg = math.degrees(angle_rad)

# Ищем азимут направления от контрольной точки до искомой
angle_between_dots = azimut - angle_deg

# Создание объекта Point для контрольной точки
control_point = Point(Lat1, Lon1)

# Вычисление координат
destination = geodesic(kilometers=hypotenuse / 1000).destination(control_point, angle_between_dots)
Lat2, Lon2 = destination.latitude, destination.longitude

# Ссылка на гугл карты и вывод
google_maps_url = f"https://www.google.com/maps?q={Lat2},{Lon2}&t=k"

print(google_maps_url)

