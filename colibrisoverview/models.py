
from colibris import persist


# # Model example:
# class User(persist.Model):
#     id = persist.AutoField()
#     username = persist.CharField(max_length=128, index=True, unique=True)
#     password = persist.CharField(max_length=128)
#     first_name = persist.CharField(max_length=64)
#     last_name = persist.CharField(max_length=64)
#     email = persist.CharField(max_length=128, null=True)
#
#
# # Another model example:
# class Right(persist.Model):
#     id = persist.AutoField()
#     user = persist.ForeignKeyField(User)
#     resource = persist.CharField(max_length=128)
#     operations = persist.CharField(max_length=16)


class Owner(persist.Model):
    id = persist.AutoField()
    name = persist.CharField(max_length=256, index=True, unique=True)
    tel = persist.CharField(max_length=10)


class Pet(persist.Model):
    id = persist.AutoField()
    name = persist.CharField(max_length=256)
    type = persist.CharField(max_length=128)
    owner = persist.ForeignKeyField(Owner)
