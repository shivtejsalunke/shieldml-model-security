from dataclasses import dataclass
class AuthorizationError(Exception): pass
@dataclass(frozen=True)
class Principal:
    subject: str
    role: str
    token: str
class PolicyGate:
    def __init__(self, tokens, permissions): self.tokens=tokens; self.permissions=permissions
    def authorize(self, token, action):
        p=self.tokens.get(token)
        if p is None or action not in self.permissions.get(p.role,set()): raise AuthorizationError('not allowed')
        return p
