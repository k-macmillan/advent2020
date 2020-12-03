

def main():

    with open('3_tree_inputs.txt', 'r') as f:
        # Strip the first line out because it doesn't matter
        tree_map = [line.rstrip('\n') for line in f]

    total_trees = trees_hit(tree_map, 1, 1)
    total_trees *= trees_hit(tree_map, 3, 1)
    total_trees *= trees_hit(tree_map, 5, 1)
    total_trees *= trees_hit(tree_map, 7, 1)
    total_trees *= trees_hit(tree_map, 1, 2)
    print(total_trees)


def trees_hit(tree_map, right, down):
    tree_count = 0
    for i, line in enumerate(tree_map):
        if i % down == 0:
            if line[(i * right // down) % 31] == '#':
                tree_count += 1

    if tree_map[0][0] == '#':
        tree_count -= 1

    return tree_count


if __name__ == '__main__':
    main()