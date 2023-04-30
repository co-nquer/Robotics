import sympy as sp
from my_modules.kinematics import special_poses

def forward_kinematic(linkage: tuple[sp.Matrix, ...], joint_values: dict[sp.Symbol, float|int]) -> sp.Matrix:
    """
    For chains only!

    returns
        1) sp.eye(4) if index == 0

        2) EE pose if index is None (or index == len(self.linkage) + 1)
        
        3) pose of 'index'-th frame
    """
    P = sp.eye(4)
    for i in linkage:
        P *= i.evalf(subs=joint_values)
    return P


class KinimaticChain_RPR:
        """
        Kinematic chain from Task 01 in Robotics 2 SoSe2023.
        """
        def __init__(self):
            # Joint variables
            self.q = sp.symbols(f"q:{3}")

            # (constant) link displacements
            L1 = special_poses.trans(0, 1, 0) @ special_poses.rot_z(sp.pi / 4)
            L2 = special_poses.trans(sp.sqrt(2), 0, 0) @ special_poses.rot_y(sp.pi / 2)
            L3 = special_poses.trans(0, 0, sp.sqrt(2)) @ special_poses.rot_y(-sp.pi / 2) @ special_poses.rot_z(
                sp.pi / 2 + sp.pi / 4)
            L4 = special_poses.trans(2, 0, 0) @ special_poses.rot_y(sp.pi / 2)

            # (symbolic) joint displacements
            J12 = special_poses.rot_z(self.q[0])
            J23 = special_poses.trans(0, 0, self.q[1])
            J34 = special_poses.rot_z(self.q[2])

            self.linkage = (L1, J12, L2, J23, L3, J34, L4)

        def forward_kinematic(self, joint_values: dict[sp.Symbol, float|int], index: int = None) -> sp.Matrix:
             """
             returns
                1) sp.eye(4) if index == 0

                2) EE pose if index is None (or index == len(self.linkage))

                3) pose of 'index'-th frame
             """
             return forward_kinematic(self.linkage[:index], joint_values)
