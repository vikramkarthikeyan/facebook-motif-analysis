from elasticsearch import helpers, Elasticsearch
import csv

es = Elasticsearch()

keys = ['Node count','Edge count','Male node count','Female node count','Unknown node count','Number of motifs','Number of MMM motifs','Number of FFF motifs','Number of MMF motifs','Number of FFM motifs','Number of UUU motifs']

with open('motif_results.csv', 'r') as f:
    reader = csv.DictReader(f)
    result = []
    count = 0
    for entry in reader:
        temp = dict(entry)
        del(temp[''])

        for key in keys:
            temp[key] = int(temp[key])

        temp['Female student ratio'] = temp['Female node count'] / temp['Node count']
        temp['FFF ratio'] = temp['Number of FFF motifs']/ temp['Number of motifs']
        temp['Male student ratio'] = temp['Male node count'] / temp['Node count']
        temp['MMM ratio'] = temp['Number of MMM motifs']/ temp['Number of motifs']
        temp['MMF+FFM ratio'] = (temp['Number of MMF motifs'] + temp['Number of FFM motifs']) / temp['Number of motifs']
        temp['UUU ratio'] = temp['Number of UUU motifs']/ temp['Number of motifs']

        print("---\n")
        if temp['FFF ratio'] < temp['Female student ratio']:
            print(temp['University'])
            print("FFF RATIO:",temp['FFF ratio'])
            print("Female student RATIO:",temp['Female student ratio'])
        
        if temp['MMM ratio'] < temp['Male student ratio']:
            print(temp['University'])
            print("MMM RATIO:",temp['MMM ratio'])
            print("Male student RATIO:",temp['Male student ratio'])


        count += 1
        result.append(temp)
    helpers.bulk(es, result, index='motif')