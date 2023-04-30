import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import frame


def  matrix2frame(P) -> frame.Frame3D:
    return frame.Frame3D(
        u=frame.Vector3D(*[float(i) for i in P[:3, 0]]),
        v=frame.Vector3D(*[float(i) for i in P[:3, 1]]),
        w=frame.Vector3D(*[float(i) for i in P[:3, 2]]),
        o=frame.Vector3D(*[float(i) for i in P[:3, 3]]),
    )


def draw_pose(ax: mplot3d.axes3d.Axes3D, P, label) -> None:
    F = matrix2frame(P)
    frame.draw_3Dframe(ax, F, label)


def draw_pose_onto_xy_plane(ax: plt.axis, P, label) -> None:
    F = matrix2frame(P)
    frame.draw_3Dframe_onto_xy_plane(ax, F, label)
