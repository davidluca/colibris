
from . import fixtures


async def test_unauthenticated(web_app_client):
    resp = await web_app_client.get('/owners')
    assert resp.status == 401

    j = await resp.json()
    assert j['code'] == 'unauthenticated'


async def test_authenticated(web_app_client, test_owner, write_right):
    token = fixtures.TEST_USER_JWT
    resp = await web_app_client.get('/api/owners/me', headers={'Authorization': 'Bearer {}'.format(token)})
    assert resp.status == 200

