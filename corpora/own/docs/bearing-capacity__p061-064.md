# CECW-EG (pages 61-64)

a. Wall Footing. A wall footing 3 ft wide with a loadQ=1 2 kips/ft
(bearing pressure q = 4 ksf) is proposed to support a portion of a structure in a
selected construction site. The footing is assumed to be placed on or near the
ground surface for this analysis such that D = 0.0 ft, Figure 4-5, and σ’D = 0.0.
Depth H is expected to be < 2B o r<6f t .
(1) Soil Exploration. Soil exploration indicated a laterally uniform
cohesive soil in the proposed site. Undrained triaxial compression test results
were performed on specimens of undisturbed soil samples to determine the undrained
shear strength. Confining pressures on these specimens were equal to the total
vertical overburden pressure applied to these specimens when in the field. Results
of these tests indicated the distribution of shear strength with depth shown in
Figure 4-6. The minimum shear strength c = C u of 1.4 ksf observed 5 to 7 ft below
ground surface is selected for the analysis. The friction angle is φ = 0.0 deg and
the wet unit weight is 120 psf.
(2) Ultimate Bearing Capacity
(a) Terzaghi Method. Table 4-1 indicates N c = 5.7, Nq = 1.0 and Nγ = 0.00.
The total ultimate capacity q u is
The Terzaghi method indicates an ultimate bearing capacity q u = 8 ksf.
(b) Meyerhof Method. The ultimate bearing capacity of this wall footing
using program CBEAR yields q u = 7.196 ksf. The Hansen and Vesic solutions will be
similar.
(3) Allowable Bearing Capacity. FS for this problem from Table 1-2 is 3.0.
Therefore, qa using Equation 1-2a is q u/FS = 8.000/3 = 2.7 ksf from the Terzaghi
solution and 7.196/3 = 2.4 ksf from CBEAR. The solution using program UTEXAS2 gives
a minimum FS = 2.2 for a circular failure surface of radius 3 ft with its center at
the left edge of the footing.
(4) Recommendation. qa ranges from 2.4 to 2.7 while the proposed design
pressure q d is 4 ksf. q d should be reduced to 2.4 ksf ≤ qa.
b. Rectangular Footing With Inclined Load. A rectangular footing with B = 3
f t ,W=6f t ,D=2f t , similar to Figure 1-6, is to be placed in cohesionless soil
on a horizontal surface (β = 0.0) and without base tilt (δ = 0.0). The effective
friction angle φ’ = 30 deg and cohesion c = c u = 0.0. The surcharge soil has a
wet (moist) unit weight γD = 0.120 kip/ft3 (120 pcf), subsurface soil has a wet
(moist) unit weight γH = 0.130 kip/ft3 (130 pcf), and depth to groundwater is D GWT =
3 ft. The saturated unit weight is assumed the same as the wet unit weight. The
applied vertical load on the foundation isQ=1 0 kips and the horizontal load T =
+2 kips to the right.
Figure 4-5. Example wall footing bearing capacity analysis
Figure 4-6. Example undrained shear strength distribution with depth
(1) Effective Stress Adjustment. Adjust the unit soil weights due to the
water table using Equation 1-6
γHSUB = γH - γw = 0.130 - 0.0625 = 0.0675 kip/ft3
H = B tan(45 + φ/2) = 3.00 1.73 = 5.2 ft
γ’H = γHSUB + [(DGWT - D)/H] γw = 0.0675 + [(3 - 2)/5.2] 0.0625
= 0.08 kip/ft3
From Equation 1-7a, σ’D = σD = γD D = 0.120 2.00 = 0.24 ksf
(2) Meyerhof Method. For φ’ = 30 deg, N q = 18.40, Nγ = 15.67, and Nφ = 3.00
from Table 4-4. N c is not needed since c = 0.0. From Table 4-3,
(a) Wedge correction factor ζγ = ζγs ζγi ζγd
ζγs = 1 + 0.1 Nφ (B’/W’)=1+0 . 1 3.00 (3/6) = 1.15
R= ( Q 2 +T 2)0.5 =( 1 0 0+4 )0.5 = 10.2
θ = cos-1(Q/R) = cos -1(10/10.2) = 11.4 deg < φ =3 0d e g
ζγi =[ 1-( θ/φ’)]2 = [1 - (11.4/30)]2 = 0.384
ζγd =1+0 . 1 √Nφ (D/B)=1+0 . 1 1.73 (2/3) = 1.115
ζ = 1.15 0.384 1.115 = 0.49
(b) Surcharge correction factor ζq = ζqs ζqi ζqd
ζqs = ζγs = 1.15
ζqi =[ 1-( θ/90)]2 = [1 - (11.4/90)]2 = 0.763
ζqd = ζγd = 1.115
ζq = 1.15 0.763 1.115 = 0.98
(c) Total ultimate bearing capacity from Equation 4-1 is
qu = 0.5 B γ’HNγ ζγ + σ’D Nq ζq
= 0.5 3.00 0.08 15.67 0.49 + 0.24 18.40 0.98
= 0.92 + 4.33 = 5.25 ksf
(3) Hansen Method. For φ’ = 30 deg, N q = 18.40, Nγ = 15.07, and Nφ = 3.00
from Table 4-4. N c is not needed since c = 0.0. From Table 4-5,
(a) Wedge correction factor ζγ = ζγs ζγi ζγd ζγβ ζγδ where ζγβ = ζγδ
= 1.00
ζγs = 1 - 0.4 (B’/W’)=1-0 . 4 (3/6) = 0.80
ζγi = [1 - (0.7T/Q)]5 = [1 - (0.7 T/10)]5 = 0.47
ζγd = 1.00
ζγ = 0.80 0.47 1.00 = 0.376
(b) Surcharge correction factor ζq = ζqs ζqi ζqd ζqβ ζqδ where ζqβ = ζqδ
= 1.00
ζqs = 1 + (B/W) tan φ = 1 + (3/6) 0.577 = 1.289
ζqi = [1 - (0.5T/Q)]5 = [1 - (0.5 2/10)]5 = 0.59
k = D/B = 2/3
ζqd =1+2t a n φ’ (1 - sin φ’)2 k=1+2 0.577 (1 - 0.5)2 2/3
= 1.192
ζq = 1.289 0.59 1.192 = 0.907
(c) Total ultimate bearing capacity from Equation 4-1 is
qu = 0.5 B γ’H Nγ ζγ + σ’D Nq ζq
= 0.5 3.00 0.08 15.07 0.376 + 0.24 18.40 0.907
= 0.68 + 4.01 = 4.69 ksf
(4) Vesic Method. For φ’ = 30 deg, Nq = 18.40, Nγ = 22.40, and Nφ = 3.00
from Table 4-4. N c is not needed. From Table 4-6,
(a) Wedge correction factor ζγ = ζγs ζγi ζγd ζγβ ζγδ where ζγβ = ζγδ
= 1.00
ζγs =1-0 . 4B / W=1-0 . 43 / 6= 0.80
RBW = B/W = 3/6 = 0.5
m =( 2+R BW)/(1 + RBW) = (2 + 0.5)/(1 + 0.5) = 1.67
ζγi = [(1 - (T/Q)]m+1 = [1 - (2/10)]1.67+1 = 0.551
ζγ = 0.80 0.551 1.00 = 0.441
(b) Surcharge correction factor ζq = ζqs ζqi ζqd ζqβ ζqδ where ζqβ =
ζqδ = 1.00
ζqs = 1 + (B/W) tan φ = 1 + 3/6 0.577 = 1.289
ζqi = [1 - (T/Q)]m = [1 - (2/10)]m = 0.689
ζqd =1+2t a n φ’ (1 - sinφ’)2 k = 1 + 2 0.577 (1 - 0.5) 2/3
= 1.192
ζq = 1.289 0.689 1.192 = 1.058
(c) Total ultimate bearing capacity from Equation 3-1a is
qu = 0.5 B γ’H Nγ ζγ + σ’D Nq ζq
= 0.5 3.00 0.08 22.40 0.441 + 0.24 18.40 1.058
= 1.19 + 4.67 = 5.86 ksf
(5) Program CBEAR. Zero elevation for this problem is defined 3 ft below the
foundation base. Input to this program is as follows (refer to Figure 1-6):
(a) Foundation coordinates: x 1 = 10.00, y1 = 3.00
x2 = 13.00, y2 = 3.00
Length of footing: = 6.00
