from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import tagme
import os
import json

dump_file={}
dump_file['examples']=[]

def main():
    topics = ['CA']
#    topics = ['PSP', 'ENA', 'DC', 'SE', 'RA', 'PPL', 'MA2', 'NLP', 'NMP', 'MA3', 'DMS', 'FAL', 'ML', 'CG', 'CN', 'DAA', 'CD', 'DSA', 'AGT', 'OP', 'BIO', 'COM', 'SI', 'CA', 'PEC', 'RTS', 'OS', 'DM', 'CO', 'AI', 'PC', 'AMT', 'FLAT', 'IT', 'CAL', 'PTA', 'CNS', 'AEM', 'AMA', 'PDS', 'MAL', 'SP', 'SS', 'NMC', 'LPE', 'LCS', 'TOC', 'MI', 'SM', 'GT', 'FA', 'LA', 'NMO', 'DDA', 'PA', 'MLO', 'COP', 'COV', 'CGR', 'PS', 'PR', 'CAR', 'DD', 'BAG', 'NOP', 'MA1', 'SAD', 'FOO']
    for topicname in topics:
        print(topicname)
        topic(topicname)
    print("Keys tagged...........")

def topic(t):
    # Annotate a text.
    dump_file['examples']=[]
    dir_name="./3_Segment/"+t
    out_dir_name="./4_Topic/"
    #print(t)
    ctr = 0
    for lecture in sorted(os.listdir(dir_name)):
        #print(lecture)
        for filename in sorted(os.listdir(os.path.join(dir_name, lecture))):
            if not os.path.exists(out_dir_name):
                os.makedirs(out_dir_name)
            file_path="./"+dir_name+"/"+lecture+"/"+filename
            file_opath="./"+out_dir_name+"/"+lecture
#            print("file_path: ",file_path)
            with open(file_path, 'r') as myfile:
                data=myfile.read().encode().decode('utf-8').replace('\n', '').lower()
                # print(data)
                # print("Annotating text: ", data)
                resp = tagme.annotate(data)
                topics_list=[]
                mention_list=[]
                location_list=[]
                dir_part = dir_name.split("/")
                id_no=dir_part[2]+"_"+lecture.split('.')[0]+"_"+filename.split('.')[0]
                if (resp!=None and resp.get_annotations(0.4)!=None):
                    for ann in resp.get_annotations(0.4):
                        if ann.mention not in mention_list:
                            topics_list.append(ann.entity_title)
                            mention_list.append(ann.mention)
                #print(topics_list)
                dump_file['examples'].append({"id":id_no,"text":data,"topics":topics_list,"mentions":mention_list})
    filename=os.path.join(out_dir_name, t+".json")
    with open(filename, 'w') as outfile:  
        json.dump(dump_file['examples'], outfile, indent=4)

if __name__ == "__main__":
    tagme.GCUBE_TOKEN = "0b4eed68-e456-4488-a5a6-7a608ea7e32b-843339462"
    main()
