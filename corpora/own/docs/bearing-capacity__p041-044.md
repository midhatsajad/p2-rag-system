# CECW-EG (pages 41-44)

(4-1)
where
qu = ultimate bearing capacity, ksf
c = unit soil cohesion, ksf
B’ = minimum effective width of foundatio nB-2 e B,f t
eB = eccentricity parallel with foundation width B, M B/Q, ft
MB = bending moment parallel with width B, kips-ft
Q = vertical load applied on foundation, kips
γ’H = effective unit weight beneath foundation base within the failure
zone, kips/ft3
σ’D = effective soil or surcharge pressure at the foundation depth D,
γ’D D, ksf
γ’D = effective unit weight of soil from ground surface to foundation
depth, kips/ft3
D = foundation depth, ft
Nc,Nγ,Nq = dimensionless bearing capacity factors of cohesion c, soil
weight in the failure wedge, and surcharge q terms
ζc,ζγ,ζq = dimensionless correction factors of cohesion c, soil weight
in the failure wedge, and surcharge q accounting for
foundation geometry and soil type
(1) Net Bearing Capacity. The net ultimate bearing capacity q’ u is the
maximum pressure that may be applied to the base of the foundation without
undergoing a shear failure that is in addition to the overburden pressure at depth
D.
(4-2)
(2) Bearing Capacity Factors. The dimensionless bearing capacity factors
Nc,N q, and N γ are functions of the effective friction angle φ’ and depend on the
model selected for solution of Equation 4-1.
(3) Correction Factors. The dimensionless correction factors ζ consider a
variety of options for modeling actual soil and foundation conditions and depend on
the model selected for solution of the ultimate bearing capacity. These options are
foundation shape with eccentricity, inclined loading, foundation depth, foundation
base on a slope, and a tilted foundation base.
b. Terzaghi Model. An early approximate solution to bearing capacity was
defined as general shear failure (Terzaghi 1943). The Terzaghi model is applicable
to level strip footings placed on or near a level ground surface where foundation
depth D is less than the minimum width B. Assumptions include use of a surface
footing on soil at plastic equilibrium and a failure surface similar to Figure 1-3a.
Shear resistance of soil above the base of an embedded foundation is not included in
the solution.
(1) Bearing Capacity Factors. The Terzaghi bearing capacity factors N c and
Nq for general shear are shown in Table 4-1 and may be calculated by
TABLE 4-1
Terzaghi Dimensionless Bearing Capacity Factors (after Bowles 1988)
φ’N q Nc Nγ
28 17.81 31.61 15.7
30 22.46 37.16 19.7
32 28.52 44.04 27.9
34 36.50 52.64 36.0
35 41.44 57.75 42.4
36 47.16 63.53 52.0
38 61.55 77.50 80.0
40 81.27 95.66 100.4
42 108.75 119.67 180.0
44 147.74 151.95 257.0
45 173.29 172.29 297.5
46 204.19 196.22 420.0
48 287.85 258.29 780.1
50 415.15 347.51 1153.2
φ’N q Nc Nγ
0 1.00 5.70 0.0
2 1.22 6.30 0.2
4 1.49 6.97 0.4
6 1.81 7.73 0.6
8 2.21 8.60 0.9
10 2.69 9.60 1.2
12 3.29 10.76 1.7
14 4.02 12.11 2.3
16 4.92 13.68 3.0
18 6.04 15.52 3.9
20 7.44 17.69 4.9
22 9.19 20.27 5.8
24 11.40 23.36 7.8
26 14.21 27.09 11.7
(4-3a)
(4-3b)
Factor N γ depends largely on the assumption of the angle ψ in Figure 1-3a. N γ
varies from minimum values using Hansen’s solution to maximum values using the
original Terzaghi solution. N γ shown in Table 4-1, was backfigured from the
original Terzaghi values assuming ψ = φ’ (Bowles 1988).
(2) Correction Factors. The Terzaghi correction factors ζc and ζγ
consider foundation shape only and are given in Table 4-2. ζq = 1.0 (Bowles 1988).
TABLE 4-2
Terzaghi Correction Factors ζc and ζγ
Factor Strip Square Circular
ζc 1.0 1.3 1.3
ζγ 1.0 0.8 0.6
c. Meyerhof Model. This solution considers correction factors for
eccentricity, load inclination, and foundation depth. The influence of the shear
strength of soil above the base of the foundation is considered in this solution.
Therefore, beneficial effects of the foundation depth can be included in the
analysis. Assumptions include use of a shape factor ζq for surcharge, soil at
plastic equilibrium, and a log spiral failure surface that includes shear above the
base of the foundation. The angle ψ =4 5+ φ/2 was used for determination of N γ.
Table 4-3 illustrates the Meyerhof dimensionless bearing capacity and correction
factors required for solution of Equation 4-1 (Meyerhof 1963).
(1) Bearing Capacity Factors. Table 4-4 provides the bearing capacity
factors in 2-degree intervals.
(2) Correction Factors. Correction factors are given by
Cohesion: ζc = ζcs ζci ζcd
Wedge: ζγ = ζγs ζγi ζγd
Surcharge: ζq = ζqs ζqi ζqd
where subscript s indicates shape with eccentricity, subscript i indicates
inclined loading, and d indicates foundation depth.
(3) Eccentricity. The influence of bending moments on bearing capacity can
be estimated by converting bending moments to an equivalent eccentricity e.
Footing dimensions are then reduced to consider the adverse effect of eccentricity.
(a) Effective footing dimensions may be given by
(4-4a)
(4-4b)
(4-4c)
(4-4d)
where
MB = bending moment parallel with foundation width B, kips-ft
MW = bending moment parallel with foundation length W, kips-ft
Orientation of axes, eccentricities,and bending moments are shown in Table 4-3.
(b) The ultimate load applied to footings to cause a bearing failure is
(4-5)
where
qu = ultimate bearing capacity of Equation 4-1 considering eccentricity
in the foundation shape correction factor, Table 4-3, ksf
Ae = effective area of the foundation B’W’, ft 2
