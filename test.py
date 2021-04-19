# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 22:33:34 2021

@author: gianc
"""

#====================================================================================================================
#PROYECTO GRAFOS
#====================================================================================================================

import pandas as pd
import networkx as nx
import matplotlib.pyplot as mt
import numpy as np

# impostamos los datos del excel
xlsx = pd.ExcelFile("all_seasons.xlsx") 
datos = xlsx.parse()

# funcion que crea bosques
def crear_bosque(data):
    bosque = nx.Graph()
    counter=0
    aux1=len(data) 
    for m in data:
        bosque.add_node(counter,data=m)
        counter  += 1
    if counter==aux1:
        print("Se creó el bosuqe correctamente")
    else:
        print("Se perdió información")
    return bosque

# sacamos cada una de las columnas
pl_name = datos['player_name']
pl_height = datos['player_height']
pl_weight = datos['player_weight']
pl_gp = datos['gp']
pl_age = datos['age']
pl_pts = datos['pts']
pl_reb = datos['reb']
pl_ast = datos['ast']

# creamos los bosques
bo_nm=crear_bosque(pl_name)
bo_ht=crear_bosque(pl_height)
bo_wh=crear_bosque(pl_weight)
bo_gp=crear_bosque(pl_gp)
bo_age=crear_bosque(pl_age)
bo_pts=crear_bosque(pl_pts)
bo_reb=crear_bosque(pl_reb)
bo_ast=crear_bosque(pl_ast) 


nx.draw_random(bo_gp,node_size = 30 )
mt.savefig ("") # guardar como png 
mt.show () # mostrar

