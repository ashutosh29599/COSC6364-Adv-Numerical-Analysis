'''
Ashutosh Kumar
UH ID 1854393

COSC 6364 Advanced Numerical Analysis 
Assignment 2
'''


import numpy as np
import matplotlib.pyplot as plt


def fun(w):
    w1, w2 = w[0], w[1]

    return (w1**2) + (w1 * w2) + (2 * w2**2)


def gradient_of_fun_at(w):
    w1, w2 = w[0], w[1]

    return np.array([2*w1 + w2, w1 + 4*w2])


def gradient_descent(w_start, learning_rate, max_num_of_steps, tolerance):
    num_opt_steps = 0
    w = w_start
    path = [w]

    for i in range(max_num_of_steps):
        gradient = gradient_of_fun_at(w)
        w_next = w - (learning_rate * gradient)

        if ((w[0] - w_next[0]) < tolerance) and ((w[1] - w_next[1]) < tolerance):
            num_opt_steps = i + 1
            break

        w = w_next
        path.append(w)
        
    f_min = fun(w)
    
    return w, f_min, num_opt_steps, path


def plot(path, learning_rate_lambda):
    fig = plt.figure()
    w1grid, w2grid = np.meshgrid(np.linspace(-2, 2.1, 100), np.linspace(-2, 2.1, 100))
    fgrid = fun([w1grid, w2grid])
    plt.contour(w1grid, w2grid, fgrid, levels=30)

    arg1 = [d[0] for d in path]
    arg2 = [d[1] for d in path]
    plt.plot(arg1, arg2, 'o-')

    plt.xlabel('w1')
    plt.ylabel('w2')
    plt.title(f'Gradient Descent Trajectory, \u03BB = {learning_rate_lambda}')
    
    fig.savefig(f'plots/gd_lambda_{learning_rate_lambda}.png')

    plt.show()


if __name__ == "__main__":
    learning_rate_lambda = 0.1    # learning rate
    w_start = np.array([2,2])
    max_num_of_steps = 1000
    termination_tolerance = 1e-6

    w_opt, f_min, num_opt_steps, path = gradient_descent(w_start, learning_rate_lambda, max_num_of_steps, termination_tolerance)

    print(f"Lambda (Learning rate) = {learning_rate_lambda}")
    print(f"Termination tolerance = {termination_tolerance}")
    print(f"Optimal number of steps = {num_opt_steps}")
    print(f"Optimal w = {w_opt}")
    print(f"Minimum f = {f_min}")

    plot(path, learning_rate_lambda)

