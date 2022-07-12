## reading the dataframe with chunk size

trafficMAD = pd.DataFrame()
chunksize = 10 ** 6
for chunk in pd.read_csv('/content/drive/MyDrive/THESIS/all_traffic_data.csv', chunksize=chunksize):
  trafficMAD = pd.concat([trafficMAD, chunk])
  nrows = chunk.shape[0]
  print(f'Chunk is uploaded with {nrows} rows succesfully.')
  
############## googlemaps ###############

!pip install googlemaps
import googlemaps

gmaps = googlemaps.Client(key="")

AIzaSyDMNISpkVD4bKVWRWOnIqOB-h_xwJmMf-U

fig = px.scatter_mapbox(merged_trafficMAD, lat='latitude', lon='longitude', hover_name="id", hover_data=["id", "intensity"], 
                        color="intensity",
                        size="intensity", color_continuous_scale=px.colors.sequential.matter, size_max=20,
                        zoom=5, height=1000, mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()



################ google maps api #################
!pip install ipywidgets
!pip install widgetsnbextension
from google.colab import output
import ipywidgets as widgets
from ipywidgets.embed import embed_minimal_html
import IPython
output.enable_custom_widget_manager()

# Use google maps api
gmaps.configure(api_key="AIzaSyDMNISpkVD4bKVWRWOnIqOB-h_xwJmMf-U") 

#Get the locations from the data set
locations = merged_trafficMAD[['latitude', 'longitude']]
#Get the magnitude from the data
weights = merged_trafficMAD['intensity']
#Set up your map
fig = gmaps.figure()
fig.add_layer(gmaps.heatmap_layer(locations, weights=weights))
fig
#embed_minimal_html('export.html', views=[fig])
#IPython.display.HTML(filename="export.html")