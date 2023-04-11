import numpy as np


def fun(w):
    w1, w2 = w[0], w[1]

    return w1**2 + w1*w2 + 2*w2**2


def gradient_of_fun_at(w):
    w1, w2 = w[0], w[1]

    return np.array([2*w1 + w2, w1 + 4*w2])


def gradient_descent(w_start, learning_rate, max_num_of_steps, tolerance):
    num_opt_steps = 0
    w = w_start

    for i in range(max_num_of_steps):
        gradient = gradient_of_fun_at(w)
        w_next = w - (learning_rate * gradient)
        
        # if all(abs(w - w_next)) > tolerance:
        if np.linalg.norm(w - w_next) < tolerance:
            num_opt_steps = i + 1
            break

        w = w_next
        
    f_min = fun(w)
    
    return w, f_min, num_opt_steps

if __name__ == "__main__":
    learning_rate_lambda = 0.1    # learning rate
    w_start = np.array([2,2])
    max_num_of_steps = 1000
    termination_tolerance = 1e-6

    w_opt, f_min, num_opt_steps = gradient_descent(w_start, learning_rate_lambda, max_num_of_steps, termination_tolerance)

    print(f"Lambda (Learning rate) = {learning_rate_lambda}")
    print(f"Optimal number of steps = {num_opt_steps}")
    print(f"Optimal w = {w_opt}")
    print(f"Minimum f = {f_min}")
