// Key gate for the research site. Every request passes through here; without
// the right cookie you get the key form. Key lives in the RESEARCH_KEY env var.
export const config = { matcher: '/:path*' };

const COOKIE = 'research_key';

async function sha256(s) {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map(b => b.toString(16).padStart(2, '0')).join('');
}

function form(error) {
  return new Response(`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>Sanibha Research</title>
<style>body{font:15px system-ui,sans-serif;display:grid;place-items:center;min-height:100vh;margin:0;background:#f6f7f8;color:#1b2228}
@media(prefers-color-scheme:dark){body{background:#12171b;color:#e3e8ec}}
form{display:grid;gap:10px;width:min(320px,90vw)}input,button{font:inherit;padding:10px;border-radius:6px;border:1px solid #99a}
button{background:#1f5f7a;color:#fff;border:0;cursor:pointer}p{margin:0;color:#b33}</style>
<form method="post" action="/login"><strong>Sanibha category research</strong>
<input type="password" name="key" placeholder="Access key" autofocus required>${error ? '<p>Wrong key.</p>' : ''}
<button>Open</button></form>`, { status: 401, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' } });
}

export default async function middleware(request) {
  const key = process.env.RESEARCH_KEY;
  if (!key) return new Response('RESEARCH_KEY not set', { status: 500 });
  const want = await sha256(key);
  const url = new URL(request.url);

  if (url.pathname === '/login' && request.method === 'POST') {
    const given = (await request.formData()).get('key') || '';
    if ((await sha256(String(given))) !== want) return form(true);
    return new Response(null, {
      status: 303,
      headers: {
        location: '/',
        'set-cookie': `${COOKIE}=${want}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=2592000`,
      },
    });
  }

  const cookie = request.headers.get('cookie') || '';
  if (cookie.split(/;\s*/).includes(`${COOKIE}=${want}`)) return; // pass through to the static page
  return form(false);
}
