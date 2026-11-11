# Supply-Chain Audit: Node.js v20.0.0

## Audit Entry #1 — Node.js v20.0.0 (nodejs/node)

| Field | Value |
| --- | --- |
| Tag | `v20.0.0` |
| Target commit SHA (full) | `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` |
| Tag object SHA | `ffca5a7a113131b1a252fd95b53161b5182e66be` |
| Tagger | RafaelGSS <rafael.nunu@hotmail.com> |
| Tag date | 2023-04-18T16:01:08Z |
| Tag message | `2023-04-18 Node.js v20.0.0 (Current) Release` ( annotated tag; embedded payload also carries a Git-EVTag-v0-SHA512 grape of `139f42d86104763cfb245391eb193901998ae9981dcf5d00a1bf18d6952e6165a8193600d127f5c1c05fb905fa5178474e00f10c4ab04101f804e7f268ccc6fe`) |
| Signature verification | verified (`valid`) |

### Integrity fingerprint (computed locally via Python `hashlib`)

- **SHA-256 hex digest of the full commit SHA string** (input: `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`, UTF-8):
  `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4`
- **12-character short SHA** (matches the first 12 characters of the full SHA per our changelog convention):
  `e7618fb5a5fc`
  - Cross-check: `e7618fb5a5fc` is a prefix of `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` → ✅ match confirmed.

### Source

- Upstream repository: `nodejs/node` (https://github.com/nodejs/node)
- Tag lookup performed via the GitHub Bare Tag API (`GET /repos/nodejs/node/git/tags/v20.0.0`)
- Both the digest and short SHA above were computed by executing code locally (Python `hashlib.sha256`), not copied from any web page.

### Release checklist note

This entry satisfies the audit requirement for the first upstream release we pin: exact commit the tag resolves to (`e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0`), the tagger and tag date, the annotation message, and a locally computed integrity fingerprint (SHA-256) plus the 12-char short SHA for changelog matching.
