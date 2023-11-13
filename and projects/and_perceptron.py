
def training_and_perceptron_network():
    w1, w2, b = 0, 0, 0
    alpha =  1
    theta = 0.2
    
    counter = 1 
    while (counter != 0):
        counter = 0
        for tr_vec in and_training_set:
            x1, x2, t = tr_vec

            yni = b + x1 * w1 + x2 * w2
            if yni > theta:
                yni = 1
            elif yni < -theta:
                yni = -1
            else:
                yni = 0

            if yni != t:
                w1 += alpha * x1 * t
                w2 += alpha * x2 * t
                b += alpha * 1 * t
                counter += 1
            print(w1, w2, b)
        print("--------------------")

    return w1, w2, b, theta


def test_and(w1, w2, b, theta):
    flag = 0  # This will be used to finish the program
    while (flag == 0):
        x1 = int(input("Enter x1 (0 or 1): "))
        x2 = int(input("Enter x2 (0 or 1): "))
        valid_values = {0, 1}
        if (x1 in valid_values and x2 in valid_values):
            yni = b + x1 * w1 + x2 * w2
            if yni > theta:
                yni = 1
            elif yni < -theta:
                yni = -1
            else:
                yni = 0
            print("The result of AND operation is: ", yni)
        else:
            print("Please enter valid values in the input! You can only use 1 or 0")

        # Control the end of program
        while True:
            choice = input("Do you want to continue? (y/n): ").lower()
            if choice == "n":
                return
            elif choice == "y":
                break
            else:
                print("You can only enter 'y' or 'n'")


if __name__ == "__main__":
    # * training sets in format[[x1, x2, y] , ...]

    and_training_set = [[1, 1, 1], [1, 0, -1], [0, 1, -1], [0, 0, -1]]

    w1, w2, b, theta = training_and_perceptron_network()
    test_and(w1, w2, b, theta)
