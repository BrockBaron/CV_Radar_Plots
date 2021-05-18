# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np
import matplotlib.colors as mcolors
 
# Set data
df = pd.DataFrame({
'Skill': ['Tools'],
'MathCAD': [4],

'Matlab': [1.5],
'Minitab': [2.5],

'Qualica': [1.5],

'Hyperworks': [3.5],
'DOORS' : [1],

'P6': [2],
'KANBAN': [2.5],




})


# ------- PART 1: Define a function that do a plot for one line of the dataset!
 
def make_spider( row, title, color):

    # number of variable
    categories=list(df)[1:]
    N = len(categories)

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(2,2,row+1, polar=True, )

    # If you want the first axis to be on top:
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=8)

    # Draw ylabels
    ax.set_rlabel_position(30)
    plt.yticks(np.arange(1, 6), ['1', '2', '3', '4', '5'], color='black', size=10)
    plt.ylim(0, 5)


    # Ind1
    values=df.loc[row].drop('Skill').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=0, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    # Add a title
    plt.title(title, size=11, color=color, y=1.1)

    
# ------- PART 2: Apply the function to all individuals
# initialize the figure
my_dpi=96
plt.figure(figsize=(1000/my_dpi, 1000/my_dpi), dpi=my_dpi)
 
# Create a color palette:
my_palette = plt.cm.get_cmap("nipy_spectral", len(df.index))
 
# Loop to plot
for row in range(0, len(df.index)):
    make_spider( row=row, title='Skill '+df['Skill'][row], color=my_palette(row))
