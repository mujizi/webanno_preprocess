import re
NUM = re.compile(r'\d{4}')
import numpy as np
sentences = [["[", "0066", "]", "The", "back", "wall", "24", "contains", "on"], ["its", "interior", "surface", "a", "pair", "of", "raised", "walls", "or", "ribs", "44a", "and", "44b", "for", "enhancing", "the", "strength", "and", "rigidity", "thereof", "."]]


def sentence_start_end_index(sentences):
    """
    :param sentences: sentences list example: [['i', 'like'], ['cat']]
    :return: sentences start list and end list just like start:[0, 2], end:[1, 2]
    """
    start_l, end_l = [], []
    offset = -1
    for sentence in sentences:
        start_ = offset + 1
        end_ = len(sentence) + offset
        try:
            if sentence[0] == '[' and NUM.match(sentence[1]) and sentence[2] == ']':
                start_ = start_ + 3
        finally:
            offset = offset + len(sentence)
            start_l.append(start_)
            end_l.append(end_)
    assert len(start_l) == len(end_l)
    return np.array(start_l), np.array(end_l)


if __name__ == '__main__':
    # start_list, end_list = sentence_start_end_index(sentences)
    # print(start_list, len(start_list), type(start_list))
    # print(end_list, len(end_list), type(end_list))
    l = [1,2,3]
    l.insert(0,"1")
    l.append("1")
    print(l)
