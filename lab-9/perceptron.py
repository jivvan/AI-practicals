#include <stdio.h>
def step(val, threshold):
    if (val >= threshold):
        return 1
    else:
        return 0

def main():
    x1 = [0, 0, 1, 1]
    x2 = [0, 1, 0, 1]
    y = [0, 0, 0, 1]

    for i in range(4):
        print(f"{x1[i]}\t{x2[i]}\t{y[i]}")

    # defining neural network architecture
    w1 = 0.6
    w2 = 0.2
    alpha = 0.1
    threshold = 0.5
    flag = 1
    epoch = 0
    while (flag):
        flag = 0
        epoch+=1
        print(f"epoch: {epoch}")
        for i in range(4):
            print(f"w1: {w1} \tw2: {w2}")
            # ith row training dataset
            # activation
            ya = step(x1[i] * w1 + x2[i] * w2, threshold)
            # error calc
            error = y[i] - ya
            if (error != 0):
                flag = 1
                deltaWX1 = error * alpha * x1[i]
                w1 = w1 + deltaWX1
                deltaWX2 = error * alpha * x2[i]
                w2 = w2 + deltaWX2

    # testing the final weights
    for i in range(4):
        print(f"{x1[i]}\t{x2[i]}\t{step(x1[i] * w1 + x2[i] * w2, threshold)}")

main()