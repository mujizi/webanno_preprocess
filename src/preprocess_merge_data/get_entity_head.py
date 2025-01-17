from src.tools import write_jsonline, read_jsonline


def span2head(cluster):
    if (cluster[0][1] - cluster[0][0] + 1) > 3:
        cluster[0][1] = cluster[0][0] + 3
        return cluster
    else:
        return cluster


def get_entity_head(dic):
    clusters = dic["clusters"]
    new_clusters = []
    for cluster in clusters:
        cluster = span2head(cluster)
        # print(cluster)
        new_clusters.append(cluster)
    return new_clusters


def batch_get_head(path, dest_path):
    file_list = read_jsonline(path)
    for file in file_list:
        new_clusters = get_entity_head(file)
        file["clusters"] = new_clusters
        print(sum(file["sentences"], [])[file["clusters"][0][0][0]:file["clusters"][0][0][1] + 1])
        print(sum(file["sentences"], [])[file["clusters"][0][1][0]:file["clusters"][0][1][1] + 1])
    # print(len(file_list))
    write_jsonline(dest_path, file_list)


if __name__ == '__main__':
    path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/cut_off_file/xulei1_zhaoqi3_cut_off.jsonlines"
    dest_path = "/home/patsnap/PycharmProjects/webanno_preprocess/data/jsonline_data/head_entity_for_test/" \
                "x_z_3_head.jsonlines"
    batch_get_head(path, dest_path)