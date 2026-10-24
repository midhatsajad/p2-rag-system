# CECW-EG (pages 73-76)

Figure 3-21. Embankment for example application
b. Time Rate of Consolidation . The procedure described in Table 3-9
was applied to evaluate the rate of settlement beneath the edge and center of
the embankment by hand calculations assuming an instantaneous rate of loading.
The solution is worked out in Table 3-13b.
3-15. Accuracy of Settlement Predictions . Experience shows that predictions
of settlement are reasonable and within 50 percent of actual settlements for
many soil types. Time rates of settlement based on laboratory tests and empirical correlations may not be representative of the field because time rates
are influenced by in situ fissures, existence of high permeable sand or low
permeable bentonite seams, impervious boundaries, and nonuniform soil parameters as well as the rate of construction.
a. Preconsolidation Stress . Soil disturbance of laboratory samples
used for 1-D consolidation tests decreases the apparent preconsolidation
stress.
Table 3-13
Evaluation of Consolidation Settlement by Hand Calculations
for Example Application of Embankment, Figure 3-21
a. Total Settlment
Step Description
1 The preconsolidation stress σ’p after the Casagrande construction
procedure, Table 3-6a, is 6.6 tsf shown in Figure 3-13 (neglecting a
minimum and maximum range). Since σ’p > σ’o , the soil is overconsolidated with an OCR of about 22. The field virgin consolidation
line is evaluated by the procedure in Table 3-6b.
2 The initial effective stress distribution σ’o , is shown in Figure
3-21b. The wet unit weight γ is 0.061 ton/ft3 and γw is 0.031
ton/ft. σ’o at 10 ft of depth is 0.3 tsf.
3 The initial void ratio of the specimen prior to consolidation is e o =
1.05, Figure 3-13.
4 The virgin compression index C c = 0.42 and the recompression index
Cr = 0.078 , Figure 3-13.
5 The pressure distribution applied by the embankment was calculated
using the trapezoidal distribution, Table C-1b (Appendix C). At 10 ft
below ground surface the vertical stress applied by the embankment at
the edge is 0.22 tsf and at the center is 1.01 tsf. The final effective pressure σ’f 10 ft below ground surface at the edge is 0.55 tsf
and at the center 1.30 tsf. The estimated pressure distributions are
shown in Figure 3-21b.
6 The change in void ratio ∆e at the 10 ft depth may be found from
Equation 3-23 where the right-hand part of the equation containing C c
is ignored because σ’f < σ’p ,
7, 8 Settlement of the stratum from Equation 3-20 is
Improved reliability may be obtained by testing additional specimens
at different depths within the compressible stratum, calculating settlements within smaller depth increments, and adding the calculated
settlements, Equation 3-22.
Table 3-13. Continued
Step Description
9 Settlement may be corrected for overconsolidation effects after the
Skempton and Bjerrum procedure, Equation 3-24. λ is about 0.8 from
Figure 3-15 for an overconsolidation ratio > 18.
b. Time Rate of Settlement
Step Description
1,2 Minimum and maximum estimates of the coefficient of consolidation may
be made using the methods in Table 3-11 from a plot of the deformation as a function of time data, Figure 3-17. These data indicate c v
values from 0.007 ft2/day to 0.010 ft2/day, Table 3-11. The range of
applied consolidation pressures is from 1 to 2 tsf using double
drainage during the consolidation test.
3 The time factors for the range of c v from 0.007 to 0.010 ft2/day is,
Equation 3-26,
where the time t is in days. The compressible stratum is assumed to
drain on both top and bottom surfaces; therefore, the equivalent
height H e is 10 ft.
4 The excess pore water pressure distribution given by σst in Figure
3-21 appears to be similar to case 2 at the edge and case 1 at the
center, Figure 3-16a. The average degree of consolidation in percent
after 1, 10, and 50 years using Table 3-10 is
Time Tv Ut , Percent
Years Days Min Max Edge (Case 2) Center (Case 1)
Min Max Min Max
1 364 0.025 0.036 14.7 18.8 17.1 21.4
10 3640 0.255 0.364 54.7 65.4 56.7 67.0
50 18200 1.274 3.640 95.6 98.9 95.8 98.9
5 Cases 1 and 2 of Figure 3-16a are considered representative of the
initial excess pore water pressure distributions so that superposition
of the cases in Table 3-9, step 5 and 6, is not necessary.
Table 3-13. Concluded
Step Description
6 Consolidation settlement as a function of time t is, Equation 3-24
Settlement ρct , inches
Time, Years Edge Center
Min Max Min Max
1 0.27 0.35 0.80 1.00
10 1.02 1.22 2.65 3.14
50 1.79 1.85 4.48 4.63
∞ 1.87 4.68
b. Virgin Compression Index . Soil disturbance decreases the compression index.
c. Swelling and Recompression Indices . Soil disturbance increases the
swelling and recompression indices.
d. Coefficient of Consolidation . Soil disturbance decreases the coefficient of consolidation for both virgin compression and recompression, Figure
3-18, in the vicinity of initial overburden and preconsolidation stresses.
The value of c v decreases abruptly at the preconsolidation stress for good
undisturbed samples.
e. Field Test Embankment . A field test embankment may be constructed
for significant projects to estimate field values of soil parameters such as
Cc and c v . Installation of elevation markers, inclinometers, and piezometers allow the measurement of settlement, lateral movement, and pore pressures as a function of time. These field soil parameters may subsequently be
applied to full-scale structures.
3-16 Computer Solutions. Several computer programs are available to expedite
calculation of settlement and rates of settlement of structures constructed on
multilayer soil profiles.
a. Vertical Stress Distribution. The vertical stress distribution from
Boussinesq and Westergaard solutions may be computed beneath foundations, single and multiple footings, and embankments from Program CSETT (item 61) and
Program I0016 (item 45).
b. Ultimate Consolidation Settlement . Long-term consolidation settlement of structures may be computed assuming the Terzaghi 1-D consolidation by
Program MAGSETTI (item 45) using output from Program CSETT or I0016.
c. Ultimate Consolidation and Rate of Settlement . One-dimensional consolidation settlement and rates of settlement by Terzaghi 1-D consolidation
theory may be computed by Program FD31 (item 45) and Program CSETT (item 61).
