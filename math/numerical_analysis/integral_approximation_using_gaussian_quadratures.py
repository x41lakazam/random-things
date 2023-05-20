from scipy.special import roots_legendre
import math

def gaussian_quadrature_integrate(N, func, a, b):

    # First change the variables to approximate integral between -1 and 1 --> Integrate f, not func
    def f(t):
        x = ((b-a)*t + a + b)/2
        return func(x)

    roots, weights = roots_legendre(N)

    return ((b-a)/2)*sum(
        weights[i] * f(roots[i])
        for i in range(N)
    )


if __name__ == "__main__":

    # we're trying to approximate the integral of cosx between 0 and pi/2
    # First, initialize variables:
    MAX_ITER = 100         # Maximum number of iterations
    tol = 0.01          # Error tolerance
    func = math.cos     # Function to integrate
    a = 0               # Integration lower bound
    b = math.pi/2       # Integration upper bound

    prev = None
    r = None

    for N in range(1, MAX_ITER):
        r = gaussian_quadrature_integrate(N, func, a, b)
        if prev and abs(r-prev) < tol:
            print(f"Satisfiability reached with {N} sample points")
            break
        prev = r
    else:
        print(f"Max iterations reached without going below the tolerance level")

    print(f"Approximation of the integral: {r}")

