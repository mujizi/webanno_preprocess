from src.tools import read_jsonline, write_jsonline


def count_sentence_entity(dic):
    sentences = dic['sentences']
    clusters = dic['clusters']
    if len(clusters) == 0:
        return 1
    sentences = sum(sentences, [])
    if len(clusters) > 0:
        print(dic['pn'])
        print("sentence_len:", len(sentences))
        print(clusters)
        print("out of", clusters[0][0][1])
        print('sentences')
        if sentences[clusters[0][0][1]] == ".":
            # print(sentences[clusters[0][0][0]: clusters[0][0][1] + 1])
            return {}
        else:
            print(dic["pn"])
            print("len(phrase):", sentences[clusters[0][0][0]:clusters[0][0][1] + 1], len(sentences[clusters[0][0][0]:clusters[0][0][1] + 1]))
            print("this:", sentences[clusters[0][1][0]:clusters[0][1][1] + 1])
            return dic


def jsonlines_count(path, dest_path):
    jsonlines_list = read_jsonline(path)
    new_jsonline_list = []
    a = 0
    for dic in jsonlines_list:
        new_dic = count_sentence_entity(dic)
        if new_dic == 1:
            a += 1
        if new_dic != {} and new_dic != 1:
            new_jsonline_list.append(new_dic)
    write_jsonline(dest_path, new_jsonline_list)
    phrases_count = len(new_jsonline_list)
    sentences_count = len(jsonlines_list) - phrases_count
    print(sentences_count/len(jsonlines_list))
    print(len(jsonlines_list))
    print('new', len(new_jsonline_list))
    return sentences_count, phrases_count


if __name__ == '__main__':
    path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1/sentence_coref_xulei1.jsonlines'
    dest_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei1/count_xulei1.jsonlines'


    # path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/zhaoqi3/sentence_coref_zhaoqi3.jsonlines'
    # dest_path = '/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/zhaoqi3/count_zhaoqi3.jsonlines'
    sentences, phrase = jsonlines_count(path, dest_path)
    print(sentences)
    print(phrase)