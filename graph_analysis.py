import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import argparse as ap

def read_graph(filename):
    return nx.read_gml(filename)

def write_graph(graph, file):
    nx.write_gml(graph, file)

def plot_graph(graph, graph_type):
    pos = nx.spring_layout(graph)
    if graph_type == 'C':

        pass
    if graph_type == 'N':

        pass
    if graph_type == 'P':

        pass
    #nx.draw()
    plt.show(graph)

def clustering_coefficient(graph):
    return nx.clustering(graph)

def neighborhood_overlap(graph):

    pass

def partition_graph(graph, components): # partitions graph based on inputted components
    while nx.number_connected_components(graph) < components: # iterates through components until we reach our desired amount
        betweeness = nx.edge_betweenness_centrality(graph) # networkx function for computing betweeness for edges
        biggest_edge = max(betweeness, edge=betweeness.get) # gets edge w/ highest betweeness
        graph.remove_edge(*biggest_edge) # removes edge w/ highest betweeness
    return graph

def verify_homophily(graph):

    pass

def verify_balanced_graph(graph):
    for triangle in nx.cycle_basis(graph): # networkx function, cycles through different groups of nodes
        if len(triangle) == 3: # ensures 3 edges to make up a triangle
            x,y,z = triangle # each node that makes up triangle
            sign = (graph[x][y]['sign'] * graph[y][z]['sign'] * graph[x][z]['sign']) # takes edges and determines if possitive or negative
            if sign < 0: # if negative, then graph is not balanced, returns False, if possitive, return True
                return False
    return True

def parse_args(): # input arguments & check validation
    parser = ap.ArgumentParser(description='Plots graph based on what parameters you put in, i.e. the graph you input and C N P, also verifies balnce and/or homophily of the graph')
    # desired input for running "./graph_analysis.py": (graph,gml) --components n --plot [C|N|P] --verify_homophily --verify_balanced_graph --output out_graph_file.gml
    parser.add_argument('--file', choices=['homophily.gml','imbalanced_graph.gml','balanced_graph.gml'], help='Choose which graph you would like to use: homophily.gml, imbalanced_graph.gml, or balanced_graph.gml')
    parser.add_argument('--components', type=int, help='Amount of componants, used to partition graph')
    parser.add_argument('--plot', choices=['C','N','P'], help='Which plot you would like: cluster coefficient = C, neighborhood overlap = N, partition = P')
    parser.add_argument('--verify_homophily', action='store_true', help='Checks homophily of graph, returns True or False')
    parser.add_argument('--verify_balanced_graph', action='store_true' help='Checks balance of graph, returns True or False')
    parser.add_argument('--output', type=str, help='Filename for new plotted graph, ex. "out_graph_file.gml"')

    return parser.parse_args()

def main():
    args = parse_args()

    graph = None

    if args.file:
        if args.file == 'homophily.gml':
            graph = 'homophily.gml'
        if args.file == 'imbalanced_graph.gml':
            graph = 'imbalanced_graph.gml'
        if args.file == 'balanced_graph.gml':
            graph = 'balanced_graph.gml'

    if args.components:
        pass

    if args.plot and graph:
        if args.plot == 'C':
            graph = clustering_coefficient(graph)
            plot_graph(graph, args.plot)
        if args.plot == 'N':
            graph = neighborhood_overlap(graph)
            plot_graph(graph, args.plot)
        if args.plot == 'P' and args.components:
            graph = partition_graph(graph, args.components)
            plot_graph(graph, args.plot)
        elif args.plot == 'P' and not args.components:
            print('Please enter number of components if you wanna partition the graph.')
            print('Try again.')
            exit

    if args.verify_homophily and graph == 'homophily.gml':
        verify_homophily(graph)

    elif args.verify_homophily and graph != 'homophily.gml':
        print('Please use "homphily.gml" as the graph input you want to use to verify homophily')
        print('Try again.')
        exit

    if args.verify_balanced_graph and graph:
        verified = verify_balanced_graph(graph)
        return verified
    
    if args.output and graph:
        write_graph(graph, args.output)

if __name__ == "__main__":
    main()