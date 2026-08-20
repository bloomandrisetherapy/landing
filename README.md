# Bloom & Rise — launch page

One screen. Wordmark, headline, short intro, Roshunda's own line, and a two-field
signup wired for Kit. Built for the community health fair, and reusable as a
"coming soon" page until the full site ships.

`index.html` is self-contained. The artwork is embedded, so it opens with no build
step, no server, and no external image requests. Fonts come from Google Fonts.

```
index.html              the page
build.py                regenerates index.html
art-coneflower.webp     the embedded plate
og.png                  social preview card, must sit at the site root
qr-bloomandrise.png     QR code pointing at https://bloomandrisetherapy.com
```

## Preview locally

```
cd landing
python3 -m http.server 8000
```

Then open http://localhost:8000. Opening `index.html` by double-clicking works too,
but a local server matches production behaviour.

## Connecting Kit

Create the form in Kit, take the numeric ID out of its URL, and put it in `build.py`:

```python
KIT_FORM_ID = '1234567'
```

Then `python3 build.py`. The page posts `email_address` and `fields[first_name]` to
`https://app.kit.com/forms/<id>/subscriptions` and keeps the visitor on the page,
showing an inline confirmation. Until a real ID is set, submitting shows a notice
saying the form isn't connected yet, so it can't fail silently in front of anyone.

## Deploying

Cloudflare Pages, connected to this repo. Build command: none. Output directory:
`landing` (or move these files to the repo root and use `/`).

Confirm `og.png` resolves at `https://bloomandrisetherapy.com/og.png` after deploy,
since the social preview references an absolute URL.

## Email

`hello@bloomandrisetherapy.com` is referenced in the fine print and in the structured
data. Set it up as a free forward in Porkbun and point it wherever Roshunda wants it
to land. It does not need to exist for the page to work, but the link is live copy,
so set it before the event.

## Notes

Meta title, description, canonical, Open Graph, Twitter card, and ProfessionalService
JSON-LD are all in place, including licensure in Texas, Virginia, and Colorado.

Copy leads with individual therapy, body image and weight inclusive care, identity,
self trust, and anxiety. OCD appears only in the structured data service list, which
keeps it discoverable in search without making it the headline.

Palette is pulled straight from the artwork: monarch orange, coneflower magenta,
jade, morning yellow, on warm paper.
