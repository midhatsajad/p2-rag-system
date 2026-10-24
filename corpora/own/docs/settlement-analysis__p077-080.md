# CECW-EG (pages 77-80)

(1) Program FD31 does not consider the influence of the vertical stress
distribution with depth, and, therefore, it is applicable to fills or embankments with lateral dimensions substantially greater than the thickness of the
consolidating soil.
(2) Program CSETT considers loaded regions of simple and complex geometric shapes for single or multiple and time-dependent loads. Loads may be
2- or 3-D. Stress distributions may be calculated by either Boussinesq or
Westergaard methods. The program allows analysis of multiple soil layers and
a variety of drainage conditions. Output consists of total settlement, settlement of individual layers, and degree of consolidation as a function of
time and location requested by the user.
d. Settlement of Soft Soil . Settlement from desiccation and consolidation in soft, compressible soil with large void ratios may be computed by Program PCDDF (item 8). This program is applicable to dredged material and considers time-dependent loads, influence of void ratio on self-weight, permeability, nonlinear effective stress relationships, and large strains.
e. Settlement of Shallow Foundations in Sand . Corps Program I0030,
"CSANDSET", can calculate the immediate settlement in sands of 14 different
procedures including Alpan, Schultze and Sherif, Terzaghi and Peck, Schmertmann, and elastic methods. Program I0030 considers water table depth, embedment depth, and foundation dimensions for a variety of soil conditions in
multilayer sands. Soil input data include SPT, CPT, elastic modulus, and
water table depth.
f. Vertical Displacement of Various Soil Types . Appendix F provides a
user’s manual and listing of computer program VDISPL for calculating immediate
settlement of granular materials using Schmertmann’s procedure modified to
consider prestress. Program VDISPL also can calculate immediate settlement of
an elastic soil, consolidation/swell of an expansive soil, and settlement of a
collapsible soil (see Chapter 5). Finite element program CON2D (item 15) may
be used to calculate plane strain 2-D consolidation settlement of embankments
and structures on multiple soil layers using the Cam Clay elasto-plastic constitutive soil model. CON2D may also analyze consolidation of saturated and
partly saturated earth masses for time-dependent vertical loads to determine
settlement, rate of settlement, and pore pressure distribution. This program
may analyze the condition of saturated and partly saturated earth mass.
Section IV. Secondary Compression and Creep
3-17. Description . Secondary compression and creep are time-dependent deformations that appear to occur at essentially constant effective stress with
negligible change in pore water pressure. Secondary compression and creep may
be a dispersion process in the soil structure causing particle movement and
may be associated with electrochemical reactions and flocculation. Although
creep is caused by the same mechanism as secondary compression, they differ in
the geometry of confinement. Creep is associated with deformation without
volume and pore water pressure changes in soil subject to shear; whereas,
secondary compression is associated with volume reduction without significant
pore water pressure changes.
a. Model . Secondary compression and creep may be modeled by empirical
or semi-empirical viscoelastic processes in which hardening (strengthening) or
softening (weakening) of the soil occurs. Hardening is dominant at low stress
levels; whereas, weakening is dominant at high stress levels. Deformation in
soil subject to a constant applied stress can be understood to consist of
three stages. The first stage is characterized by a change in rate of deformation that decreases to zero. The second or steady state stage occurs at a
constant rate of deformation. A third stage may also occur at sufficiently
large loads in which the rate of deformation increases ending in failure as a
result of weakening in the soil. Soil subject to secondary compression in
which the volume decreases as during a 1-D consolidometer test may gain
strength or harden with time leading to deformation that eventually ceases,
and, therefore, the second (steady state) and third (failure states) may never
occur.
b. Relative Influence . Secondary compression and creep are minor relative to settlement caused by elastic deformation and primary consolidation in
many practical applications. Secondary compression may contribute significantly to settlement where soft soil exists, particularly soft clay, silt,
and soil containing organic matter such as peat or Muskeg or where a deep compressible stratum is subject to small pressure increments relative to the
magnitiude of the effective consolidation pressure.
3-18. Calculation of Secondary Compression . Settlement from secondary compression ρs has been observed from many laboratory and field measurements to
be approximately a straight line on a semi-logarithmic plot with time, Figure
3-17a, following completion of primary consolidation. The decrease in void
ratio from secondary compression is
(3-30)
where
∆est = change in void ratio from secondary compression at time t
Cα = coefficient of secondary compression
t = time at which secondary compression settlement is to be calculated, days
t100 = time corresponding to 100 percent of primary consolidation, days
Secondary compression settlement is calculated from Equation 3-20 similar to
primary consolidation settlement.
a. Coefficient of Secondary Compression .C α is the slope of the void
ratio-logarithm time plot for time exceeding that required for 100 percent of
primary consolidation, t100 .t 100 is arbitrarily determined as the intersection of the tangent to the curve at the point of inflection with the tangent to the straight line portion representing a secondary time effect, Figure
3-17a.
b. Estimation of C α. A unique value of C α/Cc has been observed,
Table 3-14, for a variety of different types of soils. The ratio C α/Cc is
constant and the range varies between 0.025 and 0.100 for all soils. High
values of C α/Cc relate to organic soils. C α will in general increase with
Table 3-14
Coefficient of Secondary Compression C α
(Data from Item 43)
Soil Cα/Cc
Clay 0.025 - 0.085
Silt 0.030 - 0.075
Peat 0.030 - 0.085
Muskeg 0.090 - 0.100
Inorganic 0.025 - 0.060
time if the effective consolidation pressure σ’ is less than a critical
pressure or the preconsolidation stress σ’p . For σ’ greater than σ’p ,C α
will decrease with time; however, C α will remain constant with time within
the range of effective pressure σ’> σ’p if C c also remains constant (e.g.,
the slope of the e-log σ curve is constant for σ’> σ’p ). A first approximation of the secondary compression index C α is 0.0001Wn for 10 < Wn < 3000
where W n is the natural water content in percent (after NAVFAC DM 7.1).
c. Accuracy . Soil disturbance decreases the coefficient of secondary
compression in the range of virgin compression. Evaluation of settlement
caused by secondary compression has often not been reliable.
d. Example Problem . The coefficient of secondary compression was determined to be 0.0033 and time t 100 is 392 minutes or 0.27 day , Figure 3-
17a, for this example problem. The change in void ratio after time t = 10
years or 3640 days is, Equation 3-30,
The settlement from Equation 3-20 for an initial void ratio e 100 = 0.96 is
for a stratum of 20-ft thickness.
CHAPTER 4
EVALUATION OF SETTLEMENT FOR
DYNAMIC AND TRANSIENT LOADS
4-1. General . Dynamic and transient forces cause particle rearrangements and
can cause considerable settlement, particularly in cohesionless soils, when
the particles move into more compact positions. A large portion of dynamic
live forces applied to foundation soil is from traffic on pavements. Dynamic
forces from a rolling wheel depressing a pavement cause a multidirectional
combination of cyclic shear and compression strains that precludes presentation of an appropriate settlement analysis in this chapter. This chapter provides guidance for analysis of settlement from earthquakes and repeated loads.
a. Amount of Settlement . The amount of settlement depends on the initial density of the soil, thickness of the soil stratum, and the maximum shear
strain developed in the soil. Cohesionless soils with relative densities D r
greater than about 75 percent should not develop significant settlement; however, intense dynamic loading can cause some settlement of 1 to 2 percent of
the stratum thickness even in dense sands.
b. Cause of Differential Settlement . A major cause of differential
settlement is the compaction of loose sands during dynamic loading. Vibrations caused by machinery often cause differential settlement that may require
remedial repairs or limitations on machine operations.
c. Time Effects . Time required for settlement from shaking can vary
from immediately to almost a day. Settlement in dry sands occurs immediately
during shaking under constant effective vertical stress. Shaking of saturated
sands induces excess pore water pressures which lead to settlement when the
pore pressures dissipate.
d. Accuracy . Errors associated with settlement predictions from dynamic loads will exceed those for static loads and can be 50 percent or more.
These first order approximations should be checked with available experience.
e. Minimizing Settlement . Dynamic settlement may be insignificant provided that the sum of dynamic and static bearing stresses remain less than 1/2
of the allowable bearing capacity. Settlements that might occur under sustained dynamic loadings may be minimized by precompaction of the soil using
dynamic methods. Dynamic compaction subjects the soil to severe dynamic loads
that reduces the influence of any later shaking on settlement. Refer to Chapter 6 for dynamic compaction methods of minimizing settlement. Refer to ER
1110-2-1806 for general guidance and direction for seismic design and evaluation for all Corps of Engineer civil works projects.
4-2. Settlement from Earthquakes . Earthquakes primarily cause shear stress,
shear strain, and shear motion from deep within the earth that propagates up
toward the ground surface. This shear can cause settlement initially in deep
soil layers followed by settlement in more shallow layers. Settlement caused
by ground shaking during earthquakes is often nonuniformly distributed and can
cause differential movement in structures leading to major damage. Settlement
can occur from compaction in moist or dry cohesionless soil and from dissipation of excess hydrostatic pore pressure induced in saturated soil by earth
quake ground motions. Ground motions are multidirectional; however, measure-
