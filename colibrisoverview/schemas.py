
from colibris.schemas import ModelSchema
from colibris.schemas import fields, validate, pre_load

from colibrisoverview import models

#
# Schema example:


# class UserSchema(ModelSchema):
#     email = fields.String(validate=[validate.Email(error='Invalid email address.'),
#                                     validate.Length(max=128)])
#
#     @pre_load
#     def process_input(self, data, **kwargs):
#         data['email'] = data['email'].lower().strip()
#
#         return data
#
#     class Meta:
#         model = models.User
#         name = 'user'
#         name_plural = 'users'


class OwnerSchema(ModelSchema):
    name = fields.String(validate=validate.Length(max=256))
    tel = fields.String(validate=validate.Length(max=10))

    @pre_load
    def process_input(self, data, **kwargs):
        data['name'] = data['name'].lower().strip()

        return data

    class Meta:
        model = models.Owner

#
# class PetSchema(ModelSchema):
#     name = fields.String(validate=validate.Length(max=128))
#     type = fields.String(validate=validate.OneOf(choices=['cat', 'dog']))
