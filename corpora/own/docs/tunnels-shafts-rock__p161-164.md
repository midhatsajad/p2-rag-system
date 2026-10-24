# CECW-EG (pages 161-164)

calculated from elasto-plastic analyses. The simplest case
is that of a circular tunnel driven in a homogeneous, isotropic, initially elastic rock subject to a hydrostatic stress
field. lhe analysis is axisymmetric. The solution assumes
plane strain conditions in the axial direction and that the
axial stress remains the principal intermediate stress. As
the stresses induced by the opening exceed the yield
strength of the rock, a yield zone of radius R, develops
about the tunnel while the rock outside the yield zone
remains elastic. The analysis is illustrated in Boxes 8-2
through 8-5. The rock tends to expand or dilate as it
breaks, and displacements of the tunnel wall will be greater
than those predicted by elasticity theory. Support requirements are theoretically related to the displacement of the (c-$).
excavation. Deformations are limited by applying a high
support pressure, whereas, support pressures are reduced as
deformations take place. These theoretical provisions must
be tempered with judgment since excessive deformation
can adversely affect stability and lead to incnm.sed support
requirements that are not predicted by the analyses. The
elastoplastic solutions for stress distributions and
deformations around circular-cylindrical underground openings are summarized in Boxes 8-2, 8-3, and 8-4. It is
assumed that the opening is far enough removed from the
ground surface that the stress field may be assumed homogeneous and that a lithostatic stress field exists. Body
forces are not considered. The assumption is made that the
material is either plastic frictionless ($ = O) or frictional
Box 8-2. Elasto Plastic Solution
Reference: Salencon 1969.
P, =0” =0” p, = Internal Pressure
yield condition: pZ~ (pi + c cos $) / l-sin $
radius of yield zone:
R = a.[(1- sin I$)(pZ + c. cot 1$)/(pl + c cot $)] “(b’)
where 1$= (1 + sin $) / (1 - sin $)
EIASTIC ZONE:
stresses: q = p, - (p, - o-) (R#)2
C%= P, + (P, - ~~)(RJr)2
CJw= p, (1 - sin 1$1)- C.COS $ = Radial stress at the Elasto-Plastic interface
deformations: u,= (p, sin $ +C.COS$).(R 2/r) /(2G)
PIASTIC ZONE:
stresses: q = -c.cot 1$1+ (pi + c,cot @).(r/a)b’
rs~= -c. cot o + (pi + c.cot $). KP(r/a)*’
oY = (IS,+aO)/2 = c.cot~+(pi+c. cot $).(1 -sim$) “’.(r/a)m’
deformations: u, = r/(2 G). x
where x = (2v-1).(pZ+c, cot 1$)+ (l-v ).[(KP2-1) (1$+ &)] (p, + c.mt $). (R/a) (@’).(R/r~W+’)
+ [ (1 ‘v ).(~. ~+l)/(&+ &)-v]. (p, + c.cot $).(r/a)(W’)
and & = (1 + sin w,) /(1 - sin vs) and G = E/2(l+v)
Box 8-3. Elasto Plastic Particular Solutions
Particular Solutions to Elastoplastic Problem - c-$ Material - Dilation Angle stresses in the elastic and plastic zones are the
same as given in Sox 8-2.
CASE 1: Y = $, Associated flow rule, KP = KP~
deformations: u, = r/(2 G). ~
where ~ = (2v-1).(pZ+c.cot $) + (1-v).(K 2-1)/(2.~) (~ + c.mt $). (lWa). (* ’).(R/r)(@’)
+ [(1 -v).(~2+1 )/(2$J -v] . (p~+ c.cot $).(r/a)(*’)
CASE 2: Y = O, No dilation, KP = 1
deformations: u,= r/(2 G). ~
where ~ = (2v-1).(pZ+c.cot $) + (l-v).(KP -l).(pi + c.cot $). (R/a) .( Kp_’).(R/r)2 + (1-2.v) .(R + c.c.ot $). (r/a) .(KP’)
Particular Solutions to Elastoplastic Problem - c-$ Material
CASE 3: 1$= $, and c = O , Friti”onal Material
PLASTIC ZONE:
stresses: or s q.(r/a)@’
Ce = q.l$.(r/a)@-’
~Y = (~r + @/2 = pi.[(1 +Kp)/2].(r/a)@-’
deformations: Ur = r/(2 G). z
for yr= $
z = (2v-1).pZ+(l-v) .(KP2-l )/2.1$ .pi.(FUa).(~l). (FUr)(K~’) + [(1-v).(KP2+l)/(2. KP)-v].pi. (r/a)(K~’)
foryr= O
L = (2v-1).pZ + (l-v).(KP -l).pi. (FUa).(*1).(FUr)2 + (1-2.v).pi.(r/a) .(K~’)
8-4. Continuum Analyses Using Finite 1983). While thereare subtle advantages of one method
Difference, Finite Element, or -
Boundary Element Methods
Advances in continuum analysis techniques and the advent
of fast low-cost computers have led to the proliferation of
continuum analysis programs aimed at the solution of a
wide range of geomechanieal problems including tunnel
and shaft excavation and constmction. For the purpose of
this manual, continuum analyses refer to those methods or
techniques that assume the reek medium to be a continuum
and require the solution of a large set of simultaneous
equations to calculate the states of stress and strain
throughout the rock medium. The available techniques
include the Finite Difference Method (FDM) (Cundall
1976), the Finite Element Method (FEM) (Bathe 1982),
and the Boundary Element Method (BEM) (Venturini
over another for some specialized applications, the three
methods are equally useful for solving problems encountered in practice. Each of the three numerical techniques is
used to solve an excavation problem in a rock medium
whereby the field of interest is discretized and represented
by a variety of elements. The changes in stress state and
deformations are calculated at the element level given the
(unloading (construction) history and material properties.
These numerical techniques provide the designer with
powerful tools that can give unique insights into the tunnel/
shaft support interaction problem during and after construction. Box 8-5 summarizes the steps followed in performing a continuum analysis. The following paragraphs
deseribe these steps and how to consider continuum analyses as part of the design process. Advantages as well as
the limitations of the numericat techniques are described.
Box 8-4. Elasto Plastic Particular Solution
Particular Solutions to Elastopiastic Problem
CASE4: l$l=o, c=c
yield condition: pz ~ ~ + c
radius of yield zone: R = a . exp [ (pz-pi)/(2.c) - 1/2 ]
PLASTIC ZONE:
stresses: 13r= ~ + 2.c. In(r/a)
00 = ~ + 2.c.(1 + In(r/a))
Cy = (or + 6.)/2 = ~ + c.(1 + 2.ln(r/a))
ELASTIC ZONE:
stresses: Ur = pz - c.(tir)2 . exp [(pz - Pi)fc -1]
ISO = pz - c.(a/r)2 . exp [(pZ - p#c -1]
lsy = 2.v.pz
deformations:
u= = c (1 +v).[1 - c (1 +v)/2.E ]. exp [(pZ-pi)/c -1] ~ [c(1 +v)/E] exP [(pz-@/c -1]
Box 8-5. Steps to Follow in Continuum Analysis of Tunnel and Shaft Excavations
1. Identify the need for and purpose of continuum analysis.
2. Define computer coda requirements.
3. Modeling of the rock medium.
4. Two- and three-dimensional analyses.
5. Modeling of ground support and construction sequence.
6. Analysis approach.
7. Interpretation of analysis results,
8. Modification of support design and construction sequence, reanalysis.
a. Identlfi the need for and purpose of continuum transfer into supports. Safety factors and load factors
analysis. The fiist step in carrying out a continuum commonly used in conventional methods should not be
analysis is identifying whether an ~al~sis is needed. The used in numerical analyses. Continuum analyses can incor-
FEM, FDM, or BEM numerical techniques are not substi- porate details that cannot be accounted for using conventutes for conventional methods of support design. The tional methods such as inhomogeneous rock strata and
support system of a tunnel or shaft opening should fwst be nonuniform initial in situ stress, and hence provide guidseleetedusing methods deiwibed in Chapters7 and 9, The ante for modifications required in the support system, The
continuum analysis is then used to study the influence of continuum methods can best serve to improve support
the construction sequence and ground deformation on load design through the opportunity they provide to study types
of situations from which general practical procedures can
be developed (e.g., Hocking 1978). Modes of behavior
that can be assessed using continuum anatysis include the
following:
(1) Elastic and elasto-plastic ground/support interaction. Convergence-confinement curves can be constructed
using continuum analysis.
(2) Study of modes of failure.
(3) Identification of stress concentrations.
(4) Assessment of plastic zones requiring support.
(5) Analysis of monitoring data.
b. Define computer code requirements. A wide range
of commercial and in-house programs are available for
modeling tunnel and shaft construction. Prior to performing an analysis using a particular computer code, the user
should determine the suitability of the program. Example
analyses of problems for which a closed form solution is
available (such as those given in Section 8-3) should be
performed and the analysis results checked against those
solutions. The user should verify that the program is capable of modeling the excavation process correctty and is
able to represent the various support elements such as
concrete and shotcrete lining, lattice girders, and bolts.
c. Modeling of the rock medium.
(1) The FEM, FDM, and BEM techniques model the
rock mass as a continuum. This approximation is adequate
when the rock mass is relatively free of discontinuities.
However, these methods can still be used to model jointed
rock masses by using equivalent material properties that
reflect the strength reduction due to jointing (e.g., Zhu and
Wang 1993; Pariseau 1993) or a material model that incorporates planes of weakness such as the Ubiquitous Joint
Model (ITASCA 1992). Interface elements may be used to
model displacements afong discontinuities if they are
deemed to be an important factor in the behavior of the
system. The designer should first use as simple a model as
possible and avoid adding details that may have littfe effect
on the behavior of the overall system.
(2) The initial state of stress in the rock mass is
important in determining the deformation due to excavation
and the subsequent load carried by the support system. In
a cross-anisotropic rock mass (in a horizontal topography)
where materiaf properties are constant in a horizontal
plane, the state of stress can be described by a vertical
stress component rsv due to the weight of rock and a horizonM stress component Oh = Koov. ~ is the lateral in situ
stress ratio. In situations where the reck mass is anisotropic, has nonhorizontd strata, or where the ground surface is inclined (e.g., sloping ground), methods such as
those proposed by Amadei and Pan (1992) ,and Pan and
Amadei (1993) should be used to establish the initial state
of stress in the rock. Such methods are necessary because
the initial stresses in the rock mass include nonzero shear
stress components.
(3) The choice of a materiaf model to represent the
rock medium depends on the available properties obtained
from laboratory and in situ testing programs and the
required accuracy in the anatysis. Many of the available
continuum analysis programs have a large materiat model
library that can be used. These include linear elastic and
nonlinear elasto-plastic models and may have provisions to
incorporate creep and thermal behavior. Available
materiaf/constitutive laws for modeling of the rock medium
include the following:
Linear Elastic.
Non-Linear Elastic (Hyperbolic Model).
Visco-Elastic.
Elastic-plastic (Mohr-Coulomb failure criteria
with an associated or nonassociated flow rule that
controls material dilatancy, Hock and Brown
failure criteria).
Elastic-viscoplastic.
Bounding Surface Plasticity (Whittle 1987).
(4) The continuum analysis can be performed assuming either an effective stress or a total stress material
behavior. Using effective stress behavior may be more
appropriate for use in saturated rock masses and those of
sedimentary origin such as shales or sandstones. There is
sufficient evidence in the literature that would support the
use of the effective stress law for some rocks (e.g.,
Warpinski and Teufel 1993; Berge, W,ang, and Bonner
1993; Bellwald 1992). Examples of effective stress analysis of tunnels can be found in Cheng, Abousleim.an, and
Roegiers (1993).
(5) The size of the rock field (mesh size) and boundary conditions applied afong the far-field edges of the
model depend on the size of the opening and the hydrologic conditions. As a rule of thumb. the far-field
