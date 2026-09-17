# Upstream Pin Audit

Release checklist audit entries for upstream releases we pin. For each pin we
record the exact commit the tag resolves to, plus an integrity fingerprint we
compute ourselves.

| # | Upstream | Release | Tag | Target commit SHA | Short SHA (12) | SHA-256 of commit SHA |
|---|----------|---------|-----|-------------------|----------------|-----------------------|
| 1 | nodejs/node | Node.js v20.0.0 | `v20.0.0` | `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` | `e7618fb5a5fc` | `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4` |

## Entry 1 — Node.js v20.0.0

- **Upstream repository:** nodejs/node
- **Tag:** `v20.0.0` (annotated, signed; tag object SHA: `ffca5a7a113131b1a252fd95b53161b5182e66be`)
- **Target commit SHA (exact, as returned by GitHub):** `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`
- **Tagger:** RafaelGSS <rafael.nunu@hotmail.com>
- **Tag date:** 2023-04-18T16:01:08Z
- **Tag annotation message:** `2023-04-18 Node.js v20.0.0 (Current) Release` (the full tag message also includes a Git-EVTag-v0-SHA512 and a PGP signature block)

### Computed integrity fingerprint

Computed locally, not copied from any webpage:

- **Input hashed (exact string, 40 chars):** `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`
- **SHA-256 hex digest:** `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4`
- **12-character short SHA (changelog convention):** `e7618fb5a5fc` (confirmed prefix of the full SHA)
