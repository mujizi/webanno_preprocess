from src.preprocess import *
from src.tools import *
if __name__ == '__main__':
    # path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/raw_data/xulei1/annotation/this_method_E_US5131472_9743977e-a1ce-4d08-af37-3ef3f5b64bf5.txt_0/xulei.tsv"

    path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/test_data/nw16.jsonlines'
    dic = read_jsonline(path)
    print(dic[0])
    print(dic[0]['sentences'])
    print(len(sum(dic[0]['sentences'], [])))
