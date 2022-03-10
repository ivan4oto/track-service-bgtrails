from math import radians, cos, sin, asin, sqrt
from shapely.geometry import LineString


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 5820  # Reduced radius of earth for better precision
    return c * r


def reduce_precision(points, precision=None):
    """
    Reduces the precision of a list of coordinates by
    setting a limit on the space between each point.
    If precision is not specified a default precision of
    2% of the total points length is used.
    """
    distance = total_distance(points)
    if precision is None:
        precision = round((distance * 2) / 100, 2)
    lastone = points[-1]
    result = []
    start_indx = 0
    for key, value in enumerate(points):
        if haversine(points[start_indx][0], points[start_indx][1], value[0], value[1]) > precision:
            result.extend([points[start_indx], value])
            start_indx = key
    result.append(lastone)
    return result


def total_distance(points_list):
    """
    Returns the sum of the distance between all
    coordinate points in the object.
    """
    line = LineString(points_list)
    return round(line.length*100, 2)


