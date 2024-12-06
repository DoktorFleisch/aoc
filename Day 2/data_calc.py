def load_data():
    reports_list = []

    with open("day_2_input.txt", "r") as f:
        data = f.readlines()

    return [list(map(int, line.split())) for line in data]


def check_safety(data_list):
    increased = all([data_list[i] < data_list[i + 1] for i in range(len(data_list) - 1)])
    decreased = all([data_list[i] > data_list[i + 1] for i in range(len(data_list) - 1)])

    if not (increased or decreased):
        return False

    differences = [abs(data_list[i] - data_list[i + 1]) for i in range(len(data_list) - 1)]

    return all(1 <= diff <= 3 for diff in differences)


def count_safe_combinations(data):
    return sum([check_safety(line) for line in data])


def can_be_made_safe(data_list):
    for i in range(len(data_list)-1):
        modified_data = data_list[:i] + data_list[i + 1:]

        if check_safety(modified_data):
            return True

    return False


def count_safe_level_combinations(data):
    sum_safe = 0

    for line in data:
        if check_safety(line) or can_be_made_safe(line):
            sum_safe += 1

    return sum_safe
