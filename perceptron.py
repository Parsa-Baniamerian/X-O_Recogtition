import random

def training(dataset_file):
    weights = [random.uniform(-0.5, 0.5) for _ in range(25)]
    bias = 0
    learning_rate = 0.02
    theta = 0.2

    max_iterations = 150
    iteration_count = 0
    weight_changed = True
    while weight_changed and iteration_count < max_iterations:
        iteration_count += 1
        weight_changed = False
        with open(dataset_file, "r") as dataset:
            for line in dataset:
                training_vec = list(map(int, line.strip().split(",")))
                target = training_vec[0]
                yni = bias
                for i in range(1, len(training_vec)):
                    yni += weights[i-1] * training_vec[i]
                if yni > theta:
                    yni = 1
                elif yni < -theta:
                    yni = -1
                else:
                    yni = 0

                if yni != target:
                    weight_changed = True
                    bias += learning_rate * target
                    for i in range(1, len(training_vec)):
                        weights[i - 1] += learning_rate*training_vec[i]*target

    return weights, bias


def testing(input_data, weights, bias):
    theta = 0.2
    yni = bias
    for i in range(1, len(input_data)):
        yni += weights[i-1] * input_data[i]
    if yni > theta:
        return "X"
    elif yni < -theta:
        return "O"
    return "Unknown"
