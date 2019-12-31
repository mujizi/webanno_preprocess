from src.tools import read_jsonline, write_jsonline


def merge_two_jsonlines(path, path2, dest_path):
    file1 = read_jsonline(path)
    file2 = read_jsonline(path2)
    file1.extend(file2)
    tag = 0
    for i in file1:
        i["doc_key"] = "nw" + str(tag)
        tag += 1
        print(i["doc_key"])
    print(len(file1))
    write_jsonline(dest_path, file1)


if __name__ == '__main__':
    path_1 = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei2_1zhaoqi2_2_dup.jsonlines'
    path_2 = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval_dup.jsonlines'
    dest_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_x2_1_z2_2_dup_eval.jsonlines'
    merge_two_jsonlines(path_1, path_2, dest_path)
