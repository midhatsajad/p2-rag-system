# CECW-EG (pages 101-104)

Figure 5-12. Load-transfer curves applied in AXILTR
where
Gs = soil shear modulus at an applied shear stress τ, pounds/square
foot (psf)
Gi = initial shear modulus, psf
τ = shear stress, psf
τmax = shear stress at failure, psf
R = curve fitting constant, usually near 1.0
The curve fitting constant R is the slope of the relationship of 1 - G s/Gi
versus τ/τmax and may be nearly 1.0. The soil shear modulus G s is found from the
elastic soil modulus E s by
(5-19b)
where νs is the soil Poisson’s ratio. A good value for νs is 0.3 to 0.4.
(a) Load-transfer functions may also be input into AXILTR for each soil layer
up to a maximum of 11 different functions. Each load-transfer function consists of
11 data values consisting of the ratio of the mobilized skin friction/maximum
mobilized skin friction f s/f-s correlated with displacement as illustrated in
Figure 5-12b. The maximum mobilized skin friction f- s is assumed the same as the
maximum soil shear strength. The corresponding 11 values of the shaft displacement
(or shaft movement) in inches are input only once and applicable to all of the loadtransfer functions. Therefore, the values of f s/f-s of each load transfer function
must be correlated with the given shaft displacement data values.
(b) The full mobilized skin friction f- s is computed for effective stresses
from
(5-20)
where
c’ = effective cohesion, psf
βf = lateral earth pressure and friction angle factor
σ’v = effective vertical stress, psf
The factor βf is calculated in AXILTR by
(5-21)
where
Ko = lateral coefficient of earth pressure at rest
φ’ = effective peak friction angle from triaxial tests, deg
The effective cohesion is usually ignored.
(c) The maximum mobilized skin friction f- s for each element is computed for
total stresses from Equation 5-10 using αa from Table 5-1 or Equations 5-11.
(5) Influence of Soil Movement. Soil movement, heave or settlement, alters
the performance of the shaft. The magnitude of the soil heave or settlement is
controlled by the swell or recompression indices, compression indices, maximum past
pressure and swell pressure of each soil layer, depth to the water table, and depth
of the soil considered active for swell or settlement. The swell index is the slope
of the rebound pressure - void ratio curve on a semi-log plot of consolidation test
results as described in ASTM D 4546. The recompression index is the slope of the
pressure-void ratio curve on a semi-log plot for pressures less than the maximum
past pressure. The swell index is assumed identical with the recompression index.
The compression index is the slope of the linear portion of the pressure-void ratio
curve on a semi-log plot for pressures exceeding the maximum past pressure. The
maximum past pressure (preconsolidation stress) is the greatest effective pressure
to which a soil has been subjected. Swell pressure is defined as a pressure which
prevents a soil from swelling at a given initial void ratio as described by method C
in ASTM D 4546.
(a) The magnitude of soil movement is determined by the difference between
the initial and final effective stresses in the soil layers and the soil parameters.
The final effective stress in the soil is assumed equivalent with the magnitude of
the total vertical overburden pressure, an assumption consistent with zero final
pore water pressure. Program AXILTR does not calculate soil displacements for shaft
load transferred to the soil.
(b) Swell or settlement occurs depending on the difference between the input
initial void ratio and the final void ratio determined from the swell and
compression indices, the swell pressure, and the final effective stress for each
soil element. The method used to calculate soil swell or settlement of soil
adjacent to the shaft is described as Method C of ASTM D 4546.
(c) The depth of the active zone Z a is required and it is defined as the
soil depth above which significant changes in water content and soil movement can
occur because of climate and environmental changes after construction of the
foundation. Refer to EM 1110-1-1904 for further information.
5-4. Lateral Load Capacity of Single Shafts. Deep foundations may be subject to
lateral loads as well as axial loads. Lateral loads often come from wind forces on
the structure or inertia forces from traffic. Lateral load resistance of deep
foundations is determined by the lateral resistance of adjacent soil and bending
moment resistance of the foundation shaft. The ultimate lateral resistance T u
often develops at lateral displacements much greater than can be allowed by the
structure. An allowable lateral load T a should be determined to be sure that the
foundation will be safe with respect to failure.
a. Ultimate Lateral Load. Brom’s equations given in Table 5-5 can give good
results for many situations and these are recommended for an initial estimate of
ultimate lateral load T u. Ultimate lateral loads can be readily determined for
complicated soil conditions using a computer program such as COM624G based on beamcolumn theory and given p-y curves (Reese, Cooley, and Radhakkrishnan 1984). A p-y
curve is the relationship between the soil resistance per shaft length (kips/inch)
and the deflection (inches) for a given lateral load T.
TABLE 5-5
Brom’s Equations for Ultimate Lateral Load (Broms 1964a, Broms 1964b, Broms 1965)
a. Free Head Pile in Cohesive Soil
Pile Equations Diagram
Short
L ≤ Lc (5-22a)
(5-22b)
Long
L ≥ Lc
(5-22c)
b. Free Head Pile in Cohesionless Soil
Pile Equations Diagram
(5-24a)
Short
L ≤ Lc
(5-24b)
Long (5-24c)
L ≥ Lc
