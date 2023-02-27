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
    x = []
    y = []
    errors = []

    while current_input <= T_b:
        x.append(current_input)

        current_output = func_to_diff(input_function, current_input, 0.01)
        y.append(current_output)
        
        ground_truth = calculate_ground_truth(current_input)
        errors.append(abs(ground_truth - current_output))

        current_input += 0.001
    
    plt.plot(x, errors, label=f"{rule_name}")

    plt.legend()
    plt.savefig(f"output/diff.png")


def calculate_ground_truth(value):
    return (0.055 * math.exp(0.055*value) * math.cos(2*value)) - (2 * math.exp(0.055*value) * math.sin(2*value))


if __name__ == "__main__":
    T_a = 0.001
    T_b = 2.0

    calculate_and_plot_differentiation(T_a, T_b, forward_difference, "Forward Difference")
    calculate_and_plot_differentiation(T_a, T_b, central_difference, "Central Difference")

    
