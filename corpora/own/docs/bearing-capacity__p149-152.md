# CECW-EG (pages 149-152)

APPENDIX C
COMPUTER PROGRAM AXILTR
C-1. Organization
Program AXILTR, AXIal Load-TRansfeR, consists of a main routine and two subroutines.
The main routine feeds in the input data, calculates the effective overburden
stress, and determines whether the load is axial down-directed, pullout, or if
uplift/downdrag forces develop from swelling or consolidating soil. The main
routine also prints out the computations. Subroutine BASEL calculates the
displacement at the base for given applied down-directed loads at the base.
Subroutine SHAFL evaluates the load transferred to and from the shaft for relative
displacements between the shaft and soil. An iteration scheme is used to cause the
calculated applied loads at the top (butt) to converge within 10 percent of the
input load applied at the top of the shaft.
a. Input Data
Input data are illustrated in Table C-1 with descriptions given in Table C-2.
TABLE C-1
Input Data
Line Input Parameters Format Statement
1 TITLE 20A4
2 NMAT NEL DX GWL LO IQ IJ 2I5,2F6.2,3I5
3 I J K SOILP DS DB 3I5,3F10.3
4 E50 (Omitted unles sK=2 ,5 ,9 ) E13.3
5 LLL I5
6 MAT GS EO WO PS CS CC C PHI AK PM I3,3F6.2,F7.0,
(Line 5 repeated for each material M = 1,NMAT) 2F7.2,F7.0,2F6.2
F7.0
7 ALPHA (Omitted unles sI=6 ) 7F10.5
(α input for each material MAT = 1,NMAT)
8 M IE(M) 2I5
(Line 8 repeated for each element M and number
of soil IE(M). Start with 1. The last line
is NEL NMAT)
9 RFF GG F6.3,E13.3
(Omitted unlessK=7 ,8 ,9 )
10 (Omitted unles s K = 3,4,5,6)
10a NCA ( <12) I5
C-1
TABLE C-1 (Concluded)
Line Input Parameters Format Statement
10b T(M,1)... T(M,11) (Input for each curve M=1,NCA) 11F6.2
10c S(M) (Input on new line for each F6.3
M = 2,11; S(1) input in program as 0.00)
11 (Omitted unles sI=5 )
11a NCC ( <12) I5
11b FS(N) ZEPP(N) NCUR 2F10.3,I5
(Input on new line for each N = 1,NCC)
12 (Omitted unles sJ=0 )
12a NC ( >1) I5
12b EP(M) ZEP(M) E13.3,F6.2
(Input on new line for each M = 1,NC; at least
a top and bottom term required)
13 R(M) S(M) F10.5,F15.3
(Omitted unlessK=6 ; repeat on new line for
each M = 1,IJ)
14 STRUL SOILP XA 3F15.2
15 NON I5
(Omitted unless XA < 0.0)
TABLE C-2
Description of Input Parameters
Line Parameter Description
1 TITLE Name of problem
2 NMAT Total number of materials
NEL Total number of elements
DX Thickness of each element, ft (usually 0.5 or 1.0 ft)
GWL Depth to groundwater level, ft
LO Amount of output data
= 0 Extensive data output used to check the program
= 1 Shaft load-displacement behavior and detailed load
distribution-displacement response along shaft
length for input top load prior to and following
soil movement (load transfer, load, shaft compression
increment, and shaft movement at given depth
C-2
TABLE C-2 (Continued)
Line Parameter Description
= 2 Shaft load-displacement behavior and load
distribution-displacement response along shaft
length for input top load prior to and following
soil movement
= 3 Shaft load-displacement behavior and load
distribution-displacement response along shaft
length for input top load on shaft following soil
movement
IQ Total number of shaft increments (shaft length/element
thickness); top of shaft at ground surface
IJ Number of points for shaft load-displacement behavior
(usually 12, but maximum of 18 for PARAMETER statement = 40)
3 I Magnitude of reduction factor α applied to total
(undrained) or effective (drained) shear strength for skin
friction resistance
=0 α = 1 (usually used for drained strength)
=1 α = sin(πx/L), x = depth, ft; L = shaft length, ft
=2 α = 0.6
=3 α = 0.45
=4 α = 0.3
= 5 Permits maximum skin friction f-s input as a
function of depth, psf (see line 11)
=6 α is input for each material (see line 7)
J Option for elastic shaft modulus
= 0 shaft modulus input
= 1 shaft modulus set to near infinity
K Option for load-transfer functions (see Figure 5-12)
Base Shaft
= 0 Consolidation Seed and Reese
= 1 Vijayvergiya Seed and Reese
= 2 Reese and Wright Seed and Reese
= 3 Consolidation Input (see line 10)
= 4 Vijayvergiya Input (see line 10)
= 5 Reese and Wright Input (see line 10)
= 6 Input (see line 13) Input (see line 10)
= 7 Consolidation Kraft, Ray, and Kagawa
= 8 Vijayvergiya Kraft, Ray, and Kagawa
= 9 Reese and Wright Kraft, Ray, and Kagawa
C-3
TABLE C-2 (Continued)
Line Parameter Description
SOILP Pressure on top layer of soil exerted by surrounding
structure, fill, etc., psf
DS Diameter shaft, ft
DB Diameter base, ft
4 E50 Strain at 1/2 maximum deviator stress, Equation 5-19
5 LLL Option for type of shear failure at base
= 0 Local shear failure, Equation 5-7 or N c =7
= 1 General shear failure, Equation 5-8 or N c =9
6 MAT Number of material
GS Specific gravity
EO Initial void ratio
WO Initial water content, percent
PS Swell pressure, psf
CS Swell index
CC Compression index
C Cohesion, psf; = undrained strength for total stress
analysis; effective cohesion c’ or zero for effective
stress analysis
PHI Angle of shearing resistance φ; = 0 for total stress
analysis
AK Coefficient of lateral earth pressure
PM Maximum past pressure, psf (program sets PM = PS if PM
input < PS)
7 ALPHA Reduction factor αa for each material MAT, Equation 5-11,
Table 5-1, Table 5-10; used when optionI=6 , Line 3
8 M Number of element
IE(M) Material number of soil, MAT
9 RFF Hyperbolic reduction factor R for Kraft, Ray, and Kagawa
model, Equation 5-19a; use 1.0 if not known
GG Shear modulus G s, psf, Equation 5-19b
10 Input data for shaft load-transfer curves (K = 3,4,5,6)
10a NCA Total number of shaft load-transfer curves to input, < 12
10b T(M,1)... Skin friction ratio of developed shear strength/maximum
..T(M,11) mobilized shear strength of each shaft load-transfer
curve; 11 values required for each load-transfer curve,
the first value T(1,1) = 0.0
C-4
