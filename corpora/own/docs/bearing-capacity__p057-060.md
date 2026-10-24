# CECW-EG (pages 57-60)

(4) Extrapolation of Test Results. Load tests performed using several plate
sizes may allow extrapolation of test results to foundations up to 6 times the plate
diameter provided the soil is similar. Other in situ test results using standard
penetration or cone penetration data are recommended for large foundation diameters
and depths more than 4Bp.
b. Standard Penetration Test (SPT). The SPT may be used to directly obtain
the allowable bearing capacity of soils for specific amounts of settlement based on
past correlations.
(1) Footings. Meyerhof’s equations (Meyerhof 1956; Meyerhof 1974) are
modified to increase bearing capacity by 50 percent (Bowles 1988)
(4-19a)
(4-19b)
where
qa,1 = allowable bearing capacity for 1 inch of settlement, ksf
Kd = 1 + 0.33(D/B) ≤ 1.33
Nn = standard penetration resistance corrected to n percent energy
Equation 4-19b may be used for footings up to 15 ft wide.
(a) F factors depend on the energy of the blows. n is approximately
55 percent for uncorrected penetration resistance and F 1 = 2.5, F 2 = 4, and F 3 =
1. F factors corrected to n = 70 percent energy are F 1 =2 , F 2 = 3.2 and F 3 =
1.
(b) Figure 3-3 of EM 1110-1-1904 provides charts for estimating q a for
1 inch of settlement from SPT data using modified Terzaghi and Peck approximations.
(2) Mats. For mat foundations
(4-20a)
where q a,1 is the allowable bearing capacity for limiting settlement to 1 inch. The
allowable bearing capacity for any settlement q a may be linearly related to the
allowable settlement for 1 inch obtained from Equations 4-19 assuming settlement
varies in proportion to pressure
(4-20b)
where
ρ = settlement, inches
qa,1 = allowable bearing capacity for 1 inch settlement, ksf
c. Cone Penetration Test (CPT). Bearing capacity has been correlated with
cone tip resistance q c for shallow foundations with D/B ≤ 1.5 (Schmertmann 1978).
(1) The ultimate bearing capacity of cohesionless soils is given by
(4-21a)
(4-21b)
where q u and q c are in units of tsf or kg/cm2.
(2) The ultimate bearing capacity of cohesive soils is
(4-22a)
(4-22b)
Units are also in tsf or kg/cm2. Table 4-9 using Figure 4-3 provides a procedure
for estimating q u for footings up toB=8f ti n width.
d. Vane Shear Test. The vane shear is suitable for cohesive soil because
bearing capacity is governed by short-term, undrained loading which is simulated by
this test. Bearing capacity can be estimated by (Canadian Geotechnical Society
1985)
(4-24)
where
Rv = strength reduction factor, Figure 4-4
τu = field vane undrained shear strength measured during the test, ksf
D = depth of foundation, ft
B = width of foundation, ft
L = length of foundation, ft
σvo = total vertical soil overburden pressure at the foundation level, ksf
4-5. Examples. Estimation of the bearing capacity is given below for (1) a wall
footing placed on the ground surface subjected to a vertical load, (2) a rectangular
footing placed below the ground surface and subjected to an inclined load, and (3) a
tilted, rectangular footing on a slope and subjected to an eccentric load.
Additional examples are provided in the user manual for CBEAR (Mosher and Pace
1982). The slope stability analysis of embankments is described in the user manual
for UTEXAS2 (Edris 1987). Bearing capacity analyses should be performed using at
least three methods where practical.
TABLE 4-9
CPT Procedure for Estimating Bearing Capacity
of Footings on Cohesive Soil (Data from Tand, Funegard, and Briaud 1986)
Step Procedure
1 Determine equivalent q c from footing base to 1.5B below base by
(4-23a)
where
qc = equivalent cone tip bearing pressure below footing, ksf
qcb1 = average tip resistance from 0.0 to 0.5B, ksf
qcb2 = average cone tip resistance from 0.5B to 1.5B, ksf
2 Determine equivalent depth of embedment D e , ft, to account for effect of
strong or weak soil above the bearing elevation
(4-23b)
where
n = number of depth increments to depth D
D = unadjusted (actual) depth of embedment, ft
∆zi= depth increment i, ft
qci = cone tip resistance of depth increment i, ksf
qc = equivalent cone tip bearing pressure below footing, ksf
3 Determine ratio of equivalent embedment depth to footing width
(4-23c)
4 Estimate bearing ratio R k from Figure 4-3 using Rd. The lower bound curve
is applicable to fissured or slickensided clays. The average curve is
applicable to all other clays unless load tests verify the upper bound curve
for intact clay.
5 Estimate total overburden pressure σvo, then calculate
(4-23d)
where q ua = ultimate bearing capacity of axially loaded square or round
footings with horizontal ground surface and base. Adjust q ua obtained from
Equation 4-23d for shape, eccentric loads, sloping ground or tilted base
using Hansen’s factors for cohesion, Table 4-5, to obtain the ultimate
capacity
(4-23e)
where ζc is defined by Equation 4-8a.
Figure 4-3. Bearing ratio R k for axially loaded square
and round footings (Data from Tand, Funegard, and Briaud 1986)
Figure 4-4. Strength reduction factor for field vane shear
(Data from Bjerrum 1973)
