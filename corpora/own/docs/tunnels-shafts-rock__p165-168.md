# CECW-EG (pages 165-168)

boundary is placed at a distance 5-10 times the size of the
opening away from the centerline. Pore-pressure boundary
conditions along the edges of the model and along the
ground surface influence the predicted drawdown condition, pore-presswe buildup, and water inflow into the
opening.
d. Two- and three-dimensional analyses. The available numerical techniques can be used to solve a shaft or
tunnel excavation problem in two or three dimensions.
Twodimensional (2-D) analysis is appropriate for modeling tunnel sections along a running tunnel. Threedimensional (3-D) analysis can be useful for understanding
the behavior at tunnel and shaft intersections. However,
3-D analyses are laborious and involve the processing of
large amounts of data. It is recommended that the analyst
use a simplified 2-D model and arrive at a good understanding of the system response before commencing a full
blown 3-D analysis. Examples of 2-D and 3-D analyses
are given in Box 8-6 and Box 8-7.
e. Modeling of supports and construction sequence.
The constructionsequence of a tunnel/shaft is complicated
and involves many details. It is not practical to incorporate
all these details in the numerical simulation. Material
removal and liner and dowel installation should be simplified into discrete steps. The following are a few examples
of the possible simplifications:
(1) Tunnel support. Tunnel suppxt can be cast-inplace concrete, precast concrete segments, shotc@e, or
steel sets. The support can be modeled using the same
types of elements used to model the rock, but using material models and properties that correspond to the support
material. Since the thickness of the support is usually
much less than the size of the opening, structural (beam)
elements can be used to model the liner. In many situations, these elements are prefemd as they better capture
the bending behavior of the supports.
(2) Shotcrete application. There is usually a lag time
between the application of shotcrete and the development
of the full strength of the shotcrete. A simple approach to
incorporate this effect into the continuum model would be
to simulate shotcrete “installation” at the stage when the
shotcrete develops its full strength.
(3) Simulation of tran~er of load to tunnel liner in a
2-D analysis. During tunnel driving, support is installed
close to the tunnel face. As the face is advanced, the rock
relaxes further and load is applied to the supports. This
problem is three-dimensional in nature. In a 2-D model,
the rock is allowed to deform a percentage of its otherwise
free deformation prior to “installation” of the support. This
percentage ranges between 50 and 90 percent (Schwartz,
Azzouz, and Einstein 1980) depending on how far the
supports are installed behind the tunnel face. Section 8-2
discusses the development of deformations at the tunnel
face in the context of the convergence-confinement
method.
(4) Fully grouted dowel with bearing plate. The
principal function of this support element is to reinforce
the rock the bearing plate has a relatively minor role in
providing support for the overall system. In the numerical
model, the bearing plate can be ignored; only a fully
grouted dowel element needs to be represented.
(5) Simulation of bolts and lattice girders in 2-D
analysis. Bolts and lattice girders are usually installed in a
pattern in a tunnel/shaft section and at a specified spacing
along the length of the excavation. Therefore, bolts and
lattice girders are three-dimensional physical support components. In a 2-D analysis, the properties of bolts and
lattice girders are “smeared” along the length of the tunnel.
The properties of the bolts and lattice girders used in the
model are equal to those of the actual supports averaged by
the support spacing along the tunnellshaft length (i.e.,
equivalent properties per unit length of tunnel/shaft).
f. Analysis approach. Throughout the process of
constructing the model and performing the analyses, it is
important to keep the number of details and analyses to a
minimum. A well-defined set of parametric studies should
be prepared and adjusted as the results of the analyses are
examined. The analyst should maintain open communications with the design team. A common mistake is to
expect the analysis to provide a resolution or accumcy
higher than that of the input data.
8. Interpreting analysis results.
(1) Upon performing the first analysis, the analyst
should carefully examine the results. The first step is to
check whether the results are reasonable. Some of the
questions that should be answered are as follows:
Is the rock deforming as expected?
Is the load distribution in the support system consistent with rock deformations?
Is the change in the state of stress in the rock
consistent with the failure criteria and other material properties?
Box 8-6. Two-Dimenstional Analysis of Elliptical Tunnel Section
)biective: Study the influence of initial in situ lateral stress ratio, ~, on deformations and development of plastic zones around an ellipi2al tunnel section.
lock Medium: Saturated Taylor Marl Shale, effective mhesion c’ = 344 kPa and friction angle Phi’ = 30°, Effective stress behavior,
Jastic-perfectly plastic material with a Mohr-Coulomb failure criteria
;Upport Type: Unsupported and supported with fully grouted dowels and 10-cm shotcrete lining.
malysis Type: Finite Difference Analysis (FLAC Program, 2-D)
,
,. “.. -.-– ----
L
‘ “‘“”$(.//EE&2!E?&”:ElII
Iiw
,,,.../l\. \
t
,
I
,
!
1
I
,
,
,
(
(
II
m
~eformation and yielded zones, Deformation and yielded zones, Deformation and yielded zones,r
‘o =1 KO =1.5 KO=1.5
nalysis Results: The increase in ~ leads to an increase in the extent of the yielded zones in the crown and invert, Installation of
owels (longer dowels in the crown and invert compared with the springline) and the liner reduces the yielded zone.
Ieference: Hashash, Y. M.A., and Cook, R. F. (1994) “Effective Stress Analysis of Supercollider Tunnels, ” 8th Int. Conf. Assoc. Comp
lethods and Advances in Rock Mechanics, Morgantown, West Virginia.
Did the solution converge numerically? Parametric studies can be used to develop general design
charts that apply to more than one opening size or support
Answering these and similar questions might reveal an
error in the input data. A detailed check of the numerical
results is necessary for the first anafysis. A less rigorous
check is required for subsequent analyses, but nonetheless
the analyst should check for any possible anomalies in the
results.
(2) Evaluation of the results of the continuum analyses
and their implication regarding the rock-support interaction
includes examining the following:
(a) Deformations around the opening. Deformations
in the reek mass are related to the load transferred to the
support system. Data from numerical analyses can be used
to develop ground reaction curves (Section 8-2).
configuration,
(b) Loads in supporf system. The analyses can provide moment, thrust, and shear force distributions in the
liner. The data provided can be used to address possible
modification in the liner, such as the introduction of pin
connections to reduce excessive moments. Dowel load
data can also be used to revise the distribution and modify
the capacity of the proposed dowels. l%e analyses provide
information on the influence of the opening on adjacent
structures such as adjacent tunnels or surface buildings that
may be distressed due to tunnet/shaft construction. Excessive deformations indicate the need for a more effective
support system or a change in the construction method or
sequence to mitigate potentiat damage.
Box 8-7. Three-Dimensional Analysis of a Shaft and Tunnel Intersection
Q!XSQ!EStUCJYthe stress distribution at shaft inter=tion with tunneland anciW !@leries
Rock Medium: Eagle Ford Shale overlain by Austin Chalk. Total Stress behavior, linear elastic material
Support Type: No Support
Analysis Type: Finite Element Analysis (ABAQUS Program 3-D)
Analysis Results: Stress concentrations occur at tunnel/shaft intersections at zones experiencing a sudden change in geometry. The extent of the stress concentration is usad to estimate the required dowel length in these areas.
Reference: Clark, G. T., and Schmidt, B. (1994) “Analysis and Design of SSC Underground Structures,” Proceedings Boston
Society of Civil Engineers.
(c) Yielded and overstressed rock zones. These zones that provide the user with a wide range of output capabiliindicate a potential for reek spalling and rock falls if
located near the excavated surface. Large yielded zones
indicate a general weakening of the reek and the need to
provide reinforcement. The zones ean be used to size reek
reinforcements (bolts and dowels).
(d) Pore-pressure distribution and water inj70w. This
will provide information on the direction of potential water
flow, as well as the expected changes in pore pressures in
the rock. The information is relevant in reek masses with
discontinuities, as well as in swelling rocks. Contours of
pore-pressu~ distribution are useful in this regard. Many
of the commercially available codes have postprocessors
ties including tabulated data, contour plots, deformed mesh
plots, and color graphics. These am useful tools that can
convey the results of the analysis in a concise manner
especially to outside reviewers.
h. Mod#ication of support system, reanalysis. Continuum analyses provide insight into the behavior of the
overall support system and the adequacy of the support
system. The analyses may highlight some deficiencies or
possible overdesign in the proposed support system.
Several analysis iterations may be required to optimize the
design.
i. Lindtations of continuum analyses. Continuum
analysis techniques are versatile tools that provide much
understanding of problems involving underground structures. However, they have several limitations that have to
be considered to use these techniques effectively. Continuum analysis techniques are not a substitute for conventional design techniques and sound engineering judgement.
A continuum analysis cannot give warning of phenomena
such as localized spalling. Continuum analysis in geotechnical applications is vastly different from applications in
the structural field. Continuum analysis in structural
application is g-d to satisfy code requirements where
the parameters are well defined. Continuum analysis in
geotechnical and underground applications involves many
unknown factors and requires much judgement on the part
of the user. The complexity of a continuum analysis is
often limited by the availability of geomechanics data and
rock properties. The designer should avoid making too
many assumptions regarding the material properties in a
model while still expecting to obtain useful information
from the analysis. Continuum analyses predict stresses,
strains, and displacements but generally do not tell anything about stability and safety factors. Some specialized
programs can provide predictions of stability (e.g, Sloan
1981).
j. Example applications. Boxes 8-7 and 8-8 illustrate
the use of continuum analyses for shaft and tunnel problems as applied to the Superconducting Super Collider
underground structures.
8-5. Discontinuum Analyses
Closed form solutions and continuum analyses of tunnel
and shaft problems in rock ignore weaknesses and flaws
that interrupt the continuity of the rock mass. The presence of weaknesses makes the rock a collection of tightly
fitted blocks. The rock, thus, exhibits a behavior different
from a continuous material. This section describes
approaches to analysis of openings in rock behaving as a
discontinuum.
a. Key block theory.
(1) The best known theory for discontinuous analysis
of rocks is the key block theory pioneered by Goodman
and Shi (1985). In a key block analysis, the object is to
find the critical blocks created by intersections of discontinuities in a rock mass excavated along defined surfaces.
The analysis can skip over many combinations of joints
and proceed directly to consider certain critical (key)
blocks. If these blocks are stabilized, no other blocks can
EM 1110-2-2901
30 May 97
fall into the opening. The principal assumptions are as
follows:
(a) All joint surfaces are planar. Linear vector analysis can therefore be used for the solution of the problem.
(b) Joint surfaces extend through the entire volume of
the rock mass. No discontinuities terminate within a block.
No new discontinuities can develop due to cracking.
(c) The intact blocks defined by the discontinuities
are rigid. Deformations are due to block movement but
not block deformation.
(d) The discontinuity and excavation surfaces are
defined. If the joint set orientations are actually dispersed
about a central tendency, one direction must be chosen to
represent the set.
(2) Figure 8-5 illustrates the concept of key block
analysis. Block analysis can be camied out using stereographic projection graphicaJ methods or vector methods.
Hatzor and Goodman (1993) illustrate the application of
the analysis to the Hanging Lake Tunnel, Glenwood Canyon, Colorado. The analysis methods have been incorporated into computer progr,ams.
b. Discrete element methods.
1 I
Figure 8-5. Key block analysis
