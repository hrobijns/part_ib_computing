# Monte Carlo method of approximating ln(2)
# consider curve y = 1/x bounded by 1x1 square from x=1 to x=2 and y=0 and y=1
# ratio of points under the curve to overall number of points will tend to ln2 as number of points tends to infinity

#import required libraries
import numpy as np
import random
import matplotlib.pyplot as plt

#allow user to choose number of points to use for estimation
N = int(input("How many points do you want to use? (higher number takes longer, but provides a more accurate estimate): "))

# create empty lists
iterations = []
results = []

# perform the monte carlo estimation, plotting each point in a different colour depending on its place
count_in = 0
for i in range(N):
    x,y = random.random() + 1, random.random()
    if y <= 1/x:
        count_in += 1
        plt.plot(x,y,"ro", markersize=1)
    else:
        plt.plot(x,y,"go", markersize=1)
        continue

answer = count_in / N
print(f"Approximation for ln2 is: {round(answer, 5)}")


# plot a graph for visualisation purposes
xaxis= np.linspace(0.5,2.5,1000)
plt.plot(xaxis, 1/xaxis)
plt.grid()
plt.title("Monte Carlo estimation of ln(2)")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
