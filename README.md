# Augmentations for Video Lectures

# Introduction:
This project presents a video lecture augmentation system by linking its off-topic concepts with topically relevant lecture segments. Such lecture segments are retrieved to furnish basic understanding of the associated off-topic concepts. The proposed augmentation model comprises five modules: video lecture segmentation, concept extraction, off-topic identification, retrieval of relevant video segments and video segment re-ranking.
1. Video Lecture Segmentation: Video lectures are segregated by identifying the topical shifts using a word embedding-based technique.
2. Concept Extraction: The segmented video lectures are indexed using its concepts, extracted with an entity annotation service.
3. Off-Topic Identification: The task of predicting off-topic concepts is implemented as a community structure analysis problem on concept similarity graphs.
4. Retrieval of relevant video segments: For each off-topic concept, appropriate video segments are fetched.
5. Video Segment Re-ranking: These initially retrieved video segments are further re-ranked so that the top-ranked video segment offers the most basic understanding of the target off-topic concept.

# Steps:
## 1. Data collection:
Transcript data for 2581 Lectures present in 68 Courses (39 and 19 related to Computer science and Mathematics domains, respectively) collected from https://nptel.ac.in/course.html. These data are collected and stored in 1_Data folder in PDF format. Further details of the data is provided in 'Data.md' file. You can download the data from [https://drive.google.com/open?id=1KTWhbPk-N8_rz-p-wSIMo9nKKYWU7PU9](https://drive.google.com/drive/folders/1LtTD1bECyaQrlgJ74z0lVg6x8RlUjWud?usp=sharing)
## 2. Preprocessing:
Transcripts (PDFs) are converted into TXT format and pre-processed by removing spurious data (course metadata). The code '1_preprocess.py' converts and preprocesses the data from folder '1_Data' and stores in '2_Text' folder.
## 3. Segmentation:
The transcript data are segmented into topical segments. The code '2_segment.py' segments transcripts from '2_Text' folder and stores in '3_Segment' folder.
## 4. Concept Extraction:
A. Topics are extracted for each video lecture segments. The code '3_tag.py' extracts the topics and stores in '4_Topic' folder in JSON format.

B. Wikipedia articles are extarcted for the extracted topics. The code '3_topic_out.py' extracts the articles and stores in '4_Topic_pkl' folder in Pickle format.

C. Outlinks for the extracted Wikipedia articles are extracted to generate the concept-graph. The code '3_off_out.py' extracts the backlinks and stores in '4_Out_pkl' folder in Pickle format.

D. The concepts from '4_Topic' folder is shown to the annotators and the annotated concepts arestored in the '5_Annotated' folder in JSON format. Download '5_Annotated' folder from [https://drive.google.com/open?id=1peCDKd2u1xUuez5waN-2OgFRaSvUelh3 ](https://drive.google.com/drive/folders/1Tx_LN1O-cCcLxdW6ulqH6bM4qHrq7Kfd?usp=sharing).
## 5. Off-topic Identification:
The off-topics are identified automatically. The code '4_off_predict.py' identifies the off-topics, stores them in '5_off' folder and also evaluates the concerned modules.
## 6. Retrieval of Relevant Video Segments:
Video lecture segments relevant to each of the off-topics are retrieved. The code '6_retrieval.py' retrieves the segments and stores in '6_Retrieved' folder in JSON format and as 'RT.txt' in '8_Retrieved/trec-eval/test' folder in TREC suggested text format. The '8_Result' folder is downloadable from [https://drive.google.com/open?id=17-IxebyTtNsSXY98FfkTJWHK9goHhkOT](https://drive.google.com/drive/folders/1GEU8VBjIEItmsz8N5GcqvaOwzgtXcLyO?usp=sharing) which contains the folder 'trec-eval', providing the performance evaluation codes.
## 7. Reranking of Video Segments:
A. Code '7_feature.py' extracts the features and stores them in 'rerank.txt' file under '7_Reranked' folder.

B. The extracted features are combined with the the labels (relevant or not) from 'GS.txt' by code '7_L2R.py' and stores in 'L2R.txt'. Running linear regression models, the code '7_L2R.py' further detemines the weights for the features.

C. The retrieved video lecture segments are reranked using code '7_rerank.py' where the learned weights are used. The reranked segments are stored in '7_Reranked' folder in JSON format and as 'RR.txt' in '8_Retrieved/trec-eval/test' folder in TREC suggested text format.
## 8. Evaluation:
A. The retrieved and reranked segmnets are shown to the annotators and their relevance are tagged. The gold standard is present in 'GS.txt' file. The file can be downloaded from [https://drive.google.com/open?id=1sKfmBveCkUtaL_5cJqKG0li_z-c0wns4 ](https://drive.google.com/file/d/1fl_sIoJhaC21O13wOzg3q4I_Yw6Gn1sy/view?usp=sharing).

B. The code '8_eval.py' evaluates the retrieval and re-ranking performance. The '8_Result' folder is downloadable from [https://drive.google.com/open?id=17-IxebyTtNsSXY98FfkTJWHK9goHhkOT](https://drive.google.com/drive/folders/1GEU8VBjIEItmsz8N5GcqvaOwzgtXcLyO?usp=sharing) which contains the folder 'trec-eval', providing the performance evaluation codes.

# Run:
## Prepare the pre-requisites:
A. One needs a ist of supporting files to be present in the current directory. One can download these files (as recipients of 'lib' folder) from [https://drive.google.com/open?id=11PJ0Y-3RavS2F0B8lj247M5pK19fK11I](https://drive.google.com/drive/folders/144lSB61RGqfjuuSTMz3ir7spOUrLgRiY?usp=sharing)

B. Geckodriver is also required. Download this from [https://drive.google.com/open?id=1Mf92NT_MNV-z2ZXVkkuneIGw7hLoe8n1](https://drive.google.com/file/d/1Rdkq4OSDVSJG2aekY1_8OVBFs9hF2A3L/view?usp=sharing) and export it in PATH before running the codes.

## Execute:
Finally, run 'main.py' which offers a menu-based control to execute each of the above-mentioned modules.

# Contacts
In case of any queries, you can reach us at kghosh.cs@iitkgp.ac.in

# Cite
If this work is helpful for your research, please cite our paper 'Augmenting Video Lectures: Identifying Off-topic Concepts and Linking to Relevant Video Lecture Segments' available at https://link.springer.com/article/10.1007/s40593-021-00257-z.

    @article{ghosh2021augmenting,
        title = "Augmenting Video Lectures: Identifying Off-topic Concepts and Linking to Relevant Video Lecture Segments",
        journal = "International Journal of Artificial Intelligence in Education",
        year = "2021",
        doi = "https://doi.org/10.1007/s40593-021-00257-z",
        url = "https://link.springer.com/article/10.1007/s40593-021-00257-z",
        author = "Krishnendu Ghosh, Sharmila Reddy Nangi, Yashasvi Kanchugantla, Pavan Gopal Rayapati, Plaban Kumar Bhowmick and Pawan Goyal ",
        keywords = "Video lecture augmentation, Off-topic concept identification, MOOCs, Concept similarity, Community detection, Retrieval and re-ranking"
    }

The module on retrieving questions is discussed in details in our paper 'Using Re-Ranking to Boost Deep Learning Based Community Question Retrieval' available at https://dl.acm.org/doi/pdf/10.1145/3106426.3106442.

    @inproceedings{ghosh2017using,
    author = {Ghosh, Krishnendu and Bhowmick, Plaban Kumar and Goyal, Pawan},
    title = {Using Re-Ranking to Boost Deep Learning Based Community Question Retrieval},
    year = {2017},
    isbn = {9781450349512},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3106426.3106442},
    doi = {10.1145/3106426.3106442},
    booktitle = {Proceedings of the International Conference on Web Intelligence},
    pages = {807–814},
    numpages = {8},
    keywords = {question retrieval, re-ranking, community question answering},
    location = {Leipzig, Germany},
    series = {WI '17}
    }

A similar work "Remediating Textbook Deficiencies by Leveraging Community Question Answers" has been deployed for textbook data available at : https://doi.org/10.1007/s10639-022-10937-5.

@article{ghosh2022remediating,
  title={Remediating textbook deficiencies by leveraging community question answers},
  author={Ghosh, Krishnendu},
  journal={Education and Information Technologies},
  volume={27},
  number={7},
  pages={10065--10105},
  year={2022},
  publisher={Springer}
}
