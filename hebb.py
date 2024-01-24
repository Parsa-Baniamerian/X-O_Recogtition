def training(dataset_file):
    weights = [0] * 25
    bias = 0
    with open(dataset_file, "r") as file:
        for line in file:
            training_vec = list(map(int, line.strip().split(",")))
            y = training_vec[0]  # y = target
            for i in range(1, len(training_vec)):
                x = training_vec[i]
                weights[i - 1] += x * y
                bias += 1 * y
    return weights, bias


def testing(input_data, weights, bias):
    result = bias
    for i in range(1, len(input_data)):
        result += weights[i - 1] * input_data[i]
    if result >= 1:
        return "X"  # return 1
    return "O"  # return -1
