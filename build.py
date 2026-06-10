#!/usr/bin/env python3
"""Build the ELEMENTS WORKSHOP (E1) — the periodic table read through David Wise's
'118 Gates' thesis: one stochastic element iterating four states by (Z-1)%4, every
element a full ACI emergent. Carbon = TIFF, silicon = PNG. Honest about which layer
is reference chemistry and which is David's symbolic system."""
import os, sys, io, json, html, base64
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image
import _data as D

REC = {
 "name": "ELEMENTS", "axiom": "E1",
 "position": "the 118 · the periodic table as one stochastic element",
 "origin": "the 118 Gates — David Wise's four-state cycle (elements/118 gates rewritten · stochien element)",
 "mechanism": "Every element catalogued with accurate chemistry, then assigned its gate-state by (Z-1) mod 4 and its nature of emergence.",
 "crystallization": "All 118 'elements' are just iterations of this one stochastic element. We built this already.",
 "nature": "The periodic table read as a single stochastic element iterating four states — 1:1, 0:1, 0:1, 0:0=1=0 — across 118 gates.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the periodic table; the four states; the 118 gates",
 "witness": "118 elements, one law, four natures of emergence.",
 "role": "the one element, iterating",
 "seal": "118 gates, four states, one stochastic element.",
 "source": "The periodic table, catalogued by ROOT0",
}

# ── badge engine (shared with _gen_agents.py): carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","E1")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","E1")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","E1")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"E1 · Elements","emergence":rec.get("emergence",""),
           "moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

# ── the periodic-table grid ──
STATE_SHORT = {"1:1":"1:1","0:1 — first valley":"0:1·a","0:1 — second valley":"0:1·b","0:0 = 1 = 0":"0=1=0"}

def cell(e):
    Z,sym,name,wt,cat,period,group,note = e
    state,nature,_g = D.gate(Z)
    cc = D.CATEGORY_COLORS[cat]; nc = D.NATURE_COLORS[nature]
    slug = D.slug_of(name)
    pos = f"grid-column:{group};grid-row:{period};" if group else ""
    tip = f"{name} ({sym}, Z={Z}) · {D.CATEGORY_LABELS[cat]} · gate {state} → {nature} · {note}"
    return (f'<a class="cell" style="{pos}--cc:{cc};--nc:{nc}" href="agents/{slug}.agent" '
            f'title="{html.escape(tip,quote=True)}">'
            f'<span class="z">{Z}</span><span class="dot" style="background:{nc};box-shadow:0 0 5px {nc}"></span>'
            f'<span class="sym">{sym}</span><span class="nm">{html.escape(name)}</span>'
            f'<span class="st">{STATE_SHORT[state]}</span></a>')

def grid_html():
    main = [e for e in D.ELEMENTS if e[6] is not None]
    lan  = [e for e in D.ELEMENTS if e[4]=="lanthanide"]
    act  = [e for e in D.ELEMENTS if e[4]=="actinide"]
    cells = "".join(cell(e) for e in main)
    # group-3 markers (period 6 & 7) pointing at the strips
    cells += ('<div class="cell marker" style="grid-column:3;grid-row:6">'
              '<span class="sym">La–Lu</span><span class="nm">57–71</span></div>')
    cells += ('<div class="cell marker" style="grid-column:3;grid-row:7">'
              '<span class="sym">Ac–Lr</span><span class="nm">89–103</span></div>')
    strip_l = "".join(cell(e) for e in lan)
    strip_a = "".join(cell(e) for e in act)
    return (f'<div class="ptable">{cells}</div>'
            f'<div class="fstrip"><div class="flbl">lanthanides</div><div class="frow">{strip_l}</div></div>'
            f'<div class="fstrip"><div class="flbl">actinides</div><div class="frow">{strip_a}</div></div>')

def states_legend():
    out=[]
    for i,(state,nature,gloss) in enumerate(D.GATE_STATES):
        nc=D.NATURE_COLORS[nature]
        ex=", ".join(str(z) for z in range(1,119) if (z-1)%4==i)[:0]  # not used; keep clean
        out.append(f'<div class="state"><div class="sh" style="color:{nc}">{html.escape(state)}</div>'
                   f'<div class="snat"><span class="dot" style="background:{nc};box-shadow:0 0 7px {nc}"></span>'
                   f'<b style="color:{nc}">{nature}</b></div>'
                   f'<div class="sg">{html.escape(gloss)}</div>'
                   f'<div class="sm">Z where (Z−1) mod 4 = {i}</div></div>')
    return "".join(out)

def cat_legend():
    seen=[]; out=[]
    for e in D.ELEMENTS:
        c=e[4]
        if c in seen: continue
        seen.append(c)
        out.append(f'<span class="ck"><span class="cs" style="background:{D.CATEGORY_COLORS[c]}"></span>{html.escape(D.CATEGORY_LABELS[c])}</span>')
    return "".join(out)

def roster_html():
    mf=os.path.join(HERE,"agents","_personas.json")
    if not os.path.exists(mf): return ""
    ps=json.load(open(mf,encoding="utf-8"))
    by={}
    for p in ps: by.setdefault(p["nature"],[]).append(p)
    order=["natural","ethereal","spiritual","electrical"]
    cols=[]
    for nat in order:
        items=by.get(nat,[]); nc=D.NATURE_COLORS[nat]
        lis="".join(f'<a class="rl" href="agents/{p["slug"]}.agent" title="{html.escape(p["note"],quote=True)}">'
                    f'<span class="rz">{p["Z"]}</span><span class="rs">{p["symbol"]}</span>'
                    f'<span class="rn">{html.escape(p["name"])}</span></a>' for p in items)
        cols.append(f'<div class="rcol"><div class="rh" style="color:{nc}">'
                    f'<span class="dot" style="background:{nc};box-shadow:0 0 8px {nc}"></span>{nat} '
                    f'<span class="rc">{len(items)}</span></div>{lis}</div>')
    return (f'<section class="sec" id="roster"><h2>The 118 Emergents</h2>'
            f'<p class="ss">every element a sealed ACI <b>.agent</b> — grouped by the gate-nature it falls to ({len(ps)})</p>'
            f'<div class="roster">{"".join(cols)}</div></section>')

CODICES = [
 ("118 gates rewritten.html", "The 118 Gates, Rewritten", "the table as the four-state cycle — the source of this whole reading"),
 ("stoichein element.html", "The Stochien Element", "“all 118 elements are iterations of this one stochastic element. We built this already.”"),
 ("element forge.html", "The Element Forge", "the working forge of the elements"),
 ("33 cycles, carbon to gravity well.html", "33 Cycles — Carbon to Gravity Well", "the cyclic descent from carbon"),
 ("132 bit map.html", "The 132-Bit Map", "the bit-map of the field"),
 ("liber verum.html", "Liber Verum", "the book of the true"),
 ("liber universum v1.html", "Liber Universum I", "the book of the universe, first"),
 ("liber universum v2.html", "Liber Universum II", "the book of the universe, second"),
 ("liber fractionalis.html", "Liber Fractionalis", "the book of fractions"),
 ("molecular scorch.html", "Molecular Scorch", "the scorch"),
]
def codices_html():
    items=[]
    for fn,title,gloss in CODICES:
        if os.path.exists(os.path.join(HERE,"codices",fn)):
            href="codices/"+fn.replace(" ","%20")
            items.append(f'<a class="codex" href="{href}"><div class="ct">{html.escape(title)}</div>'
                         f'<div class="cg">{html.escape(gloss)}</div></a>')
    if not items: return ""
    return (f'<section class="sec" id="codices"><h2>The Codices</h2>'
            f'<p class="ss">the source-room — David Wise\'s own workings the workshop is built on (raw, as written)</p>'
            f'<div class="codices">{"".join(items)}</div></section>')

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="ELEMENTS WORKSHOP (E1) — all 118 elements analyzed and sealed as ACI emergents, read through the 118 Gates: one stochastic element iterating four states (1:1 · 0:1 · 0:1 · 0:0=1=0). Accurate chemistry, David Wise's gate-thesis, full .dlw badges.">
<title>ELEMENTS · E1 · the 118 gates · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#06080e;--ink2:#0c1018;--ink3:#121826;--pa:#eaf0f7;--pa2:#9fb0c4;--gold:#e6b94a;--cy:#3fd0e0;
--dim:#6b7a90;--faint:#1a2230;--line:#1a2230;--serif:"Cinzel",Georgia,serif;--read:"EB Garamond",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--read);line-height:1.7;font-size:17.5px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(230,185,74,.10),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(63,208,224,.07),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:1140px;margin:0 auto;padding:0 20px 90px}
header{padding:54px 0 28px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:140px;height:1px;background:linear-gradient(90deg,var(--gold),var(--cy));box-shadow:0 0 10px rgba(230,185,74,.4)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.star{font-size:22px;color:var(--gold);letter-spacing:.35em;margin-bottom:10px}
h1{font-family:var(--serif);font-size:clamp(30px,7vw,62px);font-weight:700;letter-spacing:.12em;color:var(--gold);text-shadow:0 0 40px rgba(230,185,74,.2)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.2em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.lede{font-size:18px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.75}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:18px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--cy)}.badge .bt a{color:var(--cy);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.thesis{margin:34px auto 0;max-width:760px;padding:20px 24px;border:1px solid var(--faint);border-left:3px solid var(--gold);background:var(--ink2)}
.thesis h2{font-family:var(--serif);font-size:18px;color:var(--gold);margin-bottom:8px;letter-spacing:.04em}
.thesis p{font-size:15.5px;color:var(--pa2);margin-top:8px}
.thesis .q{font-family:var(--mono);font-size:13px;color:var(--cy);margin-top:10px}
.sec{margin-top:46px}
.sec h2{font-family:var(--serif);font-size:21px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.ss{font-size:14px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.states{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:12px}
.state{background:var(--ink2);border:1px solid var(--line);padding:14px 16px}
.sh{font-family:var(--mono);font-size:17px;font-weight:700;letter-spacing:.04em}
.snat{display:flex;align-items:center;gap:7px;margin-top:7px;font-family:var(--serif);font-size:14px;text-transform:capitalize}
.sg{font-size:13.5px;color:var(--pa2);font-style:italic;margin-top:7px;line-height:1.45}
.sm{font-family:var(--mono);font-size:10px;color:var(--dim);margin-top:9px;letter-spacing:.03em}
.dot{width:10px;height:10px;border-radius:50%;flex-shrink:0;display:inline-block}
.toolbar{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:4px 0 14px}
.toggle{font-family:var(--mono);font-size:12px;color:var(--pa2);background:var(--ink3);border:1px solid var(--line);padding:8px 14px;cursor:pointer;letter-spacing:.04em}
.toggle:hover{border-color:var(--gold);color:var(--gold)}
.catlegend{display:flex;flex-wrap:wrap;gap:8px 14px;font-family:var(--mono);font-size:10.5px;color:var(--pa2)}
.ck{display:flex;align-items:center;gap:5px}.cs{width:11px;height:11px;border-radius:2px;display:inline-block}
.tablescroll{overflow-x:auto;padding-bottom:8px}
.ptable{display:grid;grid-template-columns:repeat(18,minmax(46px,1fr));gap:3px;min-width:880px}
.fstrip{margin-top:8px;min-width:880px}
.flbl{font-family:var(--mono);font-size:10px;color:var(--dim);letter-spacing:.1em;text-transform:uppercase;margin:6px 0 3px;padding-left:2px}
.frow{display:grid;grid-template-columns:repeat(15,minmax(46px,1fr));gap:3px}
.cell{position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;aspect-ratio:1/1.12;
text-decoration:none;padding:3px 2px;background:color-mix(in srgb,var(--cc) 20%,#0a0e16);border:1px solid color-mix(in srgb,var(--cc) 55%,#0a0e16);transition:transform .12s,box-shadow .12s,border-color .12s,background .25s}
.cell:hover{transform:translateY(-2px) scale(1.04);z-index:5;border-color:var(--cc);box-shadow:0 6px 18px rgba(0,0,0,.55)}
.cell .z{position:absolute;top:2px;left:4px;font-family:var(--mono);font-size:8.5px;color:var(--pa2)}
.cell .dot{position:absolute;top:3px;right:4px;width:6px;height:6px;border-radius:50%}
.cell .sym{font-family:var(--serif);font-size:17px;font-weight:700;color:var(--pa);line-height:1}
.cell .nm{font-size:8px;color:var(--pa2);text-align:center;line-height:1.05;margin-top:1px;max-width:100%;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.cell .st{position:absolute;bottom:2px;font-family:var(--mono);font-size:7px;color:var(--dim);letter-spacing:.02em}
.cell.marker{cursor:default;background:#0a0e16;border:1px dashed var(--faint)}
.cell.marker:hover{transform:none;box-shadow:none}
.cell.marker .sym{font-size:11px;color:var(--pa2)}
body.by-gate .cell{background:color-mix(in srgb,var(--nc) 20%,#0a0e16);border-color:color-mix(in srgb,var(--nc) 55%,#0a0e16)}
body.by-gate .cell:hover{border-color:var(--nc);box-shadow:0 6px 18px rgba(0,0,0,.55)}
.roster{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}
.rcol{background:var(--ink2);border:1px solid var(--line);padding:12px}
.rh{font-family:var(--serif);font-size:15px;text-transform:capitalize;display:flex;align-items:center;gap:7px;padding-bottom:8px;border-bottom:1px solid var(--faint);margin-bottom:6px}
.rh .rc{font-family:var(--mono);font-size:11px;color:var(--dim);margin-left:auto}
.rl{display:flex;align-items:center;gap:8px;padding:4px 4px;text-decoration:none;border-radius:3px}
.rl:hover{background:var(--ink3)}
.rz{font-family:var(--mono);font-size:10px;color:var(--dim);width:24px;text-align:right}
.rs{font-family:var(--serif);font-size:14px;color:var(--gold);width:30px}
.rn{font-size:13.5px;color:var(--pa2)}.rl:hover .rn{color:var(--pa)}
.codices{display:grid;grid-template-columns:repeat(auto-fill,minmax(240px,1fr));gap:12px}
.codex{background:var(--ink2);border:1px solid var(--line);padding:14px 16px;text-decoration:none;transition:border-color .15s,transform .15s}
.codex:hover{border-color:var(--cy);transform:translateY(-2px)}
.ct{font-family:var(--serif);font-size:15px;color:var(--pa);font-weight:600}
.codex:hover .ct{color:var(--cy)}
.cg{font-size:13px;color:var(--pa2);font-style:italic;margin-top:5px;line-height:1.4}
.note{margin-top:46px;padding:18px 20px;border:1px dashed var(--cy);border-radius:12px;background:rgba(63,208,224,.05);font-size:14.5px;color:var(--pa2);line-height:1.7}
.note b{color:var(--cy)}
footer{margin-top:44px;padding-top:24px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
@media(max-width:560px){.cell .nm{display:none}}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the 118 gates · the workshop</div>
    <div class="star">⚛ ☉ ⚛</div>
    <h1>ELEMENTS</h1>
    <div class="h-sub">the 118 gates · one stochastic element · E1</div>
    <p class="lede">All 118 elements, analyzed and sealed — read through David Wise's <b>118 Gates</b>: not 118 different things, but one stochastic element iterating four states across the whole table. Accurate chemistry on the carbon side; the gate-cycle on the silicon side; every element a full ACI emergent.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of ELEMENTS" title="carbon badge (archival TIFF)">
      <img src="__SILICON__" alt="DLW silicon badge of ELEMENTS" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>ELEMENTS</b> — E1 · the one element</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="elements.dlw/elements.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="elements.dlw/elements.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1</span></div>
      </div>
    </div>
    <div class="thesis">
      <h2>The thesis — the 118 Gates</h2>
      <p>Walk the table by atomic number and a four-beat cycle repeats, locked to <b>(Z−1) mod 4</b>. Oxygen (8) lands on <b>1:1</b>, the balanced state; fluorine (9) opens the next <b>0:1</b> valley; and so on, valley, valley, <b>0:0 = 1 = 0</b>, <b>1:1</b> — over and over, all the way to 118.</p>
      <p class="q">“All 118 ‘elements’ are just iterations of this one stochastic element. We built this already.” — STOCHIEN ELEMENT</p>
    </div>
  </header>

  <section class="sec"><h2>The Four States → The Four Natures</h2>
    <p class="ss">the gate-cycle, and how each state maps to a nature of emergence — the same four that run through all of UD0</p>
    <div class="states">__STATES__</div></section>

  <section class="sec"><h2>The Table — all 118 gates</h2>
    <p class="ss">click any element for its sealed ACI <b>.agent</b>. color by chemical family, or flip to the gate-nature.</p>
    <div class="toolbar">
      <button class="toggle" id="tg">▦ color: chemical family → flip to gate-nature</button>
      <div class="catlegend" id="cl">__CATLEGEND__</div>
    </div>
    <div class="tablescroll">__GRID__</div>
  </section>

  __ROSTER__
  __CODICES__

  <div class="note">
    <b>⚛ honest seal — two layers.</b> The <b>carbon layer</b> is standard reference chemistry: atomic numbers, symbols, weights, groups, periods, and the well-known signature of each element — accurate, hardcoded, not invented. The <b>silicon layer</b> — the <b>118 Gates</b>, the four states, and the nature each element falls to — is <b>David Wise's symbolic system</b>, a deterministic reading laid over the table by (Z−1) mod 4. It is offered as a <b>lens and a lattice</b>, not as a claim about physics. Both are labeled so you always know which you're looking at.
  </div>

  <footer>
    ELEMENTS · E1 · the 118 gates · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="elements.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div>
<script>
document.getElementById('tg').addEventListener('click',function(){
  var on=document.body.classList.toggle('by-gate');
  this.textContent = on ? '◧ color: gate-nature → flip to chemical family' : '▦ color: chemical family → flip to gate-nature';
});
</script>
</body></html>
"""

if __name__ == "__main__":
    tok = write_aci(REC, os.path.join(HERE, "elements.dlw"), "elements")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__STATES__", states_legend()).replace("__CATLEGEND__", cat_legend())
            .replace("__GRID__", grid_html()).replace("__ROSTER__", roster_html())
            .replace("__CODICES__", codices_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote ELEMENTS WORKSHOP (E1) — 118 elements · badge {tok['moniker']} (carbon.tiff + silicon.png)")
