import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

L1 = 1.0   # length of link 1
L2 = 1.0   # length of link 2

# define the endpoints (x, y)
endpoints = np.array([[0.7, 0.5], [-0.2, 0.8], [-0.9, -0.3], [0.3, -0.5], [1.0, 0.3], [0.2, 1.0], [-1.0, -0.2], [-0.2, -1.0], [0.7, 0.8], [-0.9, 0.7]])
#endpoints = np.array([[-1.0, 1.0], [-1.0, -1.0], [-2.0, 0.0], [2.0, 2.0], [-2.0, 2.0], [-4.0, 2.0], [-2.0, -2.0], [1.0, 2.0], [-2.0, -1.0], [3.0, 3.0]])

# initialize the joint angles array
joint_angles = np.zeros((len(endpoints), 2))

# calculate the joint angles for each endpoint
for i in range(len(endpoints)):
    x = endpoints[i, 0]
    y = endpoints[i, 1]
    theta2 = np.arccos((x**2 + y**2 - L1**2 - L2**2)/(2*L1*L2))
    theta1 = np.arctan2(y, x) - np.arctan2(L2*np.sin(theta2), L1 + L2*np.cos(theta2))
    joint_angles[i, 0] = theta1
    joint_angles[i, 1] = theta2

# create a table of the endpoints and joint angles, rounded to two decimal places, and save visualization plots
table = []
for i in range(len(endpoints)):
    x = endpoints[i, 0]
    y = endpoints[i, 1]
    theta1 = round(joint_angles[i, 0], 2)
    theta2 = round(joint_angles[i, 1], 2)
    plot_filename = 'figure_{}.png'.format(i)
    plt.figure()
    plt.plot([0, L1*np.cos(theta1), L1*np.cos(theta1) + L2*np.cos(theta1+theta2)], [0, L1*np.sin(theta1), L1*np.sin(theta1) + L2*np.sin(theta1+theta2)])
    plt.xlim([-2, 2])
    plt.ylim([-2, 2])
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Endpoint: ({:.2f}, {:.2f})\nJoint angles: ({:.2f}, {:.2f})'.format(x, y, theta1, theta2), fontsize=8)
    plt.savefig(plot_filename)
    plt.close()
    table.append([str((round(x, 2), round(y, 2))), str((theta1, theta2))])

# display the table
headers = ['Endpoint', 'Joint Angles']
print(tabulate(table, headers=headers, tablefmt='orgtbl'))
