from src.tools import read_jsonline, write_jsonline
import math
import random


def split_train_eval_dataset(path, train_path, eval_path):
    file_list = read_jsonline(path)
    print(len(file_list))
    random.shuffle(file_list)
    train_nums = math.floor(len(file_list) * 0.85)
    train_data = file_list[:train_nums]
    eval_data = file_list[train_nums:]
    print(len(train_data))
    print(len(eval_data))
    write_jsonline(train_path, train_data)
    write_jsonline(eval_path, eval_data)


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei4_zhaoqi5_merge/x4_z5_cut_off.jsonlines"
    train_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_train.jsonlines"
    eval_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/train_vali/x4_z5_eval.jsonlines"
    split_train_eval_dataset(path, train_path, eval_path)