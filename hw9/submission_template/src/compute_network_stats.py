import argparse
import networkx as nx
import json

def compute_stats():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i')
    parser.add_argument('-o')
    args = parser.parse_args()
    
    with open(args.i) as f:
        interactions = json.load(f)
    
    
    output = {
        'most_connected_by_num': [],
        'most_connected_by_weight': [],
        'most_central_by_betweenness': []
    }

    G = nx.Graph()
    for p in interactions:
        for edge in interactions[p]:
            G.add_edge(p,edge, weight=interactions[p][edge])
    
    output['most_connected_by_num'] = [p for p, _ in sorted(G.degree(), key=lambda x: x[1], reverse=True)[:3]]

    output['most_connected_by_weight'] = [p for p, _ in sorted(G.degree(weight='weight'), key=lambda x: x[1], reverse=True)[:3]]

    output['most_central_by_betweenness'] = [p for p, _ in sorted(nx.algorithms.betweenness_centrality(G).items(), key=lambda x: x[1], reverse=True)[:3]]

    with open(args.o, 'w') as f:
        json.dump(output, f)

if __name__ == '__main__':
    compute_stats()
