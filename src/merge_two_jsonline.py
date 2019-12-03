from src.tools import read_jsonline, write_jsonline


def merge_two_jsonlines(path, path2, dest_path):
    file1 = read_jsonline(path)
    file2 = read_jsonline(path2)
    file1.extend(file2)
    write_jsonline(dest_path, file1)


if __name__ == '__main__':
    path_1 = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1/sentence_coref_xulei1.jsonlines'
    path_2 = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/zhaoqi3/sentence_coref_zhaoqi3.jsonlines'
    dest_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1_zhaoqi3_merge/xulei1_zhaoqi3.jsonlines'
    merge_two_jsonlines(path_1, path_2, dest_path)
