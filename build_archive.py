import os, re, datetime
files = sorted([f for f in os.listdir('.') if re.match(r'^\d{4}-\d{2}-\d{2}\.html$', f)], reverse=True)
def label(f):
    d=f[:-5]
    try: return datetime.date.fromisoformat(d).strftime('%-d %B %Y')
    except Exception: return d
rows = "\n".join(f'    <li><a href="{f}">{label(f)}</a></li>' for f in files) or '    <li>No digests yet.</li>'
doc = f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Papers Digest — Archive</title><style>
:root{{--bg:#0f1419;--card:#1a212b;--ink:#e8edf2;--muted:#9bb0c3;--accent:#5cc8ff;--line:#2c3a49}}
body{{margin:0;background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;line-height:1.5}}
.wrap{{max-width:720px;margin:0 auto;padding:44px 22px 60px}}
h1{{font-size:24px;margin:0 0 6px}}
p.sub{{color:var(--muted);margin:0 0 22px;font-size:14px}}
a.latest{{display:inline-block;margin-bottom:18px;color:var(--accent);text-decoration:none;font-size:14px}}
ul{{list-style:none;padding:0;margin:0}}
li{{border:1px solid var(--line);border-radius:10px;margin:8px 0;background:var(--card)}}
li a{{display:block;padding:13px 18px;color:var(--ink);text-decoration:none;font-size:16px}}
li a:hover{{color:var(--accent)}}
</style></head><body><div class="wrap">
<h1>Papers Digest — Archive</h1>
<p class="sub">{len(files)} digest(s) · newest first</p>
<a class="latest" href="index.html">→ Latest digest</a>
<ul>
{rows}
</ul></div></body></html>"""
open("archive.html","w",encoding="utf-8").write(doc)
print("archive.html built:", len(files), "entries")
