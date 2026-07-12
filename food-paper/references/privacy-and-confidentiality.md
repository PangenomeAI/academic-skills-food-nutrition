# Privacy & Confidentiality — check before delivering

**Every skill runs a privacy check before handing any document to the user.** A
deliverable (manuscript, brief, report, response letter, figure legend, table,
code snippet, PDF/DOCX/LaTeX) must not leak information about the user's machine
or private context.

## What must never appear in a deliverable
- **Local filesystem paths** — e.g. `/Users/<name>/…`, `/home/<name>/…`,
  `C:\Users\<name>\…`, `/root/…`. Use a relative or placeholder path
  (`./figures/fig1.pdf`, `<project>/data.csv`) instead.
- **Machine / temporary paths** — `/private/tmp/…`, `/var/folders/…`, scratchpad
  or session directories.
- **Usernames, hostnames, IP addresses, or device identifiers.**
- **Secrets** — API keys/tokens, passwords, access tokens (`sk-…`, `gh?_…`,
  `AKIA…`, bearer tokens).
- **Private emails or personal data** of the user or third parties that are not
  meant to be published (the public project contact is fine).
- **Unpublished/confidential third-party content** the user did not authorize to
  include.

## The check (do this before delivery)
1. **Scan** the deliverable: `python3 scripts/privacy_scan.py <file>` (or pipe the
   text). It flags local paths, temp paths, IPs, tokens, and non-project emails.
2. **Redact / replace** every hit — swap absolute paths for relative/placeholder
   paths, remove secrets and machine details.
3. **Re-scan** until clean.
4. Only then deliver. The scanner is a safety net, not a substitute for a human/
   agent read-through.

## In practice
- Refer to files by **relative path** in all prose and code you show the user.
- Do not paste raw shell/tooling output that embeds absolute paths into a
  manuscript or report.
- If the user *asks* to keep a specific path (e.g. their own repo path in their
  own notes), that is their choice — but never insert machine paths into a
  submission-ready document by default.

Wired into `food-paper` (writer/internal_reviewer), `deep-research` (compiler),
`food-research` (deliverables), `food-review`, and `food-pipeline` (the
pre-finalize gate).
