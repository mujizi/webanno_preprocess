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
    path_1 = '/data/jsonline_data/xulei1_zhaoqi3_merge/x1_z3_dup.jsonlines'
    path_2 = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_train.jsonlines'
    dest_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/new_training_data/merge_x4_z5_x1_z3.jsonlines'
    merge_two_jsonlines(path_1, path_2, dest_path)
