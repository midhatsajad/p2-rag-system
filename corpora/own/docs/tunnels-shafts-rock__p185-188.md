# CECW-EG (pages 185-188)

4.8
3X.—
2
4.6
d 4.4
4.2
4.0
t
I f
z.
\
*
— _
~ — —
— . . . — . — -
f-l
/ ‘ / - 1
c
o
45678910111213 1415161718192
Note: At c- 2, t. 180* It-a . 360” jand + ond Y’~-
Y.f2
0.4
0.3
+ Y = 0.225
o.2n_o ,75
v-”dJ=l.73
Figure 9-7. Amstutz coefficients ss functions of “E”
where A/r = gap ratio, for gap between steel and concrete
et = one-half the angle subtended to the center of the r = tunnel liner internal radius, in.
cylindrical shell by the buckled lobe
q = yield stress of liner, psi
~ = one-half the angle subtended by the new mean
radius through the half waves of the buckled lobe f = liner plate thickness, in.
P = titid external buckling pressure, psi
0/t
70 90 !10 130 150 I 70 190 210 230 250 27o
Olt
Figure 9-8. Curves based on Amstutz equations by E. T. Moore
E* = modified modulus of elasticity, E/(l-v,)
v = Poisson’s Ratio for steel
Curves based on Jacobsen’s equations for the two different
steel types are shown on Figure 9-9.
(3) Vaughan’s analysis. Vaughan’s mathematical
equation for determination of the critical external buckling
pressure is based on work by Bryan and the theory of
elastic stability of thin shells by Timoshenko (1936). The
failure of the liner due to buckling is not based on the
assumption of a single lobe; instead, it is based on distortion of the liner represented by a number of waves as
shown in Figure 9-10.
[oy~~cr+a’+:llx@27)
OY= yield stress of liner, psi
OCr= critical slress
Ex = E/(1-V’)
Y. = gap between steel and concrete
R = tunnel liner radius
T = plate thickness
Box 9-6 is a MathCad example of the application of
Vaughan’s analysis. Vaugh,an provides a family of curves
(Figure 9-11) for estimating approximate critical pressures.
These curves are for steel with CJY= 40,000 psi with v,arious values of y(/R. It is noted that approximate pressure
values obtained from these curves do not include a s,afety
factor.
R2 R Oy - (JC,—+ o
7-T 240C, =
where
Box 9-4. MathCad Application of Amstutz’s Equations
Linerthicknesst = 0.50 in. ASTM A516-70
r = 0.50 F: = 0.50 r: = 90 k: = 0.027 k_ = 3.10-4
r
E: = 30.106 of: = 38. ld v: = 0.30
;
= 0.25
2“+
= 360
30.106
m=
3.297.107 Em: = 3.297.107 _ = 0.144 i: = 0.17 r = 529.412
& 7
- ~ . Em = -9.891 0 ld ISv: = -9.891 .103
1.5-0.5.
[[ 1!1 = 1.425 p: = 1.425
1 +0.002. &
OF
P “°F = 6,092 . 104
m
N: = 6.092.104
ON: = 12.103
~=d[::::~)[(+)Er-[1-0225+”[w)1173+~Ja = 1.294 . 104
t: = 0.50 F = 0.50 r=90 ON: = 1.294 . 104 i: = 0.17 Em: = 3.297.107 am: = 6.092.104
(:)””N”[l -0175”(+9”[=)1’652wExternalpressures:
Criticalbuckfingpressure= 85 psi
Allow.sblebucklingpressure=43 psi (Safety Fecior= 1.5)
d. Design examples. There is no one single proce- allowable buckling pressures. Most of the steel liner buckdure recommended for analysis of steel liners subjected to
external buckling pressures. Available analyses based on
various theories produce different result3. The results
depend, in particdar, on basic assumptions used in derivation of the formulas. It is the responsibility of the designer
to reeognize the limitations of the various design procedures. Use of more than one procedure is recommended to
compare and verify final results and to define safe
ling problems can best be solved with MathCad computer
applications. Table 9-2 shows the results of MathCad
applications in defining allowable buckling pressures for a
90-in. radius (ASTM A 516-70) steel liner with varying
plate thicknesses: 12, 5/8, 3/4, 7/8, and 1.0 in. Amstutz’s
and Jacobsen’s analyses are based on the assumption of a
single-lobe buckling failure. Vaughan’s analysis is based
on multiple-waves failure that produces much higher
Box 9-5. MathCad Application of Jacobsen’s Equations
Liner thickness t = 0.50 in. ASTM A 516-70
t : = 0.50 r: =90 A : = 0.027 A. 3 . ~r3-4
7
E:=3O.1O6 Oy:= 38.103 v : = 0.30
30.106
m=
3.297.107 Em : = 3.296.107
Guesses a : = 0.35 p : = 0.30 p: =40
Given
[)0.409
minerr(a, &p) = 0.37
51.321
External pressures:
Critical buckfing pressure = 51 psi
Allowable buckling pressure =34 psi (Safety Factor = 1.5)
Table 9-2
therefore, use of the Amstutz’s and Jacobsen’s equations to
Allowable Buckfing Pressures for a 80-in.diam. Steef Liner determine allowable buckling pressures is recommended.
Without Stiffenere-
Plat Thicknesses, in., ASTM A51 6-70 e. Design of steel liners with stl~eners.
Analyses/ Safety
Formulas Factor 1/2 518 314 718 1.0
Allowable Buckling Pressures, psi
Amstutz 1.5 65 82 119 160 205
Jacobsen 1.5 51 65 116 153 173
Vaughan 1.5 97 135 175 217 260
allowable buckling pressures. Based on experience, most
of the buckling failures invoive formation of a single lobe;
(1) Design considerations. Use of external circumferential stiffeners should be considered when the thickness
of an unstiffened liner designed for external pressure
exceeds the thickness of the liner required by the design
for internal pressure. Final design should be based on
economic considerations of the following three available
options that would satisfy the design ~quirements for the
external pressure (a) increasing the thickness of the liner,
(b) adding external stiffeners to the liner using the thickness required for internal pressure, and (c) increasing the
