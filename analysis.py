import integration
import numpy as np
import matplotlib.pyplot as plt

def f1(x):
    return np.sin(x)

def f2(x):
    return 1 / (1 + x**2)

def main():
    f1IntegralVal = 1/2
    a1 = 0
    b1 = np.pi/3
    f2IntegralVal = np.pi / 4
    a2 = 0
    b2 = 1
    Nvals = [10, 20, 40, 80, 160, 320, 640, 1280]

    leftVals1 = []
    midVals1 = []
    rightVals1 = []
    simpsonVals1 = []
    trapezoidVals1 = []

    leftVals2 = []
    midVals2 = []
    rightVals2 = []
    simpsonVals2 = []
    trapezoidVals2 = []
    for N in Nvals:
        leftVals1.append(integration.rect_left(f1, a1, b1, N))
        midVals1.append(integration.rect_mid(f1, a1, b1, N))
        rightVals1.append(integration.rect_right(f1, a1, b1, N))
        simpsonVals1.append(integration.simpson(f1, a1, b1, N))
        trapezoidVals1.append(integration.trapezoid(f1, a1, b1, N))
        leftVals2.append(integration.rect_left(f2, a2, b2, N))
        midVals2.append(integration.rect_mid(f2, a2, b2, N))
        rightVals2.append(integration.rect_right(f2, a2, b2, N))
        simpsonVals2.append(integration.simpson(f2, a2, b2, N))
        trapezoidVals2.append(integration.trapezoid(f2, a2, b2, N))

    leftVals1Error = np.array(leftVals1) - f1IntegralVal
    midVals1Error = np.array(midVals1) - f1IntegralVal
    rightVals1Error = np.array(rightVals1) - f1IntegralVal
    simpsonVals1Error = np.array(simpsonVals1) - f1IntegralVal
    trapezoidVals1Error = np.array(trapezoidVals1) - f1IntegralVal

    leftVals2Error = np.array(leftVals2) - f2IntegralVal
    midVals2Error = np.array(midVals2) - f2IntegralVal
    rightVals2Error = np.array(rightVals2) - f2IntegralVal
    simpsonVals2Error = np.array(simpsonVals2) - f2IntegralVal
    trapezoidVals2Error = np.array(trapezoidVals2) - f2IntegralVal

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1,2,1)
    ax2 = fig1.add_subplot(1,2,2)
    
    ax1.plot(Nvals, leftVals1Error, label = "Left")
    ax1.plot(Nvals, rightVals1Error, label = "Right")    
    ax1.plot(Nvals, midVals1Error, label = "Mid")
    ax1.plot(Nvals, simpsonVals1Error, label = "Simpson")
    ax1.plot(Nvals, trapezoidVals1Error, label = "Trapezoid")
    ax2.plot(Nvals, leftVals2Error, label = "Left")
    ax2.plot(Nvals, rightVals2Error, label = "Right")    
    ax2.plot(Nvals, midVals2Error, label = "Mid")
    ax2.plot(Nvals, simpsonVals2Error, label = "Simpson")
    ax2.plot(Nvals, trapezoidVals2Error, label = "Trapezoid")
    ax1.set_xscale('log')
    ax2.set_xscale('log')
    ax1.legend()
    ax2.legend()
    ax1.set_xlabel("N") 
    ax1.set_ylabel("Signed error")
    ax2.set_xlabel("N") 
    ax2.set_ylabel("Signed error")
    plt.show()
if __name__ == "__main__":
    main()
        
