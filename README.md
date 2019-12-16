# Video Augmentation for Video Lectures

Steps:
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
