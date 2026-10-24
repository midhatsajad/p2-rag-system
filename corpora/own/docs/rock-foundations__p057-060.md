# CECW-EG (pages 57-60)

this respect, the effects of strain compatibility may require
special interpretation of data from in-situ tests, laboratory
tests, and finite element analyses.
f. Factor of safety . Limit equilibrium solutions for
sliding stability assume that the factor of safety of all
wedges are equal.
7-7. Analytical Techniques for Multi-Wedge
Systems
a. General wedge equations . The general wedge
equations are derived from force equilibrium of all
wedges in a system of wedges defined by the geometry of
the structure and potential failure surfaces. Consider the
ith wedge in a system of wedges illustrated in Figure 7-2.
The necessary geometry notation for the ith wedge and
adjacent wedges are as shown (Figure 7-2). The origin of
the coordinate system for the wedge considered is located
in the lower left hand corner of the wedge. The x and y
axes are horizontal and vertical respectively. Axes which
are tangent ( t) and normal ( n) to the failure plane are
oriented at an angle ( α) with respect to the +x and +y
axes. A positive value of α is a counterclockwise rotation, a negative value of α is a clockwise rotation. The
distribution of pressures/stresses with resulting forces is
illustrated in Figure 7-3. Figure 7-4 illustrates the free
body diagram of the resulting forces. Summing the forces
normal and tangent to the potential failure surface and
solving for ( Pi-1 - Pi) results in the following equation for
the ith wedge:
(7-3)
(Pi 1 Pi ) ((Wi Vi )cos αi
Ui (HLi HRi )sin αi )
tanφi
FSi
(HLi HRi )cos αi

(Wi Vi )sinαi
Ci
FSi
Li
÷


cosαi sinαi
tanφi
FSi
where
i = subscript notation for the wedge considered
Figure 7-2. Hypothetical i th wedge and adjacent
wedges subject to potential sliding
P = horizontal residual forces acting between
wedges as a result of potential sliding
W = the total weight of wedge to include rock, soil,
concrete and water (do not use submerged
weights)
V = any vertical force applied to the wedge
α = angle of potential failure plane with respect to
the horizontal (- α denotes downslope sliding,
+α denotes upslope sliding)
U = the uplift force exerted on the wedge at the
potential failure surface
H = in general, any horizontal force applied to the
wedge (HL and HR refers to left and right hard
forces as indicated in Figures 7-3 and 7-4)
L = the length of the wedge along the potential
failure surface
FS = the factor of safety
Figure 7-3. Distribution of pressures, stresses and
resultant forces acting on the hypothetical i th wedge
c = the cohesion shear strength parameter
φ = the angle of internal friction
b. Equilibrium requirements . An inspection of
Equation 7-3 reveals that for a given wedge there will be
two unknowns (i.e., ( Pi-1 - Pi) and FS). In a wedge system with n number of wedges, Equation 7-3 will provide
n number of equations. Because FS is the same for all
wedges there will be n + 1 unknowns with n number of
equations for solution. The solution for the factor of
safety is made possible by a conditional equation establishing horizontal equilibrium of the wedge system. This
equation states that the sum of the differences in horizontal residual forces ( Pi-1 - Pi) acting between wedges must
equal the differences in the horizontal boundary forces.
Since boundary forces are usually equal to zero, the conditional equation is expressed as
(7-4)
i n
i 1
(Pi 1 Pi ) 0
where
Figure 7-4. Free body diagram of the hypothetical i th
wedge
n = the total number of wedges in the system.
c. Alternate equation . An alternate equation for the
implicit solution of the factor of safety for a system of n
wedges is given below:
(7-5a)FS
i n
i 1
Ci Li cosαi (Wi Vi Ui cosαi )tan φi
nαi
i n
i 1
[Hi (Wi Vi )tan αi ]
where
(7-5b)nαi
1 tanφi tanαi
FS
1 tan2αi
All other terms are as defined above. The derivation of
Equations 7-5 follows that of Equations 7-3 and 7-4
except that forces are summed with respect to the x and y
coordinates.
7-8. Preliminary Procedures
Factor of safety solutions for a multi-wedge system containing a number of potential failure surfaces can result in
a significant book-keeping problem. For this reason, it is
recommended that prior to the analytical solution for the
factor of safety, the following preliminary procedures be
implemented.
a. Define and identify on a scale drawing all potential failure surfaces based on the stratification, location,
orientation, frequency, and distribution of discontinuities
within the foundation material as well as the geometry,
location, and orientation of the structure.
b. For each potential failure surface, divide the mass
into a number of wedges. A wedge must be created each
time there is a change in slip plane orientation and/or a
change in shear strength properties. However, there can
be only one structural wedge.
c. For each wedge draw a free body diagram which
shows all the applied and resulting forces acting on that
wedge. Include all necessary dimensions on the free body
diagram. Label all forces and dimensions according to
the appropriate parameter notations discussed above.
d. Prepare a table, which lists all parameters, to
include shear strength parameters for each wedge in the
system of wedges defining the potential slip mass.
7-9. Analytical Procedures
While both the general wedge equation and the alternate
equation will result in the same calculated factor of safety
for a given design case, the procedure for calculating that
value is slightly different. Solutions for hypothetical
example problems are provided in EM 1110-2-2200 and
Nicholson (1983a).
a. General wedge method . The solution for the
factor of safety using Equations 7-3 and 7-4 requires a
trial-and-error procedure. A trial value for the factor of
safety, FS, is inserted in Equation 7-3 for each wedge to
obtain values of the differences in horizontal residual P
forces acting between wedges. The differences in P
forces for each wedge are then summed; a negative value
indicates that the trial value of FS was to high and conversely a positive value indicates that the trial value of FS
was too low. The process is repeated until the trial FS
value results in an equality from Equation 7-4. The value
of FS which results in an equality is the correct value for
the factor of safety. The number of trial-and-error cycles
can be reduced if trial values of FS are plotted with
respect to the sum of the differences of the P forces (see
examples in EM 1110-2-2200 and Nicholson (1983a)).
b. Alternate methods . Equations 7-5a and 7-5b,
when expanded, can be used to solve for the factor of
safety for a system containing one or more wedges.
Since the nα term, defined by Equation 7-5b, is a function
of FS, the solution for FS requires an iterative process.
An assumed initial value of FS is inserted into the nα term
for each wedge in the expanded form of Equation 7-5a,
and a new factor of safety is calculated. The calculated
factor of safety is then inserted into the nα term. The
process is repeated until the inserted value of FS equals
the calculated value of FS. Convergence to within two
decimal places usually occurs in 3 to 4 iteration cycles.
c. Comparison of methods . The general wedge equation (Equation 7-3) was formulated in terms of the difference in horizontal boundary forces to allow the design
engineer to solve directly for forces acting on the structure for various selected factors of safety. The procedure
has an advantage for new structures in that it allows a
rapid assessment of the horizontal forces necessary for
equilibrium for prescribed factors of safety. The alternate
equation (Equation 7-5a and 7-5b) solves directly for FS.
Its advantage is in the assessment of stability for existing
structures. Both equations are mathematically identical
(Nicholson 1983a).
7-10. Design Considerations
Some special considerations for applying the general
wedge equation to specific site conditions are discussed
below.
a. Active wedge . The interface between the group of
active wedges and the structural wedge is assumed to be a
vertical plane located at the heel of the structural wedge
and extending to the base of the structural wedge. The
magnitudes of the active forces depend on the actual
values of the safety factor, the inclination angles ( α)o f
the slip path, and the magnitude of the shear strength that
can be developed. The inclination angles, corresponding
to the maximum active residual P forces for each potential failure surface, can be determined by independently
analyzing the group of active wedges for trial safety factors. In rock the inclination may be predetermined by
discontinuities in the foundation.
b. Structural wedge . Discontinuities in the slip path
beneath the structural wedge should be modeled by
assuming an average slip-plane along the base of the
structural wedge.
c. Passive wedge . The interface between the group
of passive wedges and the structural wedge is assumed to
be a vertical plane located at the toe of the structural
wedge and extending to the base of the structural wedge.
The magnitudes of the passive residual P forces depend
on the actual values of the safety factor, the inclination
angles of the slip path, and the magnitude of shear
strength that can be developed. The inclination angles,
corresponding to the minimum passive residual P forces
for each potential failure mechanism, can be estimated by
independently analyzing the group of passive wedges for
trial safety factors. When passive resistance is used special considerations must be made. Removal of the passive wedge by future construction must be prevented.
Rock that may be subjected to high velocity water scouring should not be used unless amply protected. Also, the
compressive strength of the rock layers must be sufficient
to develop the wedge resistance. In some cases wedge
resistance should not be assumed without resorting to
special treatment such as installing rock anchors.
d. Tension cracks . Sliding analyses should consider
the effects of cracks on the active side of the structural
wedge in the foundation material due to differential settlement, shrinkage, or joints in a rock mass. The depth of
cracking in cohesive foundation material can be estimated
in accordance with the following equations.
(7-6a)dc
2cd
γ tan


45 φd
2
where
(7-6b)cd
c
FS
(7-6c)φd tan 1 

tanφ
FS
The value ( dc) in a cohesive foundation cannot exceed the
embedment of the structural wedge. The depth of cracking in massive, strong, rock foundations should be
assumed to extend to the base of the structural wedge.
Shearing resistance along the crack should be ignored and
full hydrostatic pressure should be assumed to extend to
the bottom of the crack. The hydraulic gradient across
the base of the structural wedge should reflect the
presence of a crack at the heel of the structural wedge.
e. Uplift without drains . The effects of seepage
forces should be included in the sliding analysis.
Analyses should be based on conservative estimates of
uplift pressures. Estimates of uplift pressures on the
wedges can be based on the following assumptions:
(1) The uplift pressure acts over the entire area of
the base.
(2) If seepage from headwater to tailwater can occur
across a structure, the pressure head at any point should
reflect the head loss due to water flowing through a
medium. The approximate pressure head at any point can
be determined by the line-of-seepage method. This
method assumes that the head loss is directly proportional
to the length of the seepage path. The seepage path for
the structural wedge extends from the upper surface (or
internal ground-water level) of the uncracked material
adjacent to the heel of the structure, along the embedded
perimeter of the structural wedge, to the upper surface (or
internal ground-water level) adjacentto the toe of the
structure. Referring to Figure 7-5, the seepage distance is
defined by points a, b, c, and d. The pressure head at any
point is equal to the elevation head minus the product of
the hydraulic gradient times the distance along the seepage path to the point in question. Estimates of pressure
heads for the active and passive wedges should be consistent with those of the heel and toe of the structural wedge.
(3) For a more detailed discussion of the line-ofseepage method, refer to EM 1110-2-2502, Retaining and
Flood Walls. For the majority of structural stability computations, the line-of-seepage is considered sufficiently
accurate. However, there may be special situations where
the flow net method is required to evaluate seepage
problems.
f. Uplift with drains . Uplift pressures on the base of
the structural wedge can be reduced by foundation drains.
The pressure heads beneath the structural wedge developed from the line-of-seepage analysis should be modified
to reflect the effects of the foundation drains. The maximum pressure head along the line of foundation drains
can be estimated from Equation 7-7:
(7-7)Ux U1 R 

L x
L (U2 U1)
