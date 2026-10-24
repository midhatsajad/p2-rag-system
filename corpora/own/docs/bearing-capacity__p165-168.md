# CECW-EG (pages 165-168)

TABLE C-6
Listing of Data Input for Settling Soil, File DATLTR.TXT
SETTLING SOIL
2 50 1.0 40. 2 50 16
6 0 2 0.0 2.0 5.00
0.010
0
1 2.68 .8 30. 1200. .05 .1 2000. .0 .7 4000.
2 2.65 .37 13.1 6000. .05 .1 4000. .0 2. 10000.
0.55 0.3
11
41 2
50 2
2
4.333E 08 .0
4.333E 08 50.0
150000. .0 50.
0. .0 -1.0
0
(2) Load-Transfer Models
The Seed and Reese skin friction and Reese and Wright base load-transfer models were
selected (K = 2). Two points for the elastic modulus of the shaft concrete were
input into the program.
(3) Results
The results are plotted in Figure C-3 for a downward applied load of 150 kips.
Results of the computation placed in file LTROUT.TXT are illustrated in Table C-7.
(a) Total and base ultimate bearing capacity, Figure C-3a, is about 550 and
880 kips, respectively. Base and total capacity is about 200 and 500 kips,
respectively, if settlement is limited to 0.5 inch. The factor of safety is
approximately 1.8 relative to total bearing capacity. The program does not add the
vertical plunging failure lines to the curves in Figure C-3a, which leaves the
calculated displacement load relationships nearly linear.
(b) The distribution of load with depth, Figure C-3b, is representative of
downdrag indicated in Figure 5-11. The load on the shaft base is nearly 300 kips or
double the applied load at the ground surface.
(c) The shaft will settle approximately 1 inch, while the soil settles about
2 inches at the ground surface, Figure C-3c. The soil is heaving near the ground
surface, which counters the settlement from downdrag. Maximum settlement is about
3.5 inches at 10 ft of depth.
C-17
Figure C-3. Plotted output for downdrag problem
C-18
Figure C-3. Concluded
TABLE C-7
Listing of Output, File LTROUT.TXT
SETTLING SOIL
NMAT= 2 NEL= 50 DX= 1.00 FT GWL= 40.00 FT
LO= 2 IQ (SHAFT INC)= 50 IJ (NO.LOADS)= 16
I= 6 J= 0 K= 2 SOILP= 0.00 PSF
DS= 2.00 FT
DB= 5.00 FT
E50= 0.100E-01
LOCAL SHEAR FAILURE AT BASE - LLL= 0
MAT GS EO WO(%) PS(PSF) CS CC CO(PSF) PHI K PM(PSF)
1 2.68 0.80 30.00 1200. 0.05 0.10 2000. 0.00 0.70 4000.
2 2.65 0.37 13.10 6000. 0.05 0.10 4000. 0.00 2.00 10000.
ALPHA= 0.55000 0.30000
C-19
TABLE C-7 (Continued)
ELEMENT NO OF SOIL
11
21
.1
.1
40 1
41 2
42 2
.2
.2
50 2
E SHAFT(PSF) AND DEPTH(FT):
0.433E+09 0.00 0.433E+09 50.00
BEARING CAPACITY= 549778.69 POUNDS
DOWNWARD DISPLACEMENT
TOP LOAD TOP MOVEMENT BASE LOAD BASE MOVEMENT
LBS INCHES LBS INCHES
0.43825E+06 0.36209E+00 0.10946E+06 0.24071E+00
0.47316E+06 0.46787E+00 0.13882E+06 0.33163E+00
0.50252E+06 0.57771E+00 0.16817E+06 0.42854E+00
0.53187E+06 0.69319E+00 0.19753E+06 0.53108E+00
0.56122E+06 0.81401E+00 0.22688E+06 0.63896E+00
0.59058E+06 0.93992E+00 0.25624E+06 0.75193E+00
0.61993E+06 0.10707E+01 0.28559E+06 0.86977E+00
0.64929E+06 0.12061E+01 0.31494E+06 0.99228E+00
0.67864E+06 0.13461E+01 0.34430E+06 0.11193E+01
0.70800E+06 0.14904E+01 0.37365E+06 0.12507E+01
0.73735E+06 0.16389E+01 0.40301E+06 0.13862E+01
0.76671E+06 0.17915E+01 0.43236E+06 0.15259E+01
0.79606E+06 0.19481E+01 0.46172E+06 0.16695E+01
0.82541E+06 0.21085E+01 0.49107E+06 0.18170E+01
0.85477E+06 0.22727E+01 0.52042E+06 0.19682E+01
0.88412E+06 0.24405E+01 0.54978E+06 0.21231E+01
NEGATIVE UPWARD DISPLACEMENT
TOP LOAD TOP MOVEMENT BASE LOAD BASE MOVEMENT
LBS INCHES LBS INCHES
-0.19877E+05 -0.38437E-02 0.00000E+00 0.00000E+00
-0.44463E+05 -0.18937E-01 0.00000E+00 -0.10000E-01
-0.69052E+05 -0.34038E-01 0.00000E+00 -0.20000E-01
-0.11821E+06 -0.64239E-01 0.00000E+00 -0.40000E-01
-0.21272E+06 -0.12447E+00 0.00000E+00 -0.80000E-01
C-20
