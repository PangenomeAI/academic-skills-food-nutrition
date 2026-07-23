# Institution Profiles

## How to Add Your Institution

Add only public, non-secret library entry information. The host AI uses these values
to begin an entitled-access workflow in the user's own browser; food-fetch does not
provide a separate browser proxy, credential handler, or challenge-solving service.

1. **Find `library_search`.** Open the page where your institution's library lets you
   search its catalogue, discovery index, or subscribed electronic resources. Copy
   the stable public URL from the address bar before starting a personal login, and
   enter it as `library_search`.
2. **Find `library_home`.** Open the institution's main library website and enter its
   public HTTPS URL as `library_home`.
3. **Find `openurl_base`.** Look on the library website for pages named **link
   resolver**, **linking service**, **Find It**, or **Connect**. The resolver is often
   the base of a URL used to connect a citation to subscribed full text. If the base
   is not published clearly, ask a librarian for the institution's OpenURL resolver
   base; do not guess it from a temporary redirect or copy login query parameters.
4. **Identify `authentication`.** Start one normal library login in your own browser
   and observe the hostname to which it redirects. Compare that hostname with the URL
   pattern table in [institutional-access.md](institutional-access.md): for example,
   `sso.*` or `cas.*` indicates institutional SSO/CAS, while `shibboleth` or
   `openathens` indicates the corresponding federation. Record only the descriptive
   authentication method name, never a username, credential, browser value, or login
   URL parameter.
5. Choose a short, unique lowercase `id` and add one record with the six fields shown
   below. Use HTTPS for all three URL fields. If you are uncertain about any public
   endpoint, confirm it with your library before saving the profile.

### Complete example: University of Melbourne

```yaml
institutions:
  - id: unimelb
    name: University of Melbourne
    library_home: https://library.unimelb.edu.au/
    library_search: https://librarysearch.unimelb.edu.au/
    openurl_base: https://unimelb.hosted.exlibrisgroup.com/sfxlcl41
    authentication: OpenAthens / University SSO
```
