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

def main():
    parser = ap.ArgumentParser(description='Creates graph based on Erdős–Rényi theorem and BFS algorithm')

    parser.add_argument('--input', type=str, help='Filename of graph, ex. "out_graph_file.gml"')
    parser.add_argument('--create_random_graph', action='store_true')
    parser.add_argument('--nodes', type=int, help='Number of nodes for your graph')
    parser.add_argument('--constant', type=float)
    #parser.add_argument('--BFS', type=int, help='Node to start BFS from')
    parser.add_argument('--plot', action='store_true')
    parser.add_argument('--output', type=str, help='Filename for new graph, ex. "out_graph_file.gml"')

    args = parser.parse_args()

    graph = None

    if args.create_random_graph:
        if args.nodes and args.constant:
            graph = create_random_graph(args.nodes, args.constant)
    elif args.input:
        graph = read_graph(args.input)

    #if args.BFS is not None and graph:
    #    breadth_first_search(graph, args.BFS)

    if args.plot and graph:
        plot_graph(graph, args.BFS)

    if args.output and graph:
        write_graph(graph, args.output)

if __name__ == "__main__":
    main()
