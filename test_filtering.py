"""
Ok là à partir du toy example, j'arrive à afficher uniquement les sommets avec un degree supérieur à 2
J'ai toujours pas compris comment afficher correctement la figure ... il y a un argument "pos" mais aucune idée"
"""

from graph_tool import GraphView
from graph_tool.all import graph_draw, load_graph
SIZE = 400
V_SIZE = SIZE/10
E_PWIDTH = V_SIZE/4

g = load_graph("toy_example.graphml")

'''# select some vertices
vfilt = g.new_vertex_property('bool')
vfilt[0] = True
vfilt[1] = True
vfilt[3] = True
'''

for vertex in g.vertices():
    print(f"Voisin du sommet {vertex} : ")
    print(f"Degree de {vertex} : {vertex.out_degree()}")
    print(f"Degree de {vertex} : {vertex.in_degree()}")
    for neighbor in vertex.all_neighbors():
        print('Sommet : ', neighbor)

# ils différencient les degree in et out jsp pourquoi. mais du coup j'ai fait la somme
u = GraphView(g, vfilt=lambda v: v.out_degree() + v.in_degree() > 2)

# graph non trié
graph_draw(g, output_size=(SIZE, SIZE), vertex_text=g.vertex_index)

# graph filtré avec uniquement les vertices avec un degree supérieurs à 2
graph_draw(u, output_size=(SIZE, SIZE), vertex_text=g.vertex_index)

