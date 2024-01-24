import random

def training(dataset_file):
    weights = [[random.uniform(-0.5, 0.5) for _ in range(25)] for _ in range(2)]
    bias = [random.random() for _ in range(2)]
    learning_rate = 0.01
    theta = 0.02
    weight_changed = True
    max_iterations = 150
    iteration_count = 0

    while weight_changed and iteration_count < max_iterations:
        weight_changed = False
        with open(dataset_file, "r") as dataset:
            for line in dataset:
                training_vec = list(map(int, line.strip().split(",")))
                target = [training_vec[0], -training_vec[0]]
                yni = [bias[0], bias[1]]

                for j in range(0, len(yni)):
                    for i in range(1, len(training_vec)):
                        yni[j] += weights[j][i - 1] * training_vec[i]

                    if yni[j] > theta:
                        yni[j] = 1
                    elif yni[j] < -theta:
                        yni[j] = -1
                    else:
                        yni[j] = 0

                    if yni[j] != target[j]:
                        weight_changed = True
                        bias[j] += learning_rate * target[j]
                        for i in range(1, len(training_vec)):
                            weights[j][i - 1] += learning_rate * training_vec[i] * target[j]

        iteration_count += 1

    return weights, bias


def testing(input_data, weights, bias):
    theta = 0.02
    yni = [bias[0], bias[1]]

    for j in range(0, len(yni)):
        for i in range(1, len(input_data)):
            yni[j] += weights[j][i - 1] * input_data[i]

        if yni[j] > theta:
            yni[j] = 1
        elif yni[j] < -theta:
            yni[j] = -1
        else:
            yni[j] = 0

    output = 1 if yni[0] == 1 and yni[1] == -1 else -1

    if yni[0] == yni[1]:
        return "Unknown"
    else:
        return "X" if output == 1 else "O"
