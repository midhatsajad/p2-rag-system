# CECW-EG (pages 169-172)

(F-1)
where
ρi = immediate settlement, ft
c1 = correction to account for strain relief from embedment,
1 - 0.5σ’o/∆p ≥ 0.5
σ’o = effective vertical overburden pressure at bottom of footing, tsf
∆p = net applied footing pressure, q - σ’o, tsf
q = bearing pressure on footing, tsf
∆z = depth increment, ft
Iiz = influence factor of soil layer i from Figure 3-4
Rizoc = ratio of stress increment corresponding to the overconsolidated
part in soil layer i to the total stress increment in that
layer
Riznc = ratio of stress increment corresponding to the normally
consolidated part in soil layer i to the total stress
increment in that layer
Eizoc = Young’s soil modulus of overconsolidated soil layer i at
depth z, tsf
Eiznc = Young’s soil modulus of normally consolidated soil layer i at
depth z, tsf
(1) The ratios R iz may be found as follows:
(F-2a)
(F-2b)
where
σ’p = preconsolidation or maximum past pressure, tsf
σ’v = initial vertical effective stress, tsf
σ’f = final effective stress at the center of the layer, tsf
σ’p is determined from σ’v and the overconsolidation ratio, OCR.
(2) The OCR is estimated from (item 57)
(F-3)
where φax is the axial friction angle, degrees. Equation F-3 was confirmed
(item 37) for OCR between 2 and 20.
(3) φax is estimated from the plane strain angle φps by (item 57)
(F-4)
F- 8
(4) The plane strain angle φps is estimated from the coefficient of
earth pressure and q c/σ’v using correlations suggested by (item 41). q c is
the cone penetration resistance, tsf. These correlations have been programmed
in subroutine SPLINE. Subroutine BICUBIC is used to evaluate φps . The
coefficient of earth pressure is estimated using
(F-5)
where
Koc = coefficient of earth pressure for overconsolidated soil
KD = horizontal stress index, (P o -u w)/σ’v
Po = dilatometer lift-off pressure, tsf
uw = in-situ pore water pressure, tsf
Settlements calculations are sensitive to the value of K D , the horizontal
stress index. If K oc calculated by Equation F-5 exceeds 1.8, then the OCR
calculated by Equation E-3 may exceed 20. The dilatometer lift-off pressure
Po should be a reliable value. Program VDISPL does not limit the value of
Koc . The constants in Equation F-5 may also differ from those for local
soils.
(5) The elastic soil moduli are estimated by
(F-6a)
(F-6b)
where E D = dilatometer modulus, tsf. E D is given by
(F-7)
where P 1 is the dilatometer B-pressure, the pressure required to expand the
membrane 1.1 mm at the test depths. If R izoc = 0, then E iznc = 0.9ED .
Input data include the dilatometer A and B pressures and the cone resistance
for each soil layer. Incremental and total settlement beneath the foundation
may be calculated.
d. Subroutine SCHMERT . This subroutine (NOPT=2) calculates immediate
settlement of shallow foundations on granular soils from cone penetration test
data by the Schmertmann model (item 55)
(F-8)
where the input parameters are the same as above except E si is the elastic
soil modulus of layer i. E si = 2.5qc for rectangular footings or mats and
Esi = 3.5q c for long strip footings. C t is a correction for time dependent
increase in settlement
(F-9)
F- 9
(1) Input data include cone penetration resistance q c for each soil
layer and the time in years following construction when settlement is to be
calculated. The incremental and total settlement beneath the foundation is
calculated for the provided time.
(2) This subroutine includes an option (NOPT=4) to input E si
directly for each soil layer. This option may be useful if the user does not
have cone penetration resistance data, but can determine reliable values of
Esi by some other tests.
e. Subroutine COLL . This subroutine (NOPT=3) calculates the collapse
settlement of susceptible soils after the model of Houston, et al (item 22).
The model uses the results of a one-dimensional consolidometer test performed
on collapsible soil for each soil layer, Figure 5-5. Input data include 5
points each of the applied pressure and strain distributions. The collapse
settlement is calculated from the difference in strains between the unwetted
line, points A-BB-B, and the wetted line, points A-C-D. Incremental and total
settlement in soil adjacent and above the foundation and below the foundation
may be calculated. The settlement caused by foundation loads prior to
collapse may be estimated by the Leonards and Frost (NOPT=1, item 37) and
Schmertmann (NOPT=2) models (item 57).
F-3. Example Problems
a. Heave of Expansive Soil . A footing 3 ft by 3 ft square ,B=W=3
ft, is to be constructed 3 ft below ground surface,D=3f t ,o nt w o cohesive
expansive soil layers. The amount of heave is to be calculated if the soil is
left untreated. The bottom of the soil profile is 8 ft below ground surface,
which is also the depth to the ground water level. The depth increment DX
is taken as 0.5 ft. The total number of nodal points NNP is selected as 17,
number of elements NEL=NNP-1 or 16, and the nodal point at the bottom of the
footing is NBX = (D/DX)+1 = 3/0. 5+1=7 . A schematic diagram of this
problem is illustrated in Figure 5-6. The input parameters of data file
VDIN.DAT for the consolidation/swell model, NOPT = 0, are given in Table F-4a.
The maximum past pressures were omitted, which caused the program to assume
these values equal with the swell pressures. The output data listed in data
file VDOU.DAT shown in Table F-4b indicate substantial potential heave of 0.3
ft or 3.6 inches beneath the footing.
b. Settlement of Granular Soil . The same footing illustrated in
Figure 5-6 is to be constructed in granular soil consisting of two distinctive
layers. Field tests consisting of cone penetration and dilatometer data were
obtained.
(1) The input parameters of data file VDIN.DAT for the Leonard and
Frost model, NOPT = 1, are given in Table F-5a. The output data listed in
data file VDOU.DAT shown in Table F-5b indicate 0.0092 ft or 0.11 inch of
settlement beneath the footing.
(2) The same problem was applied to the Schmertmann model using the
cone penetration resistance of the soil layers. The input data are given in
Table F-6a. The output data shown in Table F-6b indicate 0.012 ft or 0.15
inch of settlement.
F-10
Table F-4
Expansive Soil Heave
a. Input data, file VDIN.DAT
FOOTING IN EXPANSIVE SOIL
1 0 1 17 7 2 0.50
11
12 2
16 2
1 2.700 20.000 1.540
2 2.65 19.300 0.900
8.00 0 1
1.00 3.00 3.00 0
1 2.0000 0.1500 0.2500
2 3.0000 0.1000 0.2000
8.00 0
b. Output Data, File VDOU.DAT
FOOTING IN EXPANSIVE SOIL
NUMBER OF PROBLEMS= 1 NUMBER OF NODAL POINTS= 17
NUMBER OF NODAL POINT AT BOTTOM OF FOUNDATION= 7
NUMBER OF DIFFERENT SOIL LAYERS= 2 INCREMENT DEPTH= 0.50 FT
CONSOLIDATION SWELL MODEL
RECTANGULAR SLAB FOUNDATION
DEPTH OF FOUNDATION = 3.00 FEET
TOTAL DEPTH OF THE SOIL PROFILE = 8.00 FEET
ELEMENT NUMBER OF SOIL
11
21
31
41
51
61
71
81
91
10 1
11 1
12 2
13 2
14 2
15 2
16 2
F-11
