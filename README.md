# Robotics
A place to collaboratly work on tasks in *robotics*.

# Tasks
**From the lecture "Robotics 2: Modeling, Analysis, and Control":**
1. [T01: Technical Tools, Mobility, and Robotics-1 Continuation (I)](t01)
2. 
3. 

# Modules
## [Kinematics](my_modules/kinematics)
**Description:**    Provides modules related to computing the kinematics of a mechanism.
### [Special Poses](my_modules/kinematics/special_poses.py)
**Introduction:**    A pose $[ P ]_M$ is a description of position and orientation of a frame 
(wrt either an explicitly named frame $M$ or the base frame) by a homogeneous matrix

$$
P \in \mathrm{SE}(3) = \set{ \begin{pmatrix}
R & \pmb{p} \\
\pmb{0} & 1
\end{pmatrix} | R \in \mathrm{SO}(3), \pmb{p} \in \mathbb{R}^3 \}
$$

**Description:**    The module [special_poses](my_modules/kinematics/special_poses.py) should provide some functions to generate frequently
needed poses/displacements such as translation and elementary rotations.

## [Matplotlib Extension](my_modules/matplotlib_extension)
**Description:**    Provides modules that extend *matplotlib* by functions that help to visualize robotics, like drawing *frames*.

<img src="https://user-images.githubusercontent.com/131150356/235358285-dab050c2-337d-4ed4-b071-05c5be95ef36.png" width="400" /> <img src="https://user-images.githubusercontent.com/131150356/235358277-78570cff-590c-40c6-8009-0542893edc00.png" width="400" />

## [Robots](my_modules/robots)
**Description:**    Provides models of certain robots.
