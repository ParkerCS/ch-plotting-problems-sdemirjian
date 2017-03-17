#1 Import csv, numpy, and matplotlib.plot
#2 Open the chi_life_expectancy.txt file
#3 Use csv.reader(file, delimeter='\t') to read in the file to a list.  Make appropriate lists for plotting. Community name will be the x and 2010 life expectancy on the y.
#4 Plot the life_expectancy_2010_list vs a numpy arange() as a bar graph
#5 Use ax = plt.gca() to grab the axes object as ax. Use ax.set_xticklabels(community_list) to place the labels on the x axis, use the kwarg rotation=60 to tilt the lettering since there are a lot of communities
#6  Set an appropriate plt.ylim([min,max])
#7  Label your axes
#8  Add a title
#9  Add text to indicate the minimum and maximum values
#10 Customize your graph in at least two other ways using documentation from matplotlib.org
#11  Comment your code as always.

# Note:  If you would like to present something different than the above for your graph using this dataset, just let me know your intentions before you start and I will do my best to support you.
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

life_data = []
file = open("chi_life_expectancy.txt", 'r')

reader = csv.reader(file, delimiter='\t')

for line in reader:
    life_data.append(line)

print(life_data)

def name(library):
    name = life_data[library][1]
    return name

def expectancy(library):
    try:
        amount = float(life_data[library][8])
        return amount
    except:
        print(life_data[library][8])

xval = []
yval = []
patch_list = []

biggest = 2
biggest_name = ""
biggest_position = 0
smallest = 70
smallest_name = ""
smallest_position = 0
for i in range(77):
    total = expectancy(i+1)
    if total > biggest:
        biggest = total
        biggest_name = name(i)
        biggest_position = i
    elif total < smallest:
        smallest = total
        smallest_name = name(i)
        smallest_position = i
    else:
        pass

for i in range(77):
    xval.append(name(i+1))
    if name(i+1) == biggest_name:
        patch_list.append(Patch(color="orange", label="Maximum Life Expectancy"))
    elif name(i+1) == smallest_name:
        patch_list.append(Patch(color="green", label="Minimum Life Expectancy"))
    else:
        pass

for i in range(77):
    yval.append(expectancy(i+1))

print(yval)

plt.figure(1,tight_layout=True,figsize=(12,5))
plt.legend(handles=patch_list)
plt.bar(np.arange(len(yval)), yval,.6)
plt.bar(biggest_position, biggest, .5, .5)
plt.bar(smallest_position, smallest, .5, .5)


plt.title("2010 Life Expectancy in Chicago by District")
plt.xlabel("District")
plt.ylabel("Average Life Expectancy (years)")

plt.xticks(np.arange(len(yval)), xval,rotation=-90)

plt.show()