

def main():

    with open('3_tree_inputs.txt', 'r') as f:
        # Strip the first line out because it doesn't matter
        tree_map = [line.rstrip('\n') for line in f]

    total_trees = trees_hit(tree_map, 1, 1, '#')
    total_trees *= trees_hit(tree_map, 3, 1, '#')
    total_trees *= trees_hit(tree_map, 5, 1, '#')
    total_trees *= trees_hit(tree_map, 7, 1, '#')
    total_trees *= trees_hit(tree_map, 1, 2, '#')
    print(total_trees)


def trees_hit(tree_map: list, right: int, down: int, symbol: str) -> int:
    """
    Takes in a 2d grid map and walks it looking for symbol matches.

    :param tree_map: The grid map
    :param right: Steps to the right
    :param down: Steps down
    :param symbol: Symbol to look for
    :return: count of symbols found
    """
    tree_count = 0
    # Get the length of the line, used for infinite extension to the right
    length = len(tree_map[0])
    # Walk each line by setting the step size to the down parameter
    for i, line in enumerate(tree_map[::down]):
        # Modding by length allows for the pattern to repeat
        if line[(i * right) % length] == symbol:
            tree_count += 1

    # The examples did not count 0, 0, but the above code would. Clean it up if needed.
    if tree_map[0][0] == symbol:
        tree_count -= 1

    return tree_count


if __name__ == '__main__':
    main()
