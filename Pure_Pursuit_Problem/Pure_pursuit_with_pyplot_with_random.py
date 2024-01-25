import random
import matplotlib.pyplot as plt

def pure_pursuit(xb, yb, xf, yf, speed):
    x_f = []
    y_f = []
    time = 0
    escape_distance, caught_distance = 900, 10
    while True:
        x_f.append(xf)
        y_f.append(yf)

        plt.clf()
        plt.title("simulation")
        plt.plot(x_f, y_f, label = "fighter")
        plt.plot(xb[0: time+1], yb[0 : time+1], label = "bomber")
        plt.legend()
        plt.grid()
        plt.pause(1)
        distance = ((yb[time]-yf)**2 + (xb[time] - xf)**2)**0.5
        
        # distance = ((xf - x_bomber[time]) ** 2 + (yf - y_bomber[time]) ** 2) ** 0.5
        if distance < caught_distance:
            print(f"Target caught at {time} second")
            break
        if distance > escape_distance or time > len(xb):
            print(f"Target escaped at {time} second")
            break
        sin = (yb[time] - yf)/distance
        cos = (xb[time] - xf) / distance
        time += 1
        xf = xf + speed*cos
        yf+=speed*sin
    # plt.show()

def main():
    xb = []
    yb = []
    for i in range(1, 15):
        xb.append(random.randint(1, 1000))
        yb.append(random.randint(1, 1000))
    # print(xb, yb)
    xf = 0
    yf = 50
    speed = 20
    pure_pursuit(xb, yb, xf, yf, speed)

if __name__ == "__main__":
    main()