import math
import matplotlib.pyplot as plt


def p_diff(n, p_list):
    return p_list[n+1] - p_list[n]

def p_diff2(n, p_list):
    return p_list[n+2] + p_list[n] - 2*p_list[n+1]

def p_aitken(n, p_list):
    return p_list[n] - (p_diff(n, p_list)**2)/p_diff2(n, p_list)

def p_steffensen(n, p_list):
    p1 = p_list[n] + g(p_list[n])
    p2 = p_list[n+1] + g(p_list[n+1])
    return p2 - (math.pow((p2 - p1),2)/(p2 - (2*p1) + p_list[n]))


def main(g, x0, tol, method, max_tries=1000):
    p_list = [g(x0), g(g(x0)), g(g(g(x0)))]
    for i in range(max_tries):
        p = method(i-1, p_list)
        if abs(p - p_list[i-1]) < tol:
            print(f"found in {i+3} iterations")
            return p
        p_list.append(p)



if __name__ == "__main__":
    def g(x):
        return math.cos(x**2)-1

    def fixed_point(n, p_list):
        return g(p_list[n])

    print("For g=cos(x^2)-1")

    x0 = 1
    tol = 10E-10
    print("Method: fixed point")
    main(g, x0, tol, fixed_point)
    print("Method: Aitken")
    main(g, x0, tol, p_aitken)
    print("Method: Steffensen")
    main(g, x0, tol, p_steffensen)


    print("For g=x/2 + 2")
    def g(x):
        return x/2 + 2

    def fixed_point(n, p_list):
        return g(p_list[n])

    x0 = 1
    tol = 10E-10
    print("Method: fixed point")
    main(g, x0, tol, fixed_point)
    print("Method: Aitken")
    main(g, x0, tol, p_aitken)
    print("Method: Steffensen")
    main(g, x0, tol, p_steffensen)


