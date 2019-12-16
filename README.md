# Video Augmentation for Video Lectures

# Project Details:
This project presents a video lecture augmentation system by linking its off-topic concepts with topically relevant lecture segments. Such lecture segments are retrieved to furnish basic understanding of the associated off-topic concepts. The proposed augmentation model comprises five modules: video lecture segmentation, concept extraction, off-topic identification, retrieval of relevant video segments and video segment re-ranking.
1. Video Lecture Segmentation: Video lectures are segregated by identifying the topical shifts using a word embedding-based technique.
2. Concept Extraction: The segmented video lectures are indexed using its concepts, extracted with an entity annotation service.
3. Off-Topic Identification: The task of predicting off-topic concepts is implemented as a community structure analysis problem on concept similarity graphs.
4. Retrieval of relevant video segments: For each off-topic concept, appropriate video segments are fetched.
5. Video Segment Re-ranking: These initially retrieved video segments are further re-ranked so that the top-ranked video segment offers the most basic understanding of the target off-topic concept.

# Data:
Transcript data for 2581 Lectures present in 68 Courses (39 and 19 related to Computer science and Mathematics domains, respectively)

# CSE Data
1. Advanced Graph Theory AGT
2. Artificial Intelligence AI
3. Biometrics	BIO
4. Computational Geometry CG
5. Compiler Design CD
6. Combinatorics COM
7. Computer Algorithms II	CAL
8. Computer Architecture	CAR
9. Computer Graphics	CGR
10. Computer Networks	CN
11. Computer Organization	CO
12. Cryptography and Network Security	CNS
13. Data Communication	DC
14. Design and Analysis of Algorithms	DAA
15. Database Design	DD
16. Discrete Mathematical Structures	DMS
17. Fundamental Algorithms:Design and Analysis	FAL
18. Graph Theory	GT
19. Internet Technology	IT
20. Introduction to Problem Solving and Programming	PSP
21. Logic for CS	LCS
22. Natural Language Processing	NLP
23. Numerical Optimization	NOP
24. Parallel Algorithm	PA
25. Parallel Computing	PC
26. Pattern Recognition	PR
27. Performance Evaluation of Computer Systems	PEC
28. Principles of Programming Languages	PPL
29. Programming and Data Structure	PDS
30. Real Time Systems	RTS
31. Software Engineering	SE
32. Storage Systems	SS
33. System Analysis and Design	SAD
34. Theory of Automata, Formal Languages and Computation	FLAT
35. Theory of Computation	TOC
36. Data Structures and Algorithms	DSA
37. Machine Learning	ML
38. Modern Algebra	MAL
39. Operating Systems	OS
# Mathematics Data
40. Mathematics I	MA1
41. Mathematics II	MA2
42. Mathematics III	MA3
43. Numerical Methods and Computation	NMC
44. Numerical Methods and Programing	NMP
45. Advanced Engineering Mathematics	AEM
46. Advanced Matrix Theory and Linear Algebra for Engineers	AMT
47. Applied Multivariate Analysis	AMA
48. Basic Algebraic Geometry : Varieties, Morphisms, Local Rings, Function Fields and Nonsingularity	BAG
49. Calculus of Variations and Integral Equations	COV
50. Complex Analysis	CA
51. Convex Optimization	COP
52. Discrete Mathematics	DM
53. Dynamic Data Assimilation: an introduction	DDA
54. Elementary Numerical Analysis	ENA
55. Foundations of Optimization	FOO
56. Functional Analysis	FA
57. Linear Algebra	LA
58. Linear programming and Extensions	LPE
59. Mathematical Logic	MLO
60. Measure and Integration	MI
61. Numerical methods of Ordinary and Partial Differential Equations	NMO
62. Optimization	OP
63. Probability and Statistics	PS
64. Probability Theory and Applications	PTA
65. Regression Analysis	RA
66. Statistical Inference	SI
67. Statistical Methods for Scientists and Engineers	SM
68. Stochastic Processes	SP

# Steps:
1. Collect Data (Collected 68 Courses; 2581 Lectures in PDF format)
2. Data > preprocess() > Text (Converts PDFs to TXTs)
3. Text > segment() > Segment (Segments TXTs into topical segments)
4. Segment > topic() > Topic / Topic_pkl (Tags topical segments in JSON / Pickle format)
5. Topic > off-topic() > Out_pkl / Off (Stores backlinks in Pickle format; predicts off-topics)
6. Off > retrieval() > Retrived (Retrieves segments for each of the off-topics)
7. Retrived > reranking() > Reranked (Reranks the segments)
8. Collect GS 

Folders:
1. Collect Data (Collected 68 Courses; 2581 Lectures in PDF format)
2. Data > preprocess() > Text (Converts PDFs to TXTs)
3. Text > segment() > Segment (Segments TXTs into topical segments)
4. Segment > topic() > Topic / Topic_pkl (Tags topical segments in JSON / Pickle format)
5. Topic > off-topic() > Out_pkl / Off (Stores backlinks in Pickle format; predicts off-topics)
6. Off > retrieval() > Retrived (Retrieves segments for each of the off-topics)
7. Retrived > reranking() > Reranked (Reranks the segments)
8. Collect GS 

Codes:
1. main.py (Segments TXTs into topical segments)
2. preprocess.py (Segments TXTs into topical segments)
3. segment.py (Segments TXTs into topical segments)
4. Topic.py (Tags topical segments in JSON / Pickle format)
5. Topic_pkl.py (Tags topical segments in JSON / Pickle format)
5. Out_pkl.py (Stores backlinks in Pickle format; predicts off-topics)
6. retrieval.py (Retrieves segments for each of the off-topics)
7. reranking.py (Reranks the segments)
8. eval.py (Segments TXTs into topical segments)
