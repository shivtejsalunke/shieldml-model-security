# ShieldML — Model Artifact Protection & Inference Integrity Lab

ShieldML is a reproducible ML security engineering prototype for authenticated model-artifact encryption, integrity verification, authorization checks, and adversarial evaluation.

## Current scope
- AES-256-GCM artifact encryption/decryption.
- SHA-256 manifest checks and verification before decryption.
- A small role/action policy gate for demonstrating authorization boundaries.
- Optional FGSM evaluation helper and a reproducible crypto-overhead benchmark.
- Threat model, test suite, and GitHub Actions workflow.

## Quick start
```bash
python -m venv .venv
# Activate the environment, then:
python -m pip install -e '.[test]'
pytest -q
```

## Important limitations
This is a portfolio prototype, not a production identity or model-protection platform. Encryption at rest does not prevent extraction from a compromised process after decryption. A standalone checksum manifest is not sufficient against an attacker able to replace both artifact and manifest; production deployments should sign manifests or use HMAC and protected key custody. The FGSM helper evaluates robustness; it is not a defense. No production edge/browser deployment is claimed.

See `docs/threat-model.md` for assumptions and hardening priorities.
