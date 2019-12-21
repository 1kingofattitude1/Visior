from routingpy import MapboxValhalla
from pprint import pprint

# Some locations in Berlin
coords = [[13.413706, 52.490202], [13.421838, 52.514105],
          [13.453649, 52.507987], [13.401947, 52.543373]]
client = MapboxValhalla(api_key="pk.eyJ1IjoibGxoYXJpc2hsbCIsImEiOiJjazQ4NDJiN3YwNDhyM25wcjNiYXE4amtiIn0.GnNhtTCRQktOCNmS4WI9LQ")

route = client.directions(locations=coords, profile='pedestrian')
isochrones = client.isochrones(locations=coords[0], profile='pedestrian', intervals=[600, 1200])
matrix = client.matrix(locations=coords, profile='pedestrian')

pprint((route.geometry, route.duration, route.distance, route.raw))
pprint((isochrones.raw, isochrones[0].geometry, isochrones[0].center, isochrones[0].interval))
pprint((matrix.durations, matrix.distances, matrix.raw))