# CECW-EG (pages 157-160)

TABLE 3 (Continued)
c. Description of Calculations
Item Program Prints Description
1 BEARING CAP... End bearing capacity, pounds
2 DOWNWARD DISPL Load-displacment Behavior for zero soil movement in
downward direction for IJ points
3 POINT BEARING Load at bottom of shaft prior to shaft load-transfer
calculation, pounds
4 DEPTH Depth, ft
LOAD TRANS Load transferred at given depth along shaft, pounds
TOTAL LOAD Total load on shaft at given depth, pounds
COM OF INCR Incremental shaft compression at given depth, in.
TOTAL MOVMT Shaft-soil relative movement at given depth, in.
ITER Number of iterations to complete calculation
5 TOP LOAD Load at top of shaft, pounds
TOP MOVEMENT Displacement at top of shaft, in.
BASE LOAD Load at bottom of shaft, pounds
BASE MOVEMENT Displacement at bottom of shaft, in.
6 NEGATIVE UPWARD Load-displacement Behavior for zero soil movement in
upward direction for IJ points
7 Same as item 5
8 STRUC LOAD(LBS) Load applied on top of shaft, pounds
SOILP(PSF) Pressure applied on top of adjacent soil, psf
ACTIVE DEPTH Depth of soil beneath ground surface subject to soil
heave, ft
9 BELL RESTRAINT Restraining resistance of bell, pounds
10 FIRST ESTIMATE Initial calculation of pullout resistance prior to
iterations for structural loads less than zero, pounds
11 LOAD-DISPLACE Load-shaft movement distribution for given structural
load
12 EFFECTS OF ADJ Effects of soil movement considered in load-displacement
behavior
13 INITIAL BASE Initial calculation of force at bottom of shaft prior
to iterations
14 DISPLACEMENT Displacement at bottom of shaft after 100 iterations,
in.
C-9
TABLE C-3 (Concluded)
Item Program Prints Description
FORCE= Force at bottom of shaft, pounds after 100 iterations,
pounds
15 ITERATIONS Total number of iterations to converge to solution
16 DEPTH(FT) Depth, ft
LOAD(LBS) Load at given depth, pounds
SHAFT MVMT(IN) Shaft displacement, in.
SOIL MVMT(IN) Soil movement,in.
b. Output Data
Results of the computations by AXILTR are printed in LTROUT.TXT illustrated in
Table C-3b. Table C-3c provides a description of calculations illustrated in
Table C-3b.
(1) Load-displacement data are placed in file LDCOM.DAT for plotting by
graphic software.
(2) Load-depth data for a given applied load on the pile top are placed in
file LDEP.DAT for plotting by graphic software.
(3) Displacement-depth data for a given applied load on the pile top are
placed in file MDEP.DAT for plotting by graphic software.
C-2. Applications
The pullout, uplift and downdrag capabilities of AXILTR are illustrated by two
example problems. The accuracy of these solutions can be increased by using more
soil layers, which increases control over soil input parameters such as swell
pressure, maximum past pressure, and shear strength.
a. Pullout and Uplift
Table C-4 illustrates input data required to determine performance ofa2f t
diameter drilled shaft 50 ft long constructed in an expansive clay soil of two
layers, NMAT = 2. The shaft is underreamed with a 5-ft diameter bell. Soil beneath
the shaft is nonexpansive. The shaft is subject to a pullout force of 300 kips.
Refer to Figure C-1 for a schematic representation of this problem.
C-10
TABLE C-4
Listing of Data Input for Expansive Soil, File DATLTR.TXT
EXPANSIVE SOIL
2 50 1.0 40. 2 50 16
6 0 8 0.0 2.0 5.00
0
1 2.68 .8 30. 4800. .1 .2 2000. .0 .7 7000.
2 2.65 .37 13.1 6000. .1 .2 4000. .0 2. 10000.
0.9 0.9
11
41 2
50 2
.900 1.600E+05
2
4.333E 08 .0
4.333E 08 50.0
-300000. .0 50.
0. .0 -1.0
0
(1) Bearing Capacity
The alpha skin friction and local shear base capacity models are selected. Option
to input the reduction factor α (I = 6) was used. The selected α’s for the two
soils is 0.9. A high α was selected because expansive soil increases pressure
against the shaft, which may raise the skin friction.
(2) Load-Transfer Models
The Kraft, Ray, and Kagawa skin friction and the Vijayvergiya base load-transfer
models (K = 8) were selected. Two points for the elastic modulus of the shaft
concrete were input into the program.
(3) Results
The results are plotted in Figure C-2 for a pullout force of 300,000 pounds.
Results of the computation placed in file "LTROUT.TXT" are shown in Table C-5.
(a) Total and base ultimate bearing capacity is about 1,200 and 550 kips,
respectively, Figure C-2a. Base and total capacity is 250 and 600 kips,
respectively, if settlement is limited to 0.5 inch, which is representative of a FS
of approximately 2.
(b) The distribution of load with depth, Figure C-2b, is a combination of the
shapes indicated in Figures 5-9 and 5-10 because both pullout and uplift forces must
be resisted.
(c) The shaft will heave approximately 0.7 inch, while the soil heaves more
than 11 inches at the ground surface, Figure C-2c.
C-11
Figure C-2. Plotted output for pullout and uplift problem
C-12
