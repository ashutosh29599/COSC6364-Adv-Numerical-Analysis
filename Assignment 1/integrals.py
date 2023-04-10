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


def trapezoidal_rule(a, b, n):
    '''
    a is the lower end. b is the upper end. n is the number of partitions.
    '''
    delta_x = (b - a)/n
    inner_half = function_to_integrate(a) + function_to_integrate(b)

    param = a + delta_x
    for _ in range(1, n):
        inner_half += 2 * function_to_integrate(param)
        param += delta_x

    return (delta_x / 2) * inner_half


def function_to_integrate(x):
    A = 1.000
    k = 0.055
    w = 2.0
    
    return A * math.exp(k * x) * math.cos(w * x)


def simpsons_rule(a, b, n):
    if n % 2 != 0:
        return "n must be even!"
    
    h = (b - a) / n

    vals1 = [function_to_integrate(a + h*(2*i - 1)) for i in range(1, int(n/2 + 1))]
    vals2 = [function_to_integrate(a + h*(2*i)) for i in range(1, int(n/2))]


    inner = function_to_integrate(a) + function_to_integrate(b) + \
            (4 * sum(vals1)) + (2 * sum(vals2))

    return (1/3) * h * inner


def calculate_and_print_integral_results(function_to_run, rule_name, num_data_points):
    integral_output = []
    
    for i, data in enumerate(num_data_points):
        integral_output.append(function_to_run(Ta, Tb, num_data_points[i]))

    ground_truth = -0.4468465306
    errors = [abs(val - ground_truth) for val in integral_output]
    errors_log = [math.log(val) for val in errors]

    print(f"Integral values for {rule_name} -> {integral_output}")
    print(f"Errors for {rule_name} -> {errors}")
    print()
    # for err in errors:
    #     print(f"{err:.20f}", end=" ")
    # print()

    plt.figure(1)
    plt.plot(num_data_points, errors_log, label=f"{rule_name}")
    plt.legend()
    plt.savefig(f"integral_errors.png")


if __name__ == "__main__":
    Ta = 0.001
    Tb = 2.0

    error_plot = plt.figure(1)
    plt.title(f"Error in Integration Algorithms")
    plt.xlabel("Number of data points")
    plt.ylabel("Log scale of errors")

    num_data_points = [2**2, 2**4, 2**6, 2**8, 2**10]
    calculate_and_print_integral_results(midpoint_rule, "Midpoint Rule", num_data_points)
    calculate_and_print_integral_results(trapezoidal_rule, "Trapezoidal Rule", num_data_points)
    calculate_and_print_integral_results(simpsons_rule, "Simpson's Rule", num_data_points)

    