# CECW-EG (pages 113-116)

Figure 5-14. Schematic of group
Eg should be > 0.7 for spacings > 3Bs and 1.0 for spacings > 8Bs.E g should vary
linearly for spacings between 3Bs and 8B s.E g = 0.7 for spacings ≤ 2.5Bs.
(b) Group capacity by the equivalent method is
(5-28b)
where
L = depth of penetration, ft
W = horizontal length of group, ft
B = horizontal width of group, ft
Cua = average undrained shear strength of the cohesive soil in which the
group is placed, ksf
Cub = average undrained shear strength of the cohesive soil below the
tip to a depth of 2B below the tip, ksf
The presence of locally soft soil should be checked because this soil may cause some
shafts to fail.
(c) The ultimate bearing capacity of a group in a strong clay soil overlying
weak clay may be estimated by assuming block punching through the weak underlying
soil layer. Group capacity may be calculated by Equation 5-28b using the undrained
strength C ub of the underlying weak clay. A less conservative solution is
provided by (Reese and O’Neill 1988)
(5-29)
where
Qug,lower = bearing capacity if base at top of lower (weak) soil, kips
Qug,upper = bearing capacity in the upper soil if the softer lower soil
soil were not present, kips
Hb = vertical distance from the base of the shafts in the group to
the top of the weak layer, ft
B = least width of group, ft
(2) Cohesionless Soil. During construction of drilled shafts in cohesionless
soil, stress relief may be more severe than in cohesive soils because cohesionless
soils do not support negative pore pressures as well as cohesive soils. Negative
pore pressures generated during excavation in cohesive soils tend to keep effective
stresses higher than in cohesionless soil.
(a) The efficiency Equation 5-28a is usually recommended.
(b) Equation 5-29 can be used to estimate ultimate bearing capacity of a
group in a strong cohesionless soil overlying a weak cohesive layer.
b. Lateral Load Capacity. Response of groups to lateral load requires
lateral and axial load soil-structure interaction analysis with assistance of a
finite element computer program.
(1) Widely Spaced Drilled Shafts. Shafts spaced > 7Bs or far enough apart
that stress transfer is minimal and loading is by shear, the ultimate lateral load
of the group T ug is the sum of individual shafts. The capacity of each shaft may
be estimated by methodology in 5-4.
(2) Closely Spaced Drilled Shafts. The solution of ultimate lateral load
capacity of closely spaced shafts in a group requires analysis of a nonlinear soilshaft system
(5-30)
where
Tuj = ultimate lateral load capacity of shaft j, kips
n = number of shafts in the group
Refer to Poulos (1971a, Poulos (1971b), and Reese (1986) for detailed solution of
the lateral load capacity of each shaft by the Poulos-Focht-Koch method.
(3) Group Behavior as a Single Drilled Shaft. A pile group may be simulated
as a single shaft with diameter C g/π where C g is the circumference given as the
minimum length of a line that can enclose the group. The moment of inertia of the
group is n Ip where I p is the moment of inertia of a single shaft. Program
COM624G may be used to evaluate lateral load-deflection behavior of the simulated
single shaft for given soil conditions. Comparison of results between the Poulos-
Focht-Koch and simulated single pile methods was found to be good (Reese 1986).
Section II. Driven Piles
5-6. Effects of Pile Driving. Driving piles disturbs and substantially remolds
soil. Driving radially compresses cohesive soils and increases the relative density
of cohesionless soils near the pile.
a. Cohesive Soil. Soil disturbance around piles driven into soft or normally
consolidated clays is within one pile diameter. Driving into saturated stiff clays
closes fissures and causes complete loss of stress history near the pile (Vesic
1969).
(1) Driving in Saturated Clay. Soil disturbance and radial compression
increase pore water pressures that temporarily reduce the soil shear strength and
pile load capacity. Pore pressures decrease with time after driving and lead to an
increase in shear strength and pile load capacity. This effect is soil freeze.
(2) Driving in Unsaturated Clay. Driving in unsaturated clay does not
generate high pore pressures and probably will not lead to soil freeze.
b. Cohesionless Soil. The load capacity of cohesionless soil depends
strongly on relative density. Driving increases relative density and lateral
displacement within a zone around the pile of one to two pile diameters. Large
displacement piles such as closed end pipe piles cause larger increases in relative
density than small displacement piles such as H-piles. The increase in bearing
capacity can therefore be greater with large displacement piles.
(1) Driving in Dense Sand and Gravel. Driving in dense sand and gravel can
decrease pore pressures from soil dilation and temporarily increase soil shear
strength and pile load capacity. Shear strength can increase substantially and may
exceed the capacity of pile driving equipment to further drive the piles into the
soil. Pore pressures increase after driving and cause the shear strength to
decrease and reduce the pile load capacity. This effect is soil relaxation.
(2) Driving in Saturated Cohesionless Silts. Driving in saturated
cohesionless silts increases pore pressures and can temporarily reduce the soil
shear strength and pile load capacity. Pore pressures dissipate after driving and
lead to an increase in shear strength and pile load capacity. This effect is soil
freeze as described in cohesive soil, but can occur more quickly than in cohesive
soil because permeability is greater in silts.
5-7. Vertical Capacity of Single Driven Piles. The vertical capacity of driven
piles may be estimated using Equations 5-1 similar to drilled shafts
(5-1a)
(5-1b)
where
Qu = ultimate bearing capacity, kips
Qbu = ultimate end bearing resistance, kips
Qsu = ultimate skin friction, kips
qbu = unit ultimate end bearing resistance, ksf
Ab = area of tip or base, ft2
n = number of pile elements
Qsui = ultimate skin friction of pile element i, ksf
Wp = pile weight, ≈ Ab L γp without enlarged base, kips
L = pile length, ft
γp = pile density, kips/ft3
In addition, a wave equation analysis should be performed to estimate the driving
forces to prevent pile damage during driving, to estimate the total driving
resistance that will be encountered by the pile to assist in determining the
required capability of the driving equipment and to establish pile driving criteria.
Refer to program GRLWEAP (Goble Rausche Likins and Associates, Inc. 1988) for
details of wave equation analysis. Pile driving formulas are also recommended to
quickly estimate the ultimate bearing capacity.
a. End Bearing Capacity. End bearing capacity may be estimated by
(5-2a)
where
c = cohesion of soil beneath the tip, ksf
σ’L = effective soil vertical overburden pressure at pile base
≈γ ’L ,k s f
γ’L = effective wet unit weight of soil along shaft length L,
kips/ft3
Bb = base diameter, ft
γ’b = effective wet unit weight of soil beneath base, kips/ft3
Ncp,Nqp,Nγp = pile bearing capacity factors of cohesion, surcharge, and
wedge components
ζcp,ζqp,ζγp = pile soil and geometry correction factors of cohesion,
surcharge, and wedge components
Equation 5-2a may be simplified for driven piles by eliminating the N γp term
(5-2b)
or
(5-2c)
Equations 5-2b and 5-2c also adjust for pile weight W p assuming γp ≈γ ’L.
Equation 5-2c is usually used because omitting the "1" is usually negligible.
Bearing capacity does not increase without limit with increasing depth. Refer to
Figure 5-3 to determine the critical depth Lc below which effective stress remains
constant using the Meyerhof and Nordlund methods.
(1) Cohesive Soil. The shear strength of cohesive soil is c = C u, the
undrained strength, and the effective friction angle φ’ = 0. Equation 5-2a leads
to
(5-2d)
where shape factor ζcp = 1 and N cp = 9. Undrained shear strength C u is estimated
by methods in Chapter 3 and may be taken as the average shear strength within 2B b
beneath the tip of the pile.
(2) Cohesionless Soil. Meyerhof, Nordlund, and in situ methods described
below and Hanson, Vesic, and general shear methods described in Section I are
recommended for solution of ultimate end bearing capacity using Equations 5-2.
Several of these methods should be used for each design problem to provide a
reasonable range of probable bearing capacity if calculations indicate a significant
difference between methods.
