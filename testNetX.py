import networkx as nx
import matplotlib.pyplot as plt
#%matplotlib inline

edgeFile =  open('edges.csv', 'rb')
G = nx.read_edgelist(edgeFile, delimiter = ',', create_using=nx.Graph(), nodetype=str)
#print type(G)
print nx.info(G)
#G.add_node(file)

#G.add_node('Calin')
#print(G.nodes())
#G.add_edge('Matt','Jenny')
#G.add_edge('Matt', 'Calin')
#G.add_edge('Jenny', 'Calin')
nx.draw(G)
plt.show()
    





    # Now we have Headers and nodes objects
