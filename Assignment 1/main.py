import math


'''Integral Algorithms'''

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


'''Differentiation Algorithms'''

def central_difference(input_function, x, h):
    return (input_function(x + h) - input_function(x - h)) / (2 * h)


def forward_difference(input_function, x, h):
    return (input_function(x + h) - input_function(x)) / h


def input_function(x):
    return 1.0 * math.exp(0.055 * x) * math.cos(2.0 * x)

def calculate_differentiation(T_a, T_b, func_to_diff, rule_name, h):
    current_input = T_a
    input_points = []
    diff_values = []
    errors = []

    while current_input <= T_b:
        input_points.append(current_input)

        current_output = func_to_diff(input_function, current_input, h)
        diff_values.append(current_output)
        
        ground_truth = calculate_ground_truth_for_differentiation(current_input)
        errors.append(abs(ground_truth - current_output))

        # the plots were created using step size 0.001
        # current_input += 0.001
        current_input += 0.1
    
    print(f"Differentiated values for {rule_name} for h = {h}: {diff_values}")
    print(f"Errors for {rule_name} for h = {h}: {errors}")
    print()


def calculate_ground_truth_for_differentiation(value):
    '''
    Input: value (point at which you want the ground truth)
    Output: ground truth at the point "value"
    '''
    return (0.055 * math.exp(0.055*value) * math.cos(2*value)) - (2 * math.exp(0.055*value) * math.sin(2*value))


if __name__ == "__main__":
    Ta = 0.001
    Tb = 2.0

    num_data_points = [2**2, 2**4, 2**6, 2**8, 2**10]
    calculate_and_print_integral_results(midpoint_rule, "Midpoint Rule", num_data_points)
    calculate_and_print_integral_results(trapezoidal_rule, "Trapezoidal Rule", num_data_points)
    calculate_and_print_integral_results(simpsons_rule, "Simpson's Rule", num_data_points)

    h = [0.0001, 0.001, 0.01, 0.1]
    for val in h:
        calculate_differentiation(Ta, Tb, forward_difference, "Forward Difference", val)
        calculate_differentiation(Ta, Tb, central_difference, "Central Difference", val)