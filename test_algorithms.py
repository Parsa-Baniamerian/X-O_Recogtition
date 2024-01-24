import random
import time
from hebb import training as hebb_training, testing as hebb_testing
from perceptron import training as perceptron_training, testing as perceptron_testing
from multi_class_perceptron import training as multi_class_perceptron_training, testing as multi_class_perceptron_testing
from adaline import training as adaline_training, testing as adaline_testing
from MLP import training as MLP_training, testing as MLP_testing


algorithms_functions = {
    "Hebb": {"train": hebb_training, "test": hebb_testing},
    "Perceptron": {"train": perceptron_training, "test": perceptron_testing},
    "Multi-Class Perceptron": {"train": multi_class_perceptron_training, "test": multi_class_perceptron_testing},
    "Adaline": {"train": adaline_training, "test": adaline_testing},
    "MLP": {"train": MLP_training, "test": MLP_testing}
}


def split_train_test(all_data_file, train_file, test_file, split_ratio=0.9):
    with open(all_data_file, 'r') as all_data:
        lines = all_data.readlines()

    random.shuffle(lines)

    split_point = int(len(lines) * split_ratio)

    train_data = lines[:split_point]
    test_data = lines[split_point:]

    with open(train_file, 'w') as train_file:
        train_file.writelines(train_data)

    with open(test_file, 'w') as test_file:
        test_file.writelines(test_data)


def test_algorithms():
    train_dataset = "./Dataset/train_data.txt"
    test_dataset = "./Dataset/test_data.txt"

    algorithms = ["Hebb",  "Perceptron", "Adaline", "Multi-Class Perceptron", "MLP"]
    MLP = algorithms_functions.get("MLP")

    num_repeat_testing = 100

    for alg in algorithms:

        sum_time, sum_accuracy = 0, 0
        for i in range(num_repeat_testing):
            algorithm = algorithms_functions.get(alg)
            start_time = time.time()
            if alg == "MLP":
                l1_weights, l1_bias, l2_weights, l2_bias = MLP["train"](dataset_file=train_dataset)
            else:
                weights, bias = algorithm["train"](dataset_file=train_dataset)
            finish_time = time.time()

            num_correct = 0
            num_test_data = 0
            with open(test_dataset) as test_data:
                for line in test_data:
                    num_test_data += 1
                    testing_vec = list(map(int, line.strip().split(",")))
                    target = testing_vec[0]

                    if alg == "MLP":
                        result = algorithm["test"](testing_vec[1:], l1_weights, l1_bias, l2_weights, l2_bias)
                    else:
                        result = algorithm["test"](testing_vec, weights, bias)
                    if ((result == "X" and target == 1) or (result == "O" and target == -1)):
                        num_correct += 1

            execution_time = finish_time - start_time
            sum_time += execution_time
            accuracy = round((num_correct/num_test_data)*100, 2)
            sum_accuracy += accuracy
            split_train_test("./Dataset/Dataset.txt", train_dataset, test_dataset, split_ratio=0.9)

        average_execution_time = round((sum_time/num_repeat_testing)*1000, 3)
        average_accuracy = round(sum_accuracy/num_repeat_testing, 2)
        print(f"The accuracy of \"{alg}\" neural network is {average_accuracy}% \t\t\t\t \"{alg}\" it was trained in {average_execution_time} ms")


if __name__ == "__main__":
    test_algorithms()
