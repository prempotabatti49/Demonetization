# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 18:20:16 2019

@author: premp
"""


#Calculating Adjacency matrix

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd

file = pd.read_csv("users_matrix.csv")
file.head()
file = file.drop(columns = ['Unnamed: 0','Unnamed: 11298'])
file = np.array(file)

# Steps to calculate adjacency matrix 
# 1. Form a nxn blank matrix
# 2. For j >= i; calculate cosine similarity
# 3. If A[i,j] < threshold then set A[i,j] = 0
# 4. Set diagonal values = 0
# 5. Ensure that

##############################
#calculating cosine similarity
#a = np.array([1,2,0])
#b = np.array([-1,0.5,0])
#d = np.array([5,0,3])

#mat = np.vstack((d, np.vstack((a,b))))
cos_sim = cosine_similarity(file)
cos_sim = pd.DataFrame(cos_sim)
cos_sim.to_csv("cosine.csv")


threshold = 0.01

#converting cosine similarity matrix into adjacency matrix
cos_sim[abs(cos_sim) > threshold ] = 1
cos_sim[abs(cos_sim) <= threshold] = 0

mat = cos_sim
mat= np.array(mat)
#setting diagonal elements equal to zero
for i in range(mat.shape[0]):
    mat[i,i] = 0


######################################
#Networkx code to form a graph of nodes
import networkx as nx
import matplotlib.pyplot as plt


#instantiate the graph
G = nx.Graph()
#H = nx.complete_graph(100)
#I = nx.gnp_random_graph(20, 0.5)   => random Graph
#J = nx.DiGraph()                   => Directed Graph
#k = nx.circular_layout()

#add nodes
for i in range(mat.shape[0]):
    G.add_node(i+1)    #nodes from 1 to n

#add edges
for i in range(mat.shape[0]):
    for j in range(i, mat.shape[1]):
        if mat[i,j] == 1:
            G.add_edge(i+1, j+1)

#G.nodes() to check all the nodes
#G.edges() to check all the edges
 
nx.draw(G, with_labels = True)

#getting degrees of all nodes
print(G.degree)

#number of nodes
print("number of nodes: ", G.order())

#Number of Edges
print("number of edges: ", G.size())

#Network degree histogram
print(nx.degree_histogram(G))




