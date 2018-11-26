VERSION = '4.6.0'

MAX_RESULTS = 320
PARTIAL_DOWNLOAD_EXT = 'request'

DEFAULT_CONFIG_TEXT = '''toggles:
    include_md5: false

default_search:
    days: 1
    min_score: 0
    min_favs: 0
    ratings:
        - s

blacklist:

searches:
    cats:
        tags:
            - cat
            - yellow_fur
    dogs:
        tags:
            - dog
            - brown_fur

# The most common search structure has already been exemplified, but you may overwrite any of the default search settings for a specific search.
#
# searches:
#   dogs:
#       days: 30
#       min_score: 10
#       min_favs: 10
#       ratings:
#           -s
#           -q
#           -e
#       tags:
#           - dog
#           - brown_fur'''
