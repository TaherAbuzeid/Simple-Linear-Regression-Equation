
import os


def br():
    try:

        x = list(map(int, input("Enter the numbers of X : ").strip().split()))
        y = list(map(int, input("Enter the numbers of Y : ").strip().split()))

        if len(x) == len(y):

            # CXX
            sum_x2 = []
            for i in x:
                sum_x2.append(i**2)
            sum_x2 = sum(sum_x2)
            x_bar = sum(x)/len(x)
            cxx = sum_x2-len(x)*(x_bar)**2

            # CYY
            sum_y2 = []
            for i in y:
                sum_y2.append(i**2)
            sum_y2 = sum(sum_y2)
            y_bar = sum(y)/len(y)
            cyy = sum_y2-len(x)*(y_bar)**2

            # CXY
            sum_xy = []

            for i, j in zip(x, y):
                sum_xy.append(i*j)
            sum_xy = sum(sum_xy)
            y_bar = sum(y)/len(y)
            cxy = sum_xy-len(x) * x_bar * y_bar

            Equation = input("enter your Equation : R OR C ").capitalize()

            if Equation == "R":
                # B1 / B0
                B1 = cxy / cxx
                print(f"B1 --> {B1}")

                B0 = y_bar - B1 * x_bar
                print(f"B0 --> {B0}")

                os.system("cls")
                print(f"Equation is : Y = {B0} + {B1} X")
                input()
            elif Equation == "C":
                correlation = cxy / ((cxx**0.5) * (cyy**0.5))
                os.system("cls")
                print(f"correlation is: {correlation}")
                input()

        else:
            print("error")
    except:
        print("error")


br()
