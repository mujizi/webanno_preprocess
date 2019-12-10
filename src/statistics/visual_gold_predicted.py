from src.tools import read_json, read_jsonline


def visual_gold_pred(gold_path, predicted_path):
    gold_file = read_jsonline(gold_path)
    pred_file = read_json(predicted_path)
    num = 0
    for doc_key, pred in pred_file.items():
        for gold in gold_file:
            if doc_key == gold['doc_key']:

                # print("__________________")
                sentences = sum(gold['sentences'], [])
                # print("sentences:", ' '.join(sentences))
                # print("doc_key:", doc_key)
                for i in gold['clusters']:
                    # print(i)
                    print('\n', "gold:")
                    print("len(sentences):", len(sentences))
                    print(i[0][0], i[0][1], i[1][0], i[1][1])
                    print(' '.join(sentences[i[0][0]:i[0][1] + 1]), "| | |", ' '.join(sentences[i[1][0]:i[1][1] + 1]))
                    print("\n", 'predicted:')
                    gold_s = i[0][0]
                    gold_e = i[0][1]
                    gold_s_pro = i[1][0]
                    gold_e_pro = i[1][1]

                for i in pred:
                    # print(i)
                    print(i[0][0], i[0][1], i[1][0], i[1][1])
                    print(' '.join(sentences[i[0][0]:i[0][1] + 1]), '| | |', ' '.join(sentences[i[1][0]:i[1][1] + 1]))
                    if i[0][0] == gold_s and i[0][1] == gold_e and i[1][0] == gold_s_pro and i[1][1] == gold_e_pro:
                        num += 1
                print("__________________")
    print("num:", num)


if __name__ == '__main__':
    gold_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/head_entity_for_test/x_z_3_head_eval.jsonlines"
    predicted_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/predicted/coref_predictions_3.json'
    visual_gold_pred(gold_path, predicted_path)