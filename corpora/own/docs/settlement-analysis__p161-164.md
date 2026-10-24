# CECW-EG (pages 161-164)

The coefficient of consolidation c v determined by this method appears comparable with that of the SL test.
c. Evaluation of Void Ratio-Logarithm Pressure Relationship . The void
ratio-logarithm pressure relationship may be obtained by determining the void
ratio and effective stress at any time during the test.
(1) The change in void ratio ∆e over a pressure increment is (1 + e 1)ε
where e 1 is the void ratio at the beginning of the pressure increment and ε
is the strain over the pressure increment.
(2) The average effective stress over a pressure increment is σa -u h .
(3) The excess pore water pressure u h is measured at the bottom of the
specimen, Figure E-2.
d. Assumptions . This method assumes that the coefficient of consolidation and compression index are constant for the soil.
E-5. Controlled Gradient Test (CG) . This test is similar to the CRD test except that the applied vertical pressure is adjusted so that the pore water
pressure at the bottom of the specimen remains constant throughout the test
(item 38). This restriction requires a feedback mechanism that significantly
complicates the laboratory equipment.
a. Evaluation of Coefficient of Consolidation . The coefficient of consolidation may be estimated by
(E-2)
where
∆σ = change in total pressure between time increment t 2 and t 1 , psi
∆t=t 2 -t 1 , minutes
ha = average height of specimen between time t 2 and t 1 , in.
uh = excess pore water pressure at bottom of the specimen, psi
b. Evaluation of Void Ratio-Logarithm Pressure Relationship . The void
ratio-logarithm pressure relationship is evaluated similar to the above procedures. The excess pore water pressure at the bottom of the specimen should be
kept as small as possible to maintain a nearly uniform void ratio within the
specimen.
c. Assumptions . This method assumes that the coefficient of consolidation and coefficient of volume change are constant. The coefficient of volume
change is the change in strain divided by the change in total vertical stress.
E-4
APPENDIX F
COMPUTER PROGRAM VDISPL
F-1. Background . This program, Vertical DISPLacements, was developed to assist in the calculation of vertical displacements beneath shallow foundations
for various types of multilayered soils in support of this manual. The two
types of foundations considered are rectangular footings or mats and long
strip footings. These foundations are assumed flexible. Models available are
immediate settlement of granular soil from cone penetration data (item 55),
immediate settlement of granular soil from both cone penetration and dilatometer data (item 37), immediate settlement of an elastic soil using the Boussinesq pressure distribution and Young’s elastic soil modulus, consolidation or
swell of a cohesive soil (ASTM D 4546), and settlement of a collapsible soil
(item 22). Soil expansion is indicated by positive values and settlement by
negative values.
F-2. Organization . The program consists of a main routine and several
subroutines for calculation of vertical displacements by each of the models.
The main routine feeds in descriptive data for the problem, divides the soil
profile into increments from 1 to NNP where NNP is the nodal point at the
bottom of the profile, assigns a layer number to each increment or soil
element, and calculates the effective overburden pressure prior to placement
of the foundation. The number of soil elements NEL in a problem is one less
than the number of nodal points NNP. The PARAMETER statement in the program
provides a maximum NL=30 soil layers and a maximum NQ=101 soil nodal points.
Subroutine SLAB calculates the change in effective vertical pressures in the
soil following placement of the foundation using the Boussinesq pressure
distribution. The remaining subroutines described below calculate vertical
displacements for the various models.
a. Data Organization . The input data are placed in a file, "VDIN.DAT".
These data are illustrated in Table F-1 with descriptions provided in Table F-
2. The input data are also printed in the output file, "VDOU.DAT" and
illustrated in Table F-3. Calculations by the program are printed in VDOU.DAT
and illustrated in Table F-3.
b. Subroutine MECH . This subroutine (NOPT=0) calculates heave or
consolidation from results of one-dimensional consolidometer swell tests
performed on cohesive soil for each layer in a soil profile.
(1) Soil displacements are calculated after ASTM standard D 4546 (method
C) relative to the equilibrium moisture profiles of saturated (method 1),
hydrostatic with shallow water table (method 2), and hydrostatic without
shallow water table (method 3), Figure 5-1.
(2) Input data includes swell pressure, swell and compression indices,
and the maximum past pressure of each soil layer. Incremental and total
settlement in soil adjacent to the foundation and below the foundation may be
calculated.
c. Subroutine LEON . This subroutine (NOPT=1) calculates immediate
settlement of shallow foundations on granular soils using both cone penetration and dilatometer in situ test data. This method considers effects of
prestress after the model of Leonards and Frost (item 37)
F- 1
Table F-1
Input Data
Line Input Parameters Format Statement
1 TITLE 20A4
2 MPROB NOPT NBPRES NNP NBX NMAT DX 6I5,F10.2
3 N IE(N,M) 2I5
(Line 3 repeated for each new material, M=1,NMAT; last
line is NEL NMAT)
4 M G(M) WC(M) EO(M) I5,3F10.3
(Line 4 repeated for each new material, M=1,NMAT)
5 DGWT IOPTION NOUT F10.2,2I5
6 Q BLEN BWID MRECT 3F10.2,I5
7 If NOPT=0
M SP(M) CS(M) CC(M) PM(M) I5,4F10.4
If NOPT=1
M PO(M) P1(M) QC(M) I5,3F10.2
If NOPT=2
M QC(M) I5,F10.2
If NOPT=3
M PRES(M,J),J=1,5 I5,5F10.2
If NOPT=4
M ES(M) I5,F10.2
(Line 7 repeated for each new material, M=1,NMAT)
8 If NOPT=0
XA XF 2F10.2
If NOPT=2 or 4
TIME F10.2
If NOPT=3
M STRA(M,J),J=1,5 I5,5F10.2
(This line repeated for each new material, M=1,NMAT)
F- 2
Table F-2
Description of Input Data
Line Parameter Description
1 TITLE Name of problem
2 NPROB Number of problems; If NPROB >1, then the program repeats
calculations with new input data beginning with Line 5
NOPT Option for model: =0 for consolidation/swell
=1 for Leonards and Frost
=2 for Schmertmann
=3 for Collapsible soil
=4 for elastic soil settlement
NBPRES Option for foundation: =1 for rectangular slab
=2 for long strip footing
NNP Total number of nodal points; vertical displacements
calculated to depth DX*(NNP-1)
NBX Number of nodal point at bottom of foundation
NMAT Total number of different soil layers
DX Increment of depth, ft
3 N Element number
IE(N,M) Number of soil layer M associated with element N
4 M Number of soil layer
G(M) Specific gravity of soil layer M
WC(M) Water content of soil layer M, percent
EO(M) Initial void ratio of soil layer M
5 DGWT Depth to hydrostatic water table, ft; If NOPT=0 and IOPTION
=1, then set DGWT=ZA+Uwa/0.03125 where Uwa= suction (or
positive value of negative pore water pressure),tsf at
depth ZA (method 3, Figure 5-1); If Uwa=0, then DGWT=ZA
(method 2, Figure 5-1); set NNP= 1+ ZA/DX to prevent
displacement calculations below depth ZA
IOPTION Equilibrium moisture profile: =0 for saturation above the
water table (method 1, Figure 5-1); if NOPT=0, then =1 for
hydrostatic above water table
NOUT Amount of output data, =0 only total displacements
=1 for increments with totals
6 Q Applied uniform pressure on foundation, tsf
BLEN Length of foundation or 0.0 if NBPRES=2, ft
BWID Width of foundation or long continuous footing, ft
MRECT Location of calculation: =0 for center and =1 for corner
of rectangle or edge of long footing
F- 3
