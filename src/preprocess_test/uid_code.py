import os
import re
UID = re.compile(r'^uid_456456')


def get_1_3_line(path):
    with open(path, 'r') as f:
        lines = f.read().split('\n')
    return lines[0].split()[0], lines[2].split()[0]


def get_uid_from_dir(path):
    path_list = os.listdir(path)
    assert len(path_list) == 1
    h_file = path_list[0]
    h_path = path + '/' + h_file
    path_2_list = os.listdir(h_path)
    for name in path_2_list:
        if UID.match(name):
            whole_path = h_path + '/' + name
            line1, line3 = get_1_3_line(whole_path)
            dev = float(line3) - float(line1)
            print("dev: {}".format(dev))
            if dev > 1:
                return -1
            else:
                return 0


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/test_data/level1_dir"
    print(get_uid_from_dir(path))