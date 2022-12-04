""" J'ai mis tout et n'importe quoi là dessus """
import graph_tool.all as gt
import matplotlib
from numpy.random import random
SIZE = 400
V_SIZE = SIZE/20
E_PWIDTH = V_SIZE/4
'''g = gt.load_graph("PathwayCommons12.reactome.BIOPAX.graphml")
pos = gt.sfdp_layout(g)
tree = gt.min_spanning_tree(g)
u = gt.GraphView(g, efilt=tree)
gt.graph_draw(u, pos=pos, output="triang_min_span_tree.pdf")

toy_ex = load_graph("toy_example.graphml")
graph_draw(toy_ex, vertex_text=toy_ex.vertex_properties["_graphml_vertex_id"], output_size=(800, 800))

for vertex in toy_ex.vertices():
# affiche les sommets voisins de chq sommets
for vertex in g.vertices():
    print(f"Voisin du sommet {vertex} : ")
    for neighbor in vertex.all_neighbors():
        print('Sommet : ', neighbor)
'''

# génére un graphe
g, pos = gt.triangulation(random((500, 2)) * 4, type="delaunay")
tree = gt.min_spanning_tree(g)
gt.graph_draw(g, pos=pos, edge_color=tree)

# affiche le 'minimum spanning tree'..
g.set_edge_filter(tree)
gt.graph_draw(g, pos=pos)

# Epaisseur des edges et couleur des noeuds en fonction de la betweenness
bv, be = gt.betweenness(g)
be.a /= be.a.max() / 5
gt.graph_draw(g, pos=pos, vertex_fill_color=bv, edge_pen_width=be)
