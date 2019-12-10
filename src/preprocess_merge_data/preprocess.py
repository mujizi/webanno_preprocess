import csv
import re
import os
from src.tools import write_jsonline

NUM_REG = re.compile(r'\d')
ENTITY_TAG = re.compile(r'\*')
ENTITY_TAG_2 = re.compile(r'\*\[1\]')


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


def increase_token_id(tokens):
    """

    :param tokens:
    :return: increase tokens id in tokens list, it also a list
    """
    index = 0
    for token in tokens:
        # print(token)
        if len(token) > 1 and token[0][0].isdigit():
            token.insert(0, index)
            index += 1
        # print(token)
    return tokens


def get_clusters(tokens):
    """
    :param tokens:
    :return:
    """
    candidate_token_list = []
    for token in tokens:
        # print(token)
        try:
            if len(token) > 2 and ENTITY_TAG.match(token[4]):
                candidate_token_list.append(token)
                # print(token)
        except:
            continue

    clusters = []
    for index, token in enumerate(candidate_token_list):
        # print(token)
        if len(token[5]) < 2:
            continue

        elif token[5][0].isdigit():
            pair = []
            pronoun_tag = token[5].split('[')[0]
            entity_s = token[0]
            entity_e = token[0]
            entity_tag = token[4]
            for token_2 in candidate_token_list:
                if token_2[0] == (entity_e + 1) and token_2[4] == entity_tag:
                    entity_e += 1

                if token_2[1] == pronoun_tag:
                    pronoun_s = token_2[0]
                    pronoun_e = pronoun_s + 1

            pronoun, entity = [], []

            try:
                if candidate_token_list[index][3] == '[' and NUM_REG.match(candidate_token_list[index + 1][3]) and candidate_token_list[index + 2][3] == ']':
                    entity_s = entity_s + 3
            except:
                continue

            pronoun.append(pronoun_s)
            pronoun.append(pronoun_e)
            entity.append(entity_s)
            entity.append(entity_e)
            pair.append(entity)
            pair.append(pronoun)
            clusters.append(pair)
            # print(clusters)
    return clusters


def get_sentences(tokens):
    sentence = []
    sentences = []
    # print(tokens[6])
    for token in tokens[6:]:
        if len(token) == 1:
            if sentence != []:
                sentences.append(sentence)
            sentence = []
            continue

        if len(token) > 2:
            sentence.append(token[3])

        if token == tokens[-1]:
            sentences.append(sentence)
    return sentences


def get_speaker(sentences):
    speakers = []
    for i in sentences:
        speakers.append([""] * len(i))
    return speakers


def create_dic(sentences, clusters, speakers, doc_key, pn):
    dic = {}
    dic["doc_key"] = doc_key
    dic["sentences"] = sentences
    dic["clusters"] = clusters
    dic["speakers"] = speakers
    dic["pn"] = pn
    return dic


def tsv2dic(path, doc_key):
    pn = path.split('_')[5]
    tokens = read_tsv(path)
    # tag = len(tokens)
    # tokens = del_line_index(tokens)
    # if (tag - len(tokens)) / 3 == 0:
    #     print(True)
    tokens = increase_token_id(tokens)
    clusters = get_clusters(tokens)
    sentences = get_sentences(tokens)
    speakers = get_speaker(sentences)
    dic = create_dic(sentences, clusters, speakers, doc_key, pn)
    return dic


def all_tsv2dic(path):
    all_dic_list = []
    folder_paths = os.listdir(path)
    # this tag is used to doc_key name, it just like "nw0"
    tag = 0
    for folder_path in folder_paths:
        concat_path = path + '/' + folder_path
        folder_paths_2 = os.listdir(concat_path)
        concat_path_2 = concat_path + '/' + folder_paths_2[0]
        doc_key = "nw" + str(tag)
        all_dic_list.append(tsv2dic(concat_path_2, doc_key))
        tag += 1
    return all_dic_list


def create_jsonline(dest_file, all_dic_list):
    write_jsonline(dest_file, all_dic_list)


if __name__ == '__main__':
    path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/raw_data/zhaoqi5/annotation'
    dest_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/zhaoqi5/sentence_coref_zhaoqi5.jsonlines"

    all_dic_list = all_tsv2dic(path)
    create_jsonline(dest_path, all_dic_list)
