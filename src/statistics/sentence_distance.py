from src.tools import read_jsonline
import matplotlib.pyplot as plt


def sentence_distance_gold(dic):
    clusters = dic["clusters"]
    sentences = dic["sentences"]
    # print(clusters)
    pro_s = clusters[0][1][0]
    en_s = clusters[0][0][0]
    se_num = 0
    to_num = 0
    for sentence in sentences:
        for _ in sentence:
            if to_num == en_s:
                e_index = se_num
            if to_num == pro_s:
                p_index = se_num
            to_num += 1
        se_num += 1

    return p_index - e_index


def all_file_distance(path):
    file_l = read_jsonline(path)
    dic_r = {}
    method, process, problem, solution = {}, {}, {}, {}
    for i in file_l:
        r = sentence_distance_gold(i)
        sentences = sum(i["sentences"], [])
        index = i["clusters"][0][1][1]
        word = sentences[index]
        if word == "solution":
            if r in method:
                method[r] += 1
            else:
                method[r] = 1

    print(method)
    # method = sorted(method.items(), key=lambda item:item[1], reverse=True)
    # print(method)
    x = method.keys()
    y = method.values()
    # print(plt.style.available)
    # plt.style.use('fivethirtyeight')  # bmh
    plt.figure(figsize=(200, 200))
    plt.bar(x, y, facecolor='lightskyblue', edgecolor='white', lw=2)
    x_tick = method.keys()
    plt.show()


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/new_training_data/merge_x4_z5_x1_z3.jsonlines"
    all_file_distance(path)
