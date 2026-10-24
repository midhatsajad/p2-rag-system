# CECW-EG (pages 97-100)

(a) The magnitude of skin friction f s above point n that contributes to
uplift thrust will be as much or greater than that estimated for compression loads.
The adhesion factor αa of Equation 5-10 can vary from 0.6 to 1.0 and can
contribute to shaft heave when expansive soil is at or near the ground surface. αa
should not be underestimated when calculating the potential for uplift thrust;
otherwise, tension, steel reinforcement, and shaft heave can be underestimated.
(b) Skin friction resistance f n that resists uplift thrust should be
estimated similar to that for pullout loads because uplift thrust places the shaft
in tension tending to pull the shaft out of the ground and may slightly reduce
lateral pressure below neutral point n.
d. Downdrag. Deep foundations constructed through compressible soils and
fills can be subject to an additional downdrag force. This downdrag force is caused
by the soil surrounding the drilled shaft or pile settling downward more than the
deep foundation. The deep foundation is dragged downward as the soil moves down.
The downward load applied to the shaft is significantly increased and can even cause
a structural failure of the shaft as well as excessive settlement of the foundation.
Settlement of the soil after installation of the deep foundation can be caused by
the weight of overlying fill, settlement of poorly compacted fill and lowering of
the groundwater level. The effects of downdrag can be reduced by isolating the
shaft from the soil, use of a bituminous coating or allowing the consolidating soil
to settle before construction. Downdrag loads can be considered by adding these to
column loads.
(1) Force Distribution. The shaft moves up relative to the soil above point
n, Figure 5-11, and moves down relative to the soil below point n. The positive
skin friction f s below point n and end bearing capacity resists the downward
loads applied to the shaft by the settling soil and the structural loads. Negative
skin friction f n above the neutral point contributes to the downdrag load and
increases the compressive stress in the shaft.
(2) End Bearing. End bearing capacity may be estimated similar to methods
for compressive loads given by Equations 5-2.
(3) Skin Friction. Skin friction may be estimated by Equation 5-9 where the
positive skin friction is given by Equations 5-10 to 5-12.
e. Computer Analysis. Program AXILTR (AXIal Load-TRansfeR), Appendix C, is a
computer program that computes the vertical shaft and soil displacements for axial
down-directed structural, axial pullout, uplift, and down-drag forces using
equations in Table 5-4. Load-transfer functions are used to relate base pressures
and skin friction with displacements. Refer to Appendix C for example applications
using AXILTR for pullout, uplift and downdrag loads.
(1) Load-Transfer Principle. Vertical loads are transferred from the top of
the shaft to the supporting soil adjacent to the shaft using skin friction-load
transfer functions and to soil beneath the base using consolidation theory or base
load-transfer functions. The total bearing capacity of the shaft Q u is the sum of
the total skin Q su and base Q bu resistances given by Equations 5-1.
Figure 5-11. Deep foundation resisting downdrag. q load is an
area pressure from loads such as adjacent structures
(a) The load-displacement calculations for rapidly applied downward vertical
loads have been validated by comparison with field test results (Gurtowski and Wu
1984). The strain distribution from uplift forces for drilled shafts in
shrink/swell soil have been validated from results of load tests (Johnson 1984).
(b) The program should be used to provide a minimum and maximum range for the
load-displacement behavior of the shaft for given soil conditions. A listing of
AXILTR is provided to allow users to update and calibrate this program from results
of field experience.
(2) Base Resistance Load Transfer. The maximum base resistance q bu in
Equation 5-1b is computed by AXILTR from Equation 5-2a
(5-17)
where
c = cohesion, psf
Ncp = cohesion bearing capacity factor, dimensionless
Nqp = friction bearing capacity factor, dimensionless
σ’L = effective vertical overburden pressure at the pile base, psf
TABLE 5-4
Program AXILTR Shaft Resistance To Pullout, Uplift and Downdrag Loads
Soil Type of Applied Resistance to Applied
Volume Applied Load, Pounds Load, Pounds Equations
Change Load
L
None Pullout Q DL - P Straight: Q sur +W p Qsur = πBs ∫ f-sdL
0
Underream: Smaller of L
Qsub = πBb ∫τ sdL
Qsub +W p 0
Qsur +Q bur +W p πQbur =q bu (B2
b -B 2
s)4
πWp = γp B2
s L4
Ln
Swelling Uplift Q us Straight: Q sur +W p Qus = πBs ∫ f-sdL
soil thrust 0
Underream: L
Qsur = πBs ∫ f-sdL
Qsur +Q bur +W p Ln
πQbur =q bu (B2
b -B 2
s)4
LnSettling Downdrag Q d +Q sud Qsur +Q bu Qsud = πBs ∫ fndLsoil 0
L
qsur = πBs ∫ f-sdL
Ln
Nomenclature:
Bb Base diameter, ft Q DL Dead load of structure, pounds
Bs Shaft diameter, ft P Pullout load, pounds
f-s Maximum mobilized shear strength, psf Q sub Ultimate soil shear resistance of
fn Negative skin friction, psf cylinder diameter B b and length equal
L Shaft length, ft to depth of underream, pounds
Ln Length to neutral point n, ft Q sud Downdrag, pounds
qbu Ultimate base resistance, psf Q sur Ultimate skin resistance, pounds
Qbu Ultimate base capacity, pound Q us Uplift thrust, pounds
Qbur Ultimate base resistance of upper Q d Design load, Dead + Live loads, pounds
portion of underream, pounds W p Shaft weight, pounds
τs Soil shear strength, psf γp Unit shaft weight, pounds/ft3
Correction factors ζ are assumed unity and the N γp term is assumed negligible.
Program AXILTR does not limit σ’L.
(a) N qp for effective stress analysis is given by Equation 5-7 for local
shear (Vesic Alternate method) or Equation 5-8 for general shear.
(b) N cp for effective stress analysis is given by
(5-5a)
Ncp for total stress analysis is assumed 9 for general shear and 7 for local
shear; Nqp and total stress friction angle φ are zero for total stress analysis.
(c) End bearing resistance may be mobilized and base displacements computed
using the Reese and Wright (1977) or Vijayvergiya (1977) base load-transfer
functions, Figure 5-12a, or consolidation theory. Ultimate base displacement for
the Reese and Wright model is computed by
(5-18)
where
ρbu = ultimate base displacement, in.
Bb = diameter of base, ft
ε50 = strain at 1/2 of maximum deviator stress of clay from undrained
triaxial test, fraction
The ultimate base displacement for the Vijayvergiya model is taken as 4 percent of
the base diameter.
(d) Base displacement may be calculated from consolidation theory for
overconsolidated soils as described in Chapter 3, Section III of EM 1110-1-1904.
This calculation assumes no wetting beneath the base of the shaft from exterior
water sources, except for the effect of changes in water level elevations. The
calculated settlement is based on effective stresses relative to the initial
effective pressure on the soil beneath the base of the shaft prior to placement of
any structural loads. The effective stresses include any pressure applied to the
surface of the soil adjacent to the shaft. AXILTR may calculate large settlements
for small applied loads on the shaft if the maximum past pressure is less than the
initial effective pressure simulating an underconsolidated soil. Effective stresses
in the soil below the shaft base caused by loads in the shaft are attenuated using
Boussinesq stress distribution theory (Boussinesq 1885).
(3) Underream Resistance. The additional resistance provided by a bell or
underream for pullout or uplift forces is 7/9 of the end bearing resistance. If
applied downward loads at the base of the shaft exceed the calculated end bearing
capacity, AXILTR prints "THE BEARING CAPACITY IS EXCEEDED". If pullout loads
exceed the pullout resistance, the program prints "SHAFT PULLS OUT". If the shaft
heave exceeds the soil heave, the program prints "SHAFT UNSTABLE".
(4) Skin Resistance Load Transfer. The shaft skin friction load-transfer
functions applied by program AXILTR are the Seed and Reese (1957) and Kraft, Ray,
and Kagawa (1981) models illustrated in Figure 5-12b. The Kraft, Ray, and Kagawa
model requires an estimate of a curve fitting constant R from
(5-19a)
