import math

def simpsons_one_third_rule(a, b):
    '''
    a is the lower end. b is the upper end. n is the number of partitions.
    '''
    outer = (b - a) / 6
    inner = function_to_integrate(a) + (4 * function_to_integrate((a + b)/2)) + function_to_integrate(b)

    return outer * inner


def simpsons_one_eighth_rule(a, b):
    outer = (b - a) / 8
    inner = function_to_integrate(a) + function_to_integrate(b) + \
            (3 * function_to_integrate( (2*a + b) / 3 )) + (3 * function_to_integrate( (a + 2*b) / 3 ))
    
    return outer * inner


def simpsons_rule(a, b, n):
    if n % 2 != 0:
        return "n must be even!"
    
    h = (b - a) / n

    vals1 = [function_to_integrate(a + h*(2*i - 1)) for i in range(1, int(n/2 + 1))]
    vals2 = [function_to_integrate(a + h*(2*i)) for i in range(1, int(n/2))]


    inner = function_to_integrate(a) + function_to_integrate(b) + \
            (4 * sum(vals1)) + (2 * sum(vals2))

    return (1/3) * h * inner


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
    # print(simpsons_one_third_rule(a=1, b=5)) # answer = 46
    # print(simpsons_one_third_rule(a=-1, b=3)) # answer = 11.25
    # print(simpsons_one_third_rule(a=1, b=5)) # answer = 1.6833

    # print(simpsons_one_eighth_rule(a=1, b=5)) # answer = 46
    # print(simpsons_one_eighth_rule(a=-1, b=3)) # answer = 11.25
    # print(simpsons_one_eighth_rule(a=1, b=5)) # answer = 1.6833

    # hw function ->
    Ta = 0.001
    Tb = 2.0
    print(simpsons_rule(Ta, Tb, 2**2))
    print(simpsons_rule(Ta, Tb, 2**4))
    print(simpsons_rule(Ta, Tb, 2**6))
    print(simpsons_rule(Ta, Tb, 2**8))
    print(simpsons_rule(Ta, Tb, 2**10))

    # print(simpsons_one_third_rule(Ta, Tb))
    # print(simpsons_one_eighth_rule(Ta, Tb))