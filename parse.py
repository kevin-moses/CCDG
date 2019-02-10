#parse thru CHNS INPUT and create adjacency list
# coding: utf-8
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from collections import defaultdict
import networkx as nx
import json
import time
# py.tools.set_credentials_file(username='kevinmoses', api_key='••••••••••')

start_time = time.time()

#setup adjacency list
G = nx.DiGraph()

#file opening and reading
filename = "chns_input.txt"
file = open(filename, "r", encoding="utf8")

for line in file:
    arr = line.split()
    #split traditional into chars
    c = list(arr[0])
    if (len(c) == 1):
        if c[0] != ', ':
            G.add_node(c[0])
    else:
        length = len(c)
        #deals with chengyu, phrases
        for i in range(0, length-1):
            #append eliminate duplicates
            if c[i+1] != ', ':
                G.add_edge(c[i], c[i+1])

# graph_str = json.dumps(graph, ensure_ascii=False).encode('utf8')
# data = (json.loads(graph_str))
N = nx.number_of_nodes(G)
intE = nx.number_of_edges(G)
E = G.edges()


#graph
pos=nx.spring_layout(G) 


Xv=[pos[k][0] for k in pos]
Yv=[pos[k][1] for k in pos]
Xed=[]
Yed=[]
for edge in E:
    Xed+=[pos[edge[0]][0],pos[edge[1]][0], None]
    Yed+=[pos[edge[0]][1],pos[edge[1]][1], None] 
    
trace3= go.Scattergl(x=Xed,
               y=Yed,
               mode='lines',
               line=dict(color='rgb(210,210,210)', width=1),
               hoverinfo='none'
               )
trace4 = go.Scattergl(x=Xv,
               y=Yv,
               mode='markers',
               name='net',
               marker=dict(symbol='circle-dot',
                             size=5, 
                             color='#6959CD',
                             line=dict(color='rgb(50,50,50)', width=0.5)
                             ),
               hoverinfo='text'
               )

data1=[trace3, trace4]
fig1= go.Figure(data=data1)

#final output
plotly.offline.plot(fig1, filename='CCDG_SMALL_GRAPH')
print(str(N) + " nodes")
print(str(intE) + " edges")
print("--- %s seconds ---" % (time.time() - start_time))