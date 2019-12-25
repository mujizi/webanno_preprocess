from src.tools import read_jsonline, write_jsonline


def del_empty_cluster(path, dest_path):
    file_list = read_jsonline(path)
    for file in file_list:
        if len(file["clusters"]) == 0:
            print(file["clusters"])
    new_file_list = [file for file in file_list if len(file["clusters"]) != 0]
    write_jsonline(dest_path, new_file_list)
    print(len(new_file_list))
    print(len(file_list))


def cut_off_sentence(dic):
    clusters = dic["clusters"]
    for _ in range(2):
        clusters = sum(clusters, [])
    # print(max(clusters))
    num_count = 0
    sentences = dic["sentences"]
    speakers = dic["speakers"]
    # print(len(sentences))
    for id, sentence in enumerate(sentences):
        for token in sentence:
            num_count += 1
            # print(num_count)
            if num_count == max(clusters):
                tag = id
    sentences = sentences[: tag + 1]
    speakers = speakers[: tag + 1]
    # print(len(sentences))
    dic["sentences"] = sentences
    dic["speakers"] = speakers
    return dic


def cut_off_jsonlines(path, dest_file):
    file_list = read_jsonline(path)
    new_file_list = []
    for file in file_list:
        new_file = cut_off_sentence(file)
        new_file_list.append(new_file)
    # print(len(new_file_list))
    write_jsonline(dest_file, new_file_list)


def test_cut_off_result(raw_file, cut_file):
    raw_file_l = read_jsonline(raw_file)
    cut_file_l = read_jsonline(cut_file)
    for i in range(0, len(raw_file_l)):
        raw_sentences = raw_file_l[i]["sentences"]
        cut_sentences = cut_file_l[i]["sentences"]

        # print("raw", len(raw_sentences))
        # print("cut", len(cut_sentences))
        if len(cut_sentences) == 0:
            print(' '.join(cut_sentences))


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/x1_z3_del.jsonlines"
    dest_file = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/x1_z3_cut.jsonlines"
    cut_off_jsonlines(path, dest_file)

    # path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/x_z_del_cluster.jsonlines"
    # path2 = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/cut_off_file/xulei1_zhaoqi3_cut_off.jsonlines"
    # test_cut_off_result(path, path2)

    # path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/x1_z3.jsonlines"
    # dest = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/x1_z3_del.jsonlines'
    # del_empty_cluster(path, dest)