from time import time
from graph import *
from fiduccia_matthyeses import fm

writeGraph()
file_name = input('Enter the file name to read the graph: ')
adj_list = readGraph(file_name.strip())
print("Adjacency List:")
for node in adj_list:
    print(f"{node}: {adj_list[node]}")

start_time  = time()
fm(len(adj_list), adj_list)
end_time = time()

print("Time taken: ", (end_time - start_time) * 1000, "ms")
