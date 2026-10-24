# CECW-EG (pages 193-196)

0.020
0.015
0
\
: 0.010
0.009
R 0.008
g ;::::
z 0.005
& 0.0045V) 0.0040
g 0.0035
~ 0.0030
~ O.0025
0.0020
0.00[5
N 0.JFl-lnlDmo Inolrloooo 00
o“
. . . . .
660”0”
. .
60”&&:—N NmTm”m” COO—
LENGTH/01 At4ETER {L/Dl
0.020
0.015 -
0\
0.010 =
0.009 e
0.008 W
0.007 h
0.006 ~
0.005 z
0.0045>
0.00400
0.0035%
0.00305
0.0025~
0.0020
0.0015
Figure 9-13. Estimation ofn(Winderburg and Trilling)
r
<
1ii’
rl~~) = [(97c2/4~2) - 1] [n -u +~(sina/sin~)2]
,12(sina/sin~)3 [cx - (nA/r) - ~(sina/sin~) [1 +tan’(a - ~)/4]]
(9-33)
@/EF) = [(9n’/4p’) - 1] (9-34)
(r3 sin3 a)/[ (l/F) {~]
()op.! 1- sin P
[
pr sin al+ 8ahrsinatan (a-~)-+
1 (9-35)
r sm a EF sin B n sin P 12J/F
where F = cross-sectional area of the stiffener and the pipe
shell between the stiffeners
a = one-half the angle subtended to the center of the
cylindrical shell by the buckled lobe h = distance from neutral axis of stiffener to the
P = one-half the angle subtended by the new man
outer edge of the stiffener
radius through the half waves of the buckled lobe r = radius to neutral axis of the stiffener
P = critical external buckling pressure cr = yield stress of the liner/stiffener
J = moment of inertia of the stiffener and
contributing width of the shell
E = modulus of elasticity of liner/stiffener MathCad application. MathCad application does not
require a prior estimate of number of waves n in the cir-
Afr = gap ratio, i.e., gap/liner radius cumference of the steal liner at collapse. Instead, a range
of n values is defined at the beginning of either equation
Box 9-7 shows a MathCad application of Jacobsen’s and, as a result, MathCad produces a range of values for
equation. critical pressures corresponding to the assumed n values.
Critical pressures versus number of waves are plotted in
(7) Examples. Von Mises’s and Donnell’s equations graphic form. The lowest buckling pressure for each equafor rotary-symmetric buckling can best be solved by tion is readily determined from the table produced by
Box 9-7. Liner with Stiffeners-Jacobsen Equations
Liner thickness t = 0.500 in.
Stiffeners: 7/6” x 6“ @ 46 in. on centers
r: =90 J : = 44.62 F := 29.25 E: =30.106
A : = 0.027 A= 3 . 10-4 h : = 4,69i OY: =38.103
Guesses a:=l.8 ~: =1.8 p: =125
Given
. 1
[[.~]-1][~-(a)+(,)(%~]
Jfi= ,2.(*-? (a) -(1#) -(~)(*) ,+ tan@);(P)))2
._]
[A)lw= [[fi~;3’1
m: “ % “ ‘in(b)’
h.
r
12. J
2= : “(’ -=)+ :.;’;sin(a) “f + j= Jn- ]
8. (~) ~ h . r. sin(a) tan((a) - (~))
m
R. “ . sin((3)
‘“ T“ % ‘S’n(fi)
P< 130
[)
1.8
minerr(ix, p, p) = 1.8
126.027
External pressures:
‘cr. (critical buckling pressure) = 126 psi
Jail. (allowable buckling pressure) = 84 psi
MathCad computations. Design examples for determination of critical buckling pressures are included in
Boxes 9-8, 9-9, and 9-10. Number of waves in the complete circumference at the collapse of the liner can best be
determined with MathCad computer applications as shown
in Box 9-11. Table 9-3 below shows that allowable buckling pressures differ depending on the analyses used for
computations of such pressures. A designer must be
cognizant of such differences as well as the design
limitations of various procedures to determine safe allowable buckling pressures for a specific design. An adequate
safety factor must be used to obtain safe allowable pressures, depending on a specific analysis and the mode of
buckling failure assumed in the analysis.
f. Transitions between steel and concrete lining. In
partially steel-lined tunnels, the transition between the
steel-lined and the concrete-lined portions of the tunnel
requires special design features. Seepage rings iue usually
installed at or near the upstream end of the steel liner.
One or more seepage rings may be required. ASCE (1993)
recommends three rings for water pressures above 240 m
(800 ft) (see Figure 9-14). A thin liner shell may be provided at the transition, as shown on Figure 9-14 with studs,
hooked bars, U-bars, or spirals installed to prevent buckling. Alternatively, ring reinforcement designed for crack
control may be provided for a length of about twice the
tunnel diameter, reaching at least 900 mm (3 ft) in behind
the steel lining. Depending on the character of the rock
and the method of construction, a grout curtain may be
provided to minimize water flow from the concrete-lined to
the steel-lined section through the rock.
8. Bifurcations und other connections, Bifurcations,
manifolds, and other connections are generally designed in
accordance with the principles of aboveground penstocks,
ignoring the presence of concrete surrounding the steel
structure. The concrete may be assumed to transfer unbalanced thrust forces to competent rock but is not assumed
otherwise to help support internal pressures. Guidmce in
the design of these structures is found in EM 1110-2-2902,
Conduits, Culverts and Pipes, and EM 1110-2-3001. Steel
lining connections are usually straight symmetrical or asymmetrical wyes. Right-angle connections should be
avoided, as they have higher hydraulic resistance. These
connections require reinforcement to replace the tension
resistance of the full-circle steel circumference interrupted
by the cut in the pipe provided for the connection. The
reinforcement can take several forms depending on the
pressure in the pipe, the pipe size, and the pipe connection
geometry. This is expressed by (he pressure-di.arneter
value (PDV), defined as
PDV = pdz/(D sir? a)
where
(9-38)
p = design pressure, psi
d = branch difime(er, in.
D = main diameter. in.
rx = branch deflection angle
Depending on the PDV, the reinforcement should be
applied as a collar, il wrapper, or a crotch plate. Collars
and wrappers are used for smaller pipes where most tunnels would employ crotch plates. These usually take the
shape of external plates welded onto the connection
between the pipes. The selection of steel reinforcement is
made according to Table 9-4. The external steel plate
design depends on the geometry and relative pipe sizes.
One or more plates may be used, m shown in the examples
on Figure 9-15. Because space is limited around the steel
lining in a tunnel, it is often practical to replace the steel
reinforcement plale with an equivalent concrete
reinforcement. For a collar or wrapper, the reinforcement
plate should be equal in area 10 the steel area removed for
the connection, except thot for PDV between 4,000 lb/in.
and 6,000 lb/in., this area should be multiplied by PDV
times 0.00025.
Box 9-8. Liner with Stiffeners - Roark’s Forrnuia
Liner Thickness t = 112, 5/8, 314,718, and 1.99 in.
Siffenara: 7/6” x 6“ and larger for thicker finera @48 in. on centers
Design data:
RI = 90 in. - radius to the inside of the liner
t = 115, 5/6, 3/4, 718, and 1.00 in. - selected range of liner thicknesses
Es. 30,000,000 psi - modulus of elastiaty
v = 0.3- Poisson’s Ratio
L, = 48 in. - spacing of stiffeners
Pcr = “d(t)” - critical (collapsing) pressure for factor of safety F.S. = 1.0
t: = 0.50, 0.625..1.00
R1 :=90 L1 :=48 V= :=0.3 E~ :=30.106
“[[] 1
0.25
d(t) :=
0.807. .E~ . t2
LI “ R1 * “$
d(t)
H
112.081
195.796
306.86
454.076
634.028
External pressures:
- critical buckling pressure formula
o’ I I
0.5 0.6 0.7 0.8 0.9 1
IincI rbidcs.s“t”(i)
t (thickness), in. &LI?Q IWLi?Sl
F.S. = 1.5 F.S. = 2.0
1/2 112 75 66
5/6 196 131 98
3/4 309 206 154
718 454 303 227
1.0 634 423 317
