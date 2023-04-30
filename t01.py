"""
Tasks sheet T01: Technical Tools, Mobility, and Robotics-1 Continuation (I)
"""

import sys
import os
sys.path.append(os.path.join(os.getcwd(), "my_modules"))
sys.path.append(os.path.join(os.getcwd(), "my_modules", "kinematics"))
sys.path.append(os.path.join(os.getcwd(), "my_modules", "matplotlib_extension"))
sys.path.append(os.path.join(os.getcwd(), "my_modules", "robots"))

import matplotlib.pyplot as plt
import sympy as sp

from my_modules import matplotlib_extension
from my_modules import robots


##########################################################################################
# Utility
##########################################################################################
def compute_index_for_2frame_convention(i: int) -> str:
    """
    input: i = 0, 1, ...
    output: (k, k+1)_m
    """
    k = i // 2 + (0 if i%2 == 0 else 1)
    m = k + (1 if i%2 == 0 else 0)
    return f"({k}{k+1})_{m}"


def plot2D(poses: list):

    fig2D = plt.figure()
    ax2D = fig2D.subplots()

    ax2D.set_xlim(-4, 4)
    ax2D.set_ylim(-4, 4)
    ax2D.grid()

    for i, P in enumerate(poses):
        label = compute_index_for_2frame_convention(i)
        matplotlib_extension.pose.draw_pose_onto_xy_plane(ax2D, P, label)

def plot3D(poses: list):

        fig3D = plt.figure()
        ax3D = fig3D.add_subplot(111, projection='3d')

        ax3D.set_xlim(-3, 3)
        ax3D.set_ylim(-3, 3)
        ax3D.set_zlim(-3, 3)

        for i, P in enumerate(poses):
            label = compute_index_for_2frame_convention(i)
            matplotlib_extension.pose.draw_pose(ax3D, P, label)



##########################################################################################
# Exercise C
##########################################################################################
def exercise_c():
    C = robots.chainRPR.KinimaticChain_RPR()

    # Zero-pose
    q = dict(zip(C.q, [0, 0, 0]))  # dict: joint_symbol -> joint_value
    P40 = C.forward_kinematic(q)
    sp.pprint(P40)

    # An other configuration
    # q = dict(zip(C.q, [sp.pi/2, 1, sp.pi/2]))

    # Plot
    poses = [C.forward_kinematic(q, index=i) for i in range(len(C.linkage) + 1)]
    plot3D(poses)
    plot2D(poses)
    plt.show()


##########################################################################################
# Exercise D
##########################################################################################
def exercise_d() -> None:
    ...


exercise_c()
#exercise_d()
