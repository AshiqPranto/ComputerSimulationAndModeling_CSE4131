a0 = 1
b0 = .50
c0 = 0
T = 100.00
num_of_steps = 500
del_t = T / num_of_steps
k1 = 0.05
k2 = 0.05
t = 0
substance_A = [a0]
substance_B = [b0]
substance_C = [c0]
xt = [0]

a0 = int(input())


print("\tTIME\t \tA(I)\t \tB(I)\t \tC(I)\t")
print(f"\t{t:.2f}\t \t{a0:.2f}\t \t{b0:.2f}\t \t{c0:.2f}\t")
# for t in range(del_t, T, del_t):
t += del_t
while t < T:
    ai = a0 + ((k2 * c0) - (k1 * a0 * b0)) * del_t
    bi = b0 + ((k2 * c0) - (k1 * a0 * b0)) * del_t
    ci = c0 + ((2 * k1 * a0 * b0) - (2 * k2 * c0)) * del_t

    print(f"\t{t:.2f}\t \t{ai:.2f}\t \t{bi:.2f}\t \t{ci:.2f}\t")
    
    substance_A.append(ai)
    substance_B.append(bi)
    substance_C.append(ci)

    a0 = ai; b0 = bi; c0 = ci
    xt.append(t)
    t += del_t


import matplotlib.pyplot as plt

plt.plot(xt, substance_A, label="Substance_A", color="blue")
plt.plot(xt, substance_B, label="Substance_B", color="yellow")
plt.plot(xt, substance_C, label="Substance_C", color="green")
plt.xlabel("Time")
plt.legend( )
plt.show()