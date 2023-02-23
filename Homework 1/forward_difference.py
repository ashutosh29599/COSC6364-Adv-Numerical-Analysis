import math


def forward_difference(input_function, x, h):
    return (input_function(x + h) - input_function(x)) / h


def input_function(x):
    return 1.0 * math.exp(0.055 * x) * math.cos(2.0 * x)


if __name__ == "__main__":
    print(forward_difference(input_function, 0.001, 10.0e-5))
    
