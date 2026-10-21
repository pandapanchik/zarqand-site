"""Zarqand menu page: menu_data.py -> menu-desktop.html / menu-mobile.html with fonts and images inlined.

Same pipeline as build.py: html_to_figma does not fetch external URLs, so everything is embedded.
"""
import html
import pathlib

from build import IMG_DIR, ROOT, b64, font_css
from menu_data import ASOSIY, CATEGORIES, ICHIMLIK, KABOB, SALATLAR, SHIRINLIK, SHORVALAR, XAMIR

STAR = '<svg class="star" viewBox="0 0 24 24"><path d="M12 1 23 12 12 23 1 12Z"/><path d="M4.2 4.2h15.6v15.6H4.2Z"/></svg>'
ARCH_LINE = ('<svg class="arch-line" viewBox="0 0 100 130" preserveAspectRatio="none">'
             '<path vector-effect="non-scaling-stroke" d="M1 130V50C1 22 28 8 50 1 72 8 99 22 99 50V130"/></svg>')
AI = '<span class="ai">AI rasm · almashtiriladi</span>'

CSS = """
{{FONTS}}
:root{
  --lapis:#0D2A33; --lapis-d:#081D24; --lapis-t:#14394A; --feruza:#1F6F78; --zar:#C9A063; --zar-l:#E6CB98;
  --anor:#8B1E2D; --qand:#F4EADB; --komir:#120E0C; --ink:#14313A; --ink-s:#3D555C;
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:var(--lapis-d)}
body{font-family:'Mulish',sans-serif;-webkit-font-smoothing:antialiased}
.page{width:1440px;margin:0 auto;background:var(--lapis);color:var(--qand);overflow:hidden;position:relative}
.page.m{width:390px}
.serif{font-family:'Gloock',serif;font-weight:400}
svg.star{width:14px;height:14px;fill:currentColor;flex:none}
.ai{position:absolute;left:50%;bottom:14px;transform:translateX(-50%);font-size:10px;letter-spacing:.08em;text-transform:uppercase;font-weight:700;color:var(--qand);background:rgba(8,29,36,.62);border:1px solid rgba(201,160,99,.5);padding:4px 9px;border-radius:99px;white-space:nowrap}
.ph{display:inline-block;color:var(--zar-l);background:rgba(201,160,99,.14);border:1px dashed rgba(201,160,99,.6);border-radius:6px;padding:0 6px}
.light .ph{color:var(--anor);background:rgba(139,30,45,.07);border-color:rgba(139,30,45,.45)}
.btn{display:inline-flex;align-items:center;gap:12px;height:56px;padding:0 30px;border-radius:99px;font-weight:800;font-size:16px;letter-spacing:.02em;text-decoration:none;white-space:nowrap}
.btn-anor{background:var(--anor);color:var(--qand)}
.btn-qand{background:var(--qand);color:var(--ink)}
.btn svg{width:18px;height:18px}
.h2{font-family:'Gloock',serif;font-weight:400;font-size:72px;line-height:1;letter-spacing:-.02em}
.lede{font-size:18px;line-height:1.6;max-width:460px}
.pattern{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.light{background:var(--qand);color:var(--ink)}
.arch-wrap{position:relative}
.arch-line{position:absolute;inset:-14px -14px 0 -14px;width:calc(100% + 28px);height:calc(100% + 14px);overflow:visible}
.arch-line path{fill:none;stroke:var(--zar);stroke-width:1.2}
.arch{position:absolute;inset:0;background-size:cover;background-position:center;overflow:hidden}
.pic{position:relative;background-size:cover;background-position:center}
/* one dish row: name + note on the left, price on the right; space separates rows */
.it{display:grid;grid-template-columns:1fr auto;column-gap:24px;align-items:baseline}
.it b{font-size:19px;font-weight:800}
.it .pr{font-size:18px;font-weight:800;white-space:nowrap;font-variant-numeric:tabular-nums}
.it span.d{grid-column:1/2;font-size:15px;line-height:1.5;margin-top:4px}
.list{display:flex;flex-direction:column;gap:22px}
.grp h3{font-family:'Gloock',serif;font-weight:400;font-size:32px;margin-bottom:26px}
.grp+.grp{margin-top:64px}

/* ---------- NAV ---------- */
.nav{display:flex;align-items:center;justify-content:space-between;padding:28px 64px}
.logo{display:flex;align-items:center;gap:10px;color:var(--zar);font-size:30px;text-decoration:none}
.logo svg{width:22px;height:22px}
.links{display:flex;gap:40px;font-size:15px;font-weight:600}
.links a{color:var(--qand);text-decoration:none;opacity:.85}
.links a.on{opacity:1;color:var(--zar-l)}
.nav .btn{height:46px;padding:0 22px;font-size:14px}
.burger{display:none}

/* ---------- HERO: printed card beside the room ---------- */
.hero{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:0 64px;height:800px}
.card{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center;background:var(--qand);color:var(--ink);overflow:hidden;padding:0 56px 48px}
.stripe{display:flex;align-self:stretch;margin:0 -56px;height:56px;flex:none}
.stripe i{flex:none;width:28px;height:56px;background:var(--lapis)}
.stripe i:nth-child(even){background:var(--zar)}
.card .logo{margin-top:76px;color:var(--lapis);font-size:34px}
.card .logo svg{color:var(--zar);width:24px;height:24px}
.card h1{font-family:'Gloock',serif;font-weight:400;font-size:96px;line-height:.95;letter-spacing:-.03em;color:var(--lapis);margin-top:44px}
.card .sub{font-size:18px;line-height:1.6;color:var(--ink);max-width:430px;margin-top:28px}
.card .btn{margin-top:36px}
.jump{display:flex;flex-wrap:wrap;justify-content:center;gap:12px 28px;margin-top:auto;max-width:470px;font-size:16px;font-weight:700;color:var(--lapis)}
.jump a{color:var(--lapis);text-decoration:none}
.card .ph{margin-top:22px;font-size:14px;color:var(--anor);background:rgba(139,30,45,.07);border-color:rgba(139,30,45,.45)}
.hero .pic{height:100%}

/* ---------- SALATLAR: the printed sheet on the tablecloth ---------- */
.sheet-sec{position:relative;background:var(--feruza);padding:170px 64px}
.sheet-sec .pattern{opacity:.13}
.sheet-in{position:relative;display:grid;grid-template-columns:1fr 760px;gap:12px}
.sheet-in .pic{min-height:100%}
.sheet{position:relative;background:var(--qand);color:var(--ink);padding:84px 80px 76px}
.scallop{position:absolute;left:0;right:0;display:flex;justify-content:space-between;padding:0 4px;height:24px;overflow:hidden}
.scallop i{flex:none;width:24px;height:24px;border-radius:50%;background:var(--feruza)}
.scallop.t{top:-12px}
.scallop.b{bottom:-12px}
.sheet .h2{font-size:60px;text-align:center;color:var(--lapis)}
.sheet .note{font-size:17px;line-height:1.6;text-align:center;color:var(--ink);margin-top:16px}
.sheet .grp{margin-top:60px}
.sheet .grp+.grp{margin-top:60px}
.sheet .grp h3{text-align:center;color:var(--anor);font-size:30px;margin-bottom:28px}
.sheet .it .pr{color:var(--anor)}
.sheet .it span.d{color:var(--ink-s)}
.sheet .ph{color:var(--anor);background:rgba(139,30,45,.07);border-color:rgba(139,30,45,.45)}
.sheet .hours{margin-top:64px;text-align:center;font-size:16px;line-height:1.7;color:var(--ink)}

/* ---------- SHO'RVALAR: giant word, filled bars ---------- */
.soup{position:relative;background:var(--lapis);padding:150px 64px 170px}
.soup .h2{font-size:226px;line-height:.82;letter-spacing:-.045em;color:var(--zar);margin-left:-10px}
.soup-row{display:grid;grid-template-columns:5fr 7fr;gap:12px;margin-top:56px}
.soup-row .pic{min-height:100%}
.soup-row .lede{color:var(--qand);max-width:560px;margin-bottom:36px}
.bars{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.bar{background:var(--lapis-t);padding:32px 28px}
.bar .it b{font-family:'Gloock',serif;font-weight:400;font-size:28px;color:var(--qand)}
.bar .it .pr{color:var(--zar-l)}
.bar .it span.d{color:rgba(244,234,219,.82);margin-top:8px}

/* ---------- ASOSIY: tall arch beside the list ---------- */
.main{display:grid;grid-template-columns:560px 1fr;gap:120px;padding:170px 64px;align-items:stretch}
.main .arch-wrap{height:100%;min-height:1000px}
.main .arch{border-radius:280px 280px 0 0}
.main .arch-line path{stroke:var(--anor)}
.main .h2{color:var(--lapis)}
.main .lede{margin-top:22px;color:var(--ink)}
.main .grp{margin-top:72px}
.main .grp+.grp{margin-top:64px}
.main .grp h3{color:var(--anor)}
.main .it .pr{color:var(--anor)}
.main .it span.d{color:var(--ink-s)}

/* ---------- XAMIR: photo row, three text columns ---------- */
.dough{background:var(--lapis-d);padding:170px 64px}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:60px}
.head .lede{color:var(--qand)}
.dough .h2{color:var(--zar-l)}
.prow{display:grid;grid-template-columns:5fr 7fr;gap:12px;margin-top:64px;height:600px}
.prow .pic{height:100%}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:56px;margin-top:80px}
.cols .it b{font-family:'Gloock',serif;font-weight:400;font-size:28px;color:var(--zar-l)}
.cols .it span.d{color:rgba(244,234,219,.82)}
.cols .it .pr{grid-column:1/-1;margin-top:10px;color:var(--qand)}
.cols .list{gap:40px}

/* ---------- KABOB: list beside a photograph that runs to the edge ---------- */
.grill{display:grid;grid-template-columns:1fr 1fr;background:var(--komir)}
.grill-l{padding:170px 96px 170px 64px}
.grill .h2{color:var(--qand)}
.grill .lede{margin-top:22px;color:var(--qand)}
.grill .grp{margin-top:72px}
.grill .grp+.grp{margin-top:60px}
.grill .grp h3{color:var(--zar)}
.grill .it .pr{color:var(--zar-l)}
.grill .it span.d{color:rgba(244,234,219,.8)}
.grill .pic{min-height:100%}

/* ---------- SHIRINLIKLAR: centred, list on both sides of the arch ---------- */
.sweet{position:relative;padding:170px 64px}
.sweet .pattern{opacity:.07}
.sweet .h2{position:relative;text-align:center;color:var(--lapis)}
.sweet .lede{position:relative;text-align:center;margin:22px auto 0;color:var(--ink)}
.trio{position:relative;display:grid;grid-template-columns:1fr 400px 1fr;gap:80px;margin-top:90px;align-items:center}
.trio .arch-wrap{height:540px}
.trio .arch{border-radius:200px 200px 0 0}
.trio .arch-line path{stroke:var(--anor)}
.trio .list{gap:34px}
.trio .it b{font-family:'Gloock',serif;font-weight:400;font-size:27px;color:var(--lapis)}
.trio .it .pr{color:var(--anor)}
.trio .it span.d{color:var(--ink-s)}

/* ---------- ICHIMLIKLAR: four columns ---------- */
.drinks{background:var(--lapis);padding:170px 64px}
.drinks .h2{color:var(--qand)}
.dwrap{display:grid;grid-template-columns:5fr 7fr;gap:12px;margin-top:72px}
.dwrap .pic{min-height:100%}
.dcols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.dcol{background:var(--lapis-t);padding:36px 30px 40px}
.dcol h3{font-family:'Gloock',serif;font-weight:400;font-size:30px;color:var(--zar);margin-bottom:28px}
.dcol .list{gap:16px}
.dcol .it b{font-size:17px;font-weight:700;color:var(--qand)}
.dcol .it .pr{font-size:17px;color:var(--zar-l)}

/* ---------- CTA: last photograph, text beside ---------- */
.cta{position:relative;height:780px;background-size:cover;background-position:center}
.cta .shade{position:absolute;inset:0;background:rgba(8,14,16,.58)}
.cta-t{position:absolute;left:792px;right:64px;bottom:110px}
.cta .h2{font-size:64px;color:var(--qand)}
.cta p{font-size:18px;line-height:1.6;color:var(--qand);margin-top:22px;max-width:480px}
.cta .btn{margin-top:34px}
.cta .ai{left:auto;right:24px;top:24px;bottom:auto;transform:none}

/* ---------- FOOTER: photograph half, menu half ---------- */
.foot{display:grid;grid-template-columns:1fr 1fr;background:var(--lapis-d);min-height:820px}
.foot .pic{min-height:100%;background-size:170%;background-position:40% 55%}
.foot-r{display:flex;flex-direction:column;padding:80px 64px 40px 96px}
.foot-r .logo{font-size:26px}
.fmenu{display:flex;flex-direction:column;gap:14px;margin-top:56px}
.fmenu a{font-family:'Gloock',serif;font-size:40px;line-height:1.1;color:var(--qand);text-decoration:none}
.fcon{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:64px;font-size:15px;line-height:1.7;color:var(--qand)}
.fcon b{display:block;font-size:16px;color:var(--zar-l);margin-bottom:6px}
.legal{margin-top:auto;padding-top:48px;font-size:13px;color:rgba(244,234,219,.75)}

/* =================== MOBILE (390) =================== */
.m .nav{padding:22px 20px}
.m .logo{font-size:26px}
.m .links,.m .nav .btn{display:none}
.m .burger{display:flex;width:46px;height:46px;border-radius:50%;border:1px solid var(--zar);align-items:center;justify-content:center;color:var(--zar)}
.m .burger svg{width:20px;height:20px}
.m .h2{font-size:44px}
.m .lede{font-size:16px}
.m .it b{font-size:17px}
.m .it .pr{font-size:16px}
.m .it span.d{font-size:14px}
.m .grp h3{font-size:26px;margin-bottom:20px}
.m .hero{display:flex;flex-direction:column;height:auto;padding:0 20px;gap:0}
.m .hero .pic{height:340px;order:-1}
.m .card{margin-top:-24px;padding:0 22px 34px}
.m .stripe{margin:0 -22px;height:40px}
.m .stripe i{height:40px;width:20px}
.m .card .logo{margin-top:40px;font-size:26px}
.m .card h1{font-size:58px;margin-top:22px}
.m .card .sub{font-size:16px;margin-top:20px}
.m .card .btn{margin-top:26px;align-self:stretch;justify-content:center}
.m .jump{margin-top:34px;font-size:15px;gap:10px 20px}
.m .sheet-sec{padding:96px 10px}
.m .sheet-in{grid-template-columns:1fr;gap:28px}
.m .sheet-in .pic{height:380px;min-height:0}
.m .sheet{padding:56px 22px 52px}
.m .scallop i{width:18px;height:18px}
.m .scallop{height:18px}
.m .scallop.t{top:-9px}
.m .scallop.b{bottom:-9px}
.m .sheet .h2{font-size:38px}
.m .sheet .note{font-size:15px}
.m .sheet .grp,.m .sheet .grp+.grp{margin-top:44px}
.m .sheet .grp h3{font-size:24px;margin-bottom:20px}
.m .sheet .ph{color:var(--anor);background:rgba(139,30,45,.07);border-color:rgba(139,30,45,.45)}
.sheet .hours{margin-top:44px;font-size:15px}
.m .soup{padding:96px 20px}
.m .soup .h2{font-size:84px;margin-left:-4px}
.m .soup-row{grid-template-columns:1fr;gap:30px;margin-top:28px}
.m .soup-row .pic{height:360px;min-height:0}
.m .soup-row .lede{margin-bottom:28px}
.m .bars{grid-template-columns:1fr;gap:6px}
.m .bar{padding:20px 18px}
.m .bar .it b{font-size:23px}
.m .main{grid-template-columns:1fr;gap:56px;padding:96px 20px}
.m .main .arch-wrap{min-height:0;height:420px;width:310px;justify-self:center;margin-top:14px}
.m .main .arch{border-radius:155px 155px 0 0}
.m .main .grp{margin-top:48px}
.m .main .grp+.grp{margin-top:44px}
.m .dough{padding:96px 20px}
.m .head{flex-direction:column;align-items:flex-start;gap:18px}
.m .prow{grid-template-columns:1fr;height:auto;margin-top:40px;gap:8px}
.m .prow .pic{height:300px}
.m .prow .pic:last-child{height:220px}
.m .cols{grid-template-columns:1fr;gap:34px;margin-top:48px}
.m .cols .list{gap:34px}
.m .cols .it b{font-size:24px}
.m .grill{grid-template-columns:1fr}
.m .grill .pic{order:-1;height:340px;min-height:0}
.m .grill-l{padding:72px 20px 96px}
.m .grill .grp{margin-top:48px}
.m .grill .grp+.grp{margin-top:44px}
.m .sweet{padding:96px 20px}
.m .trio{grid-template-columns:1fr;gap:44px;margin-top:56px}
.m .trio .arch-wrap{order:-1;height:400px;width:300px;justify-self:center}
.m .trio .arch{border-radius:150px 150px 0 0}
.m .trio .list{gap:28px}
.m .trio .it b{font-size:23px}
.m .drinks{padding:96px 20px}
.m .dwrap{grid-template-columns:1fr;gap:8px;margin-top:44px}
.m .dwrap .pic{height:400px;min-height:0}
.m .dcols{grid-template-columns:1fr;gap:8px}
.m .dcol{padding:28px 20px 30px}
.m .dcol h3{font-size:26px;margin-bottom:20px}
.m .cta{height:auto;background-size:auto;background:var(--lapis-d)}
.m .cta .pic{height:420px}
.m .cta .shade{display:none}
.m .cta-t{position:static;padding:44px 20px 72px}
.m .cta .h2{font-size:38px}
.m .cta p{font-size:16px}
.m .cta .btn{align-self:stretch;justify-content:center;display:flex}
.m .foot{grid-template-columns:1fr;min-height:0}
.m .foot .pic{height:300px;min-height:0}
.m .foot-r{padding:48px 20px 34px}
.m .fmenu{gap:12px;margin-top:34px}
.m .fmenu a{font-size:30px}
.m .fcon{grid-template-columns:1fr;gap:22px;margin-top:44px}
"""

PATTERN = ('<svg class="pattern" aria-hidden="true"><defs><pattern id="{id}" width="72" height="72" patternUnits="userSpaceOnUse">'
           '<g fill="none" stroke="{c}" stroke-width="1"><path d="M36 16 56 36 36 56 16 36Z"/><path d="M21.9 21.9h28.2v28.2H21.9Z"/>'
           '<path d="M0 0 21.9 21.9M72 0 50.1 21.9M0 72 21.9 50.1M72 72 50.1 50.1"/></g></pattern></defs>'
           '<rect width="100%" height="100%" fill="url(#{id})"/></svg>')

e = html.escape


def item(name, desc, price):
    return f'<div class="it"><b>{e(name)}</b><span class="pr">{e(price)}</span><span class="d">{e(desc)}</span></div>'


def drink(name, price):
    return f'<div class="it"><b>{e(name)}</b><span class="pr">{e(price)}</span></div>'


def group(title, rows):
    return f'<div class="grp"><h3>{e(title)}</h3><div class="list">{"".join(item(*r) for r in rows)}</div></div>'


def page(mode: str) -> str:
    m = mode == "m"
    img = lambda name: "data:image/jpeg;base64," + b64(IMG_DIR / f"{name}.jpg")
    bg = lambda name, cls="pic", extra="": f'<div class="{cls}" style="background-image:url(\'{img(name)}\')">{extra}{AI}</div>'
    stripe = "<i></i>" * (18 if m else 24)
    scallop = "<i></i>" * (17 if m else 26)
    jump = "".join(f'<a href="#{k}">{e(v)}</a>' for k, v in CATEGORIES)
    sweet_l, sweet_r = SHIRINLIK[:4], SHIRINLIK[4:]

    body = f"""
<nav class="nav">
  <a class="logo serif" href="#">{STAR}Zarqand</a>
  <div class="links"><a class="on" href="#">Menyu</a><a href="#">Oqshom</a><a href="#">Sharhlar</a><a href="#">Aloqa</a></div>
  <a class="btn btn-anor" href="#">Stol band qilish</a>
  <span class="burger"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><path d="M4 8h16M4 16h11"/></svg></span>
</nav>

<section class="hero">
  <div class="card">
    <div class="stripe">{stripe}</div>
    <span class="logo serif">{STAR}Zarqand</span>
    <h1>Zarqand menyusi</h1>
    <p class="sub">Taomlar dasturxon tartibida: non va salatdan boshlab sho‘rva, osh va kabobgacha, oxirida choy bilan shirinlik.</p>
    <a class="btn btn-anor" href="#">Stol band qilish</a>
    <div class="jump">{jump}</div>
    <span class="ph">[Narxlar namuna — restoran tasdiqlaydi]</span>
  </div>
  {bg("interyer")}
</section>

<section class="sheet-sec" id="salatlar">
  {PATTERN.format(id="p1", c="#E6CB98")}
  <div class="sheet-in">
  {bg("salat")}
  <div class="sheet">
    <div class="scallop t">{scallop}</div>
    <h2 class="h2">Salatlar va gazaklar</h2>
    <p class="note">Dasturxon non sindirishdan boshlanadi.</p>
    {"".join(group(t, rows) for t, rows in SALATLAR)}
    <p class="hours">Oshxona har kuni ochiq<br><span class="ph">[soat] dan [soat] gacha</span></p>
    <div class="scallop b">{scallop}</div>
  </div>
  </div>
</section>

<section class="soup" id="shorvalar">
  <h2 class="h2">Sho‘rvalar</h2>
  <div class="soup-row">
    {bg("shorva")}
    <div>
      <p class="lede">Issiq sho‘rva osh oldidan keladi. Har biri sopol kosada, tandir noni bilan beriladi.</p>
      <div class="bars">{"".join(f'<div class="bar">{item(*r)}</div>' for r in SHORVALAR)}</div>
    </div>
  </div>
</section>

<section class="main light" id="asosiy">
  <div class="arch-wrap">{ARCH_LINE}{bg("osh", "arch")}</div>
  <div>
    <h2 class="h2">Asosiy taomlar</h2>
    <p class="lede">Dasturxonning to‘ri: osh va qozon taomlari, o‘tin olovida tayyorlanadi.</p>
    {"".join(group(t, rows) for t, rows in ASOSIY)}
  </div>
</section>

<section class="dough" id="xamir">
  <div class="head">
    <h2 class="h2">Xamir taomlar</h2>
    <p class="lede">Manti, chuchvara va somsa har kuni qo‘lda tugiladi.</p>
  </div>
  <div class="prow">{bg("manti")}{bg("samsa")}</div>
  <div class="cols">
    <div class="list">{"".join(item(*r) for r in XAMIR[:3])}</div>
    <div class="list">{"".join(item(*r) for r in XAMIR[3:5])}</div>
    <div class="list">{"".join(item(*r) for r in XAMIR[5:])}</div>
  </div>
</section>

<section class="grill" id="kabob">
  <div class="grill-l">
    <h2 class="h2">Kabob va shashlik</h2>
    <p class="lede">Cho‘g‘da, buyurtmangizdan keyin pishiriladi. Piyoz va tandir noni bilan.</p>
    {"".join(group(t, rows) for t, rows in KABOB)}
  </div>
  {bg("shashlik")}
</section>

<section class="sweet light" id="shirinlik">
  {PATTERN.format(id="p2", c="#8B1E2D")}
  <h2 class="h2">Shirinliklar</h2>
  <p class="lede">Oqshom choy bilan yakunlanadi: navvot, halva va uy shirinliklari.</p>
  <div class="trio">
    <div class="list">{"".join(item(*r) for r in sweet_l)}</div>
    <div class="arch-wrap">{ARCH_LINE}{bg("choy", "arch")}</div>
    <div class="list">{"".join(item(*r) for r in sweet_r)}</div>
  </div>
</section>

<section class="drinks" id="ichimlik">
  <div class="head">
    <h2 class="h2">Ichimliklar</h2>
    <p class="lede">Choy choynakda, kompot va limonad uyda tayyorlanadi.</p>
  </div>
  <div class="dwrap">
  {bg("ichimlik")}
  <div class="dcols">
    {"".join(f'<div class="dcol"><h3>{e(t)}</h3><div class="list">{"".join(drink(*r) for r in rows)}</div></div>' for t, rows in ICHIMLIK)}
  </div>
  </div>
</section>
"""
    if m:
        body += f"""
<section class="cta">
  {bg("dasturxon")}
  <div class="cta-t">
    <h2 class="h2">Stolingiz tayyor turadi</h2>
    <p>Kun va vaqtni tanlang, Telegram’da yozing: administrator bronni tasdiqlaydi.</p>
    <a class="btn btn-qand" href="#">Stol band qilish</a>
  </div>
</section>"""
    else:
        body += f"""
<section class="cta" style="background-image:url('{img("dasturxon")}')">
  <div class="shade"></div>{AI}
  <div class="cta-t">
    <h2 class="h2">Stolingiz tayyor turadi</h2>
    <p>Kun va vaqtni tanlang, Telegram’da yozing: administrator bronni tasdiqlaydi.</p>
    <a class="btn btn-qand" href="#">Stol band qilish</a>
  </div>
</section>"""

    body += f"""
<footer class="foot">
  {bg("osh")}
  <div class="foot-r">
    <span class="logo serif">{STAR}Zarqand</span>
    <div class="fmenu">{"".join(f'<a href="#{k}">{e(v)}</a>' for k, v in CATEGORIES)}</div>
    <div class="fcon">
      <div><b>Aloqa</b><span class="ph">+998 [telefon]</span><br><span class="ph">[ko‘cha, uy]</span></div>
      <div><b>Ijtimoiy tarmoq</b><span class="ph">[@username]</span> Telegram<br><span class="ph">[@zarqand]</span> Instagram</div>
    </div>
    <p class="legal">© 2026 Zarqand · Rasmlar AI’da yaratilgan, haqiqiy fotolarga almashtiriladi</p>
  </div>
</footer>
"""
    css = CSS.replace("{{FONTS}}", font_css())
    title = "Zarqand — Menyu"
    return (f'<!doctype html><html lang="uz"><head><meta charset="utf-8">'
            f'<meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title>'
            f'<style>{css}</style></head><body><div class="page {mode}">{body}</div></body></html>')


if __name__ == "__main__":
    for mode, name in (("d", "menu-desktop.html"), ("m", "menu-mobile.html")):
        out = ROOT / name
        out.write_text(page(mode))
        print(out.name, round(out.stat().st_size / 1e6, 2), "MB")
