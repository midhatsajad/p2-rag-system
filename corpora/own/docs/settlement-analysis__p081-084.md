# CECW-EG (pages 81-84)

ments are generally made in two horizontal and one vertical acceleration components that propagate upward from underlying rock. The vertical component of
acceleration is often considered to account for less than 25 percent of the
settlement, but this percentage may be exceeded. Soil affected by ground motion and subsequent settlement may extend to considerable depth depending on
the source of motion.
a. Tentative Simplified Procedure for Sand . A tentative simplified
procedure to estimate settlement from the shaking forces of earthquakes on
saturated sands that are at initial liquefaction and on dry sands is given in
Table 4-1. Input data for this procedure include the blowcount N from SPT
data as a function of depth, effective and total overburden pressures σ’o and
σo , and an estimate of the maximum horizontal acceleration of the ground surface from earthquake records (e.g., Regulation Guide 1.6, Nuclear Regulatory
Commission, items 33 and 34; Office, Chief of Engineer policy for Corps of Engineer specifications for ground motions is provided by the Earthquake Engineering and Geosciences Division, Geotechnical Laboratory, USAE Waterways Experiment Station).
(1) Application. The procedure is applied to the Tokachioki earthquake
in Table 4-2.
(2) Validation. This tentative procedure has not been fully validated.
The example problems in Table 4-2 are based on estimated field behaviors and
not on measured data against which to validate a settlement analysis.
b. WES Procedure for Sands . The Waterways Experiment Station is currently preparing a procedure on a validated (against centrifuge test data) 2-D
soil-structure interactive, nonlinear dynamic effective stress analysis which
computes dynamic response histories of motions, stresses, pore water pressures, and volume changes for the range of responses and pore water pressures
up to and including the initial liquefaction condition. The effects of pore
water pressures on moduli, motions, stresses, and volume changes are taken
into account for the entire time history of an earthquake.
4-3. Settlement from Repeated Loads and Creep . Structures subject to repeated vertical loads experience a long-term settlement from the compression of
cumulative cyclic loads and secondary compression or creep. Operating machinery, pile driving, blasting, wave or wind action are common causes of this
type of dynamic loading. Methods of estimating secondary compression are provided in Section IV, Chapter 3.
a. Compaction Settlement from Machine Vibrations . A procedure to estimate settlement in sand layers from machine vibrations is described in Table
4-3. The procedure is applied to an example in Table 4-4.
b. Settlement Calculated from Laboratory Cyclic Strain Tests . Drained
cyclic triaxial tests may be performed on pervious soil to evaluate the cyclic
settlement through a cyclic strain resistance r ε (item 25).
(1) Test procedure. The soil should be consolidated to simulate the
in situ stress state of effective horizontal and vertical pressures. The soil
is subsequently subject to three different cyclic stress levels to evaluate
rε .
Table 4-1
A Suggested Tentative Procedure for Computation of
Earthquake Settlement in Sand (Data from Item 63)
a. Saturated Sand that Reaches Initial Liquefaction
Step Description
1 Determine the blow count N from SPT tests as a function of depth and
divide the profile into discrete layers of sand with each layer containing sand with similar blow count.
2 Determine correction factor C ER as follows where C ER = estimated rod
energy in percent/60
Country Hammer Hammer Release CER
Japan Donut Free-Fall 1.3
Donut Rope and Pulley 1.12*
with special
throw release
USA Safety Rope and Pulley 1.00*
Donut Rope and Pulley 0.75
Europe Donut Free-Fall 1.00*
China Donut Free-Fall 1.00*
Donut Rope and Pulley 0.83
*Prevalent method in USA today
3 Estimate the total and effective overburden pressure σo and σ’o in
tsf units from known or estimated soil unit weights and pore water
pressures of each layer.
4 Estimate the relative density D r in percent from results of SPT
data using Figure 4-1, improved correlations for overconsolidated soil
(item 50), or the expression
(4-1a)
where N J is the blowcount by Japanese standards and σ’o is the effective overburden pressure. D r for normally consolidated material
may be estimated by (item 42)
(4-1b)
where
σ’o = effective overburden pressure, tsf
cu = uniformity coefficient, D60/D10
D60 = grain diameter at which 60 percent of soil weight is finer
D10 = grain diameter at which 10 percent of soil weight is finer
Table 4-1a. Continued
Step Description
5 Determine the correction factor C N from Figure 4-2 using σ’o and
Dr .
6 Calculate normalized blowcount
(4-2)
where (N 1)60 = SPT blowcount normalized to an effective energy
delivered to the drill rod at 60 percent of theoretical free-fall
energy.
7 Calculate the cyclic shear stress ratio causing initial liquefaction
to occur for the given earthquake of magnitude M
(4-3)
where
τav = average cyclic shear stress induced by earthquake shaking,
tsf
σ’o = effective overburden pressure, tsf
σo = total overburden pressure, tsf
amax = maximum horizontal acceleration of the ground surface in
units of g from earthquake records of magnitude M
(Regulation Guide 1.60, Nuclear Regulatory Commision;
refer to Earthquake Engineering and Geosciences Division,
Geotechnical Laboratory, USAE Waterways Experiment Station
for Corps of Engineers)
g = acceleration of gravity, 32.2 ft/sec/sec
rd = stress reduction factor; 1.0 at the ground surface decreasing to 0.9 at depth 30 ft below ground surface
8 Convert ( τav /σ’o)M to an equivalent earthquake of magnitude M = 7.5
by
(4-4)
where the scaling factor r m is
Table 4-1a. Continued
Step Description
Magnitude of *No Representative
Earthquake M Cycles at 0.65τmax rm
8.5 26 0.89
7.5 15 1.00
6.75 10 1.13
6.00 5 1.32
5.25 2 - 3 1.50
* Representative of the number of equivalent
stress cycles caused by the earthquake where
τmax = maximum cycle stress
9 Evaluate volumetric strain εc in percent after initial liquefaction
from Figure 4-3 using calculated values of (N 1)60 of step 6 and
(τav/σ’o)7.5 of step 8.
10 Evaluate earthquake settlement ρe after initial liquefaction in
inches from
(4-5)
where h j = thickness of each stratum j in inches
b. Dry Sand
Step Description
1-6 Repeat steps 1 through 6 in Table 4-1a above to evaluate D r and
(N1)60 .
7 Evaluate mean effective pressure σ’m of each stratum in tsf (e.g.,
if the coefficient of lateral earth pressure K o = 0.47) . σ’m is considered the total mean pressure in dry
sand.
8 Calculate
(4-6)
where G max = maximum shear modulus, tsf
