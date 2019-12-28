import os
import subprocess

cmd1 = './8_Result/trec_eval/trec_eval -M1000 8_Result/trec_eval/test/GS.txt 8_Result/trec_eval/test/RT.txt'
cmd2 = './8_Result/trec_eval/trec_eval -M1000 8_Result/trec_eval/test/GS.txt 8_Result/trec_eval/test/RR.txt'
os.system(cmd1)
os.system(cmd2)
