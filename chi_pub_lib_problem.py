
# MATPLOTLIB PROBLEM # 1
# Chicago Public Library Visitors by Month (25pts)
# open and read in the "chilib_visitors_2016" file into a list
# calculate (and make a list of) the total visitors to Chicago libraries each month.  Do not plot every library individually.  Find the total for all libraries and plot that.
# Additionally, add lines for the three most visited libraries.
# plot the total visitors on the y and month on the x.  You will have 4 separate lines (total and 3 libraries)
# add a legend
# label axes, title the graph

import csv
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch

lib_data = []
file = open("chilib_visitors_2016", 'r')

reader = csv.reader(file, delimiter='\t')

for line in reader:
    lib_data.append(line)

print(lib_data)

headers = lib_data[0]
lib_data = lib_data[1:]
print(lib_data)

def total_per_month(library):
    total = 0
    for i in range(len(lib_data)):
        total += int(lib_data[i][library + 1])
    return total

def total_visitors(library):
    total = int(lib_data[library][-1])
    return total

def lib_name(library):
    name = lib_data[library][0]
    return name

xval = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
yval = []
patch_list = []

for i in range(12):
    yval.append(total_per_month(i))
patch_list.append(Patch(color="purple", label="Total Visitors per Month"))

biggest = 3
medium = 2
smallest = 1
for i in range(79):
    total = total_visitors(i)
    if total > biggest:
        biggest = total
    elif total > medium and total < biggest:
        medium = total
    elif total > smallest and total < medium:
        smallest = total
    else:
        pass

lib1 = "yee"
lib2 = "yee"
lib3 = "yee"

for i in range(79):
    if total_visitors(i) == biggest:
        lib1 = lib_name(i)
        patch_list.append(Patch(color="blue",label=lib_name(i)))
    elif total_visitors(i) == medium:
        lib2 = lib_name(i)
        patch_list.append(Patch(color="red",label=lib_name(i)))
    elif total_visitors(i) == smallest:
        lib3 = lib_name(i)
        patch_list.append(Patch(color="yellow",label=lib_name(i)))
    else:
        pass

print(lib1)
print(lib2)
print(lib3)

print(biggest)
print(medium)
print(smallest)

print(patch_list)

lib1y = []
lib2y = []
lib3y = []

for i in range(79):
    if total_visitors(i) == biggest:
        for k in range(12):
            lib1y.append(lib_data[i][k + 1])
    if total_visitors(i) == medium:
        for k in range(12):
            lib2y.append(lib_data[i][k+1])
    if total_visitors(i) == smallest:
        for k in range(12):
            lib3y.append(lib_data[i][k+1])

print(lib1y, lib2y, lib3y)

plt.figure(1,tight_layout=True)
plt.legend(handles=patch_list)
plt.plot(np.arange(12), yval,"purple")
plt.plot(np.arange(12), lib1y,"blue")
plt.plot(np.arange(12), lib2y,"red")
plt.plot(np.arange(12), lib3y,"yellow")

plt.title("Total Library Visitors per Month")
plt.xlabel("Months")
plt.ylabel("Total Visitors")

#Label our x-axis
plt.xticks(np.arange(len(yval)), xval,rotation=-45)

plt.show()