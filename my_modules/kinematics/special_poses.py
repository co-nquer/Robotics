import sympy as sp


def rot_x(angle_rad) -> sp.Matrix:
    c = sp.cos(angle_rad)
    s = sp.sin(angle_rad)
    return sp.Matrix([
        [1, 0,  0, 0],
        [0, c, -s, 0],
        [0, s,  c, 0],
        [0, 0,  0, 1]])


def rot_y(angle_rad) -> sp.Matrix:
    c = sp.cos(angle_rad)
    s = sp.sin(angle_rad)
    return sp.Matrix([
        [c,  0,  s, 0],
        [0,  1,  0, 0],
        [-s, 0,  c, 0],
        [0,  0,  0, 1]])


def rot_z(angle_rad) -> sp.Matrix:
    c = sp.cos(angle_rad)
    s = sp.sin(angle_rad)
    return sp.Matrix([
        [c,  -s,  0, 0],
        [s,   c,  0, 0],
        [0,   0,  1, 0],
        [0,   0,  0, 1]])


def trans(x, y, z) -> sp.Matrix:
    return sp.Matrix([
        [1, 0, 0, x],
        [0, 1, 0, y],
        [0, 0, 1, z],
        [0, 0, 0, 1],
    ])
