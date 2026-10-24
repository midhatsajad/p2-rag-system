# CECW-EG (pages 5-8)

Subject Paragraph Page
APPENDIX D ELASTIC PARAMETERS
General ................ D - 1 D - 1
Elastic Young’s Modulus ........ D - 2 D - 1
Shear Modulus ............. D - 3 D-12
Poisson’s Ratio ............ D - 4 D-12
APPENDIX E LABORATORY CONSOLIDOMETER TESTS
General ................ E - 1 E - 1
Step Load Test (SL) .......... E - 2 E - 1
Rapid Load Test (RL) .......... E - 3 E - 2
Constant Rate of Deformation Test
(CRD) ................ E - 4 E - 2
Controlled Gradient Test (CG) ..... E - 5 E - 4
APPENDIX F COMPUTER PROGRAM VDISPL
Background............... F - 1 F - 1
Organization.............. F - 2 F - 1
Example Problems ............ F - 3 F-10
Listing ................ F - 4 F-17
APPENDIX G NOTATION ................ G - 1
iii
CHAPTER 1
INTRODUCTION
1-1. Purpose and Scope . This manual presents guidelines for calculation of
vertical displacements and settlement of soil under shallow foundations (mats
and footings) supporting various types of structures and under embankments.
a. Causes of Soil Displacements . Soil is a nonhomogeneous porous material consisting of three phases: solids, fluid (normally water), and air.
Soil deformation may occur by change in stress, water content, soil mass, or
temperature. Vertical displacements and settlement caused by change in stress
and water content are described in this manual. Limitations of these movements required for different structures are described in Chapter 2.
(1) Elastic deformation. Elastic or immediate deformation caused by
static loads is usually small, and it occurs essentially at the same time
these loads are applied to the soil. Guidance for tests and analyses to estimate immediate settlements of foundations, embankments, pavements, and other
structures on cohesionless and cohesive soils for static loading conditions is
given in Sections I and II of Chapter 3.
(2) Consolidation. Time delayed consolidation is the reduction in volume associated with a reduction in water content, and it occurs in all soils.
Consolidation occurs quickly in coarse-grained soils such as sands and gravels, and it is usually not distinguishable from elastic deformation. Consolidation in fine-grained soils such as clays and organic materials can be significant and take considerable time to complete. Guidance for tests and analyses to estimate consolidation settlement of foundations, embankments, pavements, and other structures on cohesive soil for static loading conditions is
given in Section III of Chapter 3.
(3) Secondary compression and creep. Secondary compression and creep
are associated with the compression and distortion at constant water content
of compressible soils such as clays, silts, organic materials, and peat.
Guidance for tests and analyses to estimate secondary compression settlement
is given in Section IV of Chapter 3.
(4) Dynamic forces. Dynamic loads cause settlement from rearrangement
of particles, particularly in cohesionless soil, into more compact positions.
Guidance to estimate settlement for some dynamic loads is given in Chapter 4.
(5) Expansive soil. Expansive soil contains colloidal clay minerals
such as montmorillonite that experience heave and shrinkage with changes in
the soil water content. Guidance for calculation of soil movements in expansive soil is given in Section I of Chapter 5.
(6) Collapsible soil. Collapsible soil usually consists of cohesive
silty sands with a loose structure or large void ratio. The cohesion is usually caused by the chemical bonding of particles with soluble compounds such
as calcareous or ferrous salts. Collapse occurs when the bonds between particles are dissolved. Guidance for calculation of settlement in collapsible
soil is given in Section II of Chapter 5.
b. Coping with Soil Movements . Soil movements may be minimized by
treating the soil prior to construction by numerous methods such as removal of
poor soil and replace with suitable soil, precompression of soft soil, dynamic
consolidation of cohesionless soil, and chemical stabilization or wetting of
expansive or collapsible soil. Foundations may be designed to tolerate some
differential movements. Remedial techniques such as underpinning with piles,
grouting, and slabjacking are available to stabilize and repair damaged foundations. Methodology for minimizing and coping with settlement is given in
Chapter 6.
c. Limitations of the Manual . This manual excludes settlement caused
by subsidence and undermining by tunnels, subsidence due to buried karst features or cavities, thermal effects of structures on permafrost, effects of
frost heave, loss in mass from erosion, loss of ground from rebound and lateral movement in adjacent excavations, and loss of support caused by lateral
soil movement from landslides, downhill creep, and shifting retaining walls.
(1) Horizontal deformation. Horizontal deformation of structures associated with vertical deformations may also occur, but such analysis is complex
and beyond the scope of this manual.
(2) Deep foundations. Deep foundations are driven piles and drilled
shafts used to transmit foundation loads to deeper strata capable of supporting the applied loads. Guidelines on settlement analysis of deep foundations
is given in TM 5-809-7, "Design of Deep Foundations (Except Hydraulic Structures)".
(3) Landfills. Settlement of domestic and hazardous landfills are unpredictable and cannot be readily estimated using techniques presented in this
manual.
1-2. Applicability . This manual applies to all Corps of Engineers field
operating activities. Applications include, but are not limited to, design
analysis of alternatives for new construction, analyses for rationalizing inservice performance, forensic investigations, and damage assessments and
repair/rehabilitation design.
1-3. References . Standard references pertaining to this manual are listed in
Appendix A, References. Each reference is identified in the text by the
designated Government publication number or performing agency. Additional
reading materials are listed in the Bibliography and are indicated throughout
the manual by numbers (item 1, 2, etc.) that correspond to similarly numbered
items in Appendix B.
1-4. Rescission . This manual supersedes EM 1110-2-1904, "Settlement Analysis", Chapter 4, dated January 1953.
1-5. General Considerations and Definitions . Placement of an embankment load
or structure on the surface of a soil mass introduces stress in the soil that
causes the soil to deform and leads to settlement of the structure. It is
frequently necessary to estimate the differential and total vertical soil
deformation caused by the applied loads. Differential movement affects the
structural integrity and performance of the structure. Total deformation is
significant relative to connections of utility lines to buildings, grade and
drainage from structures, minimum height specifications of dams (i.e., freeboard), and railroad and highway embankments. Soils and conditions described
in Table 1-1 require special considerations to achieve satisfactory design and
performance. Early recognition of these problems is essential to allow sufficient time for an adequate field investigation and preparation of an appropriate design.
a. Preconsolidation Stress . The preconsolidation stress or maximum effective past pressure σ’p experienced by a foundation soil is a principle
factor in determining the magnitude of settlement of a structure supported by
the soil. σ’p is the maximum effective stress to which the in situ soil has
been consolidated by a previous loading; it is the boundary between recompression and virgin consolidation, which are described in Section III, Chapter 3.
Pressures applied to the foundation soil that exceed the maximum past pressure
experienced by the soil may cause substantial settlement. Structures should
be designed, if practical, with loads that maintain soil pressures less than
the maximum past pressure.
(1) Geological evidence of a preconsolidation stress. Stresses are induced in the soil mass by past history such as surcharge loads from soil later
eroded away by natural causes, lowering of the groundwater table and desiccation by drying from the surface.
(a) Temporary groundwater levels and lakes may have existed causing
loads and overconsolidation compared with existing effective stresses.
(b) Desiccation of surface soil, particularly cyclic desiccation due to
repeated wetting and drying, creates significant microscale stresses which in
turn cause significant preconsolidation effects. Such effects include low
void ratios as well as fissures and fractures, high density, high strength and
high maximum past pressures measured in consolidation tests.
(c) A high preconsolidation stress may be anticipated if
where N is the blowcount from standard penetration test (SPT) results and
σoz (tons/square foot or tsf) is the total overburden pressure at depth z
(Table 3-2, TM 5-818-1).
(2) Evaluation from maximum past thickness. Local geologic records and
publications when available should be reviewed to estimate the maximum past
thickness of geologic formations from erosion events, when and amount of material removed, glacial loads, and crustal tilt.
(a) The minimum local depth can sometimes be determined from transvalley geologic profiles if carried sufficiently into abutment areas to be beyond the influence of valley erosion effects.
(b) The maximum past pressure at a point in an in situ soil is estimated by multiplying the unit wet soil weight (approximately 0.06 tsf) by the
total estimated past thickness of the overlying soil at that point.
(c) Results of the cone penetration test (CPT) may be used to evaluate
the thickness of overburden soil removed by erosion if the cone tip resistance
qc increases linearly with depth (refer to Figure 7 in item 56). The line of
qc versus depth is extrapolated back above the existing surface of the soil
