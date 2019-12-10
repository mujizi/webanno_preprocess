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
                for i in pred:
                    print("_______________________")
                    pred_sentence = ' '.join(sentences[:i[0][0]]) + highlight(' '.join(sentences[i[0][0]: i[0][1] + 1]), 'red') + ' '.join(sentences[i[0][1] + 1:]) + highlight(' '.join(sentences[i[1][0]: i[1][1] + 1]), 'red')
                    gold_sentence = ' '.join(sentences[:gold_clusters[0][0][0]]) + highlight(' '.join(sentences[gold_clusters[0][0][0]: gold_clusters[0][0][1] + 1]),'blue') + ' '.join(sentences[gold_clusters[0][0][1] + 1:]) + highlight(' '.join(sentences[gold_clusters[0][1][0]: gold_clusters[0][1][1] + 1]), 'blue')
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


if __name__ == '__main__':
    gold_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/head_entity_for_test/x_z_3_head_eval.jsonlines"
    predicted_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/predicted/coref_predictions_3.json'
    visual_gold_pred(gold_path, predicted_path)