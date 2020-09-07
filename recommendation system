At the beginning we have the following:

1.       A list of films

2.       A dictionary with a user’s friends as keys and lists of films watched by every friend as values

3.       An adjacency matrix, which shows us relations (similarity) between films.

First of all we need to preprocess our data. We need to transform our dictionary in such way: a key = film and a value = a list of user’s friends, who watched it.

For example, user’s friends dictionary was like this: {A: [1, 2, 3], B: [1, 2]}

And after it would be: {1: [A, B], 2: [A, B], 3: [A]}. It is important, because it helps us to see, how many people have seen a concrete film.

We also need to transform our adjacency matrix into an adjacency list. We build an undirected graph, where vertices are films (or films id) and edges are connections (similarity) between two films.

And every vertex corresponds with a key (a film) from the dictionary. (You can see an example of such graph below)

Example:

List of films [1, 2, 3]

Dictionary of user's friends: { A: [1, 2], B: [2, 3], C: [3]} we transform into the following: {1: [A], 2: [A,B], 3: [B, C]}.

Adjacency matrix: [1 1 0], [1 1 0], [0 0 1].

We have this graph: 1 ---- 2 3

And every vertex corresponds with a key from our new dictionary: 1 [A] ------ 2[A,B] 3[B, C]

Now we can start calculating discussability and uniqueness. Let us look at the graph.

For every vertex (film) we can find F (discussability) which is a number of people who have seen this film – so it’s a length of a list of a corresponding value in our dictionary (in previous example, for film ‘’1’’ it would be a key 1 : [A, B], so a length of its value is 2).

S (uniqueness ) is a mean number of similar movies seen for each friend, so we need to find all the neighbors (similar films) of the vertex, then we find corresponding values (with the same keys as our neighbor-vertecies) in a dictionary, and we need to sum all lengths of these values. So we know how many people have seen all similar films. And we divide this number by the number of all friends.

The rate index is calculated as F/S. After we get indices for all the vertices (films) and append them to a list, we sort  it in a descending order (it would be organized as a list of tuples like - (film, index)), then we take the film with the highest index.
