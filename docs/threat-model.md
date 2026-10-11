# Threat model

## Assets
- Confidentiality of serialized model artifacts before load.
- Integrity of encrypted artifact and release metadata.
- Authorization of inference or export actions.

## Considered adversary capabilities
- Reads copied artifact files, corrupts ciphertext, or supplies invalid/underprivileged tokens.
- Supplies bounded perturbations to a differentiable model during controlled evaluation.

## Out of scope
Host/root compromise, memory scraping after decryption, side channels, supply-chain compromise, rollback protection, secure boot, DDoS and formal verification.

AES-GCM authenticates the envelope under correct key/nonce handling. A SHA-256 manifest only catches tampering if the attacker cannot replace it too; production should sign the manifest or use HMAC. Model IP cannot be guaranteed after decryption in an adversary-controlled environment. Benchmark results are machine-specific.
