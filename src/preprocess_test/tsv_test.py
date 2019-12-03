import csv

def read_tsv_2(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')[:-1]
        new_lines = []
        for i, line in enumerate(lines):
            new_line = line.split('\t')
            new_lines.append(new_line)
    return new_lines


path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/raw_data/xulei1/annotation/this_method_E_US5131472_9743977e-a1ce-4d08-af37-3ef3f5b64bf5.txt_0/xulei.tsv"
t2 = read_tsv_2(path)
for i in t2:
    print(i)