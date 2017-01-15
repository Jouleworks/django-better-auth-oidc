from jose import jwt
import os
import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urlencode

class TokenResponse:
    def __init__(self, data, server=None):
        self._data = data

        if server:
            self.id = jwt.decode(
                self.id_token,
                server.keys,
                algorithms = ['RS256'],
                audience = server.client_id,
                issuer = server.issuer,
                access_token = self.access_token,
            )

    @property
    def access_token(self):
        return self._data["access_token"]

    @property
    def id_token(self):
        return self._data["id_token"]

class AuthorizationServer:
    def __init__(self, url, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret

        r = requests.get(url + ".well-known/openid-configuration")
        r.raise_for_status()
        self._data = r.json()

    @property
    def issuer(self):
        return self._data["issuer"]

    @property
    def authorization_endpoint(self):
        return self._data["authorization_endpoint"]

    @property
    def token_endpoint(self):
        return self._data["token_endpoint"]

    @property
    def jwks_uri(self):
        return self._data["jwks_uri"]

    @property
    def keys(self):
        r = requests.get(self._data["jwks_uri"])
        r.raise_for_status()
        return r.content

    def authorize(self, redirect_uri, state, scope="openid"):
        return self.authorization_endpoint + "?" + urlencode(dict(
            client_id=self.client_id,
            response_type="code",
            redirect_uri=redirect_uri,
            state=state,
            scope=scope,
        ))

    def request_token(self, redirect_uri, code):
        client_auth = HTTPBasicAuth(self.client_id, self.client_secret)
        r = requests.post(self.token_endpoint, auth=client_auth, data=dict(
            grant_type="authorization_code",
            redirect_uri=redirect_uri,
            code=code,
        ))
        r.raise_for_status()
        return TokenResponse(r.json(), self)

SERVER        = os.getenv("OIDC_SERVER")
CLIENT_ID     = os.getenv("OIDC_CLIENT_ID")
CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET")

if SERVER and CLIENT_ID and CLIENT_SECRET:
    server = AuthorizationServer(SERVER, CLIENT_ID, CLIENT_SECRET)
