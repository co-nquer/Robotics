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

######################################################################################
# Example
######################################################################################
if __name__ == "__main__":

    def example_3Dplot(poses: list):

        fig3D = plt.figure()
        ax3D = fig3D.add_subplot(111, projection='3d')
        #print(type(ax2D))

        ax3D.set_xlim(-3, 3)
        ax3D.set_ylim(-3, 3)
        ax3D.set_zlim(-3, 3)

        for i, P in enumerate(poses):
            matplotlib_extension.pose.draw_pose(ax3D, P, str(i))


    def example_2Dplot(poses: list):

        fig2D = plt.figure()
        ax2D = fig2D.subplots()
        #print(type(ax2D))

        ax2D.set_xlim(-6, 6)
        ax2D.set_ylim(-6, 6)

        for i, P in enumerate(poses):
            matplotlib_extension.pose.draw_pose_onto_xy_plane(ax2D, P, str(i))


    def main():
        C = robots.chainRPR.KinimaticChain_RPR()

        # dict: joint_symbol -> joint_value
        #q = dict(zip(C.q, [0, 0, 0]))
        q = dict(zip(C.q, [sp.pi/2, 2, sp.pi/2]))

        poses = [C.forward_kinematic(q, index=i) for i in range(len(C.linkage) + 1)]

        #print(*frames, sep="\n")
        
        example_3Dplot(poses)
        example_2Dplot(poses)
        plt.show()
        
    main()