from graph_tool.all import *

toy_ex = load_graph("toy_example.graphml")
graph_draw(toy_ex, output_size=(800, 800))

for vertex in toy_ex.vertices():
    print(f"Voisin du sommet {vertex} : ")
    for neighbor in vertex.all_neighbors():
        print('Sommet : ', neighbor)

