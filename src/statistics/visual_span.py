from src.tools import *
import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.ticker as ticker
import pandas as pd


def span_coreferent_pair(dic):
    clusters = dic["clusters"]
    # pairs = sum(clusters, [])
    dev_l = []
    for pair in clusters:
        dev = abs(pair[0][1] - pair[0][0])
        dev_l.append(dev)
    return dev_l


def batch_span(path):
    file_list = read_jsonline(path)
    print(len(file_list))

    span_list = [span_coreferent_pair(i) for i in file_list]
    span_list = sum(span_list, [])
    return span_list


def bucket_span(spans):
    bins = [i for i in range(0, 100, 10)]
    nums_cut = pd.cut(spans, bins)
    result = pd.value_counts(nums_cut, sort=False)
    # print(result)
    return result


def visual_span_distribution(spans_list, spans_list2):
    bucket = bucket_span(spans_list)
    bucket_name = [str(index) for index in bucket.index]
    bucket2 = bucket_span(spans_list2)
    length = np.arange(len(bucket_name))
    length2 = list(range(len(bucket_name)))

    y = bucket
    y2 = bucket2
    # plt.style.use('ggplot')
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.set_xticklabels(bucket_name)
    ax.set_xticks(length)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    rects1 = ax.bar(length -0.2, y, facecolor='skyblue', width=0.4, label="Coref-Patent")
    # for i in range(len(length)):
    #     #     length[i] += 0.4
    rects2 = ax.bar(length +0.2, y2, facecolor='IndianRed', width=0.4, label="CoNLL-2012")
    plt.ylim(0, 400)
    plt.xlabel("Length of Span", fontsize=12)
    plt.ylabel("Nums", fontsize=12)
    plt.title("Length of Coreference Span in Different Dataset", fontsize=15)
    plt.legend(prop={'size':12})
    sum_y = sum(y)

    def autolabel(rects, xpos='center'):
        """
        Attach a text label above each bar in *rects*, displaying its height.

        *xpos* indicates which side to place the text w.r.t. the center of
        the bar. It can be one of the following {'center', 'right', 'left'}.
        """

        xpos = xpos.lower()  # normalize the case of the parameter
        ha = {'center': 'center', 'right': 'left', 'left': 'right'}
        offset = {'center': 0, 'right': 0, 'left': 0}  # x_txt = x + w*off

        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x(), 1.02 * height,
                    '{}%'.format(round(height/sum_y * 100, 2)), va='bottom')

    autolabel(rects1, "left")
    autolabel(rects2, "right")
    plt.show()


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei2_1zhaoqi2_2.jsonlines"
    path2 = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/conll/dev.english.jsonlines"
    batch_list = batch_span(path)
    batch_list2 = batch_span(path2)
    visual_span_distribution(batch_list, batch_list2)
