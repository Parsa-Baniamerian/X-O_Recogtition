import matplotlib.pyplot as plt


def training_and_hebb_network():
    w1, w2, b = 0, 0, 0

    for tr_vec in and_training_set:
        x1, x2, y = tr_vec
        w1 += x1 * y
        w2 += x2 * y
        b += 1 * y

        # Plot
        x1_plot = [-2, 2]  # Generate values for x1
        # Calculate values for x2 (rewriting the linear equation "b + w1*x1 + w2*x2 = 0" as "x2 = (-b - w1*x1) / w2")
        x2_plot = [(-b - w1 * x) / w2 for x in x1_plot]

        for tr_vec in and_training_set:
            if tr_vec[2] == 1:
                plt.scatter(tr_vec[0], tr_vec[1],
                            color="green", marker="o", label="Class 1")
            else:
                plt.scatter(tr_vec[0], tr_vec[1], color="red",
                            marker="x", label="Class -1")

        plt.axhline(y=0, color="black")
        plt.axvline(x=0, color="black")
        plt.xlabel("x1")
        plt.ylabel("x2")
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.plot(x1_plot, x2_plot)
        plt.grid(True)
        plt.show()

        print(w1, w2)
    return w1, w2, b


def test_and(w1, w2, b):
    flag = 0  # This will be used to finish the program
    while (flag == 0):
        x1 = int(input("Enter x1 (1 or -1): "))
        x2 = int(input("Enter x2 (1 or -1): "))
        valid_values = {-1, 1}
        if (x1 in valid_values and x2 in valid_values):
            result = b + x1 * w1 + x2 * w2
            if result >= 1:
                result = 1
            elif result <= -1:
                result = -1
            print("The result of AND operation is: ", result)
        else:
            print("Please enter valid values in the input! You can only use 1 or -1")

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

    and_training_set = [[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]

    w1, w2, b = training_and_hebb_network()
    test_and(w1, w2, b)

