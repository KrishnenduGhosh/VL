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
Transcript data for 2581 Lectures present in 68 Courses (39 and 19 related to Computer science and Mathematics domains, respectively) collected from https://nptel.ac.in/course.html. These data are collected and stored in 1_Data folder in PDF format.
## 2. Preprocessing:
Transcripts (PDFs) are converted into TXT format and pre-processed by removing spurious data (course metadata). The code '1_preprocess.py' converts and preprocesses the data from folder '1_Data' and stores in '2_Text' folder.
## 3. Segmentation:
The transcript data are segmented into topical segments. The code '2_segment.py' segments transcripts from '2_Text' folder and stores in '3_Segment' folder.
## 4. Concept Extraction:
A. Topics are extracted for each video lecture segments. The code '3_tag.py' extracts the topics and stores in '4_Topic' folder in JSON format.
B. Wikipedia articles are extarcted for the extracted topics. The code '3_topic_out.py' extracts the articles and stores in '4_Topic_pkl' folder in Pickle format.
C. Outlinks for the extracted Wikipedia articles are extracted to generate the concept-graph. The code '3_off_out.py' extracts the backlinks and stores in '4_Out_pkl' folder in Pickle format.
D. The concepts from '4_Topic' folder is shown to the annotators and the annotated concepts arestored in the '5_Annotated' folder in JSON format.
## 5. Off-topic Identification:
The off-topics are identified automatically. The code '4_off_predict.py' identifies the off-topics and also evaluates the concerned modules.
## 6. Retrieval of Relevant Video Segments:
Video lecture segments relevant to each of the off-topics are retrieved. The code '6_retrieval.py' retrieves the segments and stores in '6_Retrieved' folder.
## 7. Reranking:
The retrieved video lecture segments are reranked using code '7_rerank.py'. The reranked segments are stored in '7_Reranked' folder.
## 8. Evaluation:
A. The retrieved and reranked segmnets are shown to the annotators and their relevance are tagged. The gold standard is present in 'GS.txt' file.
B. The retrieved and reranked segments are converted to the files 'RT.txt' and 'RR.txt' respectvely. This conversion made so that TREC provided evaluation module can operate on them and determine the performance measures. The code '8_eval.py' converts the segments and stores in '8_Result' folder.
# Run:
Run main.py which offers a menu-based control to execute each of the above-mentioned modules.

# Contacts
In case of any queries, you can reach us at kghosh.cs@iitkgp.ac.in
