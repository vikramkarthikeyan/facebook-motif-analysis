import pandas as pd

FILE = "Yale4/Yale4.edgelist"
OUTFILE = "Yale4/Yale4_bidirectional_unknown.edgelist"
METADATA = "Yale4/Yale4.nodelist"


with open(FILE, "r") as f:
    edges = f.readlines()

with open(METADATA, 'r') as f:
    nodes = f.readlines()
 
nodes = pd.read_csv(METADATA, delimiter="\t")
print(len(nodes))
print(nodes.loc[0, :]["gender"])

# print(nodes.groupby(['gender']).count())

with open(OUTFILE, "w") as f:
    for edge in edges:
        edge_split = edge.split()
        left = int(edge_split[0])
        right = int(edge_split[1])
        if nodes.loc[left, :]["gender"] == 0 and nodes.loc[right, :]["gender"] == 0:
        # if True:
            f.write(edge_split[0]+"\t"+edge_split[1]+"\n")
            f.write(edge_split[1]+"\t"+edge_split[0]+"\n")