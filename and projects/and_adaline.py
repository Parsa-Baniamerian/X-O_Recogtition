
def training_and_adaline_network():
    w1, w2, b = 0, 0, 0
    alpha = 0.2

    convergence_flag = False
    while not convergence_flag:
        for tr_vec in and_training_set:
            x1, x2, t = tr_vec

            yin = b + x1 * w1 + x2 * w2

            d_w1 = alpha * (t - yin) * x1
            d_w2 = alpha * (t - yin) * x2
            w1 += d_w1
            w2 += d_w2
            b += alpha * (t-yin) * 1
            
            if -0.06 < d_w1 < 0.06 or -0.06 < d_w2 < 0.06:
                convergence_flag = True

            print(round(w1,4), round(w2,4), round(b,4))

    return w1, w2, b


def test_and(w1, w2, b):

    while True:
        x1 = int(input("Enter x1 (1 or -1): "))
        x2 = int(input("Enter x2 (1 or -1): "))

        valid_values = {-1, 1}
        if (x1 in valid_values and x2 in valid_values):
            yin = b + x1 * w1 + x2 * w2
            result = 1 if yin >= 0 else -1
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

    w1, w2, b = training_and_adaline_network()
    test_and(w1, w2, b)
