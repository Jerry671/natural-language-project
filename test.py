import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
path = "E:\\Mechine_training data\\soc-pokec-relationships.txt"

relation = pd.read_table(path, sep=' ', header=None)