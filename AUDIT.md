# AUDIT.md — Supply Chain Pin Audit

## Upstream Release Pinned: Node.js v20.0.0

- **Upstream repository:** nodejs/node (https://github.com/nodejs/node)
- **Tag:** `v20.0.0`
- **Target commit SHA (full):** `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`
- **Short SHA (changelog convention, 12 chars):** `e7618fb5a5fc`
- **SHA-256 hex digest of the full commit SHA string:** `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4`
- **Tagger:** RafaelGSS <rafael.nunu@hotmail.com>
- **Tag date:** 2023-04-18T16:01:08Z
- **Tag annotation message:** `2023-04-18 Node.js v20.0.0 (Current) Release` (annotated tag also carries a Git-EVTag-v0-SHA512 checksum and a PGP signature block; signature verification status: verified/valid)
- **Signature verification:** verified (valid)

## How the computed values were generated

Both values below were computed by executing code (Python `hashlib.sha256()` over the UTF-8 encoded full SHA string), not copied from any webpage:

1. **SHA-256 hex digest:** input hashed was the exact string `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` (the full commit SHA as returned by GitHub for tag `v20.0.0`). Output digest: `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4` (64 hex characters).
2. **12-character short SHA:** `e7618fb5a5fc`, taken as the first 12 characters of the full SHA. A programmatic prefix check confirmed `e7618fb5a5fc` is a prefix of `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`, so it matches against the full SHA for changelog matching purposes.

## Audit entry reference

This file records the first entry on the release checklist audit for upstream releases we pin. It is committed on its own branch (`audit/node-v20.0.0-pin`) and proposed into the default branch (`main`) via an open pull request.
