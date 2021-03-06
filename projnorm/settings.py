ID_SYSTEMS = (
    'mlbam',
    'retro',
    'fangraphs',
    'fangraphs_minors',
    'bbref',
    'bbref_minors',
    'bbpro',
    'davenport',
    'cbs',
    'espn',
    'yahoo',
    'nfbc',
)

COLUMNS = (
    'name',
    'age',
)

DEFAULT_CONFIG = {
    'components': {
        'batting': (
            'g',
            'pa',
            'ab',
            'h',
            '_1b',
            '_2b',
            '_3b',
            'hr',
            'bb',
            'ibb',
            'r',
            'rbi',
            'sb',
            'cs',
            'hbp',
            'obp',
            'slg',
            'so',
            'avg',
            'sh',
            'sf',
            'babip',
        ),

        'pitching': (
            'g',
            'gs',
            'ip',
            'w',
            'l',
            'qs',
            'sv',
            'hld',
            'so',
            'h',
            'bb',
            'ibb',
            'er',
            'era',
            'whip',
            'hra',
            'hbp',
            'gb',
            'fb',
            'ld',
            'k_9',
            'bb_9',
            'k_bb',
            'hr_9',
            'hr_fb',
            'lob_pct',
            'cg',
            'sho',
            'tbf',
            'babip',
            'ra',
        )
    }
}
