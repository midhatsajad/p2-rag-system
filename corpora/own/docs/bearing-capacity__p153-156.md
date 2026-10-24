# CECW-EG (pages 153-156)

TABLE C-2 (Concluded)
Line Parameter Description
10c S(M) Movement in inches for all of the T(M,1)...T(M,11) curves;
only 10 values required from S(2)...S(11); S(1) = 0.0 in
code; if S(M) in the code is okay (0.0,0.05,0.1,0.15,0.2,
0.23,0.3,0.45,0.75,1.05,1.5 inches)
11 Input data for maximum skin friction as a function of depth
NCC Total number of maximum skin friction terms to input, <12;
program interpolates maximum skin friction between depths
11a FS(N) Maximum skin friction f- s for point N, psf
11b ZEPP(N) Depth for the maximum skin friction for point N, ft
11c NCUR Number of the shaft load-transfer curve input M in line
10; applicable to the maximum skin friction for point N
(Repeat 11a,11b,11c for each N = 1,NCC)
12 Input data for shaft elastic modulus as function of depth;
program interpolates the elastic modulus between depths
NC Total number of terms of elastic modulus and depth, > 1
12a EP(M) Elastic modulus of shaft at point M, psf
12b ZEP(M) Depth for the elastic modulus of shaft at point M, ft
(An elastic modulus and depth term are required at least
at the top and bottom of the shaft)
13 Input data for base displacements i fK=6 (The number of
input terms or R(M) and S(M) equals IJ - 1, line 2)
13a R(M) Base displacement, in. (The first displacement is 0.0 inches
and already input in the program)
13b S(M) Base load for displacement R(M), pounds; the base load for
0.0 displacement is approximated as the overlying soil
weight and already input in the program.
14 Structural load, pressure on adjacent soil at the ground
surface, and depth of the active zone for heave input for
each problem for evaluation of specific load
distribution-displacement computations
14a STRUC Structural vertical load on top of shaft, pounds
14b SOILP Pressure on top layer of soil exerted by surrounding
structure, fill, etc., psf
14c XA Depth of the active zone for heave, ft; = 0.01 yields
load-displacement behavior for zero soil movement; a
saturated soil profile is assumed when computing soil
movement; < 0.0 program goes to line 15 below
15 NON Execution stops if 0; program goes to line 1 if > 0
C-5
(1) The program is set to consider up to a total of 40 soil types and 100
soil elements. Figure C-1 provides an example layout of soil types and elements
used in AXILTR.
(2) The program can accommodate up to 18 points of the load-displacement
curve. This capacity may be altered by adjusting the PARAMETER statement in the
program.
(3) The input data are placed in a file, "DATLTR.TXT". These data are
printed in output file, "LTROUT.TXT" illustrated in Table C-3a.
Figure C-1. Schematic diagram of soil/pile elements
C-6
TABLE C-3
Output Data
a. Repeat of Input Data (See Table C-1)
Line Output Parameters Fortran Statement
1 TITLE 20A4
2 NMAT= NEL= DX= FT GWL= FT I5,I5,F6.2,F6.2
LO= IQ (SHAFT INC)= IJ (NO.LOADS)= I5,I5,I5
3 I= J= K= SOILP= PSF I5,I5,I5,F10.2
DS= FT F10.2
DB= FT F10.2
4 (If K = 2,5,9)
E50 E13.3
5 LOCAL SHEAR FAILURE AT BASE - LLL = 0 or I5
GENERAL SHEAR FAILURE AT BASE - LLL = 1 I5
6 MAT GS EO WO(%) PS(PSF) CS CC CO(PSF) PHI K PM(PSF) I3,3F6.2,F7.0,
27.2,F7.0,2F6.2,
F7.0
7 (If I = 6) ALPHA = 2(7F10.5)
8 ELEMENT NO OF SOIL I5,10X,I5
9 (If K = 7,8,9)
REDUCTION FACTOR= SHEAR MODULUS= F6.3,3X,E13.3
10 (If K = 3,4,5,6)
NO. OF LOAD-TRANSFER CURVES(<12)?= I5
For each curve 1 to NCA:
CURVE I5
RATIO SHR DEV,M=1,11 ARE 11F6.3
MOVEMENT(IN.) FOR LOAD TRANSFER M= IS INCHES I5,F6.3
11 (If I = 5)
NO OF SKIN FRICTION-DEPTH TERMS(<12)? ARE I5
SKIN FRICTION(PSF) DEPTH(FT) CURVE NO F10.3,F10.3,I5
12 (If J = 0)
E SHAFT(PSF) AND DEPTH(FT): 4(E13.3,2X,F6.2)
13 (If K = 6)
BASE DISPLACEMENT(IN.),BASE LOAD(LBS) > FOR POINTS F10.2,I5
C-7
TABLE C-3 (Continued)
b. Output Calculations
Item Program Prints Format Statement
1 BEARING CAPACITY= POUNDS F13.2
2 DOWNWARD DISPLACEMENT
3 (Omitted unless LO = 0,1)
POINT BEARING(LBS)= F13.2
4 (Omitted unless LO = 0,1)
DEPTH LOAD TRANS TOTAL LOAD COM OF INCR TOTAL MOVMT ITER
FT LBS LBS INCHES INCHES
5E13.5,I5
5 TOP LOAD TOP MOVEMENT BASE LOAD BASE MOVEMENT 4E13.5
LBS INCHES LBS INCHES
6 NEGATIVE UPWARD DISPLACEMENT
7 TOP LOAD TOP MOVEMENT BASE LOAD BASE MOVEMENT 4E13.5
LBS INCHES LBS INCHES
8 STRUC LOAD(LBS) SOILP(PSF) ACTIVE DEPTH(FT) F10.0,2F10.2
(Line 14 of Table C-2)
9 BELL RESTRAINT(LBS)= F13.2
10 (If STRUL < 0.0 See Line 14, Table C-2)
FIRST ESTIMATE OF PULLOUT RESTRAINT(LBS)= F13.2
11 LOAD-DISPLACEMENT BEHAVIOR
12 (If LO <2)
EFFECTS OF ADJACENT SOIL
13 INITIAL BASE FORCE(LBS)= F13.2
(If LO = 0) BASE FORCE(LBS)=
14 DISPLACEMENT(INCHES)= FORCE= POUNDS F8.4,F12.2
15 ITERATIONS= I5
16 DEPTH(FT) LOAD(LBS) SHAFT MVMT(IN) SOIL MVMT(IN) F7.2,2X,E13.5,
2F15.5
C-8
