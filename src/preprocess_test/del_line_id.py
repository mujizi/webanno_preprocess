import re
NUM_REG = re.compile(r'\d')


def read_tsv(path):
    """
    :param path:
    :return: tokens list
    """
    with open(path, 'r') as f:
        lines = f.read().split('\n')[:-1]
        new_lines = []
        for i, line in enumerate(lines):
            new_line = line.split('\t')
            new_lines.append(new_line)
    return new_lines


def del_line_index(list):
    del_l = []
    for index, i in enumerate(list):
        try:
            if len(i) == 6 and i[2] == '[' and NUM_REG.match(list[index + 1][2]) and list[index + 2][2] == ']':
                del_l.extend([i for i in range(index, index + 3)])
        except:
            continue
    new_list = [list[i] for i in range(len(list)) if i not in del_l]
    return new_list


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/raw_data/xulei1/annotation/this_method_A_US20040152784A1_c169a306-00dd-4b30-9132-10a8ed09c812.txt_0/xulei.tsv"
    l = read_tsv(path)
    print(len(l))
    new = del_line_index(l)
    print(len(new))
    # for i in new:
    #     print(i)



