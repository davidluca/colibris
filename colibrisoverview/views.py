import jwt

from aiohttp import web
from aiohttp_apispec import docs, request_schema, response_schema

from colibris import api
from colibris import authentication
from colibris import cache
from colibris.schemas import many_envelope
from colibris.shortcuts import get_object_or_404

from colibrisoverview import models
from colibrisoverview import schemas
from colibrisoverview import notification
from colibrisoverview import settings


# View examples:


# @docs(tags=['Users'],
#       summary='Reveal details about the current user')
# @response_schema(schemas.UserSchema())
# async def get_me(request):
#     user = authentication.get_account(request)
#     result = schemas.UserSchema().dump(user)
#
#     return web.json_response(result)
#
#
# class UsersView(web.View):
#     @docs(tags=['Users'],
#           summary='List all users')
#     @response_schema(many_envelope(schemas.UserSchema))
#     async def get(self):
#         users = models.User.select().order_by(models.User.username.asc())
#         result = schemas.UserSchema(many=True).dump(list(users))
#
#         return web.json_response(result)
#
#     @docs(tags=['Users'],
#           summary='Add a new user')
#     @request_schema(schemas.UserSchema())
#     @response_schema(schemas.UserSchema())
#     async def post(self):
#         data = self.request['data']
#
#         if models.User.select().where(models.User.username == data['username']).exists():
#             raise api.DuplicateModelException(models.User, 'username')
#
#         user = models.User.create(**data)
#         result = schemas.UserSchema().dump(user)
#
#         return web.json_response(result, status=201)
#
#
# class UserView(web.View):
#     @docs(tags=['Users'],
#           summary='Reveal details about a specific user')
#     @response_schema(schemas.UserSchema())
#     async def get(self):
#         user_id = self.request.match_info['id']
#         user = get_object_or_404(models.User, user_id)
#
#         result = schemas.UserSchema().dump(user)
#
#         return web.json_response(result)
#
#     @docs(tags=['Users'],
#           summary='Update an existing user')
#     @request_schema(schemas.UserSchema(partial=True))
#     @response_schema(schemas.UserSchema(partial=True))
#     async def patch(self):
#         user_id = self.request.match_info['id']
#         user = get_object_or_404(models.User, user_id)
#         data = self.request['data']
#
#         if 'username' in data:
#             query = (models.User.username == data['username']) & (models.User.id != user_id)
#             if models.User.select().where(query).exists():
#                 raise api.DuplicateModelException(models.User, 'username')
#
#         user.update_fields(data)
#         user.save()
#
#         result = schemas.UserSchema().dump(user)
#
#         return web.json_response(result)
#
#     @docs(tags=['Users'],
#           summary='Delete a user')
#     async def delete(self):
#         user_id = self.request.match_info['id']
#         if models.User.delete().where(models.User.id == user_id).execute() == 0:
#             raise api.ModelNotFoundException(models.User)
#
#         return web.json_response(status=204)


@docs(tags=['Owners'],
      summary='Reveal details about the current owner')
# documenteaza efectiv functia ce urmeaza a fi folosita
@response_schema(schemas.OwnerSchema())
# Add response info into the swagger spec
async def get_me(request):
    owner = authentication.get_account(request)
    result = schemas.OwnerSchema().dump(owner)

    return web.json_response(result)


class OwnersView(web.View):
    @docs(tags=['Owners'],
          summary='List all owners')
    @response_schema(many_envelope(schemas.OwnerSchema))
    async def get(self):
        owners = models.Owner.select().order_by(models.Owner.name.asc())
        result = schemas.OwnerSchema(many=True).dump(list(owners))

        return web.json_response(result)

    @docs(tags=['Owners'],
          summary='Add a new owner')
    @request_schema(schemas.OwnerSchema())
    @response_schema(schemas.OwnerSchema())
    async def post(self):
        data = self.request['data']

        if models.Owner.select().where(models.Owner.name == data['name']).exists():
            raise api.DuplicateModelException(models.Owner, 'name')

        user = models.Owner.create(**data)

        token = jwt.encode({'user_id': data['name'], 'admin': True},
                           settings.AUTHENTICATION['secret_field'], algorithm='HS256')

        result = schemas.OwnerSchema().dump(user)
        notification.notify_customer_on_sign_up(tel=data['tel'], name=data['name'])

        return web.json_response(result, status=201)


class OwnerView(web.View):
    @docs(tags=['Owners'],
          summary='Reveal details about a specific owner')
    @response_schema(schemas.OwnerSchema())
    async def get(self):
        owner_id = self.request.match_info['id']
        owner = get_object_or_404(models.Owner, owner_id)

        result = schemas.OwnerSchema().dump(owner)

        return web.json_response(result)

    @docs(tags=['Owners'],
          summary='Update an existing owner')
    @request_schema(schemas.OwnerSchema(partial=True))
    @response_schema(schemas.OwnerSchema(partial=True))
    async def patch(self):
        owner_id = self.request.match_info['id']
        owner = get_object_or_404(models.Owner, owner_id)
        data = self.request['data']

        if 'name' in data:
            query = (models.Owner.name == data['name']) & (models.Owner.id != owner_id)
            if models.Owner.select().where(query).exists():
                raise api.DuplicateModelException(models.Owner, 'name')

        owner.update_fields(data)
        owner.save()

        result = schemas.OwnerSchema().dump(owner)

        return web.json_response(result)

    @docs(tags=['Owners'],
          summary='Delete a owner')
    async def delete(self):
        owner_id = self.request.match_info['id']

        owner = models.Owner.select().where(models.Owner.id == owner_id)
        print('--------------', owner)
        cache.set('del', owner_id, lifetime=300)
        if models.Owner.delete().where(models.Owner.id == owner_id).execute() == 0:
            raise api.ModelNotFoundException(models.Owner)

        my_value = cache.get('del', default='some_default')
        print('=================', my_value, '=====================')
        return web.json_response(status=204)
