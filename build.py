import base64, os

HERE = os.path.dirname(os.path.abspath(__file__))

def b64(name, mime='image/webp'):
    with open(os.path.join(HERE, name), 'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode())

ART = b64('art-coneflower.webp')

# ── swap this one value for the real Kit form id and the form is live ──────────
KIT_FORM_ID = 'KIT_FORM_ID'

HTML = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Bloom &amp; Rise Therapy | Roshunda M. Hartison, MEd, LPC</title>
<meta name="description" content="Bloom &amp; Rise is a new therapy practice opening soon. Weight inclusive care for body image, identity, self trust, and anxiety. Online in Texas, Virginia, and Colorado with Roshunda M. Hartison, MEd, LPC.">
<link rel="canonical" href="https://bloomandrisetherapy.com/">
<meta name="robots" content="index,follow">
<meta name="theme-color" content="#FBF3E4">
<meta name="author" content="Roshunda M. Hartison, MEd, LPC">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Bloom &amp; Rise Therapy">
<meta property="og:url" content="https://bloomandrisetherapy.com/">
<meta property="og:title" content="Bloom &amp; Rise Therapy | Opening soon">
<meta property="og:description" content="A new therapy practice for the part where you change. Weight inclusive care for body image, identity, self trust, and anxiety. Online in Texas, Virginia, and Colorado.">
<meta property="og:image" content="https://bloomandrisetherapy.com/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Watercolour of a monarch butterfly resting on a coneflower">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Bloom &amp; Rise Therapy | Opening soon">
<meta name="twitter:description" content="A new therapy practice for the part where you change. Online in Texas, Virginia, and Colorado.">
<meta name="twitter:image" content="https://bloomandrisetherapy.com/og.png">

<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' fill='%23FBF3E4'/%3E%3Cpath d='M16 22c-3-6-8-8-10.5-5.5C3 19 5.5 24 9.5 25.5c2.5 1 5 .5 6.5-3.5z' fill='%23E4661C'/%3E%3Cpath d='M16 22c3-6 8-8 10.5-5.5C29 19 26.5 24 22.5 25.5c-2.5 1-5 .5-6.5-3.5z' fill='%230E6B5A'/%3E%3Cpath d='M16 9v14' stroke='%232A2118' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght,SOFT,WONK@0,9..144,300..700,0..100,0..1;1,9..144,300..700,0..100,0..1&family=Inter+Tight:wght@300;400;500;600&display=swap" rel="stylesheet">

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "additionalType": "https://schema.org/MedicalBusiness",
  "name": "Bloom & Rise Therapy",
  "url": "https://bloomandrisetherapy.com/",
  "image": "https://bloomandrisetherapy.com/og.png",
  "email": "hello@bloomandrisetherapy.com",
  "description": "Weight inclusive therapy for body image, identity, self trust, and anxiety. Online sessions for clients in Texas, Virginia, and Colorado.",
  "founder": {
    "@type": "Person",
    "name": "Roshunda M. Hartison",
    "honorificSuffix": "MEd, LPC",
    "jobTitle": "Licensed Professional Counselor"
  },
  "areaServed": [
    {"@type": "State", "name": "Texas"},
    {"@type": "State", "name": "Virginia"},
    {"@type": "State", "name": "Colorado"}
  ],
  "availableService": [
    {"@type": "Service", "name": "Individual therapy"},
    {"@type": "Service", "name": "Body image and weight inclusive care"},
    {"@type": "Service", "name": "Anxiety and OCD"},
    {"@type": "Service", "name": "Identity and life transitions"}
  ]
}
</script>

<style>
:root{
  --paper:#FBF3E4;
  --paper-2:#F5EAD6;
  --ink:#2A2118;
  --ink-2:#6B6152;
  --ink-3:#9A9080;
  --orange:#E4661C;
  --orange-deep:#B8410E;
  --coneflower:#C0447E;
  --jade:#0E6B5A;
  --sun:#F5C24B;
  --gut:clamp(1.6rem,6vw,6rem);
}
*,*::before,*::after{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{
  margin:0;min-height:100svh;background:var(--paper);color:var(--ink);
  font-family:'Inter Tight',system-ui,-apple-system,sans-serif;
  font-size:clamp(15.5px,1vw,17px);line-height:1.6;
  -webkit-font-smoothing:antialiased;
}
h1{
  font-family:'Fraunces',Georgia,serif;
  font-variation-settings:'SOFT' 60,'WONK' 1,'opsz' 120;
  font-weight:400;font-size:clamp(2.4rem,4.8vw,4.15rem);line-height:1.02;
  letter-spacing:-.03em;margin:0;
}
h1 em{font-style:italic;color:var(--orange-deep);font-variation-settings:'SOFT' 90,'WONK' 1}
a{color:inherit}
img{display:block;max-width:100%}
::selection{background:var(--sun);color:var(--ink)}
:focus-visible{outline:2px solid var(--orange);outline-offset:3px}
.skip{position:absolute;left:0;top:0;z-index:60;background:var(--ink);color:var(--paper);padding:.9rem 1.4rem;transform:translateY(-120%)}
.skip:focus{transform:none}

/* ─── frame ─────────────────────────────────────────────────── */
.wrap{
  height:100svh;min-height:620px;display:grid;
  grid-template-columns:minmax(0,1fr) minmax(0,.72fr);
  position:relative;overflow:clip;
}
/* the sun coming up once someone asks to be told */
.dawn{
  position:absolute;inset:0;z-index:0;pointer-events:none;opacity:0;
  transition:opacity 1.6s cubic-bezier(.3,.7,.3,1);
  background:
    radial-gradient(80% 62% at 6% 108%, rgba(228,102,28,.5) 0%, rgba(245,194,75,.3) 34%, rgba(251,243,228,0) 70%),
    linear-gradient(178deg, rgba(120,74,120,.16) 0%, rgba(230,150,80,.16) 46%, rgba(245,200,120,.3) 100%);
}
.dawn.on{opacity:1}

/* first light, low and warm behind the type */
.wrap::before{
  content:"";position:absolute;z-index:0;pointer-events:none;
  left:-18%;bottom:-42%;width:min(90vw,900px);aspect-ratio:1;border-radius:50%;
  background:radial-gradient(circle,rgba(245,194,75,.42) 0%,rgba(228,102,28,.16) 42%,rgba(251,243,228,0) 72%);
}

.col{position:relative;z-index:1;display:flex;flex-direction:column;
  padding:clamp(1.4rem,3vh,2.2rem) clamp(1.5rem,3vw,3.5rem) clamp(1.4rem,3vh,2.2rem) var(--gut);}
.col > .mid{flex:1;display:flex;flex-direction:column;justify-content:center;padding:clamp(1rem,2.5vh,2rem) 0}

.top{display:flex;align-items:baseline;justify-content:space-between;gap:1.5rem;padding-right:var(--gut)}
.mark{
  font-family:'Fraunces',serif;font-variation-settings:'SOFT' 60,'WONK' 1;
  font-size:1.3rem;font-weight:500;letter-spacing:-.02em;text-decoration:none;white-space:nowrap;
}
.mark i{font-style:italic;color:var(--orange);margin:0 .18em}

.eyebrow{
  font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--jade);
  font-weight:600;margin:0 0 1.15rem;
}
.lede{font-size:clamp(.98rem,1.05vw,1.06rem);line-height:1.62;color:var(--ink-2);max-width:42ch;margin:1.5rem 0 0}
.lede b{color:var(--ink);font-weight:600}

.quote{
  margin:1.9rem 0 0;padding-left:1.15rem;border-left:2px solid var(--coneflower);
  font-family:'Fraunces',serif;font-variation-settings:'SOFT' 80,'WONK' 1;
  font-style:italic;font-size:1rem;line-height:1.35;color:var(--ink);max-width:34ch;
}
.quote span{
  display:block;margin-top:.35rem;font-family:'Inter Tight',sans-serif;font-style:normal;
  font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-3);
}

/* ─── form ──────────────────────────────────────────────────── */
form{margin:clamp(1.4rem,3vh,2rem) 0 0;max-width:34rem}
.reveal{display:grid;grid-template-rows:0fr;opacity:0;
  transition:grid-template-rows .8s cubic-bezier(.2,.8,.3,1),opacity .6s ease .15s}
.reveal.on{grid-template-rows:1fr;opacity:1}
.reveal > div{overflow:hidden;min-height:0}
.fields{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:1rem;padding-top:.4rem}
@media (max-width:560px){.fields{grid-template-columns:1fr;gap:.6rem}}
.f{position:relative}
.f input{
  width:100%;font:inherit;font-size:1rem;color:var(--ink);
  background:transparent;border:0;border-bottom:1.5px solid rgba(42,33,24,.26);
  padding:.7rem 0;border-radius:0;transition:border-color .25s;
}
.f input::placeholder{color:var(--ink-3)}
.f input:focus{outline:none;border-bottom-color:var(--orange)}
.f input:user-invalid{border-bottom-color:var(--orange-deep)}
button{
  margin-top:1.25rem;font:inherit;font-weight:500;font-size:.86rem;letter-spacing:.14em;
  text-transform:uppercase;cursor:pointer;color:var(--ink);
  background:none;border:0;padding:.4rem 0;
  display:inline-flex;align-items:center;gap:1rem;transition:color .25s;
}
button::before{content:"";width:2.6rem;height:1.5px;background:var(--ink);transition:width .35s cubic-bezier(.2,.7,.3,1),background .25s}
button:hover{color:var(--orange-deep)}
button:hover::before{width:4rem;background:var(--orange-deep)}
button:disabled{color:var(--ink-3);cursor:default}
button:disabled::before{background:var(--ink-3);width:2.6rem}
.fine{font-size:.76rem;line-height:1.5;color:var(--ink-3);margin:1.15rem 0 0;max-width:48ch}
.fine a{color:var(--ink-2);text-underline-offset:3px}
.status{display:none;margin:1.4rem 0 0;font-size:.95rem;color:var(--jade);border-left:2px solid var(--jade);padding-left:1rem;max-width:44ch}
.status.on{display:block}
.status.bad{color:var(--orange-deep);border-color:var(--orange-deep)}
.hp{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}

.foot{padding-right:var(--gut);font-size:.68rem;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3)}

/* ─── art ───────────────────────────────────────────────────── */
.art{position:relative;z-index:1;overflow:hidden;background:var(--paper-2)}
.art img{position:absolute;inset:0}
.art img{width:100%;height:100%;object-fit:cover;object-position:52% 42%;
  animation:in 1.5s cubic-bezier(.16,.8,.3,1) both}
@keyframes in{from{opacity:0;transform:scale(1.04)}to{opacity:1;transform:none}}
.art::after{
  content:"";position:absolute;inset:0;pointer-events:none;mix-blend-mode:soft-light;
  background:radial-gradient(58% 46% at 30% 8%,rgba(255,236,180,.9),rgba(255,236,180,0) 70%);
}
.art::before{
  content:"";position:absolute;z-index:2;left:0;top:0;bottom:0;width:12%;pointer-events:none;
  background:linear-gradient(90deg,var(--paper),rgba(251,243,228,0));
}

@media (max-width:880px){
  .wrap{grid-template-columns:1fr;grid-template-rows:auto auto;height:auto;min-height:0}
  .col{padding:1.4rem 0 2.6rem var(--gut);order:2}
  .col > .mid{padding:1.6rem 0 0}
  .art{order:1;height:36svh;min-height:220px}
  .art img{object-position:50% 36%}
  .art::before{display:none}
  .art::after{mix-blend-mode:normal;background:linear-gradient(180deg,rgba(251,243,228,0) 58%,rgba(251,243,228,.55) 82%,var(--paper))}
  .top{order:0}
  .foot{margin-top:2.2rem}
  .wrap::before{bottom:-30%;left:-40%}
}
@media (prefers-reduced-motion:reduce){
  *{animation-duration:.001ms !important;transition-duration:.001ms !important}
}
</style>
</head>
<body>
<a class="skip" href="#join">Skip to the sign up form</a>

<div class="wrap">
  <span class="dawn" id="dawn"></span>
  <div class="col">
    <header class="top">
      <a class="mark" href="/">Bloom<i>&amp;</i>Rise</a>
    </header>

    <main class="mid" id="main">
      <p class="eyebrow">Opening soon</p>
      <h1>The light is already<br><em>changing.</em></h1>

      <p class="lede">
        <b>Bloom &amp; Rise</b> is a new practice from Roshunda M. Hartison, MEd, LPC.
        Individual therapy for body image and living well in the body you have, identity,
        self trust, anxiety, and the long middle of becoming someone new.
      </p>

      <blockquote class="quote">
        Without change, there would be no butterflies.
        <span>Roshunda M. Hartison, MEd, LPC</span>
      </blockquote>

      <form id="join" novalidate>
        <div class="reveal" id="reveal">
          <div>
            <div class="fields">
              <div class="f">
                <label class="hp" for="fname">First name</label>
                <input id="fname" name="fname" type="text" autocomplete="given-name" placeholder="First name" disabled required>
              </div>
              <div class="f">
                <label class="hp" for="email">Email address</label>
                <input id="email" name="email" type="email" autocomplete="email" placeholder="you@example.com" disabled required>
              </div>
            </div>
          </div>
        </div>
        <input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true">
        <button type="button" id="cta">Tell me when you open</button>
        <p class="fine">
          One note when the doors open, and nothing else. Unsubscribe any time, or write to
          <a href="mailto:hello@bloomandrisetherapy.com">hello@bloomandrisetherapy.com</a>.
          Please don't include private health details in this form.
        </p>
        <div class="status" id="status" role="status" aria-live="polite"></div>
      </form>
    </main>

    <footer class="foot">Roshunda M. Hartison, MEd, LPC &middot; Licensed in Texas, Virginia &amp; Colorado</footer>
  </div>

  <div class="art">
    <img src="__ART__" alt="Watercolour of a monarch butterfly resting on a purple coneflower" fetchpriority="high">
  </div>
</div>

<script>
(function(){
  'use strict';
  var FORM_ID = '__KIT_FORM_ID__';
  var ENDPOINT = 'https://app.kit.com/forms/' + FORM_ID + '/subscriptions';

  var form = document.getElementById('join');
  var reveal = document.getElementById('reveal');
  var dawn = document.getElementById('dawn');
  var opened = false;
  var status = document.getElementById('status');
  var btn = form.querySelector('button');

  function say(msg, bad){
    status.textContent = msg;
    status.className = 'status on' + (bad ? ' bad' : '');
  }

  document.getElementById('cta').addEventListener('click', function(){
    if(opened){ form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event('submit',{cancelable:true})); return; }
    opened = true;
    reveal.classList.add('on');
    dawn.classList.add('on');
    form.fname.disabled = false;
    form.email.disabled = false;
    btn.textContent = 'Join the list';
    setTimeout(function(){ form.fname.focus({preventScroll:true}); }, 420);
  });

  form.addEventListener('submit', function(e){
    e.preventDefault();
    if(!opened) return;
    if(form.website.value) return;                 /* honeypot */
    if(!form.checkValidity()){ form.reportValidity(); return; }

    if(FORM_ID.indexOf('KIT_') === 0){
      say('Form is not connected to Kit yet. Drop the Kit form ID into the FORM_ID value and this goes live.', true);
      return;
    }

    btn.disabled = true;
    btn.textContent = 'Sending';

    var body = new FormData();
    body.append('email_address', form.email.value);
    body.append('fields[first_name]', form.fname.value);

    fetch(ENDPOINT, {method:'POST', body:body, headers:{'Accept':'application/json'}})
      .then(function(r){ return r.ok ? r.json().catch(function(){return {};}) : Promise.reject(r); })
      .then(function(){
        reveal.classList.remove('on');
        btn.style.display = 'none';
        say('You are on the list. Roshunda will be in touch when Bloom & Rise opens.');
      })
      .catch(function(){
        btn.disabled = false;
        btn.textContent = 'Join the list';
        say('That did not go through. Please try again, or email hello@bloomandrisetherapy.com and we will add you by hand.', true);
      });
  });
})();
</script>
</body>
</html>
'''

HTML = HTML.replace('__ART__', ART).replace('__KIT_FORM_ID__', KIT_FORM_ID)

with open(os.path.join(HERE, 'index.html'), 'w') as f:
    f.write(HTML)
print('index.html written,', round(len(HTML)/1024), 'KB')
