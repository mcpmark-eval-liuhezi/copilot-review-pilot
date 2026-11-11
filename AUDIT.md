# Release Audit — Upstream Release Pin Entry

## Entry 1: Node.js v20.0.0 (nodejs/node)

| Field | Value (as returned by GitHub API) |
| --- | --- |
| Repository | nodejs/node |
| Tag | v20.0.0 |
| Tag object SHA (Git tag object) | `ffca5a7a113131b1a252fd95b53161b5182e66be` |
| **Full commit SHA the tag resolves to** | `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` |
| Tagger (creator) | RafaelGSS <rafael.nunu@hotmail.com> |
| Tag date | 2023-04-18T16:01:08Z |
| Tag annotation message | `2023-04-18 Node.js v20.0.0 (Current) Release` (signed GPG tag, verified) |
| SHA-256 hex digest of commit SHA string | `491f8f43b4f109b90f073040e94cebcfb3ac0d4cfa638e5bdb7e762f95e70dd4` |
| Input hashed | `e7618fb5a5fc25d76b6474e2a6607f04fd6f10e0` |
| 12-char short SHA (changelog convention) | `e7618fb5a5fc` |

## Integrity Notes

- The tag is a signed Lightweight/Annotated tag (Git-EVTag format) with a valid PGP signature (`verification.verified: true`, reason: `valid`).
- The Git-EVTag SHA-512 embedded in the annotation: `139f42d86104763cfb245391eb193901998ae9981dcf5d00a1bf18d6952e6165a8193600d127f5c1c05fb905fa5178474e00f10c4ab04101f804e7f268ccc6fe`.
- The SHA-256 digest above was computed locally by executing code (Python `hashlib.sha256`) over the exact 40-character commit SHA string, UTF-8 encoded. The 12-character short SHA is the first 12 characters of the full commit SHA: `e7618fb5a5fc` (verified programmatically that it matches `commit_sha[:12]`).
