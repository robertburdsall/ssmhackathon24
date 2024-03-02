from altair import LayerSpec
import geopandas as gpd
import fiona

layerslist = []
for layer in fiona.listlayers('Resources/NC_Northern_slr_final_dist.gdb/'):
    layerslist.append(layer)

print(gpd.read_file("Resources/NC_Northern_slr_final_dist.gdb/", driver='FileGDB', layer=0))
