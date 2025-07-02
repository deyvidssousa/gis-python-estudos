import geopandas as gpd
import rasterio
import rasterstats
import matplotlib as plt
import pandas as pd

#leitura do arquivo shapefile
caminho_talhao = "01_ndvi_por_talhao/dados/talhao.shp"
talhao = gpd.read_file(caminho_talhao)

#leitura do arquivo raster
caminho_ndvi = "01_ndvi_por_talhao/dados/NDVI_28052025.tiff"
ndvi = rasterio.open(caminho_ndvi)