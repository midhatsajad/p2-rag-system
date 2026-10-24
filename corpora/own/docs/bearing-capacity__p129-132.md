# CECW-EG (pages 129-132)

Figure 5-23. Schematic of wave equation model
(1) Description. The pile driving and soil system consists of a series of
elements supported by linear elastic springs and dashpots which have assumed
parameters, Figure 5-23. Characteristics of commonly used pile hammers and piles
are available in the program data files driving systems. Input parameters include
the dynamic damping constants for each dashpot, usually in units of seconds/inch,
ultimate soil resistance Q u in kips and quake in fractions of an inch for each
spring. Each dashpot and spring represent a soil element. The quake of the pile is
its displacement at Q ub. Input data for Q ub, quake, and ultimate skin resistance
of each element Q sui are usually assumed. Actual load distribution data are
normally not available and require results of instrumented load tests. Standard
values are available in the user’s manual for soil input parameters.
(2) Analysis. The wave equation analysis provides a relationship between the
pile capacity and the driving resistance in blows per inch (or blows per foot if
needed). This relationship can be developed for different pile lengths and then
used in the field when the pile has been driven sufficiently to develop the required
capacity. The wave equation can also be used to develop relationships between
driving stresses in the pile and penetration resistance for different combinations
of piles and pile driving equipment.
(3) Application. The wave equation analysis is used to select the most
suitable driving equipment to ensure that the piles can develop the required
capacity and select the minimum pile section required to prevent overstressing the
pile during driving.
(4) Calibration. Calculations from program GRLWEAP may be calibrated with
results of dynamic load tests using pile driving analyzer (PDA) equipment. The
force and velocity versus time curves calculated from GRLWEAP are adjusted to agree
with the force and velocity versus time curves measured by the PDA during pile
driving or during a high strain test. A high strain causes a force at the pile tip
sufficient to exceed the ultimate soil resistance Q ub. Drilled shafts may be
analyzed with the PDA during a high strain test where heavy loads are dropped by a
crane on the head of the shaft.
(5) Factors of Safety. In general, pile capacity calculated by GRLWEAP
should be divided by a factor of safety FS=3t o estimate allowable capacity or FS
= 2.5 if calibrated with results of dynamic load tests. If load tests are
performed, FS = 2 can be used with GRLWEAP.
(6) Restriking. Soils subject to freeze or relaxation could invalidate a
wave equation analysis; therefore, installed piles should be tested by restriking
while using PDA equipment after a minimum waiting period following installation such
as 1 day or more as given in the specifications.
d. Pile Driving Formulas. Pile driving formulas, Table 5-11, although not as
good as wave equation analysis, can provide useful, simple estimates of ultimate
pile capacity Q u and they can be obtained quickly. The allowable bearing capacity
can be estimated from Equations 1-2 using FS in Table 5-11. Two or more of these
methods should be used to provide a probable range of Q u.
e. Example Application. A steel circular 1.5-ft diameter closed end pipe
pile is to be driven 30 ft through a 2-layer soil of clay and fine uniform sand,
Figure 5-7. The water table is 15 ft below ground surface at the clay-sand
interface. The pile will be filled with concrete grout with density γconc = 150
lbs/ft3. Design load Q d = 100 kips.
(1) Soil Parameters.
(a) The mean effective vertical stress in the sand layer adjacent to the
embedded pile σ’s and at the pile tip σ’L is limited to 1.8 ksf for the Meyerhof
and Nordlund methods. Otherwise, σ’L is 2.4 ksf from Equation 5-13b.
TABLE 5-11
Pile Driving Formulas
Method Equation for Ultimate Factor of
Bearing Capacity Q u, kips Safety
Gates 27(E hEr)1/2(1 - log10S) 3
Pacific Coast 12E hErCp1 Wr +c pWp QuL,C p1 =, C p2 =4Uniform S + C p2 Wr +W p AEp
Building Code c p = 0.25 for steel piles; = 0.10 for other piles
Initially assume Cp2 = 0 and compute Qu; reduce
Qu by 25 percent, compute Cp2, then recompute Qu;
compute a new Cp2, compute Qu until Qu used = Qu
computed
1/212EhEr 144EhErLDanish , C d = , inches 3 - 6S+C d 2AEp
12WrhEngineering Drop Hammers: 6 S + 1.0News Record
24ErOther Hammers: 6S + 0.1
Nomenclature:
A = area of pile cross-section, ft 2
Eh = hammer efficiency
Ep = pile modulus of elasticity, ksf
Er = manufacturer’s hammer-energy rating (or Wrh), kips-ft
h = height of hammer fall, ft
L = pile length, inches
S = average penetration in inches per blow for the last 5 to 10 blows
for drop hammers and 10 to 20 blows for other hammers
Wr = weight of striking parts of ram, kips
Wp = weight of pile including pile cap, driving shoe, capblock and
anvil for double-acting steam hammers, kips
(b) The average undrained shear strength of the upper clay layer is C u =2
ksf. The friction angle of the lower sand layer is estimated at φ’ = 36 deg. Cone
penetration test results shown in Figure 5-21 indicate an average cone tip
resistance q c = 40 ksf in the clay and 160 ksf in the sand.
(2) End Bearing Capacity. A suitable estimate of end bearing capacity q bu
for the pile tip in the sand may be evaluated from the various methods for
cohesionless soil as described below.
(a) Meyerhof Method. From Figure 5-3, Rc = 10 and Lc = Rc B = 10 1.5 or
15 ft for φ’ = 36 deg. N qp from Figure 5-15 is 170 for Rb = L/B = 15/1.5 = 10.
From Equation 5-2c with limiting pressure q from Equation 5-31c
qbu = σ’L Nqp ≤ Nqp tanφ’i fL > L c
σ’L Nqp = 1.8 170 = 306 ksf
Nqp tanφ’= 170 tan 36 = 123.5 ksf
qbu ≤ q , therefore q bu = 123.5 ksf
(b) Nordlund Method. The procedure in Table 5-8a may be used to estimate end
bearing capacity.
αf = 0.67 for φ’ = 36 deg from Figure 5-17a
Nqp = 80 for φ’ = 36 deg from Figure 5-17b
σ’L = 1.8 ksf
qup = αfNqpσ’L = 0.67 80 1.8 = 96.5 ksf
q= N qptanφ’ = 170 tan36 = 123.5 ksf where N qp is from Figure 5-15.
Therefore, qbu = 96.5 ksf ≤ q
(c) Hansen Method. From Table 4-5 (or calculated from Table 4-4) N qp =
37.75 and N γp = 40.05 for φ’ = 36 deg. From Table 4-5,
ζqs = 1 + tan φ = 1 + tan36 = 1.727
ζqd = 1 + 2tan φ(1 - sinφ)2 tan-1(Lsand/B)
= 1 + 2tan36(1 - sin36) 2 tan-1(15/1.5) π/180
= 1 + 2 0.727(1 - 0.588) 2 1.471 = 1.363
ζqp = ζqs ζqd = 1.727 1.363 = 2.354
ζγs = 1 - 0.4 = 0.6
ζγd = 1.00
ζγp = ζγs ζγd = 0.6 1.00 = 0.6
From Equation 5-2a
qbu = σ’L NL ζqp +( Bb/2) γ’s Nγp ζγp
= 2.4 37.75 2.354 + (1.5/2) 0.04 40.05 0.6
= 213.3 + 0.7 = 214 ksf
The N γp term is negligible and could have been omitted.
(d) Vesic Method. The reduced rigidity index from Equation 5-5c is
Ir 57.3Irr = = = 42.61+ εv Ir 1 + 0.006 57.3
where
1-2 μs σ’L 1 - 2 0.3 2.4(Equation 5-5e): εv = = = 0.0062(1 - μs)G s 2(1 - 0.3) 100
Gs 100(Equation 5-5d): I r = = = 57.3σ’L tanφ’ 2.4 tan36
