def read(path):
    rows = []
    with open(path) as f:
        for line in f:
            t, ch, v = line.strip().split(",")
            rows.append((int(t), ch, float(v)))
    return rows
# parse time, channel, value
