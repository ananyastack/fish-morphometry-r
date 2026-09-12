import folium
from folium.plugins import MousePosition

# 1. Initialize a small, compact base map (NO API KEYS REQUIRED)
m = folium.Map(location=[22.85, 88.45], zoom_start=10, tiles='OpenStreetMap')

# 2. Add your three exact thesis station dots
sites = [
    {"name": "Kalyani Hub", "coord": [22.9743, 88.4354], "color": "blue"},
    {"name": "Gayeshpur Hub", "coord": [22.9622, 88.4891], "color": "green"},
    {"name": "Barasat Hub", "coord": [22.7232, 88.4861], "color": "red"}
]

for site in sites:
    folium.CircleMarker(
        location=site["coord"],
        radius=10,
        popup=site["name"],
        color="black",
        weight=2,
        fill=True,
        fill_color=site["color"],
        fill_opacity=0.9
    ).add_to(m)

# 3. ADDITIONS ONLY: Coordinates tracking and a clean vector North Arrow
MousePosition(
    position="topright",
    separator=" | ",
    lng_first=False,
    num_digits=4,
    prefix="Lat/Long Ticks:"
).add_to(m)

compass_html = """
<div style="position: fixed; top: 20px; left: 80px; width: 40px; height: 50px; 
            z-index:9999; font-size:16px; font-family: 'Arial', sans-serif; 
            font-weight: bold; color: #2c3e50; text-align: center;
            background: rgba(255, 255, 255, 0.8); padding: 5px; border-radius: 4px;
            border: 1px solid #bdc3c7;">
    ↑<br><span style="font-size:12px;">N</span>
</div>
"""
m.get_root().html.add_child(folium.Element(compass_html))

# 4. Render the compact map layout cleanly inside your notebook window
m
