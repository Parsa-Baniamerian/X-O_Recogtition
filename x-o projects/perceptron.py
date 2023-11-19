def training(dataset_file):
    weights = [0] * 25
    bias = 0
    learning_rate = 0.2
    theta = 0.2
    weight_changed = True
    while weight_changed:
        weight_changed = False
        with open(dataset_file, "r") as file:
            for line in file:
                training_vec = list(map(int, line.strip().split(",")))
                target = training_vec[0]
                for i in range(1, len(training_vec)):
                    yni = bias + weights[i-1] * training_vec[i]
                if yni > theta:
                    yni = 1
                elif yni < -theta:
                    yni = -1
                else:
                    yni = 0

                if yni != target:
                    for i in range(1, len(training_vec)):
                        weights[i - 1] += learning_rate*training_vec[i]*target
                    bias += learning_rate * target
                    weight_changed = True
                print(weights, bias)
    return weights, bias


def testing(input_data, weights, bias):
    theta = 0.2
    for i in range(1, len(input_data)):
        yni = bias + weights[i-1] * input_data[i]
    if yni > theta:
        return "X"
    elif yni < theta:
        return "O"
    return "Unknown"
