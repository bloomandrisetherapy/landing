# Bloom & Rise Therapy: bloomandrisetherapy.com

Static site, deployed by Cloudflare Pages from the `main` branch (no build step,
output directory is the repo root). Every page is self-contained: artwork is embedded,
fonts come from Google Fonts.

- Consult form: Cloudflare Pages Function `functions/api/contact.js`, sent through Resend -> hello@bloomandrisetherapy.com (see below)
- Workshop interest form: Kit form 9823089
- Source and build scripts live in github.com/losmanzanos/Roshunda (staging preview)
- The previous "coming soon" landing page is saved on the `landing-page` branch

## Contact form (Resend, since November 2026)

The consult form (on `/contact`, `/about` and `/feels`) posts to `/api/contact`, a Cloudflare Pages Function in `functions/api/contact.js`. It sends through Resend from `website@notify.bloomandrisetherapy.com`, so it no longer depends on a Gmail sign-in, and a password change can't break it. The workshop interest form still goes to Kit and is unchanged.

What it sends:
- A branded notification to the practice inbox with name, email, phone, the state the person will be in during sessions (flagged if it isn't Texas, Virginia or Colorado), the page they sent it from, and their message. Hitting Reply answers the visitor.
- A short confirmation to the visitor: two business day reply time, phone, email, the 988 line, and a note if they picked another state.

Cloudflare Pages > Settings > Variables and Secrets (set for Production and Preview):

| Name | What |
|---|---|
| `RESEND_API_KEY` | Secret. Resend API key for this domain |
| `TO_EMAIL` | `hello@bloomandrisetherapy.com` |
| `FROM_EMAIL` | `website@notify.bloomandrisetherapy.com` |
| `HEALTH_TOKEN` | Secret. Random string used by the daily health check |
| `HEALTH_TO` | Where health checks go (not the practice inbox) |
| `TURNSTILE_SECRET` | Optional. Turns on the Cloudflare Turnstile spam check |

Optional: bind a KV namespace as `SUBMISSIONS` and every request is saved for 30 days before any email goes out, so nothing is lost if email delivery fails.

Health check: POST to `/api/contact` with header `x-health-token: <HEALTH_TOKEN>` and a JSON body with a name, a valid email and a message. It emails only `HEALTH_TO`, with a `[Health check]` subject, sends no auto-reply, saves nothing, and never touches the practice inbox. A wrong token gets a 401 and sends nothing.

To rotate the Resend key: create a new key in Resend, paste it into `RESEND_API_KEY`, redeploy, then delete the old key.

If the form ever shows an error, visitors get the phone number and email address directly, so no one is left without a way to reach the practice. Keep the old EmailJS service connected for a week after the switch, then retire it.
