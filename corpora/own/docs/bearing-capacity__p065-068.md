# CECW-EG (pages 65-68)

(b) Soil Coordinates: x 1 =x s1 = 10.00, y1 =y s1 = 3.00
(top elevation of x 2 =x s2 = 13.00, y2 =y s2 = 3.00
subsurface soil)
(c) Soil Properties: moist (wet) unit weight γH = 130 pounds/ft3
(subsurface soil) saturated unit weight = γH
friction angle = 30 deg
cohesion = 0.00
(d) Options: One surcharge y coordinate of top of
layer surcharge = 5.00 ft
moist unit weight = 120 pounds/ft 3
saturated unit weight = 120 pounds/ft3
Water table y coordinate of top of
description water table = 2.00 ft
unit weight of water = 62.5 pounds/ft 3
Applied load applied load (R) = 10.2 kips
description x coordinate of base
application point = 11.5 ft
z coordinate of base
application point = 3.00 ft
inclination of load clockwise
from vertical = 11.4 deg
(e) CBEAR calculates q u = 5.34 ksf
(f) Comparison of methods indicates bearing capacities
Total Net
Method q u, ksf q’ u, ksf
Meyerhof 5.25 5.01
Hansen 4.69 4.45
Vesic 5.86 5.62
Program CBEAR 5.34 5.10
The net bearing capacity is found by subtracting γD D = 0.12 2 = 0.24 ksf from qu,
Equation 4-2. The resultant applied pressure on the footing is q r = R/(BW) =
10.2/(3 6) = 0.57 ksf. The factor of safety of all of the above methods with
respect to the net bearing capacity is on the order of q’u/qr ≈ 9. The Hansen
method is most conservative.
c. Rectangular Footing With Eccentricity, Base Tilt, and Ground Slope. A
rectangular footing,B=3f ta n dW=5f t ,i s placed in a cohesionless soil with
base tilt δ = 5 deg and ground slope β = 15 deg as illustrated in Table 4-5 and
Figure 4-7. φ’=2 6d e ga n dc=c a = 0.0. Soil wet unit weight γD = 120 lbs/ft3,
subsurface soil wet unit weight γH = 130 lbs/ft3, and depth to groundwater D GWT =3
ft. Vertical applied load Q = 10 kips and horizontal load T = 0 kips, but M B =5
kips-ft and M W = 10 kips-ft.
Figure 4-7. Shallow foundation with slope and base tilt
(1) Coordinate Adjustment. δ = 5 deg indicates right side elevation of the
base is 3 sin 5 deg = 0.26 ft higher than the left side. β = 15 deg indicates right
side foundation elevation at the ground surface is 3 sin 15 deg = 0.78 ft higher
than the left side.
(2) Effective Stress Adjustment. Average DGWT = 3 + 0.78/2 = 3.39 ft.
Average D=2+ 0.78/2 - 0.26/2 = 2.26 ft. Adjustment of soil unit wet weight for
the water table from Equation 1-6 is
γHSUB = γH - γw = 0.130 - 0.0625 = 0.0675 kip/ft3
H = B tan[45 + ( φ/2)] = 3.00 1.73 = 5.2 ft
γ’H = γHSUB + [(DGWT - D)/H] γw
= 0.0675 + [(3.39 - 2.26)/5.2] 0.0625 = 0.081 kip/ft3
σ’D = σD = γD D = 0.120 2.26 = 0.27 ksf
(3) Eccentricity Adjustment. Bending moments lead to eccentricities from
Equations 4-4c and 4-4d
eB =M B/Q = 5/10 = 0.5 ft
eW =M W/Q = 10/10 = 1.0 ft
Effective dimensions from Equations 4-4a and 4-4b are
B ’=B-2 e B =3-20 . 5=2f t
W ’=W-2 e W =5-21 . 0=3f t
(4) Hansen Method. For φ’ = 26 deg, N q = 11.85 and N γ = 7.94 from Table
4-4. N c is not needed since c = 0.0. From Table 4-5,
(a) Wedge correction factor ζγ = ζγs ζγi ζγd ζγβ ζγδ where ζγi = 1.00
ζγs = 1 - 0.4 B’/W’=1-0 . 42 / 3= 0.733
ζγd = 1.00
ζγβ = (1 - 0.5 tan β)5 = (1 - 0.5 tan 15)5 = 0.487
ζγδ =e -0.047 δ tan φ’ =e -0.047 5 tan 26 = 0.892
ζγ = 0.733 1.000 0.487 0.892 = 0.318
(b) Surcharge correction factor ζq = ζqs ζqi ζqd ζqβ ζqδ where ζqi = 1.00
ζqs = 1 + (B’/W’) tan φ = 1 + (2/3) 0.488 = 1.325
k = D/B = 2.26/3 = 0.753
ζqd =1+2t a n φ’ (1 - sinφ’)2 k=1+2 0.488 (1 - 0.438) 0.753
ζqd = 1.232
ζqβ = ζγβ = 0.487
ζqδ =e -0.035 δ tan φ’ =e -0.035 5 tan 26 = 0.918
ζq = 1.325 1.232 0.487 0.918 = 0.730
(c) Total ultimate bearing capacity from Equation 4-1 is
qu = 0.5 B γ’H Nγ ζγ + σ’D Nq ζq
= 0.5 2.00 0.081 7.942 0.318 + 0.27 11.85 0.730
= 0.205 + 2.335 = 2.54 ksf
(5) Vesic Method. For φ’= 26 deg, Nq = 11.85 and Nγ = 12.54 from Table 4-4.
Nc is not needed. From Table 4-6,
(a) Wedge correction factor ζγ = ζγs ζγi ζγd ζγβ ζγδ where ζγi = 1.00
= 1.00
ζγs =1-0 . 4B / W=1-0 . 42 / 3= 0.733
ζγd = 1.00
ζγβ =( 1-t a n β)2 = (1 - tan 15)2 = 0.536
ζγδ = (1 - 0.017 δ tan φ’)2 = (1 - 0.017 5 tan 26)2 = 0.919
ζγ = 0.733 1.00 0.536 0.919 = 0.361
(b) Surcharge correction factor ζq = ζqs ζqi ζqd ζqβ ζqδ where ζqi = ζqδ
= 1.00
ζqs = 1 + (B/W) tan φ = 1 + 2/3 0.488 = 1.325
ζqd =1+2t a n φ’ (1 - sinφ’)2 k
ζqd =1+2 0.488 (1 - 0.438)2 0.753 = 1.232
ζqβ = ζγβ = 0.536
ζqδ = ζγδ = 0.919
ζq = 1.325 1.232 0.536 0.919 = 0.804
(c) Total ultimate bearing capacity from Equation 4-1 is
qu = 0.5 B γ’H Nγ ζγ + σ’D Nq ζq
= 0.5 2.00 0.081 12.54 0.361 + 0.27 11.85 0.804
= 0.367 + 2.572 = 2.94 ksf
(6) Program CBEAR. Input is as follows (refer to Figure 4-7):
(a) Foundation coordinates: x 1 = 10.00, y1 = 3.00
x2 = 13.00, y2 = 3.26
Length of footing: = 5.00
(b) Soil Coordinates: x s1 = 10.00, ys1 = 5.00
xs2 = 13.00, ys2 = 5.78
(c) Soil Properties: moist (wet) unit weight γH = 120 pounds/ft3
saturated unit weight = γH
friction angle = 26 deg
cohesion = 0.00
(d) Options: One surcharge y coordinate of top of
layer subsurface soil = 3.00 ft
moist unit weight = 130 pounds/ft 3
saturated unit weight = 130 pounds/ft3
friction angle = 26 degrees
cohesion = 0.0
Water table y coordinate of top of
description water table = 2.00 ft
unit weight of water = 62.5 pounds/ft 3
Applied load applied load (R) = 10.0 kips
description x coordinate of base
application point = 11.0 ft
z coordinate of base
application point = 2.00 ft
inclination of load clockwise
from vertical = 0.0 deg
(e) CBEAR calculates q u = 2.21 ksf
(f) Comparison of methods indicates bearing capacities
Total Net
Method q u, ksf q’ u, ksf
Hansen 2.55 2.28
Vesic 3.94 2.67
Program CBEAR 2.21 1.94
