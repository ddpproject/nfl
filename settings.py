# Settings for this app.

settings = dict(
    # You MUST update the author, uin, and agree_to_honor_code fields before you
    # turn this assignment in.
    author = "Dilim Nwobu",
    uin = '119-00-0493',
    email = 'dilim.nwobu@gmail.com',
    agree_to_honor_code = True,

    # the collaborators list contains tuples of 2 items, the name of the helper
    # and their contribution to your homework assignments
    collaborators = {
        ('Dr. Caverlee','taught csce 470'),
    },

    # You probably don't need to mess with these settings.
    http_host = 'localhost',
    http_port = 8000,
    mongo_host = 'localhost',
    mongo_port = 27017,
)

try:
    # pull in settings_local if it exists
    from settings_local import settings as s
    settings.update(s)
except ImportError:
    pass
