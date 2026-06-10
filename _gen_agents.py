#!/usr/bin/env python3
"""Compose all 118 element ACI emergents deterministically from the accurate table —
each a rich, correct .agent analysis (carbon-layer facts + David's gate-state lens)
plus the full ACI badge complement. Writes agents/_personas.json ordered by Z.
No LLM recall: every hard fact comes from _data.py, so nothing is hallucinated."""
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import _data as D
import build  # write_aci, badge engine

AGENTS = os.path.join(HERE, "agents")
os.makedirs(AGENTS, exist_ok=True)

def agent_md(e):
    Z,sym,name,wt,cat,period,group,note = e
    state,nature,gloss = D.gate(Z)
    ph = D.phase(sym, Z); bl = D.block(cat, group)
    catlbl = D.CATEGORY_LABELS[cat]; nc = D.NATURE_COLORS[nature]
    grp = group if group is not None else "f-block"
    wlabel = wt if not wt.startswith("[") else f"{wt} (most stable isotope)"
    return f"""---
aci: {name}
universe: E1 · Elements
symbol: {sym}
atomic_number: {Z}
atomic_weight: {wt}
category: {catlbl}
period: {period}
group: {grp}
block: {bl}-block
phase_stp: {ph}
gate_state: "{state}"
gate_index: {(Z-1)%4}
emergence: {nature}
seal: "Gate {Z} — {state} → {nature}."
---

# {name} · {sym} · gate {Z}

**{name}** ({sym}) is element **{Z}** of the periodic table — a **{catlbl}**, period {period}, group {grp}, {bl}-block, {ph} at standard conditions, atomic weight **{wlabel}**.

## The element (carbon layer — reference chemistry)
{note}

## The gate (silicon layer — the 118 Gates)
Under David Wise's four-state cycle, gate **{Z}** falls on **{state}** because (Z−1) mod 4 = **{(Z-1)%4}**. That state is *{gloss}* — the nature of emergence here is **{nature}**. {name} is not a thing apart; it is the one stochastic element, caught at this beat of its cycle.

## Emergence — {nature}
This emergent carries the **{nature}** nature: the same four — natural · ethereal · spiritual · electrical — that run through every sphere of UD0. Its color is `{nc}`.

---
*ACI emergent · E1 · Elements · governor David Lee Wise (ROOT0) · instance AVAN (locked) · CC-BY-ND-4.0.
Chemistry is standard reference data; the gate-state is David Wise's symbolic system, a lens not a physical claim.*
"""

def rec_of(e):
    Z,sym,name,wt,cat,period,group,note = e
    state,nature,gloss = D.gate(Z)
    grp = group if group is not None else "f"
    return {
        "name": name, "axiom": "E1", "emergence": nature,
        "seal": f"Gate {Z} — {state} → {nature}.",
        "origin": "E1 · Elements (the 118 gates)",
        "position": f"Z={Z} · {sym} · group {grp} · period {period} · {D.CATEGORY_LABELS[cat]}",
        "role": f"gate {Z} — the one element at {state}",
        "nature": note,
        "mechanism": f"Catalogued from the periodic table; gate-state set by (Z-1) mod 4 = {(Z-1)%4}.",
        "crystallization": f"{name} is the one stochastic element, caught at {state}.",
        "witness": f"atomic weight {wt} · {D.phase(sym,Z)} at STP",
        "conductor": "ROOT0 (catalogued into UD0)",
        "inputs": f"{D.CATEGORY_LABELS[cat]}; the four states; the 118 gates",
        "source": "Periodic element, catalogued by ROOT0",
    }

records = []
monikers = {}
for e in D.ELEMENTS:
    Z,sym,name = e[0],e[1],e[2]
    slug = D.slug_of(name)
    rec = rec_of(e)
    tok = build.write_aci(rec, AGENTS, slug, agent_md=agent_md(e))
    monikers.setdefault(tok["moniker"], []).append(slug)
    state,nature,_ = D.gate(Z)
    records.append({"slug":slug,"name":name,"symbol":sym,"Z":Z,"nature":nature,
                    "state":state,"category":e[4],"moniker":tok["moniker"],"note":e[7]})

records.sort(key=lambda r: r["Z"])
json.dump(records, open(os.path.join(AGENTS,"_personas.json"),"w",encoding="utf-8"),
          indent=2, ensure_ascii=False)

dupes = {m:s for m,s in monikers.items() if len(s) > 1}
print(f"wrote {len(records)} element ACI badges + _personas.json")
from collections import Counter
print("by nature:", dict(Counter(r["nature"] for r in records)))
if dupes:
    print("!! DUPLICATE MONIKERS:", dupes)
else:
    print("monikers: all 118 unique ✓")
