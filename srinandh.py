# Title :- Miss and Relative miss calculator
# Name of the file:- srinandh.py
# List of external file : NA
# List of external file created by the program : NA
# Name :- Srinandh Reddy
# Email address :- srinandhreddygadda@lewisu.edu

# this gets the value os n
number_n = int(input("please enter a number for n"))
if (number_n > 2) and (number_n < 12):
    n = number_n
    print(n)
else:
    pass

# this gets the value of k
number_k = int(input("please enter a unmber for k"))
if (number_k > 10):
    k = number_k
    print(k)
else:
    pass


# this calculates the X^n, Y^n, Z^n, Z+1^n and takes them iinto a list
xn_vals = [i**n for i in range(10, k+1)]
yn_vals = [i**n for i in range(10, k+1)]
z_vals = [i for i in range(1, (2*k+1))]
z1_vals = [i+1 for i in z_vals]

zn_vals = [i**n for i in z_vals]
z1n_vals = [i**n for i in z1_vals]


# this calculates the sum of x^n and y^n
sum_x_and_y = []
for i in xn_vals:
    for j in yn_vals:
        sum_x_and_y.append(i+j)


# this calculates the difference between x^n + y^n with z^n
zminxandy = []
for i in sum_x_and_y:
    for j in zn_vals:
        zminxandy.append(i - j)


# this calculates the difference between x^n + y^n with z+1^n
z_1minxandy = []
for i in sum_x_and_y:
    for j in z1n_vals:
        z_1minxandy.append(i - j)


# this will return the min between teh z^n and z+1^n
def get_min_miss(x, y):
    minimum = min(x,y)
    return minimum


miss = get_min_miss(zminxandy, z_1minxandy)

# this is the miss
total_miss = sum(miss)/len(miss)
print("Miss =", total_miss)

# this is the relative miss
relative_miss = total_miss/(sum(sum_x_and_y) / len(sum_x_and_y))
print("Relative miss =", relative_miss)












