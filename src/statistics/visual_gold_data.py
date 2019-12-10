from src.tools import read_json, read_jsonline
import spacy
nlp = spacy.load("en_core_web_sm")


def visual_gold_pred(gold_path):
    gold_file = read_jsonline(gold_path)
    for gold in gold_file:
        sentences = sum(gold["sentences"], [])
        clusters = gold["clusters"]
        print(clusters[0][0][0])
        gold_s = clusters[0][0][0]
        gold_e = clusters[0][0][1]
        gold_s_pro = clusters[0][1][0]
        gold_e_pro = clusters[0][1][1]
        print("________________")
        print(' '.join(sentences[gold_s: gold_e + 1]))
        # doc = nlp(' '.join(sentences[gold_s: gold_e + 1]))
        # print([chunk for chunk in doc.noun_chunks])
        # for token in doc:
        #     print(token.pos_)
        print(' '.join(sentences[gold_s_pro: gold_e_pro + 1]))


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei4_zhaoqi5_merge/x4_z5_cut_off.jsonlines"
    visual_gold_pred(path)