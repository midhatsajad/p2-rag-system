# CECW-EG (pages 177-180)

Box 9-1. General Recommendations for Loads and Distortions
1. Minimum loading for bending: Vertical load uniformly distributed over the tunnel width, equal to a height of rock 0.3 times the
height of the tunnel.
2. Shatter zone previously stabilized: Vertical, uniform load equal to 0.6 times the tunnel height,
3. Squeezing rock: Use pressure of 1.0 to 2.0 times tunnel height, depending on how much displacement and pressure relief is
permitted before placement of concrete. Alternatively, use estimate based on elastoplastic analysis, with plastic radius no wider
than one tunnel diameter.
4. For cases 1, 2, and 3, use side pressures equal to one-half the vertical pressures, or as determined from analysis with selected
horizontal modulus. For excavation by explosives, increase values by 30 percent.
5. Swelling rock, saturated in situ: Use same as 3 above.
6. Swelling rock, unsaturated or with anhydrite, with free access to water: Use swell pressures estimated from swell tests.
7. Noncircular tunnel (horseshoe): Increase vertical loads by 50 percent,
8. Nonuniform grouting load, or loads due to void behind lining: Use maximum permitted grout pressure over area equal to onequarter the tunnel diameter, maximum 1.5 m (5 ft).
Free-standing ring subject to vertical and honzontai loads (no ground interaction).
Continuum mechanics, closed solutions.
Loaded ring supported by springs simulating
ground interaction (many structural engineering
codes).
. Continuum mechanics, numerical solutions.
The designer must select the method which best
approximates the character and complexity of the conditions and the tunnel shape and size.
(1) Continuum mechanics, closed solutions. Moments
developed in a lining are dependent on the stiffness of the
lining relative to that of the rock. The relationship
between relative stiffness and moment can be studied using
the ciosed solution for elastic interaction between rock and
lining. The equations for this solution are shown in
Box 9-2, which also shows the basic assumptions for the
solution. These assumptions are hardly ever met in real
life except when a lining is installed immediately behind
the advancing face of a tunnel or shaft, before elastic
stresses have reached a state of plane strain equilibrium.
Nonetheless, the solution is useful for examining the
effects of variations in important parameters. It is noted
that the maximum moment is controlled by the flexibility
ratio
ct = E,R 3/(Ec)I (9-14)
For a large value of u (large rock mass modulus), the
moment becomes very small. Conversely, for a small
value (relatively rigid lining), the moment is large. If the
rock mass modulus is set equal to zero, the rock does not
restrain the movement of the lining, and the maximum
moment is
M = 0.250,(1 - KO)R2 (9-15)
With KO = 1 (horizontal and vertical loads equal), the
moment is zero; with KO= O (corresponding to pure vertical loading of an unsupported ring), the largest moment is
obtained. A few examples wiil show the effect of the
flexibility ratio. Assume a concrete modulus of 3,600,000
psi, lining thickness 12 in. (I = 123/12), rock mass modulus
500,000 psi (modulus of a reasonably competent limestone), v, = 0.25, and tunnel radius of 72 in.; then ct =
360. and the maximum moment
M = 0.0081 X CV(l - KJR2 (9-16)
This is a very small moment. Now consider a relatively
rigid lining in a soft material: Radius 36 in., thickness
9 in., and rock mass modulus 50,000 psi (a soft shale or
crushed rock); then Ihe maximum moment is
Ground
/
Conaele Llnlng
Box 9-2. Lining in Elastic Ground, Continuum Model
Assumptions: + 0“
Plane strain, elastic radial lining pressures are equal to in situ
stresses, or a proportion thereof
Includes tangetial bond between lining and ground
Lining distortion and ocmpression resisted/relieved by ground
reactions &av
Maximum/minimum bending movement
M = *OV (1 - Ko) f?2/(4 +
3 - 2V, E, R’
3 (1 + v, (1 + v, ~
Maximum/minimum hoop force
rv=o”(l +Ko)R/(2+(1-Ko)
2(1 - VJ 4v, f, R3
‘m) + CTv(1- KO)R/(2 +
1 2VJ (1 +V)
m -
(3 - 4vJ (12(1 + v,) E,/ + E, R’)
Maximum/minimum radial displacement
;
= CT,(/ + KJ R3/(& E,fP + 2E4R2 + 2EJ) * a, (1 - Ko) /7’/(12 Ec/ + 3 - 2V,
E,R3)
r (1 + v, (3-4J v,
M = 0.068 x Ov(1 - K<JR2 (9-17) “ Irregular boundaries and shapes can be handled.
Incremental construction loads can be analyzed,
It is seen that even in this inst,ance, with a relatively rigid
lining in a soft rock, the moment is reduced to about
27 percent of the moment that would be obtained in an
unsupported ring. Thus, for most lining applications in
rock, bending moments are expected to be small.
(2) Analysis of moments and forces using finite elements computer programs. Moments and forces in circul.u
and noncircular tunnel linings can be determined using
structural finite-element computer programs. Such analyses
have the following advantages:
Variable properties can be given to rock as well as
lining elements.
including, for example, loads from backfill
grouting.
Two-pass lining interaction can also be analyzed.
In a finite elcmen[ analysis (FEM) analysis, the lining is
divided inlo beam elements. Hinges can be introduced to
simulate structural properties of the lining. Tangential and
radial springs are applied at each node to simulate elastic
interaction between the lining and the reek. The interface
between lining and rock cannot withstand tension;
therefore, interface elements may be used or the springs
deactivated when tensile stresses occur. The radial and
tangential spring stiffnesses, expressed in units of force/
displacement (subgrade reaction coefficient), are es[imated
from
k, = E, b e/(1 + v,)
k, = k, G/E, = 0.5 kj(l + v,)
(9-18)
(9-19)
where
k, and k, = radial and tangential spring stiffnesses,
respective y
G = shear modulus
t3= arc subtended by the beam element (radian)
b = length of tunnel element considered
If a segmental lining is considered, b can be taken as the
width of the segment ring. Loads can be applied to any
number of nodes, reflecting assumed vertical rock loads
acting over part or ,all of the tunnel width, grouting loads,
external loads from groundwater, asymmetric, singular rock
loads, internal loads, or any other loads. Loads can be
applied in stages, reflecting a sequence of construction.
Figure 9-3 shows the FEM model for a two-pass lining
system. The initial lining is ,an unbolted, segmental concrete lining, and the final lining is reinforced cast-in-place
concrete with an impervious waterproofing membrane.
Rigid links are used to interconnect the two linings at
alternate nodes. These links transfer only axial loads and
have no flexural stiffness and a minimum of axial deformation. Hinges are introduced at crown, invert, and springlines of the initial lining to represent the joints between the
segments.
(3) Continuum analysis, nunwrical solutions.
Continuum analyses (Section 8-4) provide the complete
stress state throughout the rock mass and the support structure. These stresses are used to calculate the (axial and
shear) forces and the bending moments in the components
of the support structure. The forces and moments ,are
provided as a direct output from the computer analyses
with no need for .an additionat calculation on the part of
the user. The forces and moments give the designer information on the working load to be applied to the structure
and can be used in the reinforced concrete design. Figure 9-4 shows a sample output of moment and force distribution in a lining of a circular tunnel under two different
excavation conditions.
(4) Design oj’ concrete cross section jbr bending and
normal jbrce. Once bending moment ,and ring thrust in a
lining have been determined, or a lining distortion estimated, based on rock-structure interaction, the lining must
be designed to achieve acceptable performance. Since the
lining is subjected to combined normal force and bending,
the analysis is conveniently ctarried out using the capacityinteraction curve, also called the moment-thrust diagram.
EM 1110-2-2104 should be used to design reinforced concrete linings. The interaction diagmm displays the envelope of acceptable combinations of bending moment and
axial force in ii reinforced or unreinforced concrete member. As shown in Figure 9-5, the allowable moment for
low values of thrust increases with the thrust because it
reduces the limiting tension across the member section.
The maximum allowable moment is reached at the
so-called balance point. For higher thrust, compressive
stresses reduce [he allowable moment. General equations
to calculate points of the interaction diagram tare shown in
EM 1110-2-2104. Each combination of cross-section area
and reinforcement results in a unique interaction diagram,
and families of curves can be generated for different levels
of reinforcement for a given cross section. The equations
are e,asily set up on a computer spreadsheet, or standard
structural computer codes can be used. A lining cross
section is deemed adequate if the combination of moment
and thrust VJIUCSare within the envelope defined by the
interaction diagram. The equations shown in EM 1110-2-
2104 are applicable to a tunnel lining of uniform cross
section wilh reinforcement at both interior and exterior
faces. Linings wi[h nonuniform cross sections, such as
coffered segmental linings, are analyzed using slightly
more complex equalions, such as those shown in standard
structural engineering handbooks, but based on the same
principles. Tunnel lining distortion stated as a relative
diameter change (AD/D) may be derived from computerized rock-structure analyses, from estimates of long-term
swelling effects, or may be a nominal distortion derived
from past experience. The effect of an msurned distortion
can be analyzed using the interaction diagram by converting the distortion to an equivalent bending moment in the
lining. For a uniform ring structure, the conversion formula is
M = (3.!31/It)(AD/D) (9-20)
In the event that the lining is not properly described as a
uniform ring structure, the representation of ring stiffness
in this equation (3.El/f?) should be modified. For example,
joints in a segmental lining introduce a reduction in the
moment of inertia of the ring that can be approximated by
the equation
9-1o
LEGEND: NOTE:
● NOOE TANGENTIAL SPRINGS
O ELEMENT
\ SPRING
NOT SHOWN FCR CLARITY.
SEE DETAIL 1.
e HINGE
BEAM-SPRING MCOEL
~ INITIAL PRECAST
G CONCRETELINING
\
%
RIGID LINK
TYP
F
~
-1
4 RADIAL SPRING
ZJ TYP-- .—
EFINAL CAST-IN-PLACE
CONCRETE LINING
TANGENTIAL
SPRING, TYP
DETAIL 1
(a) Undrained Excavation
>
i
i
I
’19Kips-irl/in I 11 Kips/in
Moment A&i Fome
Maximum Values
i 0.93 Kips/in
Shear Force
23 fiPS-ill/iIl
Moment
(b) Steady State
)1
I Ii ii i1i3 fipdin 0.70 Kips/in
Hal Force Shear Force
Moment, thrust and shear diaarams in liner
Figure 9-3. Descretization of a two-pass lining system
for analysis
Figure 9-4. Moments and forces in lining shown in
Figure 9-3
