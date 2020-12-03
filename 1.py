
def walk_expenses_part_1(expenses) -> int:
    """
    This could be better with some binary searching and logic, but I'm being lazy

    :return: tuple of data points
    """
    for i in range(len(expenses)):
        for j in range(len(expenses)):
            if i != j and expenses[i] + expenses[-j] == 2020:
                return expenses[i] * expenses[-j]
    return 0


def walk_expenses_part_2(expenses) -> int:
    """
    This could be better with some binary searching and logic, but I'm being lazy

    :return:
    """
    for i in range(len(expenses)):
        for j in range(len(expenses)):
            if i != j:
                for k in range(len(expenses)):
                    if k != i and k != j :
                        if expenses[i] + expenses[j] + expenses[k] == 2020:
                            return expenses[i] * expenses[j] * expenses[k]
    return 0


def main():
    expense_report = '1_expenses.txt'

    with open(expense_report, 'r') as f:
        expenses = [int(line.rstrip('\n')) for line in f]

    # Sorted for first part
    expenses.sort()

    print(walk_expenses_part_1(expenses))

    print(walk_expenses_part_2(expenses))


if __name__ == '__main__':
    main()
