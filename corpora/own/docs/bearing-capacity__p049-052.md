# CECW-EG (pages 49-52)

f. Computer Solutions. Analyses by computer programs provide effective
methods of estimating ultimate and allowable bearing capacities.
(1) Program CBEAR. Program CBEAR (Mosher and Pace 1982) can be used to
calculate the bearing capacity of shallow strip, rectangular, square, or circular
footings on one or two soil layers. This program uses the Meyerhof and Vesic
bearing capacity factors and correction factors.
(2) Program UTEXAS2. UTEXAS2 is a slope stability program that can be used
to calculate factors of safety for long wall footings and embankments consisting of
multilayered soils (Edris 1987). Foundation loads are applied as surface pressures
on flat surfaces or slopes. Circular or noncircular failure surfaces may be
assumed. Noncircular failure surfaces may be straight lines and include wedges.
Shear surfaces are directed to the left of applied surface loading on horizontal
slopes or in the direction in which gravity would produce sliding on nonhorizontal
slopes (e.g., from high toward low elevation points). This program can also
consider the beneficial effect of internal reinforcement in the slope. q u
calculated by UTEXAS2 may be different from that calculated by CBEAR partly because
the FS is defined in UTEXAS2 as the available shear strength divided by the shear
stress on the failure surface. The assumed failure surfaces in CBEAR are not the
same as the minimum FS surface found in UTEXAS2 by trial and error. FS in Table 1-2
are typical for CBEAR. Program UTEXAS2 calculates factors of safety, but these FS
have not been validated with field experience. UTEXAS2 is recommended as a
supplement to the Terzaghi, Meyerhof, Hansen, and Vesic models until FS determined
by UTEXAS2 have been validated.
g. Multilayer Soils. Foundations are often supported by multilayer soils.
Multiple soil layers influence the depth of the failure surface and the calculated
bearing capacity. Solutions of bearing capacity for a footing in a strong layer
that is overlying a weak clay layer, Figure 4-1, are given below. These solutions
are valid for a punching shear failure. The use of more than two soil layers to
model the subsurface soils is usually not necessary.
Figure 4-1. Schematic of a multilayer foundation-soil system
(1) Depth of Analysis. The maximum depth of the soil profile analyzed need
not be much greater than the depth to the failure surface, which is approximately
2B for uniform soil. A deeper depth may be required for settlement analyses.
(a) If the soil immediately beneath the foundation is weaker than deeper
soil, the critical failure surface may be at a depth less than 2B.
(b) If the soil is weaker at depths greater than 2B, then the critical
failure surface may extend to depths greater than 2B.
(2) Dense Sand Over Soft Clay. The ultimate bearing capacity of a footing in
a dense sand over soft clay can be calculated assuming a punching shear failure
using a circular slip path (Hanna and Meyerhof 1980; Meyerhof 1974)
Wall Footing:
(4-10a)
Circular Footing:
(4-10b)
where
qu,b = ultimate bearing capacity on a very thick bed of the bottom
soft clay layer, ksf
γsand = wet unit weight of the upper dense sand, kips/ft3
Ht = depth below footing base to soft clay, ft
D = depth of footing base below ground surface, ft
Kps = punching shear coefficient, Figure 4-2a,4-2b, and 4-2c
φsand = angle of internal friction of upper dense sand, degrees
Ss = shape factor
qut = ultimate bearing capacity of upper dense sand, ksf
The punching shear coefficient k ps can be found from the charts in Figure 4-2
using the undrained shear strength of the lower soft clay and a punching shear
parameter Cps.C ps, ratio of ζ/φsand where ζ is the average mobilized angle of
shearing resistance on the assumed failure plane, is found from Figure 4-2d using
φsand and the bearing capacity ratio R bc.R bc = 0.5γsandBNγ/(CuNc). B is the diameter
of a circular footing or width of a wall footing. The shape factor S s, which
varies from 1.1 to 1.27, may be assumed unity for conservative design.
(3) Stiff Over Soft Clay. Punching shear failure is assumed for stiff over
soft clay.
(a) D = 0.0. The ultimate bearing capacity can be calculated for a footing
on the ground surface by (Brown and Meyerhof 1969)
Figure 4-2. Charts for calculation of ultimate bearing capacity
of dense sand over soft clay (Data from Hanna and Meyerhof 1980)
Wall Footing: (4-11a)
(4-11b)
Circular Footing: (4-11c)
(4-11d)
where
Cu,upper = undrained shear strength of the stiff upper clay, ksf
Cu,lower = undrained shear strength of the soft lower clay, ksf
Ncw,0 = bearing capacity factor of the wall footing
Ncc,0 = bearing capacity factor of the circular footing
Bdia = diameter of circular footing, ft
A rectangular footing may be converted to a circular footing by B dia = 2(BW/π)1/2
where B = width and W = length of the footing. Factors N cw,0 and N cc,0 will
overestimate bearing capacity by about 10 percent if Cu,lower/Cu,upper ≥ 0.7. Refer to
Brown and Meyerhof (1969) for charts of Ncw,0 and Ncc,0.
(b) D > 0.0. The ultimate bearing capacity can be calculated for a footing
placed at depth D by
Wall Footing: (4-12a)
Circular Footing: (4-12b)
where
Ncw,D = bearing capacity factor of wall footing with D > 0.0
Ncc,D = bearing capacity factor of rectangular footing withD>0 . 0
=N cw,D[1 + 0.2(B/W)]
γ = wet unit soil weight of upper soil, kips/ft3
D = depth of footing, ft
Ncw,D may be found using Table 4-7 and N cw,0 from Equation 4-11b. Refer to
Department of the Navy (1982) for charts that can be used to calculate bearing
capacities in two layer soils.
(4) Computer Analysis. The bearing capacity of multilayer soils may be
estimated from computer solutions using program CBEAR (Mosher and Pace 1982).
Program UTEXAS2 (Edris 1987) calculates FS for wall footings and embankments, which
have not been validated with field experience. UTEXAS2 is recommended as a
supplement to CBEAR until FS have been validated.
