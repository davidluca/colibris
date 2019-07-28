
from colibris.conf.schemas import fields, SettingsSchema


class GeneralSettingsSchema(SettingsSchema):
    DEBUG = fields.Boolean()
    LISTEN = fields.String()
    PORT = fields.Integer()
    SECRET_KEY = fields.String()

    class Meta:
        sensible_fields = ['SECRET_KEY']


class DatabaseSettingsSchema(SettingsSchema):
    NAME = fields.String()
    HOST = fields.String()
    PORT = fields.Integer()
    USERNAME = fields.String()
    PASSWORD = fields.String()

    class Meta:
        prefix = 'DATABASE_'
        sensible_field = ['PASSWORD']


DEBUG = True

LISTEN = '0.0.0.0'
PORT = 8888

SECRET_KEY = 'replace-me-with-random-ascii-string-or-supply-via-environment'

DATABASE = {
    'backend': 'colibris.persist.PostgreSQLBackend',
    'name': 'colibrisdb',
    'host': '127.0.0.1',
    'port': 5432,
    'username': 'david',
    'password': 'rootpass'
}


AUTHENTICATION = {
    'backend': 'colibris.authentication.jwt.JWTBackend',
    'model': 'colibrisoverview.models.Owner',
    'identity_claim': 'sub',
    'identity_field': 'david',
    'secret_field': 'password',
    # 'cookie_name': 'auth_token',
    # 'cookie_domain': 'example.com',
    # 'validity_seconds': 3600 * 24 * 30
}

# AUTHORIZATION = {
#     'backend': 'colibris.authorization.role.RoleBackend',
#     'role_field': 'role'
# }


GeneralSettingsSchema().load_from_env(globals())
DatabaseSettingsSchema().load_from_env(globals())


CACHE = {
    'backend': 'colibris.cache.redis.RedisBackend',
    'host': '127.0.0.1',
    'port': 6379,
    'db': 0,
    # 'password': 'redispass'
}

# TASK_QUEUE = {
#  'backend': 'colibris.taskqueue.rq.RQBackend',
#  'host': '127.0.0.1',
#  'port': 6379,
#  'db': 0,
#  'password': 'yourpassword',
#  'poll_results_interval': 1
# }

TEMPLATE = {
    'backend': 'colibris.template.jinja2.Jinja2Backend',
    'extensions': [...],
    'translations': 'gettext'
}

EMAIL = {
    'default_from': 'david.luca@safefleet.eu',
    'backend': 'colibris.email.console.ConsoleBackend'
}
# EMAIL = {
#     'backend': 'colibris.email.console.ConsoleBackend'
# }
# EMAIL = {
#     'backend': 'colibris.email.smtp.SMTPBackend',
#     'host': 'smtp.gmail.com',
#     'port': 587,
#     'use_tls': True,
#     'username': 'david.luca@safefleet.eu',
#     'password': 'safefleetmailpass'
# }
