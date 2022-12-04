""" J'ai mis tout et n'importe quoi là dessus """
import graph_tool.all as gt
import matplotlib
from numpy.random import random
SIZE = 400
V_SIZE = SIZE/20
E_PWIDTH = V_SIZE/4

# Load reactome graph
g = gt.load_graph("PathwayCommons12.reactome.BIOPAX.graphml")
pos = gt.sfdp_layout(g)
tree = gt.min_spanning_tree(g)
u = gt.GraphView(g, efilt=tree)
gt.graph_draw(u, pos=pos, output="triang_min_span_tree.pdf")


# Work on toy example
toy_ex = gt.load_graph("toy_example.graphml")
# display toy example
gt.graph_draw(toy_ex, vertex_text=toy_ex.vertex_properties["_graphml_vertex_id"], output_size=(800, 800), output="toy_example.pdf")

# add vertex
v1 = toy_ex.add_vertex()
v2 = toy_ex.add_vertex()
# add edges
e1 = toy_ex.add_edge(v1, v2)

# print source and target of e1
print(f"The source of e1 is : {e1.source()}", ", ", f"The target of e1 is {e1.target()}")
# print degrees
print(f"the degree of v1 is {v1.out_degree()}")

# display modified toy example
gt.graph_draw(toy_ex, vertex_text=toy_ex.vertex_properties["_graphml_vertex_id"], output_size=(800, 800))

for vertex in toy_ex.vertices():
# affiche les sommets voisins de chq sommets
#for vertex in g.vertices():
    print(f"Voisin du sommet {vertex} : ")
    for neighbor in vertex.all_neighbors():
        print('Sommet : ', neighbor)

# génére un graphe
g, pos = gt.triangulation(random((500, 2)) * 4, type="delaunay")
tree = gt.min_spanning_tree(g)
gt.graph_draw(g, pos=pos, edge_color=tree)

# affiche le 'minimum spanning tree'..
g.set_edge_filter(tree)
gt.graph_draw(g, pos=pos)
new_property = toy_ex.new_vertex_property("test")# Epaisseur des edges et couleur des noeuds en fonction de la betweenness
bv, be = gt.betweenness(g)
be.a /= be.a.max() / 5
gt.graph_draw(g, pos=pos, vertex_fill_color=bv, edge_pen_width=be)
