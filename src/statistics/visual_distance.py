from src.tools import *
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker


def distance_coreferent_pair(dic):
    clusters = dic["clusters"]
    # pairs = sum(clusters, [])
    dev_l = []
    for pair in clusters:
        dev = abs(pair[0][0] - pair[1][0])
        dev_l.append(dev)
    return dev_l


def batch_distance(path):
    file_list = read_jsonline(path)
    distances_list = [distance_coreferent_pair(i) for i in file_list]
    distances_list = sum(distances_list, [])
    print(distances_list)
    print(len(distances_list))
    return distances_list


def bucket_distance(distances):
    """
    Places the given values (designed for distances) into 10 semi-logscale buckets:
    [0, 1, 2, 3, 4, 5-7, 8-15, 16-31, 32-63, 64+].
    """
    logspace_idx = math.floor(math.log(distances)/math.log(2)) + 3
    use_identity = distances <= 4
    combined_idx = use_identity * distances + (1 - use_identity) * logspace_idx
    if combined_idx > 11:
        return 11
    elif combined_idx < 0:
        return 0
    else:
        return combined_idx


def visual_distance_distribution(distances_list):
    bucket_list = [bucket_distance(i) for i in distances_list]
    bucket_id_l = set(bucket_list)
    id_dic = {}
    for id in bucket_id_l:
        id_num = 0
        for i in bucket_list:
            if id == i:
                id_num += 1
        id_dic[id] = id_num
    # print(id_dic)
    x = id_dic.keys()
    y = id_dic.values()
    print(plt.style.available)
    # plt.style.use('fivethirtyeight')  # bmh
    plt.figure(figsize=(200, 200))
    plt.bar(x, y, facecolor='lightskyblue', edgecolor='white', lw=2)
    x_tick = ['2', '3', '4', '5-7', '8-15', '16-31', '32-63', '64-128', '129-256', '257-512']
    plt.ylim(0, 1000)
    plt.xlabel("Distance of span")
    plt.ylabel("Nums")
    plt.xticks(list(x), x_tick)
    # plt.locator_params('x', nbins=5)
    plt.title("Distance of coreferent pair")
    sum_y = sum(y)
    for x1, y1 in zip(x, y):
        plt.text(x1, y1 + 10, '{:.2f}%'.format(y1/sum_y * 100), ha="center", va="top")
    plt.show()


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/conll/dev.english.jsonlines"
    batch_list = batch_distance(path)
    visual_distance_distribution(batch_list)
