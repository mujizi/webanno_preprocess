from src.bert.tokenization import FullTokenizer
from src.tools import read_jsonline, write_jsonline


def get_sub_token(dic, tokenizer, length):
    sentences = sum(dic["sentences"], [])
    sub_word_list = []
    sub_token_map = []
    word_index = 0
    for word in sentences:
        subword = tokenizer.tokenize((word))
        sub_word_list.append(subword)
        sub_map = [word_index] * len(subword)
        word_index += 1
        sub_token_map.append(sub_map)
    sub_token_map = sum(sub_token_map, [])
    sub_word_list = sum(sub_word_list, [])

    new_token_map = [sub_token_map[i:i + length] for i in range(0, len(sub_token_map), length)]
    new_sentences = [sub_word_list[i:i + length] for i in range(0, len(sub_word_list), length)]

    dic["sentences"] = new_sentences
    dic["subtoken_map"] = new_token_map
    return dic


def get_cls_sep(dic):
    sentences = dic["sentences"]
    subtoken_map = dic["subtoken_map"]
    for sentence in sentences:
        sentence.insert(0, "[CLS]")
        sentence.insert(-1, "[SEP]")
    for index in subtoken_map:
        end = index[-1]
        start = index[0]
        index.insert(0, start)
        index.insert(-1, end)
    subtoken_map = sum(subtoken_map, [])
    dic["subtoken_map"] = subtoken_map

    return dic


def get_speaker(dic):
    sentences = dic["sentences"]
    speakers = []
    for i in sentences:
        speakers.append([""] * len(i))
    dic["speakers"] = speakers
    return dic


def get_sentence_map(dic):
    subtoken_map = dic["subtoken_map"]
    sentences = sum(dic["sentences"], [])
    dic["sentence_map"] = [0] * len(subtoken_map)
    # print(dic["sentence_map"])
    assert len(dic["sentence_map"]) == len(dic["subtoken_map"]) == len(sentences)
    return dic


def finally_get_cluster(dic):
    clusters = dic["clusters"]
    subtoken_map = dic["subtoken_map"]
    sentences = sum(dic["sentences"], [])
    # print(sentences)
    zip_map = list(zip(subtoken_map, sentences))
    print(zip_map)
    new_clusters = []
    for cluster in clusters:
        new_clusters.append(cluster_change(zip_map, cluster))
    dic["clusters"] = new_clusters
    print(len(sentences))

    print(sentences[new_clusters[0][0][0]:new_clusters[0][0][1] + 1])
    print(sentences[new_clusters[0][1][0]:new_clusters[0][1][1] + 1])
    return dic


def cluster_change(zip_map, cluster):
    print(cluster)
    new_cluster = []
    entity_l = []
    pro_l = []
    tag = 0
    for index, token in zip_map:
        if index == cluster[0][0] and token != "[CLS]":
            entity_l.append(tag)
        if index == cluster[1][0] and token != "[CLS]":
            pro_l.append(tag)
        tag += 1

    pro_l = pro_l[:1]
    entity_l = entity_l[:1]

    tag2 = 0
    for index, token in zip_map[::-1]:
        if index == cluster[0][1] and token != "[SEP]":
            entity_l.append(len(zip_map) - 1 - tag2)
        if index == cluster[1][1] and token != "[SEP]":
            pro_l.append(len(zip_map) - tag2 - 1)
        tag2 += 1

    pro_l = pro_l[:2]
    entity_l = entity_l[:2]
    new_cluster.append(entity_l)
    new_cluster.append(pro_l)
    assert len(new_cluster) == 2
    # print(new_cluster)
    return new_cluster


def all_file(path, dest_path, vocab_file):
    file_l = read_jsonline(path)
    tokenizer = FullTokenizer(
        vocab_file=vocab_file, do_lower_case=False)
    new_file = []
    for i in file_l:
        dic = get_sub_token(i, tokenizer, 128)
        dic = get_cls_sep(dic)
        dic = get_speaker(dic)
        dic = get_sentence_map(dic)
        dic = finally_get_cluster(dic)
        new_file.append(dic)
        print("_______________________")
    write_jsonline(dest_path, new_file)


if __name__ == '__main__':
    vocab_file = "/home/patsnap/PycharmProjects/webanno_preprocess/data/vocab/vocab.txt"
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval_dup.jsonlines"
    dest = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/bert_test/bert_x4_z5_eval_dup.jsonlines"
    all_file(path, dest, vocab_file)

