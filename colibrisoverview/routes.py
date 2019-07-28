
import os

from colibris.conf import settings
from colibris.authorization import ANY_PERMISSION

from colibrisoverview import views
from colibrisoverview.constants import ROLE_ADMIN, ROLE_REGULAR

#
# Routes example:

ROUTES = [
    ('GET',     r'/owners/me',           views.get_me,           ANY_PERMISSION),
    (None,      r'/owners',              views.OwnersView,        {ROLE_ADMIN}),
    (None,      r'/owners/{id:\d+}',     views.OwnerView,         {ROLE_ADMIN})
]

# ROUTES = [
#     ('GET',     r'/users/me',           views.get_me,           ANY_PERMISSION),
#     (None,      r'/users',              views.UsersView,        {ROLE_ADMIN}),
#     (None,      r'/users/{id:\d+}',     views.UserView,         {ROLE_ADMIN})
# ]


#
# Add static routes, for development purposes
#
# if settings.DEBUG:
#     STATIC_ROUTES = [
#         (os.path.join(settings.PROJECT_PACKAGE_DIR, 'static'), '/static'),
#     ]
#
