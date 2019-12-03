from src.tools import read_json, read_jsonline


def visual_gold_pred(gold_path):
    gold_file = read_jsonline(gold_path)
    for gold in gold_file:
        sentences = sum(gold["sentences"], [])
        clusters = gold["clusters"]
        gold_s = clusters[0][0][0]
        gold_e = clusters[0][0][1]
        gold_s_pro = clusters[0][1][0]
        gold_e_pro = clusters[0][1][1]
        print("________________")
        print(' '.join(sentences[gold_s: gold_e + 1]))
        print(' '.join(sentences[gold_s_pro: gold_e_pro + 1]))


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/cut_off_file/xulei1_zhaoqi3_cut_off.jsonlines"
    visual_gold_pred(path)