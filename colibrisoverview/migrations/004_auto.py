"""Peewee migrations -- 004_auto.py.

Some examples (model - class or model name)::

    > Model = migrator.orm['model_name']            # Return model in current state by name

    > migrator.sql(sql)                             # Run custom SQL
    > migrator.python(func, *args, **kwargs)        # Run python code
    > migrator.create_model(Model)                  # Create a model (could be used as decorator)
    > migrator.remove_model(model, cascade=True)    # Remove a model
    > migrator.add_fields(model, **fields)          # Add fields to a model
    > migrator.change_fields(model, **fields)       # Change fields
    > migrator.remove_fields(model, *field_names, cascade=True)
    > migrator.rename_field(model, old_field_name, new_field_name)
    > migrator.rename_table(model, new_table_name)
    > migrator.add_index(model, *col_names, unique=False)
    > migrator.drop_index(model, *col_names)
    > migrator.add_not_null(model, *field_names)
    > migrator.drop_not_null(model, *field_names)
    > migrator.add_default(model, field_name, default)

"""

import datetime as dt
import peewee as pw
from decimal import ROUND_HALF_EVEN

try:
    import playhouse.postgres_ext as pw_pext
except ImportError:
    pass

SQL = pw.SQL


def migrate(migrator, database, fake=False, **kwargs):
    """Write your migrations here."""

    @migrator.create_model
    class Owner(pw.Model):
        id = pw.AutoField()
        name = pw.CharField(max_length=256, unique=True)
        tel = pw.DecimalField(auto_round=False, decimal_places=0, max_digits=10, rounding=ROUND_HALF_EVEN)

        class Meta:
            table_name = "owner"

    @migrator.create_model
    class Pet(pw.Model):
        id = pw.AutoField()
        name = pw.CharField(max_length=256)
        type = pw.CharField(max_length=128)
        owner = pw.ForeignKeyField(backref='pet_set', column_name='owner_id', field='id', model=migrator.orm['owner'])

        class Meta:
            table_name = "pet"

    migrator.remove_model('user')

    migrator.remove_model('right')


def rollback(migrator, database, fake=False, **kwargs):
    """Write your rollback migrations here."""

    @migrator.create_model
    class Right(pw.Model):
        id = pw.AutoField()
        user = pw.ForeignKeyField(backref='right_set', column_name='user_id', field='id', model=migrator.orm['user'])
        resource = pw.CharField(max_length=128)
        operations = pw.CharField(max_length=16)

        class Meta:
            table_name = "right"

    @migrator.create_model
    class User(pw.Model):
        id = pw.AutoField()
        username = pw.CharField(max_length=128, unique=True)
        password = pw.CharField(max_length=128)
        first_name = pw.CharField(max_length=64)
        last_name = pw.CharField(max_length=64)
        email = pw.CharField(max_length=128, null=True)

        class Meta:
            table_name = "user"

    migrator.remove_model('pet')

    migrator.remove_model('owner')
