#!/usr/bin/env python

from Bio import SeqIO, AlignIO, pairwise2
from Bio.Seq import Seq
from Bio.pairwise2 import format_alignment
import pandas as pd
import mysql.connector, os, sys

cnx = mysql.connector.connect(user='<enter>', password='<enter>',
                              host='<enter>',
                              database='<enter>')
cursor = cnx.cursor()

temp = []
colnames = ['orf_name','seq_exp','seq_rec']
alignments = []

for file in os.listdir():
    if file.endswith(".seq"):
        for seq_record in SeqIO.parse(file, "fasta"):
            seq_rec = str(seq_record.seq)
        query = ("""
            select orf_name, seq_nt_atg
            from ORFS_SEQUENCES
            where orf_name = '%s'
            """)%str(file)[:-4]
        cursor.execute(query)
        for i in cursor:
            temp.append([i[0],'ACAAGTTTGTACAAAAAAGCAGGCTCCACC' + i[1][:-3] + 'TAG' + 'GACCCAGCTTTCTTGTACAAAGTGGT',seq_rec])
            
orf_data = pd.DataFrame(temp,columns=colnames)

scores = []
for i in range(0,len(orf_data)):
    temp = pairwise2.align.globalms(orf_data.iloc[i,2], orf_data.iloc[i,1],1, -1, -1, 0,score_only=1)
    scores.append((temp+2)/len(orf_data.iloc[i,1])*100)
    alignments.append((orf_data.iloc[i,0],
                   format_alignment(*pairwise2.align.globalms(orf_data.iloc[i,2], orf_data.iloc[i,1],1, -1, -1, 0)[0])))

orf_data['perc_match'] = scores

orf_data.to_csv('all_aligns.csv', sep=',')
orf_data[orf_data.perc_match<90].to_csv('bad_aligns.csv', sep=',')
with open('alignments.txt', 'w') as f:
    for item in alignments:
        f.write("%s\n%s\n\n" % (item[0],item[1][:-12]))
        
cursor.close()
