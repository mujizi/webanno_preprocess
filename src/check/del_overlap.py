from src.tools import read_jsonline, write_jsonline


def del_all_overlap(path, dest_path):
    file_l = read_jsonline(path)
    print(len(file_l))
    num = 0
    sorted_l = []
    for raw_index, raw_file in enumerate(file_l):
        raw_sentences = sum(raw_file["sentences"], [])
        raw_cluster = raw_file["clusters"]
        r_entity_s = raw_cluster[0][0][0]
        r_entity_e = raw_cluster[0][0][1]
        r_pn = raw_file["pn"]
        new_l = []
        for new_index, new_file in enumerate(file_l):
            new_sentences = sum(new_file["sentences"], [])
            new_cluster = new_file["clusters"]
            n_entity_s = new_cluster[0][0][0]
            n_entity_e = new_cluster[0][0][1]
            n_pn = new_file["pn"]
            if new_index != raw_index and r_pn == n_pn and new_sentences[n_entity_s: n_entity_e] == raw_sentences[r_entity_s: r_entity_e]:
                new_l.append(raw_index)
                new_l.append(new_index)
        new_l = sorted(set(new_l))
        if len(new_l) > 0:
            sorted_l.append(new_l)

    # print(sorted_l)
    final_l = []
    for i in sorted_l:
        if i not in final_l:
            final_l.append(i)
    final_l2 = [i[1:] for i in final_l]
    final_l3 = sum(final_l2, [])
    print(len(final_l3))
    overlap_l = []
    for raw_index, raw_file in enumerate(file_l):
        if raw_index not in final_l3:
            overlap_l.append(raw_file)
    write_jsonline(dest_path, overlap_l)
    print(len(overlap_l))


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei2_1zhaoqi2_2_cut.jsonlines"
    dest_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/xulei2_1zhaoqi2_2_dup.jsonlines"
    del_all_overlap(path, dest_path)