from collections import Counter


def meter(opens, roster, week):
    counts = Counter()
    for row in opens:
        if row['week'] == week and row['edition'] in roster:
            counts[roster[row['edition']]['outlet']] += 1
    return dict(sorted(counts.items()))
