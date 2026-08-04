## Context

The `loris` and `seyis` apps send branded confirmation emails via the shared `tools.send_sucess_mail()` utility, rendering HTML templates with hardcoded logo URLs. The `loris` template (`loris/templates/loris/mail.html`) points to `https://cancunconciergedmc.com/loris/imgs/logo.png`, which returns 404 because that asset was never uploaded to the WordPress frontend host — producing a broken image in emails. The `seyis` template (`seyis/templates/seyis/mail.html`), cloned from `loris`, omits the logo entirely.

The site-wide logo `https://cancunconciergedmc.com/imgs/logo.png` is confirmed to return HTTP 200 and is hosted in the same site-wide directory pattern already used elsewhere in the ecosystem (e.g. `rhea_peeyush` uses `/imgs/logo-v1.png`).

## Goals / Non-Goals

**Goals:**
- Make the loris confirmation email render the site-wide logo.
- Make the seyis confirmation email render the same site-wide logo.
- Keep changes scoped strictly to the `loris` and `seyis` email templates.

**Non-Goals:**
- No changes to other apps' email templates.
- No changes to `tools.send_sucess_mail()`, models, views, or API behavior.
- No change to where the logo is hosted (it already exists on the frontend host).

## Decisions

| Decision | Choice | Rationale |
|---|---|---|
| **Logo URL** | Use `https://cancunconciergedmc.com/imgs/logo.png` | Verified HTTP 200; site-wide asset already in use; avoids any dependency on per-app paths that may not be deployed |
| **loris template edit** | Replace `src` of the existing `<img>` with the site-wide URL | Minimal diff; element, width, and alt text stay as-is |
| **seyis template edit** | Insert the same `<img>` element above the `<h2>` "Name" block, matching loris's structure | Restores branding parity with the app it was cloned from |
| **Deployment of asset** | None required | The image already exists on `cancunconciergedmc.com`; this is purely a code change |
| **Static `logo.png` copies** | Left untouched | `loris/static/loris/imgs/logo.png` and any seyis copy are not referenced by the email templates; removing them is out of scope |

## Risks / Trade-offs

- [Email clients block external images by default] → Same exposure as all other apps in this repo; end users can "display images". Acceptable, and the current pattern across the project.
- [External URL check is network-dependent and could be flaky as a CI test] → The "Logo URL resolves" scenario is intentionally a manual/out-of-band verification (mirrored by tasks 3.2 via `curl`), not an automated CI test. Decision: keep the network check.
- [If the frontend host ever removes `/imgs/logo.png`, logos break] → Same host serves all other apps' logos; single shared asset reduces the number of distinct URLs to maintain.
- [Template assertions in tests] → Tests asserting on rendered HTML must use the new URL; the template-render check in `tools.send_sucess_mail` is unaffected.
