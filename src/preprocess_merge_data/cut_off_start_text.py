from src.tools import read_jsonline, write_jsonline


def cut_off_sentence(dic):
    clusters = dic["clusters"]
    big_s = 0
    small_s = 0
    print(len(dic["sentences"]))
    if len(dic["sentences"]) > 50:
        print('?')
        print(len(dic["sentences"]))

    for _ in range(2):
        clusters = sum(clusters, [])
    # print('!:', clusters)
    num_count = 0
    sentences = dic["sentences"]
    speakers = dic["speakers"]
    tag = 0
    sentence_index_tag = 0
    for id, sentence in enumerate(sentences):
        sentence_index_tag = sentence_index_tag + len(sentence)
        for token in sentence:
            num_count += 1
            # print(num_count)
            if num_count == min(clusters):
                tag = id
                break

    if tag > 1:
        sentences = sentences[tag:]
        speakers = speakers[tag:]
        new_clusters = [(i - sentence_index_tag) for i in clusters]
        new_clusters = [[new_clusters[0], new_clusters[1]], [new_clusters[2], new_clusters[3]]]
        dic["clusters"] = [new_clusters]
        # print(dic["clusters"])
        dic["sentences"] = sentences
        dic["speakers"] = speakers
    print(len(dic["sentences"]))
    print('___')
    return dic


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/bert_test/bert_256_merge_x4_z5_x1_z3.jsonlines"
    dest_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/bert_test/cut_bert_256_merge_x4_z5_x1_z3.jsonlines"
    file_list = read_jsonline(path)
    new = []
    for dic in file_list:
        # print(len(dic["sentences"]), '??')
        dic = cut_off_sentence(dic)
        # print(len(dic["sentences"]))
        new.append(dic)
    write_jsonline(dest_path, new)