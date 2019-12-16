# Video Augmentation for Video Lectures

# Introduction:
This project presents a video lecture augmentation system by linking its off-topic concepts with topically relevant lecture segments. Such lecture segments are retrieved to furnish basic understanding of the associated off-topic concepts. The proposed augmentation model comprises five modules: video lecture segmentation, concept extraction, off-topic identification, retrieval of relevant video segments and video segment re-ranking.
1. Video Lecture Segmentation: Video lectures are segregated by identifying the topical shifts using a word embedding-based technique.
2. Concept Extraction: The segmented video lectures are indexed using its concepts, extracted with an entity annotation service.
3. Off-Topic Identification: The task of predicting off-topic concepts is implemented as a community structure analysis problem on concept similarity graphs.
4. Retrieval of relevant video segments: For each off-topic concept, appropriate video segments are fetched.
5. Video Segment Re-ranking: These initially retrieved video segments are further re-ranked so that the top-ranked video segment offers the most basic understanding of the target off-topic concept.

# Steps:
## 1. Data collection:
Transcript data for 2581 Lectures present in 68 Courses (39 and 19 related to Computer science and Mathematics domains, respectively) collected from https://nptel.ac.in/course.html. These data are present in the 1_Data folder in PDF format.
## 2. Preprocessing:
Converts transcripts PDFs into TXT format and pre-processes by removing spurious data (course metadata). These data are present in the 2_Text folder in TXT format.
## 3. Segmentation:
Segments the transcripts into topical segments. These data are present in the 3_Segment folder in TXT format.
## 4. Concept Extraction:
A. Extracts topics for each video lecture segments. These data are present in the 4_Topic folder in JSON format.
B. Extracts the linked Wikipedia articles for the extracted topics. These data are present in the 4_Topic_pkl folder in JSON format.
C. Extracts the linked Wikipedia articles for the articles present in 4_Topic_pkl folder. These data are present in the 4_Out_pkl folder in JSON format.
D. Annotates the extracted concepts. These data are present in the 5_Annotated_1 folder in JSON format.
## 5. Off-topic Identification:
Identifies the off-topics. These data are present in the 5_Off folder in JSON format. It also evaluates the concerned module.
## 6. Retrieval of Relevant Video Segments:
A. Retrieves relevant video lecture segments for each of the off-topics. These data are present in the 6_Retrieved folder in JSON format.
B. Annotates the retrieved segments. These data are present in the 8_Annotated_2 folder.
## 7. Reranking:
Reranks the retrieved video lecture segments. These data are present in the 7_Reranked folder in JSON format.
## 8. Evaluation:
Evaluates the extracted concepts.

# Run:
Run main.py which offers a menu-based control to execute each of the modules.

# Cite

# Contacts
In case of any queries, you can reach us at kghosh.cs@iitkgp.ac.in
