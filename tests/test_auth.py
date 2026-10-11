import pytest
from shieldml.auth import Principal,PolicyGate,AuthorizationError

def test_role_policy():
 p=Principal('test-user','inference','demo-token'); gate=PolicyGate({'demo-token':p},{'inference':{'predict'}})
 assert gate.authorize('demo-token','predict').subject=='test-user'
 with pytest.raises(AuthorizationError): gate.authorize('demo-token','export-weights')
 with pytest.raises(AuthorizationError): gate.authorize('wrong','predict')
