from .editions import corrections, roster
from .traffic import meter


def weekly(source):
    issues = roster(source['editions'])
    return {'week': source['week'], 'station_opens': meter(source['opens'], issues, source['week']),
            'editions': list(issues), 'withdrawn': corrections(source['editions'])}
