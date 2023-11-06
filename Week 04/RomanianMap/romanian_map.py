
class RomanianMap:

    def __init__(self, straigth_line_distances_filepath, city_connections_filepath):
        self.straigth_line_distances = self.read_straigth_line_distances(straigth_line_distances_filepath)
        self.city_connections = self.read_city_connections(city_connections_filepath)

    def read_straigth_line_distances(self, filepath):
        straigth_line_distances = {}
        with open(filepath) as file:
            for line in file:
                city, distance = line.split(",")
                straigth_line_distances[city.strip()] = int(distance.strip())
        return straigth_line_distances
    
    def read_city_connections(self, filepath):
        city_connections = []
        with open(filepath) as file:
            for line in file:
                city1, city2, path_cost = line.split(",")
                city_connections.append((city1.strip(), city2.strip(), int(path_cost.strip())))
        return city_connections