import matplotlib.pyplot as plt
import numpy as np
import math
import json


def Sierpinski(n):
	centro = [int(3**n/2), int(3**n/2)]
	return centro

def get_points(pair,n):
	return [
		
		[pair[0]-3**n,pair[1]+3**n],
		[pair[0],pair[1]+3**n],
		[pair[0]+3**n,pair[1]+3**n],
	
	
		[pair[0]-3**n,pair[1]],
		[None,None],
		[pair[0]+3**n,pair[1]],
	
	
		[pair[0]-3**n,pair[1]-3**n],
		[pair[0],pair[1]-3**n],
		[pair[0]+3**n,pair[1]-3**n]
	]

	
def calculo_puntos_centrales(n,puntos,first=True):
	print(puntos)
	if first:
		return calculo_puntos_centrales(n-1,get_points(puntos,n),False)
	else:
		if n == 0:
			return puntos
		else:
			points = []
			for element in puntos:
				if element[0]!= None:
					points.append(calculo_puntos_centrales(n-1,get_points(element,n),False))
# calculo_puntos_centrales(2,[40,40],False)
# [40,40]
# [[0,1][0,1][0,1][0,1][0,1][0,1][0,1][0,1][0,1]]

print(json.dumps(calculo_puntos_centrales(2,[13,13]),indent=4))


