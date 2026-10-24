# CECW-EG (pages 105-108)

TABLE 5-5 (Continued)
c. Fixed Head Pile in Cohesive Soil
Pile Equations Diagram
(5-23a)
Short
L ≤ Lcs
(5-23b)
(5-23c)Intermediate
Lcs ≤ L
L ≥ Lcl
(5-23d)
(5-23e)
Long
L ≥ Lcl
d. Fixed Head Pile in Cohesionless Soil
Pile Equations Diagram
(5-25a)
Short
L ≤ Lcs
(5-25b)
TABLE 5-5 (Concluded)
Pile Equations Diagram
(5-25c)
Intermediate
Lcs ≤ Lcl
L ≥ Lcl (5-25d)
(5-25e)
Long
L ≥ Lcl
e. Nomenclature
Bs = diameter of pile shaft, ft
Cu = undrained shear strength, kips/ft2
c = distance from centroid to outer fiber, ft
e = length of pile above ground surface, ft
1.5Bs + f = distance below ground surface to point of maximum bending moment in cohesive soil, ft
f = distance below ground surface at point of maximum bending moment in cohesionless soil, ft
fy = pile yield strength, ksf
Ip = pile moment of inertia, ft4
Kp = Rankine coefficient of passive pressure, tan2(45 + φ’/2)
L = embeded pile length, ft
Lc = critical length between long and short pile, ft
Lcs = critical length between short and intermediate pile, ft
Lcl = critical length between intermediate and long pile, ft
Ma = applied bending moment, positive in clockwise direction, kips-ft
My = ultimate resisting bending moment of entire cross-section, kips-ft
T = lateral load, kips
Tu = ultimate lateral load, kips
Tul = ultimate lateral load of long pile in cohesionless soil, kips
Z = section modulus I p/c, ft3
Zmax = maximum section modulus, ft3
Zmin = minimum section modulus, ft3
γ = unit wet weight of soil, kips/ft3
φ’ = effective angle of internal friction of soil, degrees
(1) Considerations.
(a) Lateral load failure may occur in short drilled shafts and piles, which
behave as rigid members, by soil failure and excessive pile deflection and in long
piles by excessive bending moment.
(b) Computation of lateral deflection for different shaft penetrations may be
made to determine the depth of penetration at which additional penetration will not
significantly decrease the groundline deflection. This depth will be approximately
4β for a soil in which the soil stiffness increases linearly with depth
(5-26)
where
Ep = elastic modulus of shaft or pile, ksf
Ip = moment of inertia of shaft, ft4
k = constant relating elastic soil modulus with depth, E s =k z
kips/ft3
Shafts which carry insignificant axial loads such as those supporting overhead signs
can be placed at this minimum depth if their lateral load capacity is acceptable.
(c) Cyclic loads reduce the support provided by the soil, cause gaps to
appear near the ground surface adjacent to the shaft, increase the lateral
deflection for a given applied lateral load and can reduce the ultimate lateral load
capacity because of the loss of soil support.
(d) Refer to ASTM D 3966 for details on conducting lateral load tests.
(2) Broms’ Closed Form Solution. Broms’ method uses the concept of a
horizontal coefficient of subgrade reaction and considers short pile failure by flow
of soil around the pile and failure of long piles by forming a plastic hinge in the
pile. Refer to Broms (1964a), Broms (1964b), Broms (1965), and Reese (1986) for
estimating T u from charts.
(a) Cohesive soil to depth 1.5B s is considered to have negligible
resistance because a wedge of soil to depth 1.5B s is assumed to move up and when
the pile is deflected.
(b) Iteration is required to determine the ultimate lateral capacity of long
piles T ul in cohesionless soil, Table 5-5. Distance f, Table 5-5b and 5-5d, may
first be estimated and T ul calculated; then, f is calculated and T ul
recalculated as necessary. T ul is independent of length L in long piles.
(3) Load Transfer Analysis. The method of solution using load transfer p-y
curves is also based on the concept of a coefficient of horizontal subgrade
reaction. A fourth-order differential equation is solved using finite differences
and load transfer p-y curves.
(a) Numerous p-y relationships are available to estimate appropriate values
of soil stiffness for particular soil conditions (Reese 1986). p-y curves developed
from local experience and back-calculated from lateral load tests may also be used
in program COM624G.
(b) Program COM624G has provided excellent agreement with experimental data
for many load test results.
b. Allowable Lateral Loads. Estimates of allowable lateral load T a is best
accomplished from results of lateral load-deflection (p-y) analysis using given p-y
cuves and a computer program such as COM624G. The specified maximum allowable
lateral deflection should be used to estimate T a.
(1) Minimum and maximum values of the expected soil modulus of subgrade
reaction should be used to determine a probable range of lateral load capacity.
This modulus may be estimated from results of pressuremeter tests using the Menard
deformation modulus (Reese 1986), estimates of the elastic soil modulus with depth,
or values given in Table 5-6b.
(2) A rough estimate of allowable lateral load T a may be made by
calculating lateral groundline deflection y o using Equations in Table 5-6,
(5-27)
where y a is a specified allowable lateral deflection and T u is estimated from
equations in Table 5-5.
c. Example Application. A concrete drilled shaft is to be constructed to
support a design lateral load Td = 10 kips. This load will be applied at the ground
surface, therefore length above the ground surfacee=0 . Lateral deflection should
be no greater than ya = 0.25 inch. An estimate is required to determine a suitable
depth of penetration and diameter to support this lateral load in a clay with
cohesion C u = 1 ksf for a soil in which the elastic modulus is assumed to increase
linearly with depth. A trial diameter B s = 2.5 ft (30 inches) is selected with 1
percent steel. Yield strength of the steel f’ ys = 60 ksi and concrete strength f’c =
3 ksi.
(1) Minimum Penetration Depth. The minimum penetration depth may be
estimated from Equation 5-26 using E pIp and k. Table 5-7 illustrates calculation
of E pIp for a reinforced concrete shaft which is 2.7 105 kips-ft2. k = 170 kips/ft 3
from Table 5-6b when the elastic modulus increases linearly with depth. Therefore,
The minimum depth of penetration L = 4 β = 4 4.37 = 17.5 ft. Select L = 20 ft.
