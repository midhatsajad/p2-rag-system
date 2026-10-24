# CECW-EG (pages 125-128)

where q c1 and q c2 are unit cone resistances determined by the procedure described
in Figure 5-21. For example, q c1 calculated over the minimum path is as follows:
qc2 over the minimum path is as follows:
From Equation 5-36, q bu = (172 + 153.75)/2 = 162.9 ksf.
Figure 5-21. Estimating pile tip capacity from CPT data
(Data from Schmertmann 1978)
(4) Scale Effects. Ultimate end bearing capacity q bu tends to be less for
larger diameter driven piles and drilled shafts than that indicated by Equations 5-
33 or 5-34 or Equation 5-2b using Equations 5-31 to estimate N cp or N qp (Meyerhof
1983). Skin friction is independent of scale effects.
(a) Sands. The reduction in end bearing capacity has been related with a
reduction of the effective angle of internal friction φ’ with larger diameter deep
foundations. End bearing capacity q bu from Equation 5-2 should be multiplied by a
reduction factor R bs (Meyerhof 1983)
(5-37a)
for B > 1.64 ft. The exponent m = 1 for loose sand, 2 for medium dense sand, and
3 for dense sand.
(b) Clays. The reduction factor R bc appears related to soil structure and
fissures. For driven piles in stiff fissured clay, R bc is given by Equation 5-37a
where m = 1. For bored piles
(5-37b)
for B from 0 to 5.75 ft.
b. Skin Resistance Capacity. The maximum skin resistance that may be
mobilized along an element of pile length ∆L may be estimated by
(5-9)
where
Asi = area of pile element i, C si ∆L, ft2
Csi = shaft circumference at pile element i, ft
∆L = length of pile element, ft
fsi = skin friction at pile element i, ksf
(1) Cohesive Soil.
(a) Alpha method. The skin friction of a length of pile element may be
estimated by
(5-10)
where
αa = adhesion factor
Cu = undrained shear strength, ksf
Local experience with existing soils and load test results should be used to
estimate appropriate αa. Estimates of αa may be made from Table 5-10 in the
absence of load test data and for preliminary design.
(b) Lambda Method. This semi-empirical method is based on numerous
load test data of driven pipe piles embedded in clay assuming that end bearing
capacity was evaluated from Equation 5-2a using N cp = 9 and ζcp = 1 (Vijayvergiya
and Focht 1972). The N qp and N γp terms are not used. Skin friction is
(5-38a)
where
λ = correlation factor, Figure 5-22
σ’m = mean effective vertical stress between the ground surface and
pile tip, ksf
Cum = mean undrained shear strength along the pile length, ksf
TABLE 5-10
Adhesion Factors for Driven Piles in Cohesive Soil
(Data from Tomlinson 1980)
Length/Width Ratio Undrained Shear Adhesion
L Strength C u, ksf Factor αa
B
< 20 < 3 1.2 - 0.3C u
> 3 0.25
> 20 0.0 - 1.5 1.0
1.5 - 4.0 1.5 - 0.4C u
> 4 0.3
Figure 5-22. Lambda correlation factor
(Data from Vijayvergiya and Focht 1972)
λ may also be given approximately by
(5-38b)
where L is the pile length, ft.
(2) Cohesionless Soil. The soil-shaft skin friction may be estimated using
effective stresses
(5-12a)
(5-12b)
where
βf = lateral earth pressure and friction angle factor
K = lateral earth pressure coefficient
δa = soil-shaft effective friction angle, ≤φ ’, deg
σ’i = effective vertical stress in soil in pile element i, ksf
Cohesion c is taken as zero.
(a) Figure 5-5 indicates appropriate values of βf as a function of the
effective friction angle φ’ of the soil prior to installation of the deep
foundation.
(b) The effective vertical stress σ’i approaches a limiting stress at the
critical depth Lc, then remains constant below Lc. Lc may be estimated from
Figure 5-3.
(c) The Nordlund method in Table 5-8b provides an alternative method of
estimating skin resistance.
(3) CPT Field Estimate. The skin friction f si may be estimated from the
measured cone resistance q c for the piles described in Table 5-2b using the curves
given in Figure 5-6 for clay and silt, sand and gravel, and chalk (Bustamante and
Gianeselli 1983).
c. Ultimate Capacity From Wave Equation Analysis. Estimates of total bearing
capacity may be performed using computer program GRLWEAP (Goble Rausche Likins and
Associates, Inc. 1988). The analysis uses wave propagation theory to calculate the
force pulse transmitted along the longitudinal pile axis caused by impact of the
ram, Figure 5-23. The force pulse travels at a constant velocity depending on the
pile material and this pulse is attenuated by the soil frictional resistance along
the embedded length of the pile. The pile penetrates into the soil when the force
pulse reaching the pile tip exceeds the ultimate soil resistance at the pile tip
Qub. Program GRLWEAP and user’s manual are licensed to the Waterways Experiment
Station and it is available to the US Army Corps of Engineers.
