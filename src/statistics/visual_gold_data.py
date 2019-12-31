from src.tools import read_json, read_jsonline
import spacy
nlp = spacy.load("en_core_web_sm")
from src.highlight import highlight
from src.tools import read_json, read_jsonline


def visual_gold_hight(gold_path):
    gold_file = read_jsonline(gold_path)
    num = 0
    for gold in gold_file:
        sentences = sum(gold['sentences'], [])
        gold_clusters = gold["clusters"]
        # print(gold_clusters)
        print("_______________________")
        gold_sentence = ' '.join(sentences[:gold_clusters[0][0][0]]) + ' ' + highlight(
            ' '.join(sentences[gold_clusters[0][0][0]: gold_clusters[0][0][1] + 1]), 'blue') + ' ' + ' '.join(
            sentences[gold_clusters[0][0][1] + 1: gold_clusters[0][1][0]]) + ' ' + highlight(
            ' '.join(sentences[gold_clusters[0][1][0]: gold_clusters[0][1][1] + 1]), 'blue') + ' ' + ' '.join(sentences[gold_clusters[0][1][1] + 1:])
        print("Gold:")
        print(gold["doc_key"])
        tag = 0
        for id, char in enumerate(gold_sentence):
            if char == '.':
                print(gold_sentence[tag:id])
                tag = id
            if id == len(gold_sentence) - 1:
                print(gold_sentence[tag:])
        print("_______________________")
    print(num)
    print(len(gold_file))


def visual_gold(gold_path):
    gold_file = read_jsonline(gold_path)
    for gold in gold_file:
        sentences = sum(gold["sentences"], [])
        clusters = gold["clusters"]
        gold_s = clusters[0][0][0]
        gold_e = clusters[0][0][1]
        gold_s_pro = clusters[0][1][0]
        gold_e_pro = clusters[0][1][1]
        print("________________")
        print(gold["doc_key"])
        print(' '.join(sentences[gold_s: gold_e + 1]))
        print(' '.join(sentences[gold_s_pro: gold_e_pro + 1]))
        print(gold_s, gold_e)


if __name__ == '__main__':
    # path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_train.jsonlines"
    # visual_gold_pred(path)

    # gold_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali_sentence_span/cut_off_start_x4_train.jsonlines'
    gold_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/bert_test/cut_bert_256_merge_x4_z5_x1_z3.jsonlines'
    visual_gold_hight(gold_path)
import matplotlib.pyplot as plt