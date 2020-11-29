import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import networkx.readwrite.pajek
G=nx.Graph()
#filename="F:\\git\\NRP\\soc-pokec-relationships.txt"
filename="F:\\git\\NRP\\Network-relation-prediction\\test.txt"
edges = pd.read_table(filename, header=None, sep='\n')
for i in range(len(edges)):
    coordinate = edges[0][i].split()
    G.add_edge(coordinate[0],coordinate[1])
print(G.number_of_nodes())
print(networkx.readwrite.pajek.generate_pajek(G))
nx.write_pajek(G,"test.net")
#nx.draw(G)
#plt.show()
