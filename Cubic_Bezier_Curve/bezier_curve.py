import matplotlib.pyplot as plt

def fact(n):
    if n is 0:
        return 1
    else:
        return n * fact(n - 1)
    
def c(n, k):
    return fact(n) / float(fact(k) * fact(n - k))

def bez(k, n, u):
    return c(n, k) * (u ** k) * ((1 - u) ** (n - k))

def bezier_curve(x_control_points, y_control_points):
    n = len(x_control_points) - 1
    u = 0.00
    eps = 0.01
    x_curve_points = []
    y_curve_points = []
    while(u < 1.01):
        x = 0
        y = 0
        for k in range(0, len(x_control_points)):
            x = x + x_control_points[k] * bez(k, n, u)
            y = y + y_control_points[k] * bez(k, n, u)
        u += eps
        x_curve_points.append(x)
        y_curve_points.append(y)
        #print x, y
        plt.clf()
        plt.title("Bezier Curve")
        plt.plot(x_control_points, y_control_points, label = "Control graph")
        plt.plot(x_curve_points, y_curve_points, label = "Bezier Curve")
        plt.legend()
        plt.grid()
        plt.pause(0.0001)
    plt.show()

def main():
    x_control_points = [1, 7, 15, 21]
    y_control_points = [5, 10, 5, 10]
    bezier_curve(x_control_points, y_control_points)

if __name__ == "__main__":
    main()


