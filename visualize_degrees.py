import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def load_data():
    # Load data from CSV files
    stars = pd.read_csv('stars.csv')
    people = pd.read_csv('people.csv')
    movies = pd.read_csv('movies.csv')

    # Merge stars with people to get actor names
    stars = stars.merge(people, left_on='person_id', right_on='id', how='left').drop(columns=['id', 'birth'])

    # Merge stars with movies to get movie titles
    stars = stars.merge(movies, left_on='movie_id', right_on='id', how='left').drop(columns=['id', 'year'])

    return stars


def create_graph(stars):
    # Create graph from pandas DataFrame
    G = nx.from_pandas_edgelist(stars, 'name', 'title', edge_attr=True)

    # Add node attributes to differentiate between actors and movies
    for node in G.nodes():
        G.nodes[node]['type'] = 'movie' if 'movie' in G.edges(node) else 'actor'

    return G


def visualize_graph(G):
    # Define node colors based on type
    colors = ['lightblue' if G.nodes[node]['type'] == 'actor' else 'lightgreen' for node in G]

    # Draw the graph
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(G, k=0.5, iterations=20)  # k: Optimal distance between nodes
    nx.draw(G, pos, with_labels=True, node_color=colors, edge_color='gray', node_size=5000, font_size=9, alpha=0.7)
    plt.title('Actor-Movie Network')
    plt.show()


def main():
    # Load data and create graph
    stars = load_data()
    G = create_graph(stars)

    # Visualize the graph
    visualize_graph(G)


if __name__ == '__main__':
    main()