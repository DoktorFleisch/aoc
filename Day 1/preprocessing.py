def get_vectors():
    vector_1 = []
    vector_2 = []

    with open("puzzle_1_input.txt", 'r') as f:
        for line in f:
            first, second = map(int, line.split())
            vector_1.append(first)
            vector_2.append(second)

    vector_1.sort()
    vector_2.sort()

    return vector_1, vector_2
