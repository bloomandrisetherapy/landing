/**
 * Consult request handler for bloomandrisetherapy.com
 * Cloudflare Pages Function: POST /api/contact
 *
 * Environment variables (Pages > Settings > Variables and Secrets, set for
 * both Production and Preview):
 *   RESEND_API_KEY    required, secret. Resend API key.
 *   TO_EMAIL          required. Where consult requests land
 *                     (hello@bloomandrisetherapy.com).
 *   FROM_EMAIL        required. Verified Resend sender, either a bare address
 *                     (website@notify.bloomandrisetherapy.com) or
 *                     "Name <address>".
 *   HEALTH_TOKEN      optional, secret. Enables the daily health check.
 *   HEALTH_TO         optional. Where health checks go (Chad only).
 *   TURNSTILE_SECRET  optional, secret. Turns on the Cloudflare Turnstile check.
 *
 * Optional binding:
 *   SUBMISSIONS       KV namespace. When bound, every real request is saved
 *                     for 30 days before any email is sent, so a lead is never
 *                     lost even if email delivery fails.
 *
 * Health check: POST with header "x-health-token: <HEALTH_TOKEN>" and any valid
 * name, email and message. It sends one email to HEALTH_TO with a
 * "[Health check]" subject, skips the auto-reply and the saved copy, and never
 * touches the practice inbox.
 */

const PRACTICE = 'Bloom & Rise Therapy';
const SITE = 'bloomandrisetherapy.com';
const PHONE = '(346) 550 9348';
const PHONE_TEL = '+13465509348';
const PRACTICE_EMAIL = 'hello@bloomandrisetherapy.com';

// The three states Roshunda is licensed in. Anything else is flagged.
const STATES = { Texas: 'Texas', Virginia: 'Virginia', Colorado: 'Colorado', other: 'Another state' };

// Site palette: paper, bark, monarch orange, coneflower plum, morning sun.
const C = {
  paper: '#F7F0E3',
  wash: '#FBF1D9',
  bark: '#3A3227',
  bark2: '#6B6152',
  bark3: '#948B7A',
  orange: '#B4551C',
  plum: '#5F2A46',
  sun: '#F0D28A',
};

const json = (data, status = 200) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'content-type': 'application/json; charset=utf-8', 'cache-control': 'no-store' },
  });

const esc = (s = '') =>
  String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const validEmail = (e) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(String(e || '').trim());

// Constant-time compare so the health token can't be guessed by timing.
function sameToken(a = '', b = '') {
  if (!a || !b || a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

const SANS = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif";
const SERIF = "Georgia, 'Times New Roman', serif";
const label = (text, top = 14) =>
  `<div style="font-family:${SANS};font-size:10px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:${C.bark3};margin:${top}px 0 4px;">${esc(text)}</div>`;
const value = (html) =>
  `<div style="font-family:${SANS};font-size:16px;color:${C.bark};line-height:1.45;">${html}</div>`;

function shell(inner, footerNote) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="margin:0;padding:0;background:${C.paper};font-family:${SANS};color:${C.bark};">
<table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.paper};padding:32px 16px;">
  <tr><td align="center">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width:600px;width:100%;background:#FFFFFF;">
      <tr><td style="background:${C.plum};padding:28px 32px 24px;">
        <div style="font-family:${SERIF};font-size:26px;color:${C.paper};line-height:1;letter-spacing:-0.01em;">Bloom <i style="color:${C.sun};">&amp;</i> Rise</div>
        <div style="font-family:${SANS};font-size:10px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:${C.sun};margin-top:8px;">Therapy &middot; Katy, Texas and online</div>
      </td></tr>
      <tr><td style="height:4px;line-height:4px;font-size:0;background:${C.orange};">&nbsp;</td></tr>
      ${inner}
    </table>
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width:600px;width:100%;margin-top:18px;">
      <tr><td align="center" style="font-family:${SANS};font-size:11px;color:${C.bark2};padding:8px 16px;line-height:1.6;">${footerNote}</td></tr>
    </table>
  </td></tr>
</table>
</body></html>`;
}

function notification(f) {
  const subject = `Re: Your message to ${PRACTICE}`;
  const stateHtml = f.outOfState
    ? `${esc(f.stateLabel)} <span style="color:${C.orange};font-weight:600;">(not Texas, Virginia or Colorado)</span>`
    : esc(f.stateLabel);
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        <div style="font-family:${SANS};font-size:11px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:${C.orange};margin-bottom:14px;">New consult request</div>
        <h1 style="margin:0;font-family:${SERIF};font-size:30px;font-weight:400;line-height:1.15;color:${C.bark};">${esc(f.name)} reached out.</h1>
      </td></tr>
      <tr><td style="padding:24px 32px 8px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.wash};border-left:3px solid ${C.orange};">
          <tr><td style="padding:18px 22px;">
            ${label('Email', 0)}${value(`<a href="mailto:${esc(f.email)}" style="color:${C.orange};text-decoration:none;font-weight:600;">${esc(f.email)}</a>`)}
            ${f.phone ? label('Phone') + value(esc(f.phone)) : ''}
            ${label('State during sessions')}${value(stateHtml)}
            ${f.page ? label('Sent from') + value(esc(f.page)) : ''}
          </td></tr>
        </table>
      </td></tr>
      <tr><td style="padding:28px 32px 8px;">
        <div style="font-family:${SANS};font-size:11px;font-weight:600;letter-spacing:0.2em;text-transform:uppercase;color:${C.orange};margin-bottom:14px;">What brings them here</div>
        <div style="font-family:${SERIF};font-size:17px;line-height:1.65;color:${C.bark};white-space:pre-wrap;">${esc(f.message)}</div>
      </td></tr>
      <tr><td style="padding:32px 32px 8px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0"><tr>
          <td style="background:${C.orange};">
            <a href="mailto:${esc(f.email)}?subject=${encodeURIComponent(subject)}" style="display:inline-block;padding:14px 28px;font-family:${SANS};font-size:12px;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:${C.paper};text-decoration:none;">Reply to ${esc(f.name)}</a>
          </td>
        </tr></table>
        <div style="font-family:${SANS};font-size:12px;color:${C.bark2};margin-top:14px;line-height:1.5;">Hitting Reply in your inbox also works. It goes straight to ${esc(f.name)}.</div>
      </td></tr>
      <tr><td style="padding:24px 32px 36px;">
        <hr style="border:none;border-top:1px solid rgba(58,50,39,0.12);margin:0 0 16px;">
        <div style="font-family:${SANS};font-size:11px;color:${C.bark3};line-height:1.6;">Submitted ${esc(f.when)}<br>Via the consult form at <a href="https://www.${SITE}" style="color:${C.orange};text-decoration:none;">${SITE}</a></div>
      </td></tr>`;
  const text = [
    `${f.name} reached out through ${SITE}.`,
    '',
    `Email: ${f.email}`,
    f.phone ? `Phone: ${f.phone}` : null,
    `State during sessions: ${f.stateLabel}${f.outOfState ? ' (not Texas, Virginia or Colorado)' : ''}`,
    f.page ? `Sent from: ${f.page}` : null,
    '',
    f.message,
    '',
    `Submitted ${f.when}`,
  ].filter((l) => l !== null).join('\n');
  return {
    html: shell(inner, 'Someone used the consult form on your website. Reply to this email to answer them directly.'),
    text,
  };
}

function autoReply(f) {
  const first = f.name.split(/\s+/)[0];
  const link = `color:${C.orange};`;
  const outOfState = f.outOfState
    ? `<p style="margin:0 0 16px;">You mentioned you will be somewhere other than Texas, Virginia or Colorado. Licensing means I can only see therapy clients who are physically in one of those three states during sessions. Workshops are open anywhere, and if therapy with me isn't possible, I'll point you toward someone who can help.</p>`
    : '';
  const inner = `
      <tr><td style="padding:36px 32px 8px;">
        <h1 style="margin:0;font-family:${SERIF};font-size:28px;font-weight:400;line-height:1.2;color:${C.bark};">Thank you, ${esc(first)}. Your message reached me.</h1>
      </td></tr>
      <tr><td style="padding:20px 32px 8px;font-family:${SERIF};font-size:17px;line-height:1.65;color:${C.bark};">
        <p style="margin:0 0 16px;">I'll reply within two business days.</p>
        <p style="margin:0 0 16px;">If you haven't heard from me by then, please call <a href="tel:${PHONE_TEL}" style="${link}">${PHONE}</a> or email <a href="mailto:${PRACTICE_EMAIL}" style="${link}">${PRACTICE_EMAIL}</a>. Messages do get lost now and then, and I would rather hear from you twice than miss you.</p>
        ${outOfState}
        <p style="margin:0 0 16px;">The consult itself is fifteen minutes, by video or phone, and free. You tell me what brings you in, in whatever order it comes out. Nobody signs anything.</p>
        <p style="margin:0;">Roshunda</p>
        <p style="margin:2px 0 0;font-family:${SANS};font-size:12px;color:${C.bark2};">Roshunda M. Hartison, MEd, LPC</p>
      </td></tr>
      <tr><td style="padding:24px 32px 12px;">
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background:${C.wash};border-left:3px solid ${C.orange};">
          <tr><td style="padding:16px 20px;font-family:${SANS};font-size:13px;line-height:1.6;color:${C.bark};">
            <b style="color:${C.orange};">If you are in crisis, please don't wait on a reply.</b> Call or text <a href="tel:988" style="${link}font-weight:600;">988</a> for the Suicide and Crisis Lifeline, or call 911. This inbox is answered during business hours and isn't monitored for emergencies.
          </td></tr>
        </table>
      </td></tr>
      <tr><td style="padding:8px 32px 36px;font-family:${SANS};font-size:12px;line-height:1.6;color:${C.bark2};">
        Email isn't a secure channel, so please keep sensitive health details out of your reply. We can talk about those on the call.
      </td></tr>`;
  const text = [
    `Thank you, ${first}. Your message reached me.`,
    '',
    "I'll reply within two business days.",
    '',
    `If you haven't heard from me by then, please call ${PHONE} or email ${PRACTICE_EMAIL}. Messages do get lost now and then, and I would rather hear from you twice than miss you.`,
    '',
    f.outOfState
      ? "You mentioned you will be somewhere other than Texas, Virginia or Colorado. Licensing means I can only see therapy clients who are physically in one of those three states during sessions. Workshops are open anywhere, and if therapy with me isn't possible, I'll point you toward someone who can help.\n"
      : null,
    'The consult itself is fifteen minutes, by video or phone, and free. You tell me what brings you in, in whatever order it comes out. Nobody signs anything.',
    '',
    'Roshunda',
    'Roshunda M. Hartison, MEd, LPC',
    '',
    "If you are in crisis, please don't wait on a reply. Call or text 988 for the Suicide and Crisis Lifeline, or call 911. This inbox is answered during business hours and isn't monitored for emergencies.",
  ].filter((l) => l !== null).join('\n');
  return {
    html: shell(inner, `${esc(PRACTICE)} &middot; Katy, Texas, and online in Texas, Virginia and Colorado &middot; <a href="https://www.${SITE}" style="color:${C.bark2};">${SITE}</a>`),
    text,
  };
}

async function send(env, payload) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: { authorization: `Bearer ${env.RESEND_API_KEY}`, 'content-type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => '');
    throw new Error(`Resend ${res.status}: ${detail.slice(0, 300)}`);
  }
}

export async function onRequestPost({ request, env, waitUntil }) {
  let data;
  try {
    const ct = request.headers.get('content-type') || '';
    data = ct.includes('application/json') ? await request.json() : Object.fromEntries(await request.formData());
  } catch {
    return json({ ok: false, error: 'Could not read that submission.' }, 400);
  }

  // Honeypot: people never see this field, so anything in it is a bot.
  if (data.website || data._gotcha) return json({ ok: true });

  // A health check with a wrong or missing token is refused outright, so a
  // misconfigured monitor can never land a test in the practice inbox.
  const healthHeader = request.headers.get('x-health-token');
  const health = healthHeader !== null && sameToken(healthHeader, env.HEALTH_TOKEN || '');
  if (healthHeader !== null && !health) return json({ ok: false, error: 'Unauthorized.' }, 401);

  const stateKey = String(data.state || '').trim();
  const f = {
    name: String(data.name || '').trim().slice(0, 120),
    email: String(data.email || '').trim().slice(0, 200),
    phone: String(data.phone || '').trim().slice(0, 60),
    message: String(data.message || '').trim().slice(0, 5000),
    stateLabel: STATES[stateKey] || 'Not given',
    outOfState: stateKey === 'other',
    page: String(data.page || '').trim().slice(0, 80),
    when: new Date().toLocaleString('en-US', { timeZone: 'America/Chicago', dateStyle: 'full', timeStyle: 'short' }) + ' CT',
  };

  if (!f.name || !validEmail(f.email) || !f.message) {
    return json({ ok: false, error: 'Please add your name, a valid email, and a few words about what brings you here.' }, 400);
  }

  if (env.TURNSTILE_SECRET && !health) {
    const body = new FormData();
    body.append('secret', env.TURNSTILE_SECRET);
    body.append('response', data['cf-turnstile-response'] || '');
    const ip = request.headers.get('CF-Connecting-IP');
    if (ip) body.append('remoteip', ip);
    const v = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', { method: 'POST', body })
      .then((r) => r.json())
      .catch(() => ({ success: false }));
    if (!v.success) return json({ ok: false, error: 'The spam check didn’t go through. Please try again.' }, 400);
  }

  if (!env.RESEND_API_KEY || !env.TO_EMAIL || !env.FROM_EMAIL) {
    return json({ ok: false, error: 'Email is not configured yet.' }, 500);
  }
  if (health && !env.HEALTH_TO) {
    return json({ ok: false, error: 'HEALTH_TO is not set.' }, 500);
  }

  const from = /</.test(env.FROM_EMAIL) ? env.FROM_EMAIL : `${PRACTICE} <${env.FROM_EMAIL}>`;

  // Save first, so the request survives even if every email below fails.
  if (env.SUBMISSIONS && !health) {
    const key = `inquiry:${new Date().toISOString()}:${crypto.randomUUID().slice(0, 8)}`;
    try {
      await env.SUBMISSIONS.put(key, JSON.stringify({ ...f, delivered: false }), { expirationTtl: 60 * 60 * 24 * 30 });
      f.savedKey = key;
    } catch (err) {
      console.error('KV save failed', err);
    }
  }

  const note = notification(f);
  try {
    await send(env, {
      from,
      to: [health ? env.HEALTH_TO : env.TO_EMAIL],
      reply_to: f.email,
      subject: `${health ? '[Health check] ' : ''}New consult request from ${f.name}`,
      html: note.html,
      text: note.text,
    });
  } catch (err) {
    console.error(err);
    return json({ ok: false, error: `Your message didn't go through. Please call ${PHONE} or email ${PRACTICE_EMAIL}.` }, 502);
  }

  if (f.savedKey) {
    waitUntil(env.SUBMISSIONS.put(f.savedKey, JSON.stringify({ ...f, delivered: true }), { expirationTtl: 60 * 60 * 24 * 30 }).catch(() => {}));
  }

  // The visitor's confirmation is a courtesy. If it fails, the request still
  // reached Roshunda, so the visitor still sees success.
  if (!health) {
    const reply = autoReply(f);
    waitUntil(
      send(env, {
        from,
        to: [f.email],
        reply_to: env.TO_EMAIL,
        subject: `Thanks for reaching out to ${PRACTICE}`,
        html: reply.html,
        text: reply.text,
      }).catch((err) => console.error('Auto-reply failed', err)),
    );
  }

  return json({ ok: true });
}

export const onRequest = () => json({ ok: false, error: 'Method not allowed.' }, 405);
