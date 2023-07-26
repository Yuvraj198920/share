import folium

# Preferred areas data for each city
preferred_areas = {
    'Utrecht': [
        {'area': 'Oudwijk', 'location': [52.0913, 5.1273]},
        {'area': 'Vogelenbuurt', 'location': [52.1040, 5.1146]},
        {'area': 'Griftpark', 'location': [52.1097, 5.1245]},
        {'area': 'Wittevrouwen', 'location': [52.0969, 5.1315]},
        {'area': 'Lombok', 'location': [52.0919, 5.0906]}
    ],
    'Rotterdam': [
        {'area': 'Witte de Withstraat', 'location': [51.9208, 4.4774]},
        {'area': 'Kralingen', 'location': [51.9219, 4.5110]},
        {'area': 'Kop van Zuid', 'location': [51.9061, 4.4881]},
        {'area': 'Oude Noorden', 'location': [51.9368, 4.4772]},
        {'area': 'Delfshaven', 'location': [51.9113, 4.4430]}
    ],
    'Amsterdam': [
        {'area': 'Canal Ring', 'location': [52.3702, 4.8952]},
        {'area': 'Jordaan', 'location': [52.3774, 4.8818]},
        {'area': 'De Pijp', 'location': [52.3540, 4.8973]},
        {'area': 'Oud-West', 'location': [52.3679, 4.8662]},
        {'area': 'Amsterdam Zuid', 'location': [52.3437, 4.8628]}
    ]
}

# Create the map centered at Utrecht
map_center = [52.0907, 5.1214]
map_Utrecht = folium.Map(location=map_center, zoom_start=13)

# Create the map centered at Rotterdam
map_center = [51.9194, 4.4799]
map_Rotterdam = folium.Map(location=map_center, zoom_start=13)

# Add markers for preferred areas in Rotterdam
for area_data in preferred_areas['Rotterdam']:
    folium.Marker(location=area_data['location'], popup=area_data['area'], icon=folium.Icon(color='green')).add_to(map_Rotterdam)

# Save the map as an HTML file
map_Rotterdam.save('Rotterdam_Map.html')

# Create the map centered at Amsterdam
map_center = [52.3680, 4.9036]
map_Amsterdam = folium.Map(location=map_center, zoom_start=13)

# Add markers for preferred areas in Amsterdam
for area_data in preferred_areas['Amsterdam']:
    folium.Marker(location=area_data['location'], popup=area_data['area'], icon=folium.Icon(color='red')).add_to(map_Amsterdam)

# Save the map as an HTML file
map_Amsterdam.save('Amsterdam_Map.html')