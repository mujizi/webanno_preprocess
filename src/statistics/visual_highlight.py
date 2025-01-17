from src.highlight import highlight
from src.tools import read_json, read_jsonline


def visual_gold_pred(gold_path, predicted_path):
    gold_file = read_jsonline(gold_path)
    pred_file = read_json(predicted_path)
    num = 0

    for doc_key, pred in pred_file.items():
        for gold in gold_file:
            if doc_key == gold['doc_key']:
                sentences = sum(gold['sentences'], [])
                gold_clusters = gold["clusters"]
                # print(sentences)
                # print(gold_clusters)
                # print(pred)
                if pred == []:
                    print("\n", "No predicted:")
                    gold_sentence = ' '.join(sentences[:gold_clusters[0][0][0]]) + ' ' + highlight(' '.join(sentences[gold_clusters[0][0][0]: gold_clusters[0][0][1] + 1]),'blue') + ' ' + ' '.join(sentences[gold_clusters[0][0][1] + 1: gold_clusters[0][1][0]]) + ' ' + highlight(' '.join(sentences[gold_clusters[0][1][0]: gold_clusters[0][1][1] + 1]), 'blue')
                    tag = 0
                    for id, char in enumerate(gold_sentence):
                        if char == '.':
                            print(gold_sentence[tag:id])
                            tag = id
                        if id == len(gold_sentence) - 1:
                            print(gold_sentence[tag:])
                    print("_______________________")

                else:
                    for i in pred:
                        num += 1
                        print("_______________________")
                        pred_sentence = ' '.join(sentences[:i[0][0]]) + ' ' + highlight(' '.join(sentences[i[0][0]: i[0][1] + 1]), 'red') + ' ' + ' '.join(sentences[i[0][1] + 1: i[1][0]]) + ' ' + highlight(' '.join(sentences[i[1][0]: i[1][1] + 1]), 'red')
                        gold_sentence = ' '.join(sentences[:gold_clusters[0][0][0]]) + ' ' + highlight(' '.join(sentences[gold_clusters[0][0][0]: gold_clusters[0][0][1] + 1]),'blue') + ' ' + ' '.join(sentences[gold_clusters[0][0][1] + 1: gold_clusters[0][1][0]]) + ' ' + highlight(' '.join(sentences[gold_clusters[0][1][0]: gold_clusters[0][1][1] + 1]), 'blue')
                        print(gold["doc_key"])
                        print("Gold:")
                        tag = 0
                        for id, char in enumerate(gold_sentence):
                            if char == '.':
                                print(gold_sentence[tag:id])
                                tag = id
                            if id == len(gold_sentence) - 1:
                                print(gold_sentence[tag:])
                        print("\n", "Pred:")
                        tag2 = 0
                        for id, char in enumerate(pred_sentence):
                            if char == '.':
                                print(pred_sentence[tag2:id])
                                tag2 = id
                            if id == len(pred_sentence) - 1:
                                print(pred_sentence[tag2:])
                        print("_______________________")
    print(num)
    print(len(gold_file))


if __name__ == '__main__':
    gold_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval_dup.jsonlines"
    predicted_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/predicted/sentence_span_del_duplication.json"
    visual_gold_pred(gold_path, predicted_path)
