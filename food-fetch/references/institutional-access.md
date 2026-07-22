# Institutional Access (the user's own entitled session)

For a paywalled article the user is **entitled to** through their institution, reach
the licensed full text by **reusing the user's own logged-in browser session** — never
by bypassing anything. In this environment that means driving the browser the user is
already signed into (Claude-in-Chrome), not a fresh profile.

## Browser-state principle
Authorized access depends on the **exact browser profile where the user is logged in**.
If the browser opens a blank/new profile with no login, that is **not** "no library
permission" — ask the user to sign in to their library in that browser first, then
proceed. A stale session looks like a paywall but isn't one.

## Start from the library, not the publisher
Begin at the **user's library resource entry / discovery portal**, not a direct
`doi.org → publisher` jump — the resolver is what carries the entitlement. Recognize
these as **sign-in stages, not failures**:

| Pattern in the URL | What it is |
|---|---|
| `cas.*` · `/authserver/login` · `sso.*` | CAS / institutional SSO |
| `idp` · `shibboleth` · `openathens` · `carsi` · `ds.carsi.edu.cn` · `wayf` | Shibboleth / OpenAthens / CARSI federation |
| `ezproxy` · `libproxy` | EZproxy remote-access proxy |
| `webvpn` · `vpn` | WebVPN |
| `webofscience` · `sciencedirect` · publisher host | database/publisher entry (check it was reached via the portal) |

A login page with `service=<url>` returns to that `service` host after auth — treat
the callback host as the real resource, not the login page.

## Get the full text
1. Find the article via the resolver (DOI or exact title).
2. Open the full-text link, preferring: **Free Full Text / Open Access** → library
   resolver links (**Find it at**, SFX, OpenURL, "Full Text available via") → the
   **publisher** link. The session usually carries through without a second login.
3. On the publisher page, save the **real PDF** (`/doi/pdf/`, "Download PDF", `pdfft`).
   If only readable **HTML full text** exists, save/read that and mark
   `full_text_html_available`; if the publisher HTML is behind a **consent/auth
   redirect** (e.g. BMC → SpringerLink), read the **PMC / Europe PMC mirror** instead.
4. If the resolver says the institution has **no entitlement**, record
   `library_no_permission` and tell the user plainly. Don't retry direct publisher
   access as if it were a temporary network error.

## Login and verification — hand off to the user
Attempt at most **one** visible, non-secret control yourself (a plain "Continue" or a
cookie-consent "Accept"). For anything identity-bearing — password, **OTP/SMS**, QR
approval, passkey, hardware key, **2FA**, or a publisher **CAPTCHA/robot check** — stop
and **ask the user to complete it in the browser**, keep the tab open, and continue
from that same tab. Never type, read, export, or ask for a credential, cookie, session
token, or code. Pace conservatively: one sensitive publisher article at a time; never
flood tabs.

## Reference-manager libraries (read-only)
The user's **EndNote** (`<Library>.Data/PDF/`), **Zotero** (`storage/`), or **Mendeley**
folder is a set of already-downloaded, licensed PDFs — the best source for cited
papers. Read them **read-only**; never modify the library. (`library_fetcher`.)
