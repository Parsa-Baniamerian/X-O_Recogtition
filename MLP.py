import numpy as np

# activation function
def bipolar_sigmoid(x):
    return 2 / (1 + np.exp(-x)) - 1


def bipolar_sigmoid_derivative(x):
    return 0.5 * (1 + bipolar_sigmoid(x)) * (1 - bipolar_sigmoid(x))


def feedforward(training_vec, l1_weights, l1_bias, l2_weights, l2_bias):
    hidden_layer_input = np.add(l1_bias, np.dot(training_vec, l1_weights))
    hidden_layer_output = bipolar_sigmoid(hidden_layer_input)

    output_layer_input = np.add(l2_bias, np.dot(hidden_layer_output, l2_weights))
    output_layer_output = bipolar_sigmoid(output_layer_input)

    return hidden_layer_output, output_layer_output




def training(dataset_file):
    epochs = 60
    learning_rate = 0.3
    # Weights between input and hidden layer
    l1_weights = np.random.uniform(low=-0.5, high=0.5, size=(25, 6))
    # biases between input and hidden layer
    l1_bias = np.random.uniform(low=-0.5, high=0.5, size=(1, 6))
    # Weights between hidden layer and output
    l2_weights = np.random.uniform(low=-0.5, high=0.5, size=(6, 2))
    # biases between hidden layer and output
    l2_bias = np.random.uniform(low=-0.5, high=0.5, size=(1, 2))


    for epoch in range(epochs): 

        with open (dataset_file, "r") as dataset:
            for line in dataset:
                line_values = np.array(line.strip().split(",")).astype(float)
                training_vec = line_values[1:]
                t = line_values[0]


                 # Feedforward
                hidden_layer_output, final_output = feedforward(training_vec, l1_weights, l1_bias, l2_weights, l2_bias)

                # Backpropagation
                if t == 1 :
                    target = [1, -1]
                else: 
                    target = [-1, 1]
                    
                delta_output = bipolar_sigmoid_derivative(final_output) * (target - final_output)
                delta_hidden = bipolar_sigmoid_derivative(hidden_layer_output) * np.dot(delta_output, l2_weights.T)

                # Weight and bias updates
                l2_weights += learning_rate * np.outer(hidden_layer_output, delta_output)
                l2_bias += learning_rate * delta_output
                
                l1_weights += learning_rate * np.outer(training_vec, delta_hidden)
                l1_bias += learning_rate * delta_hidden
    return l1_weights, l1_bias, l2_weights, l2_bias



def testing(input_data, l1_weights, l1_bias, l2_weights, l2_bias):
    hidden_layer_output, final_output = feedforward(input_data, l1_weights, l1_bias, l2_weights, l2_bias)
    
    if np.all(np.abs(final_output - [1, -1]) < 0.9):
        return "X"
    elif np.all(np.abs(final_output - [-1, 1]) < 0.9):
        return "O"
    else:
        return "Unknown"

    

