from graph_tool.all import *

toy_ex = load_graph("toy_example.graphml")
# display toy example
graph_draw(toy_ex, vertex_text=toy_ex.vertex_properties["_graphml_vertex_id"], output_size=(800, 800), output="toy_example.pdf")

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
graph_draw(toy_ex, vertex_text=toy_ex.vertex_properties["_graphml_vertex_id"], output_size=(800, 800))

for vertex in toy_ex.vertices():
    print(f"Voisin du sommet {vertex} : ")
    for neighbor in vertex.all_neighbors():
        print('Sommet : ', neighbor)

new_property = toy_ex.new_vertex_property("test")