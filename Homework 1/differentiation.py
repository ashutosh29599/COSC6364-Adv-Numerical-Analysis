import math
import matplotlib.pyplot as plt


def central_difference(input_function, x, h):
    return (input_function(x + h) - input_function(x - h)) / (2 * h)


def forward_difference(input_function, x, h):
    return (input_function(x + h) - input_function(x)) / h


def input_function(x):
    return 1.0 * math.exp(0.055 * x) * math.cos(2.0 * x)


def calculate_and_plot_differentiation(T_a, T_b, func_to_diff, rule_name):
    current_input = T_a
    input_points = []
    diff_values = []
    errors = []

    while current_input <= T_b:
        input_points.append(current_input)

        current_output = func_to_diff(input_function, current_input, 0.001)
        diff_values.append(current_output)
        
        ground_truth = calculate_ground_truth(current_input)
        errors.append(abs(ground_truth - current_output))

        current_input += 0.001
    
    # Please uncomment the following for the differentiate values & the errors
    # print(f"Differentiated values for {rule_name}: {diff_values}")
    # print(f"Errors for {rule_name}: {errors}")

    # Save the plot in separate files
    if rule_name == "Forward Difference":
        plt.figure(2)
    elif rule_name == "Central Difference":
        plt.figure(3)

    plt.plot(input_points, errors, label=f"{rule_name}")
    plt.legend()
    plt.savefig(f"{rule_name} Error.png")

    # Save the plot to the combined graph
    plt.figure(1)
    plt.plot(input_points, errors, label=f"{rule_name}")
    plt.legend()
    plt.savefig(f"differentiation_error_combined.png")



def calculate_ground_truth(value):
    '''
    Input: value (point at which you want the ground truth)
    Output: ground truth at the point "value"
    '''
    return (0.055 * math.exp(0.055*value) * math.cos(2*value)) - (2 * math.exp(0.055*value) * math.sin(2*value))


if __name__ == "__main__":
    T_a = 0.001
    T_b = 2.0

    combined_plot = plt.figure(1)
    fwd_difference_plot = plt.figure(2)
    central_difference_plot = plt.figure(3)

    calculate_and_plot_differentiation(T_a, T_b, forward_difference, "Forward Difference")
    calculate_and_plot_differentiation(T_a, T_b, central_difference, "Central Difference")

