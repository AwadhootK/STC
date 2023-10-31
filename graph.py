import random

def writeGraph():
    n=int(input('Enter the number of nodes: '))
    file_name=input('Enter file name: ')
    with open(file_name, 'w+') as file:
        for i in range(n):
            for j in range(n):
                if i != j:
                    edge = random.randint(0,1)
                    file.write(str(i) + " ")
                    file.write(str(j) + " ")
                    file.write(str(edge))
                    file.write("\n")

def readGraph(file_name):
    adjacency_list = {}
    with open(file_name, 'r') as file:
        for line in file:
            node1, node2, edge = line.split()
            node1, node2, edge = int(node1), int(node2), int(edge)
            if node1 not in adjacency_list:
                adjacency_list[node1] = []
            if edge == 1:
                if node2 not in adjacency_list[node1]:
                    adjacency_list[node1].append(node2)
            if node2 not in adjacency_list:
                adjacency_list[node2] = []
            if edge == 1:
                if node1 not in adjacency_list[node2]:
                    adjacency_list[node2].append(node1)
    return adjacency_list
