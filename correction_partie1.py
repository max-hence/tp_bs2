"""
Correction partie 1
"""

from graph_tool import GraphView
from graph_tool.all import graph_draw, load_graph, betweenness, label_out_component, find_vertex
SIZE = 400
V_SIZE = SIZE/10
E_PWIDTH = V_SIZE/4

# Question 2 : Charger le fichier toy_example.graphml
g = load_graph("toy_example.graphml")
g.set_directed(False)
graph_draw(g,
    vertex_text=g.vertex_properties["_graphml_vertex_id"],
    output_size=(SIZE, SIZE),
)

# Question 3 : Ajouter des sommets

# add vertices
id = g.vertex_properties["_graphml_vertex_id"]
name = g.vertex_properties["name"]
v12 = g.add_vertex()
id[v12] = 12
name[v12] = "P012"

v13 = g.add_vertex()
id[v13] = 13
name[v13] = "P013"

v4 = g.vertex(4)
print(id[v4]) # quand on fait vertex(4) on a le 5e ...

# add edges
g.add_edge(g.vertex(4), v13)
g.add_edge(v12, v13)

graph_draw(g,
    vertex_text=g.vertex_properties["_graphml_vertex_id"],
    output_size=(SIZE, SIZE),
)

# Question 4 : Afficher les sommets qui ont un degré = 2
for vertex in g.vertices():
    if vertex.out_degree() == 2:
        print(f"Prot {id[vertex]} \"{name[vertex]}\" has 2 neighboors")


# Question 5: Colorer les sommets en fonction de la betweenness
bv, be = betweenness(g)
print([betweenness for betweenness in bv])
graph_draw(g,
    vertex_fill_color=bv,
    vertex_text=g.vertex_properties["_graphml_vertex_id"],
    output_size=(SIZE, SIZE),
)


# Question 6 : Afficher que la composante connexe associée au sommet Expression of APOA1

vertex = find_vertex(g=g, prop=g.vertex_properties["name"], match="assembly of PLCG1:Ca2+")[0]
l = label_out_component(g, vertex)
print(l.a)
u = GraphView(g, vfilt=l)
graph_draw(u,
    vertex_text=g.vertex_properties["_graphml_vertex_id"],
)