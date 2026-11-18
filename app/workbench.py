import json
from .dispatch import weekly
from .editions import roster
from .journal import packet


def run_workbench(action, directory, key, ledger):
    if action == 'archive':
        if not key:
            raise ValueError('请指定周报期号')
        return packet(ledger, 'weekly', key)
    source = json.loads((directory / 'workbench.json').read_text())
    if action == 'edition':
        return roster(source['editions'])
    data = weekly(source)
    if action == 'dispatch':
        return packet(ledger, 'weekly', key or data['week'], data)
    return data
