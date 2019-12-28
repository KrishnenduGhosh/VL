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
Transcript data for 2581 Lectures present in 68 Courses (39 and 19 related to Computer science and Mathematics domains, respectively) collected from https://nptel.ac.in/course.html. These data are collected and stored in 1_Data folder in PDF format. Further details of the data is provided in 'Data.md' file. You can download the data from https://drive.google.com/open?id=1KTWhbPk-N8_rz-p-wSIMo9nKKYWU7PU9
## 2. Preprocessing:
Transcripts (PDFs) are converted into TXT format and pre-processed by removing spurious data (course metadata). The code '1_preprocess.py' converts and preprocesses the data from folder '1_Data' and stores in '2_Text' folder.
## 3. Segmentation:
The transcript data are segmented into topical segments. The code '2_segment.py' segments transcripts from '2_Text' folder and stores in '3_Segment' folder.
## 4. Concept Extraction:
A. Topics are extracted for each video lecture segments. The code '3_tag.py' extracts the topics and stores in '4_Topic' folder in JSON format.

B. Wikipedia articles are extarcted for the extracted topics. The code '3_topic_out.py' extracts the articles and stores in '4_Topic_pkl' folder in Pickle format.

C. Outlinks for the extracted Wikipedia articles are extracted to generate the concept-graph. The code '3_off_out.py' extracts the backlinks and stores in '4_Out_pkl' folder in Pickle format.

D. The concepts from '4_Topic' folder is shown to the annotators and the annotated concepts arestored in the '5_Annotated' folder in JSON format. Download '5_Annotated' folder from https://drive.google.com/open?id=1peCDKd2u1xUuez5waN-2OgFRaSvUelh3 .
## 5. Off-topic Identification:
The off-topics are identified automatically. The code '4_off_predict.py' identifies the off-topics, stores them in '5_off' folder and also evaluates the concerned modules.
## 6. Retrieval of Relevant Video Segments:
Video lecture segments relevant to each of the off-topics are retrieved. The code '6_retrieval.py' retrieves the segments and stores in '6_Retrieved' folder in JSON format and as 'RT.txt' in '8_Retrieved/trec-eval/test' folder in TREC suggested text format. The '8_Result' folder is downloadable from https://drive.google.com/open?id=17-IxebyTtNsSXY98FfkTJWHK9goHhkOT which contains the folder 'trec-eval', providing the performance evaluation codes.
## 7. Reranking:
The retrieved video lecture segments are reranked using code '7_rerank.py'. The reranked segments are stored in '7_Reranked' folder in JSON format and as 'RR.txt' in '8_Retrieved/trec-eval/test' folder in TREC suggested text format.
## 8. Evaluation:
A. The retrieved and reranked segmnets are shown to the annotators and their relevance are tagged. The gold standard is present in 'GS.txt' file. The file can be downloaded from https://drive.google.com/open?id=1sKfmBveCkUtaL_5cJqKG0li_z-c0wns4 .

B. The code '8_eval.py' evaluates the retrieval and re-ranking performance. The '8_Result' folder is downloadable from https://drive.google.com/open?id=17-IxebyTtNsSXY98FfkTJWHK9goHhkOT which contains the folder 'trec-eval', providing the performance evaluation codes.

# Run:
## Prepare the pre-requisites:
A. One needs a ist of supporting files to be present in the current directory. One can download these files (as recipients of 'lib' folder) from https://drive.google.com/open?id=11PJ0Y-3RavS2F0B8lj247M5pK19fK11I

B. Geckodriver is also required. Download this from https://drive.google.com/open?id=1Mf92NT_MNV-z2ZXVkkuneIGw7hLoe8n1 and export it in PATH before running the codes.
## Execute:
Finally, run 'main.py' which offers a menu-based control to execute each of the above-mentioned modules.

# Cite
If this work is helpful for your research, please cite our papers.

    @inproceedings{nangi2019offvid,
    title={OffVid: A System for Linking Off-Topic Concepts to Topically Relevant Video Lecture Segments},
    author={Nangi, Sharmila Reddy and Kanchugantla, Yashasvi and Rayapati, Pavan Gopal and Bhowmik, Plaban Kumar},
    booktitle={2019 IEEE 19th International Conference on Advanced Learning Technologies (ICALT)},
    volume={2161},
    pages={37--41},
    year={2019},
    organization={IEEE}
    }
        
# Contacts
In case of any queries, you can reach us at kghosh.cs@iitkgp.ac.in
