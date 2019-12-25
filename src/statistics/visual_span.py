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
    span_list = [span_coreferent_pair(i) for i in file_list]
    span_list = sum(span_list, [])
    return span_list


def bucket_span(spans):
    bins = [i for i in range(0, 150, 10)]
    nums_cut = pd.cut(spans, bins)
    result = pd.value_counts(nums_cut, sort=False)
    # print(result)
    return result


def visual_span_distribution(spans_list):
    bucket = bucket_span(spans_list)
    bucket_name = [str(index) for index in bucket.index]
    x = bucket_name
    y = bucket
    print(plt.style.available)
    # plt.style.use('ggplot')
    fig = plt.figure(figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    # ax.spines['bottom'].set_visible(False)
    # ax.spines['left'].set_visible(False)
    plt.bar(x, y, facecolor='lightskyblue', edgecolor='white', lw=2)
    plt.ylim(0, 400)
    plt.xlabel("Span of width")
    plt.ylabel("Nums")
    plt.title("Span width of coreferent pair")
    sum_y = sum(y)
    for x1, y1 in zip(x, y):
        plt.text(x1, y1 + 10, '{:.2f}%'.format(y1/sum_y * 100), ha="center", va="top")
    plt.show()


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei4_zhaoqi5_merge/x4_z5_cut.jsonlines"
    batch_list = batch_span(path)
    visual_span_distribution(batch_list)
