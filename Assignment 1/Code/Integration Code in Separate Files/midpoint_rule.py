import math
import matplotlib.pyplot as plt


def midpoint_rule(a, b, n):
    '''
    a is the lower end. b is the upper end. n is the number of partitions.
    '''
    delta_x = (b - a)/n

    lower = a
    upper = a + delta_x

    output = 0
    for i in range(n):
        midpoint = (lower + upper) / 2
        output += function_to_integrate(midpoint) * delta_x
        lower += delta_x
        upper += delta_x
        
    return output


def function_to_integrate(x):
    # return 1 + x**2  # ans = 46
    # return 2**x # ans = 11.25
    # return 1 / x # answer = 1.6833

    # hw function ->
    A = 1.000
    k = 0.055
    w = 2.0
    
    return A * math.exp(k * x) * math.cos(w * x)

if __name__ == "__main__":
    # print(midpoint_rule(a=1, b=5, n=4)) # answer = 46
    # print(midpoint_rule(a=-1, b=3, n=4)) # answer = 11.25
    # print(midpoint_rule(a=1, b=5, n=4)) # answer = 1.6833

    # hw function ->
    Ta = 0.001
    Tb = 2.0
    # print(midpoint_rule(Ta, Tb, 2**10))

    num_data_points = [2**2, 2**4, 2**6, 2**8, 2**10]
    integral_output = []
    
    for i, data in enumerate(num_data_points):
        integral_output.append(midpoint_rule(Ta, Tb, num_data_points[i]))

    ground_truth = -0.4468465306
    errors = [abs(val - ground_truth) for val in integral_output]

    print(f"Integral values -> {integral_output}")
    print(f"Errors -> {errors}")
    for err in errors:
        print(f"{err:.20f}", end=" ")

    errors_log = [math.log(val) for val in errors]

    plt.plot(num_data_points, errors_log)
    plt.title("Integration by Midpoint Rule")
    plt.xlabel("Number of data points")
    plt.ylabel("Log scale of errors")
    plt.show()
