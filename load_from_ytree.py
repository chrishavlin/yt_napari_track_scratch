import numpy as np
import ytree

if __name__ == "__main__":
    a = ytree.load("tiny_ctrees/locations.dat")

    my_tree = a[0]

    fields = ["position"]
    data = {field: my_tree["forest", field].T for field in ["uid"] + fields}

    times = my_tree["forest", "time"]
    utimes = np.unique(times)
    tindex = np.digitize(times, utimes) - 1
    data["time_index"] = tindex

    track_data = np.vstack([data[field] for field in ["uid", "time_index"] + fields]).T

    # construct the graph dict
    graph = {}
    for my_node in my_tree["forest"]:
        my_anc_uids = [my_anc["uid"] for my_anc in my_node.ancestors]
        if my_anc_uids:
            graph[my_node["uid"]] = my_anc_uids
