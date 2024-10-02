import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import argparse as ap

def read_graph(filename):
    return nx.read_gml(filename)

def write_graph(graph, file):
    nx.write_gml(graph, file)

def plot_graph():

    return 0

def clustering_coefficient(graph):
    return nx.clustering(graph)

def neighborhood_overlap(graph):

    return 0

def partition_graph(graph, nodes):

    return 0 

def verify_homophily(graph):

    return 0

def verify_balanced_graph(graph):

    return 0

"""
def plot_graph(graph, initial_node):
    # Compute BFS tree
    bfs_tree = nx.bfs_tree(graph, initial_node)

    # Generate a layout using bfs_tree
    pos = nx.bfs_layout(bfs_tree, start=initial_node)

    # Generate a list of edges from BFS traversal
    bfs_edges = list(nx.bfs_edges(graph, initial_node))

    # Draw the graph
    nx.draw(graph, pos=pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_color='black')
    nx.draw_networkx_edges(graph, pos=pos, edgelist=bfs_edges, edge_color='red')

    plt.show()
"""
def parse_args(): # input arguments & check validation
    parser = ap.ArgumentParser(description='Creates graph based on Erdős–Rényi theorem and BFS algorithm')

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

    #if args.BFS is not None and graph:
    #    breadth_first_search(graph, args.BFS)

    if args.plot and graph:
        if args.plot == 'C':
            graph = plot_graph(graph)
        if args.plot == 'N':
            graph = plot_graph(graph)
        if args.plot == 'P':
            graph = plot_graph(graph)

    if args.components and args.plot == 'P':
        partition_graph(graph, args.components)
    elif args.components:
        pass

    if args.verify_homophily and graph:
        verify_homophily(graph)

    if args.verify_balanced_graph and graph:
        verify_balanced_graph(graph)

    if args.output and graph:
        write_graph(graph, args.output)

if __name__ == "__main__":
    main()
