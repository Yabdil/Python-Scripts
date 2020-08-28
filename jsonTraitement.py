import json
import os

file = open('Covid_Data.json')
jsonEncode = json.load(file)
output_GeoJson = {'type': 'FeatureCollection','features':[]}
jsonFeatures = jsonEncode['features']
for feature in jsonFeatures:
    for props in feature['properties']:
        new_dict = {}
        if props != 'QUARTIER':
            properties = {}
            properties['date'] = props
            properties['QUARTIER'] = feature['properties']['QUARTIER']
            properties['cas_confirmes'] = feature['properties'][props]
            new_dict['type'] = 'feature'
            new_dict['properties'] = properties
            new_dict['geometry'] = feature['geometry']
            output_GeoJson['features'].insert(len(output_GeoJson['features']), new_dict)
print(output_GeoJson)
           
with open('{fileOutput}.geojson', 'w') as file:
    json.dump(output_GeoJson, file)
