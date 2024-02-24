# X/O Recognition

## Overview:
X/O Recognition is a Python application designed to recognize patterns of X and O on a 5x5 grid. The project utilizes various machine learning algorithms, including Hebb, Perceptron, Multi-Class Perceptron, Adaline, and MLP (Multi-Layer Perceptron), to train and test the recognition model. With a user-friendly Graphical User Interface (GUI), users can easily interact with the application to add data to the dataset, train the model, and test its accuracy.

## Features:
- **User-friendly GUI:** Intuitive graphical interface for seamless interaction.
- **Dataset Management:** Ability to add new data to the dataset by manually selecting X and O patterns on the grid.
- **Training Functionality:** Train the recognition model using different machine learning algorithms.
- **Testing Functionality:** Evaluate the accuracy of the trained model on new data.
- **Support for Multiple Algorithms:** Utilize various algorithms including Hebb, Perceptron, Multi-Class Perceptron, Adaline, and MLP.


## Algorithms:
- **Hebb Algorithm:** Utilizes Hebbian learning to strengthen connections between neurons activated simultaneously.
- **Perceptron Algorithm:** Implements a linear binary classifier that learns weights for input features and makes predictions based on a threshold function.
- **Multi-Class Perceptron Algorithm:** Extends the Perceptron algorithm for multi-class classification tasks.
- **Adaline Algorithm:** Adapts weights based on continuous output values to minimize error.
- **MLP Algorithm (Multi-Layer Perceptron):** Utilizes multiple layers, including input, hidden, and output layers, to learn complex patterns.



## Usage:
1. **Clone the Repository:** Clone the repository to your local machine using the command:
    ```bash
    git clone https://github.com/Parsa-Baniamerian/X-O_Recogtition.git
    ```
    
2. **Run the Application:** Launch the application by running the `GUI.py` file:
    ```bash
    python GUI.py
    ```
3. **Add Data to Dataset:** Use the GUI to add data to the dataset by selecting X and O patterns on the grid.
4. **Train the Model:** Choose an algorithm from the dropdown menu and click on the "Train" button to train the recognition model.
5. **Test the Model:** Evaluate the accuracy of the trained model by clicking on the "Test" button.
6. **View Results:** The output label will display the predicted pattern (X or O) based on the input data.



## Testing Algorithms

The `test_algorithms.py` script is designed to evaluate the performance of the trained recognition models using various machine learning algorithms. This script is separate from the main GUI application and is intended for evaluating the accuracy and execution time of the models trained on different algorithms.

### Usage:
1. **Run the Script:** Execute the script `test_algorithms.py` using the following command:
    ```bash
    python test_algorithms.py
    ```

### Features:
- **Algorithm Testing:** Evaluates the accuracy and execution time of recognition models trained with different machine learning algorithms.
- **Multiple Algorithm Support:** Tests the performance of models trained using Hebb, Perceptron, Multi-Class Perceptron, Adaline, and MLP algorithms.
- **Data Splitting:** Automatically splits the dataset into training and testing data, ensuring unbiased evaluation.

### Note:
- Ensure that the dataset is located at `./Dataset/Dataset.txt` with properly labeled X and O patterns.
- The `test_algorithms.py` script is not integrated into the GUI and should be run separately from the main application.

