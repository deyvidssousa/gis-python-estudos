import geopandas as gpd
import rasterio
import rasterstats
import matplotlib as plt
import pandas as pd
import os

caminho_talhao = "dados/talhao.shp"
talhao = gpd.read_file(caminho_talhao)

print(talhao.head())