from src.tools import read_jsonline, write_jsonline


def check(train, eval, dest):
    train_l = read_jsonline(train)
    eval_l = read_jsonline(eval)
    print(len(eval_l))
    num = 0
    new_l = []
    for train in train_l:
        train_sentences = sum(train["sentences"], [])
        train_cluster = train["clusters"]
        t_entity_s = train_cluster[0][0][0]
        t_entity_e = train_cluster[0][0][1]
        t_pronoun_s = train_cluster[0][1][0]
        t_pronoun_e = train_cluster[0][1][1]
        for id, eval in enumerate(eval_l):
            eval_sentences = sum(eval["sentences"], [])
            eval_cluster = eval["clusters"]
            e_entity_s = eval_cluster[0][0][0]
            e_entity_e = eval_cluster[0][0][1]
            e_pronoun_s = eval_cluster[0][1][0]
            e_pronoun_e = eval_cluster[0][1][1]
            if train["pn"] == eval["pn"] and train_sentences[t_entity_s: t_entity_e + 1] == eval_sentences[e_entity_s: e_entity_e + 1]:
                print(' '.join(eval_sentences[e_entity_s: e_entity_e + 1]))
                # print(eval_sentences[e_pronoun_s: e_pronoun_e + 1])
                num += 1
                new_l.append(id)
    new_eval_l = []
    print(len(set(new_l)))
    print(new_l)
    print(num)
    for id, eval in enumerate(eval_l):
        if id not in new_l:
            new_eval_l.append(eval)

    print(len(new_eval_l))
    # write_jsonline(dest_path, new_eval_l)


if __name__ == '__main__':
    train_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_train.jsonlines"
    eval_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval.jsonlines"
    dest_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval_dup.jsonlines"
    check(train_path, eval_path, dest_path)