def training(dataset_file):
    weights = [0] * 25
    bias = 0
    learning_rate = 0.004
    theta = 0.001

    convergence = False
    while not convergence:
        with open(dataset_file) as dataset:
            for line in dataset:
                training_vec = list(map(int, line.strip().split(",")))
                target = training_vec[0]
                yni = bias
                for i in range(1, len(training_vec)):
                    yni += weights[i - 1] * training_vec[i]

                bias += learning_rate * (target - yni) * 1
                for i in range(1, len(training_vec)):
                    delta_w = learning_rate * (target - yni) * training_vec[i]
                    weights[i - 1] += delta_w
                    if -theta < delta_w < theta:
                        convergence = True

    return weights, bias


def testing(input_data, weights, bias):
    yni = bias
    for i in range(1, len(input_data)):
        yni += weights[i - 1] * input_data[i]
    if yni >= 0:
        return "X"
    return "O"
