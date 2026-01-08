import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

#Tweaked Lat & Long for SF and NY so they'd be inset on the map
cities = pd.DataFrame({
    "city": ["New York", "San Francisco", "Chicago", "Dallas"],
    "lat": [40.7128, 37.7749, 41.8781, 32.7767 ],
    "lon": [-75.0060, -121.42, -87.6298, -96.7970 ]
})

# There may be a better map source, but it worked for this
usa = gpd.read_file(
    "https://naturalearth.s3.amazonaws.com/110m_cultural/ne_110m_admin_0_countries.zip"
)

usa = usa[usa["NAME"] == "United States of America"]

# Convert cities to GeoDataFrame
gdf_cities = gpd.GeoDataFrame(
    cities,
    geometry=gpd.points_from_xy(cities.lon, cities.lat),
    crs="EPSG:4326"
)

fig, ax = plt.subplots(figsize=(12, 8))

# Plot US map
usa.plot(
    ax=ax,
    color="#1F77B4", #dark blue
    edgecolor="white"
)

#F2F2F2  # light gray
# Plot cities
gdf_cities.plot(
    ax=ax,
    color="#FFFFFF",      # white
    markersize=150        # really big dots
)

# Optional city labels (too busy, so commented out)
#for x, y, label in zip(cities.lon, cities.lat, cities.city):
#    ax.text(x + 0.5, y + 0.3, label, fontsize=10)

ax.set_title("Major U.S. Cities", fontsize=16)
ax.axis("off")

plt.tight_layout()
plt.show()

