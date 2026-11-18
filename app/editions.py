def roster(source):
    """在架清单维持各发布站自己的稿件编号。"""
    return {row['id']: row for row in source if row['state'] == 'live'}


def corrections(source):
    return [row['id'] for row in source if row['state'] == 'withdrawn']
