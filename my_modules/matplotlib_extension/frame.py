import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from typing import NamedTuple


class Vector3D(NamedTuple):
    """
    Coordinates of a 3D vector.
    """
    x: int|float
    y: int|float
    z: int|float

    def __add__(self, other):
        return Vector3D(
            x = self.x + other.x,
            y = self.y + other.y,
            z = self.z + other.z,
        )


class Frame3D(NamedTuple):
    """
    A quadtruple of 3D vectors that should represent a 3D coordinate system, where
    (u, v and w) = basis; and o = origin; specified wrt the standard basis in R^3.
    """
    u: Vector3D
    v: Vector3D
    w: Vector3D
    o: Vector3D

    def __str__(self) -> str:
        s = "------------------------------\n"
        s += "  u       v       w       o\n"
        s += "------------------------------\n"
        for u, v, w, o in zip(self.u, self.v, self.w, self.o):
            s += "  "
            for i in (u, v, w, o):
                i = round(i, 2)
                s_tmp = str(i)
                s += s_tmp + (8 - len(s_tmp)) * " "
            s += "\n"
        s += "------------------------------"
        return s



def draw_3Dframe_onto_xy_plane(ax: plt.axis, F: Frame3D, label) -> None:
    """
    Draws the 3D frame onto the 3D axes and labels it.
    """
    # Cut of z-component
    u = F.u[:2]
    v = F.v[:2]
    w = F.w[:2]
    o = F.o[:2]

    # Origin
    ax.scatter(*o, color="black")

    # Basis, with color-coding: RGB <-> xyz
    ax.quiver(*o, *u, color="red", angles='xy', scale_units='xy', scale=1)
    ax.quiver(*o, *v, color="green", angles='xy', scale_units='xy', scale=1)
    ax.quiver(*o, *w, color="blue", angles='xy', scale_units='xy', scale=1)

    # Label
    position = [0.2 * sum(i) for i in zip(u, v, w)]
    position = [sum(i) for i in zip(o, position)]
    ax.text(*position, f"{label}")
    ...


def draw_3Dframe(ax: mplot3d.axes3d.Axes3D, F: Frame3D, label) -> None:
    """
    Draws the 3D frame onto the 3D axes and labels it.
    """

    # Origin
    ax.scatter(*F.o, color="black")

    # Basis, with color-coding: RGB <-> xyz
    ax.quiver(*F.o, *F.u, color="red")
    ax.quiver(*F.o, *F.v, color="green")
    ax.quiver(*F.o, *F.w, color="blue")

    # Label
    ax.text(*(F.o + F.w), f"{label}")


######################################################################################
# Example
######################################################################################
if __name__ == "__main__":

    def example_3Dplot(frames: list[Frame3D]):

        fig3D = plt.figure()
        ax3D = fig3D.add_subplot(111, projection='3d')
        #print(type(ax2D))

        ax3D.set_xlim(-3, 3)
        ax3D.set_ylim(-3, 3)
        ax3D.set_zlim(-3, 3)

        for i, F in enumerate(frames):
            draw_3Dframe(ax3D, F, str(i))


    def example_2Dplot(frames: list[Frame3D]):

        fig2D = plt.figure()
        ax2D = fig2D.subplots()
        #print(type(ax2D))

        ax2D.set_xlim(-3, 3)
        ax2D.set_ylim(-3, 3)

        for i, F in enumerate(frames):
            draw_3Dframe_onto_xy_plane(ax2D, F, str(i))


    def main():
        F0 = Frame3D(
            u=Vector3D(1, 0, 0),
            v=Vector3D(0, 1, 0),
            w=Vector3D(0, 0, 1),
            o=Vector3D(0, 0, 0)
        )
        F1 = Frame3D(
            u=Vector3D(1, 0, 0),
            v=Vector3D(0, 1, 0),
            w=Vector3D(0, 0, 1),
            o=Vector3D(0, 1, 2)
        )

        frames = [F0, F1]

        print(*frames, sep="\n")
        
        example_3Dplot(frames)
        example_2Dplot(frames)
        plt.show()
        
    main()