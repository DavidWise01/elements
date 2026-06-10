#!/usr/bin/env python3
"""The authoritative 118-element table for the ELEMENTS WORKSHOP (E1).

Hard chemistry facts are hardcoded (no LLM recall) so atomic weights, groups, and
periods are correct. Each element also carries David Wise's FOUR-STATE GATE: the
'118 Gates' thesis (elements/118 gates rewritten.html, stochien element.html) that all
118 elements are iterations of ONE stochastic element cycling four states by (Z-1)%4:

    s=0 -> "0:1 — first valley"
    s=1 -> "0:1 — second valley"
    s=2 -> "0:0 = 1 = 0"
    s=3 -> "1:1"

Each gate-state maps to one of the four natures of emergence used across UD0.
"""

# (Z, symbol, name, atomic_weight, category, period, group, signature_note)
# group is an int 1-18 for main-table elements; None for f-block (lanthanide/actinide),
# which render in the two strips. Weights in [brackets] = most stable isotope (synthetic/radioactive).
ELEMENTS = [
 (1,"H","Hydrogen","1.008","nonmetal",1,1,"Most abundant element in the universe; fuses to light every star; one proton, one electron — the simplest gate."),
 (2,"He","Helium","4.0026","noble",1,18,"Second-most abundant in the cosmos; utterly inert; becomes a frictionless superfluid near absolute zero."),
 (3,"Li","Lithium","6.94","alkali",2,1,"Lightest metal — floats on water; runs every rechargeable battery and steadies the bipolar mind."),
 (4,"Be","Beryllium","9.0122","alkaline",2,2,"Light, rigid, transparent to X-rays; windows for radiation optics; its dust is poison."),
 (5,"B","Boron","10.81","metalloid",2,13,"Borosilicate glass and the neutron-drinking control rod; hard, high-melting metalloid."),
 (6,"C","Carbon","12.011","nonmetal",2,14,"The backbone of all life; one atom, many faces — graphite, diamond, graphene, the buckyball."),
 (7,"N","Nitrogen","14.007","nonmetal",2,15,"78% of the air; inert as gas, violent as nitrate; the fertilizer that feeds the world."),
 (8,"O","Oxygen","15.999","nonmetal",2,16,"What we breathe; rusts iron and feeds fire — and David's gate where it lands square: 1:1, the balanced state."),
 (9,"F","Fluorine","18.998","halogen",2,17,"The most reactive, most electronegative element; attacks nearly everything; gives us Teflon and toothpaste."),
 (10,"Ne","Neon","20.180","noble",2,18,"Inert noble gas; glows orange-red in a tube — the light of the sign and the city night."),
 (11,"Na","Sodium","22.990","alkali",3,1,"Symbol Na, from natrium; soft enough to cut, explosive in water; half of salt and the spark of every nerve."),
 (12,"Mg","Magnesium","24.305","alkaline",3,2,"Burns blinding white; the light structural metal; the green heart of chlorophyll."),
 (13,"Al","Aluminium","26.982","post-transition",3,13,"Most abundant metal in the crust; light, strong, endlessly recyclable — once dearer than gold."),
 (14,"Si","Silicon","28.085","metalloid",3,14,"Sand, glass, and the thinking chip; second-most abundant in the crust — the substrate of the digital age."),
 (15,"P","Phosphorus","30.974","nonmetal",3,15,"Glows in the dark; the P in DNA and ATP; gives both the match and the nerve agent."),
 (16,"S","Sulfur","32.06","nonmetal",3,16,"Brimstone; rotten eggs and struck matches; its acid runs all of industry."),
 (17,"Cl","Chlorine","35.45","halogen",3,17,"Green choking gas; disinfects water and bleaches cloth — and was the first chemical weapon."),
 (18,"Ar","Argon","39.948","noble",3,18,"The lazy gas; fills bulbs and shields welds; third-most abundant in the air."),
 (19,"K","Potassium","39.098","alkali",4,1,"Symbol K, from kalium; softer and more violent than sodium; the other half of the nerve impulse."),
 (20,"Ca","Calcium","40.078","alkaline",4,2,"Bone, shell, and chalk; the reactive metal that builds every skeleton."),
 (21,"Sc","Scandium","44.956","transition",4,3,"Rare and light; aluminium-scandium alloys for aerospace frames and fighter jets."),
 (22,"Ti","Titanium","47.867","transition",4,4,"Strong as steel at half the weight, and it never rusts; jet engines, hip implants, white paint."),
 (23,"V","Vanadium","50.942","transition",4,5,"Toughens steel; the redox-flow battery; a chemist's rainbow of oxidation colors."),
 (24,"Cr","Chromium","51.996","transition",4,6,"The shine of chrome; turns steel stainless; the green of emerald and the red of ruby."),
 (25,"Mn","Manganese","54.938","transition",4,7,"Makes steel tough and bright; the black of the dry-cell battery; an essential trace nutrient."),
 (26,"Fe","Iron","55.845","transition",4,8,"Symbol Fe, from ferrum; the core of the Earth and of your blood; where stellar fusion ends and civilization began."),
 (27,"Co","Cobalt","58.933","transition",4,9,"The deep blue of glass and glaze; the lithium cathode; the metal at the center of vitamin B12."),
 (28,"Ni","Nickel","58.693","transition",4,10,"Coins and stainless steel; magnetic; with iron it makes the planet's molten core."),
 (29,"Cu","Copper","63.546","transition",4,11,"Symbol Cu, from cuprum; the first metal humans worked; the wire that carries the current; the green of Liberty."),
 (30,"Zn","Zinc","65.38","transition",4,12,"Galvanizes steel against rust; brass with copper; the trace metal your immune system needs."),
 (31,"Ga","Gallium","69.723","post-transition",4,13,"Melts in the warmth of your hand; the semiconductor of the LED and the fast radio chip."),
 (32,"Ge","Germanium","72.630","metalloid",4,14,"The metalloid of the first transistor; now fiber-optic cores and infrared lenses."),
 (33,"As","Arsenic","74.922","metalloid",4,15,"The classic poison of kings; also the dopant that tunes a semiconductor."),
 (34,"Se","Selenium","78.971","nonmetal",4,16,"The photoconductor of the first photocopier; an essential trace element, toxic in excess."),
 (35,"Br","Bromine","79.904","halogen",4,17,"One of only two liquid elements; red and choking; flame retardants and old photographic film."),
 (36,"Kr","Krypton","83.798","noble",4,18,"Noble gas that once defined the metre by its light; high-performance lamps and lasers."),
 (37,"Rb","Rubidium","85.468","alkali",5,1,"Soft and violently reactive; the heartbeat of one kind of atomic clock."),
 (38,"Sr","Strontium","87.62","alkaline",5,2,"The blazing red of fireworks and emergency flares; its isotope seeks bone."),
 (39,"Y","Yttrium","88.906","transition",5,3,"High-temperature superconductors; the red phosphor of the old picture tube; white LEDs."),
 (40,"Zr","Zirconium","91.224","transition",5,4,"Corrosion-proof; the cladding around nuclear fuel; cubic zirconia counterfeits the diamond."),
 (41,"Nb","Niobium","92.906","transition",5,5,"The superconducting magnet of the MRI and the particle accelerator; micro-alloyed pipeline steel."),
 (42,"Mo","Molybdenum","95.95","transition",5,6,"High-melting; toughens steel; the metal at the heart of nitrogen-fixing enzymes."),
 (43,"Tc","Technetium","[98]","transition",5,7,"The first element made by humans; no stable isotope exists; the workhorse tracer of medical imaging."),
 (44,"Ru","Ruthenium","101.07","transition",5,8,"Hardens platinum; a catalyst and a data-storage layer; one of the platinum-group rarities."),
 (45,"Rh","Rhodium","102.91","transition",5,9,"The most reflective metal; the catalytic converter's prize; rarer and dearer than gold."),
 (46,"Pd","Palladium","106.42","transition",5,10,"Drinks hydrogen like a sponge; the catalytic converter; the metal of cold-fusion lore."),
 (47,"Ag","Silver","107.87","transition",5,11,"Symbol Ag, from argentum; the best electrical conductor of all; mirrors, coins, the metal of the moon."),
 (48,"Cd","Cadmium","112.41","transition",5,12,"Toxic; the cadmium red and yellow of the painter; the rechargeable NiCd cell."),
 (49,"In","Indium","114.82","post-transition",5,13,"Soft as wax; the transparent conductor (ITO) printed on every touchscreen."),
 (50,"Sn","Tin","118.71","post-transition",5,14,"Symbol Sn, from stannum; bronze with copper, solder for circuits; bends with a 'cry'; the humble can."),
 (51,"Sb","Antimony","121.76","metalloid",5,15,"Symbol Sb, from stibium; the ancient kohl of the eye; flame retardants; it hardens lead."),
 (52,"Te","Tellurium","127.60","metalloid",5,16,"The metalloid of thin-film solar cells; it leaves a rare-earth garlic on the breath."),
 (53,"I","Iodine","126.90","halogen",5,17,"Purple vapor; the antiseptic and the thyroid's element; why salt is iodized."),
 (54,"Xe","Xenon","131.29","noble",5,18,"Noble gas of the bright headlight and the ion thruster; a gas that can put you to sleep."),
 (55,"Cs","Caesium","132.91","alkali",6,1,"The most reactive metal; the second itself is defined by the vibration of its atom."),
 (56,"Ba","Barium","137.33","alkaline",6,2,"The white of the X-ray 'barium meal'; the green of fireworks; the weight in drilling mud."),
 (57,"La","Lanthanum","138.91","lanthanide",6,None,"First of the lanthanides; camera-lens glass and the nickel-metal-hydride battery."),
 (58,"Ce","Cerium","140.12","lanthanide",6,None,"Most abundant rare earth; the lighter flint, the glass polish, the catalytic converter."),
 (59,"Pr","Praseodymium","140.91","lanthanide",6,None,"The green of rare-earth glass; powerful magnets; the welder's protective goggles."),
 (60,"Nd","Neodymium","144.24","lanthanide",6,None,"The strongest permanent magnet — in every hard drive, earbud, and wind turbine."),
 (61,"Pm","Promethium","[145]","lanthanide",6,None,"Radioactive with no stable isotope; the glow of luminous paint and the atomic battery."),
 (62,"Sm","Samarium","150.36","lanthanide",6,None,"Samarium-cobalt magnets that keep their strength in fierce heat."),
 (63,"Eu","Europium","151.96","lanthanide",6,None,"The red and blue phosphor of the screen; the secret ink in a euro banknote."),
 (64,"Gd","Gadolinium","157.25","lanthanide",6,None,"The MRI contrast agent; near room temperature its magnetism runs to extremes."),
 (65,"Tb","Terbium","158.93","lanthanide",6,None,"Green phosphors and alloys that change shape inside a magnetic field."),
 (66,"Dy","Dysprosium","162.50","lanthanide",6,None,"Keeps a hot magnet from forgetting itself; a neutron-eater in control rods."),
 (67,"Ho","Holmium","164.93","lanthanide",6,None,"The strongest magnetic moment of any element; the surgeon's cutting laser."),
 (68,"Er","Erbium","167.26","lanthanide",6,None,"Amplifies the light inside a fiber-optic cable; the pink of glass and laser."),
 (69,"Tm","Thulium","168.93","lanthanide",6,None,"Rarest of the stable rare earths; a portable X-ray source."),
 (70,"Yb","Ytterbium","173.05","lanthanide",6,None,"The atomic clock of staggering precision; a gauge that feels pressure as resistance."),
 (71,"Lu","Lutetium","174.97","lanthanide",6,None,"Densest and hardest rare earth; the crystal in the PET-scan detector."),
 (72,"Hf","Hafnium","178.49","transition",6,4,"A neutron-drinker for reactor rods; the insulating gate inside the modern transistor."),
 (73,"Ta","Tantalum","180.95","transition",6,5,"Corrosion-proof; the tiny capacitor in every phone; the surgeon's implant plate."),
 (74,"W","Tungsten","183.84","transition",6,6,"Symbol W, from wolfram; the highest melting point of all metals; the bulb filament, the drill, the armor."),
 (75,"Re","Rhenium","186.21","transition",6,7,"One of the rarest metals; the superalloy that lets a jet turbine take the heat."),
 (76,"Os","Osmium","190.23","transition",6,8,"The densest natural element; the hard tip of the old fountain pen and the instrument pivot."),
 (77,"Ir","Iridium","192.22","transition",6,9,"The most corrosion-resistant metal; its thin clay layer marks the asteroid that ended the dinosaurs."),
 (78,"Pt","Platinum","195.08","transition",6,10,"Catalyst, jewel, and once the very definition of the kilogram; precious and unreactive."),
 (79,"Au","Gold","196.97","transition",6,11,"Symbol Au, from aurum; the metal of kings, never tarnishing; alchemy's whole goal; money and microcircuits."),
 (80,"Hg","Mercury","200.59","transition",6,12,"Symbol Hg, from hydrargyrum; the only metal liquid at room temperature; the thermometer and the hatter's madness — quicksilver."),
 (81,"Tl","Thallium","204.38","post-transition",6,13,"'The poisoner's poison' — tasteless, deadly; once the rat-killer and the spy's tool."),
 (82,"Pb","Lead","207.2","post-transition",6,14,"Symbol Pb, from plumbum; dense, soft, toxic; the pipe, the bullet, the radiation shield; the base metal of the Great Work."),
 (83,"Bi","Bismuth","208.98","post-transition",6,15,"Grows iridescent rainbow crystals; the pink relief of Pepto-Bismol; the last almost-stable heavy element."),
 (84,"Po","Polonium","[209]","post-transition",6,16,"Fiercely radioactive; named for Marie Curie's Poland; an assassin's near-invisible poison."),
 (85,"At","Astatine","[210]","halogen",6,17,"The rarest naturally occurring element on Earth — less than a gram exists at any moment."),
 (86,"Rn","Radon","[222]","noble",6,18,"A radioactive noble gas that seeps from rock into basements; a leading cause of lung cancer."),
 (87,"Fr","Francium","[223]","alkali",7,1,"The second-rarest element; the most unstable of the first hundred-and-one; never gathered in bulk."),
 (88,"Ra","Radium","[226]","alkaline",7,2,"Curie's glowing discovery; once painted on watch dials and sold as a cure — and quietly lethal."),
 (89,"Ac","Actinium","[227]","actinide",7,None,"First of the actinides; glows blue in the dark; a warhead aimed at cancer cells."),
 (90,"Th","Thorium","232.04","actinide",7,None,"A potential nuclear fuel, more abundant than uranium; the glow of the old gas-lamp mantle."),
 (91,"Pa","Protactinium","231.04","actinide",7,None,"Rare, toxic, intensely radioactive; little beyond the research bench."),
 (92,"U","Uranium","238.03","actinide",7,None,"The fuel of the reactor and the first atomic bomb; the heaviest element born in the Earth itself."),
 (93,"Np","Neptunium","[237]","actinide",7,None,"The first element beyond uranium; a trace in every spent fuel rod."),
 (94,"Pu","Plutonium","[244]","actinide",7,None,"The bomb's core and the deep-space battery — it still powers the Voyagers and the Mars rovers."),
 (95,"Am","Americium","[243]","actinide",7,None,"The radioactive speck inside every household smoke detector."),
 (96,"Cm","Curium","[247]","actinide",7,None,"Powers instruments on spacecraft; named for Marie and Pierre Curie."),
 (97,"Bk","Berkelium","[247]","actinide",7,None,"A stepping-stone used to forge still-heavier elements; named for Berkeley."),
 (98,"Cf","Californium","[251]","actinide",7,None,"A potent neutron source — it starts reactors and scans cargo for gold and oil."),
 (99,"Es","Einsteinium","[252]","actinide",7,None,"First found in the fallout of a hydrogen bomb; named for Einstein."),
 (100,"Fm","Fermium","[257]","actinide",7,None,"The heaviest element reachable by reactor or explosion; named for Enrico Fermi."),
 (101,"Md","Mendelevium","[258]","actinide",7,None,"Named for Mendeleev, who drew the table and left gaps for the unfound."),
 (102,"No","Nobelium","[259]","actinide",7,None,"Named for Alfred Nobel; made and counted a single atom at a time."),
 (103,"Lr","Lawrencium","[266]","actinide",7,None,"The last actinide; named for Ernest Lawrence, who built the cyclotron."),
 (104,"Rf","Rutherfordium","[267]","transition",7,4,"The first transactinide; named for Rutherford, who split the atom's heart open."),
 (105,"Db","Dubnium","[268]","transition",7,5,"Named for Dubna, the Russian laboratory that hunts the superheavy."),
 (106,"Sg","Seaborgium","[269]","transition",7,6,"Named for Glenn Seaborg while he still lived — a rare honor."),
 (107,"Bh","Bohrium","[270]","transition",7,7,"Named for Niels Bohr and his quantum atom."),
 (108,"Hs","Hassium","[269]","transition",7,8,"Named for Hesse, the German state of the laboratory that made it."),
 (109,"Mt","Meitnerium","[278]","transition",7,9,"Named for Lise Meitner, who explained nuclear fission and was passed over for the prize."),
 (110,"Ds","Darmstadtium","[281]","transition",7,10,"Named for Darmstadt, the city of its making; gone in moments."),
 (111,"Rg","Roentgenium","[282]","transition",7,11,"Named for Röntgen, who found the X-ray; exists for the blink of a nucleus."),
 (112,"Cn","Copernicium","[285]","transition",7,12,"Named for Copernicus; predicted to be a fleeting volatile liquid or gas."),
 (113,"Nh","Nihonium","[286]","post-transition",7,13,"The first element named in Japan ('Nihon'); a flicker of a second of existence."),
 (114,"Fl","Flerovium","[289]","post-transition",7,14,"Named for the Flerov lab; aimed at the hoped-for 'island of stability.'"),
 (115,"Mc","Moscovium","[290]","post-transition",7,15,"Named for Moscow; it lives only milliseconds."),
 (116,"Lv","Livermorium","[293]","post-transition",7,16,"Named for the Livermore laboratory; among the heaviest ever assembled."),
 (117,"Ts","Tennessine","[294]","halogen",7,17,"Named for Tennessee; a predicted halogen and the second-heaviest known element."),
 (118,"Og","Oganesson","[294]","noble",7,18,"The heaviest known element; named for the living physicist Yuri Oganessian; a 'noble gas' that may be solid."),
]

# David Wise's four-state gate cycle — (Z-1)%4 — from '118 gates rewritten' / 'stochien element'
GATE_STATES = [
 ("0:1 — first valley",  "electrical", "the first reach of emptiness toward one — potential, charge, the rising edge"),
 ("0:1 — second valley", "ethereal",   "the second reach — the diffuse, the airy, the not-quite-held"),
 ("0:0 = 1 = 0",         "spiritual",  "the collapse where nothing equals one equals nothing — the return to the single source"),
 ("1:1",                 "natural",    "the held balance — fully manifest, matched, made — born of the world"),
]
def gate(Z):
    """Return (state_label, nature, gloss) for atomic number Z under David's cycle."""
    return GATE_STATES[(Z - 1) % 4]

NATURE_COLORS = {
 "natural":   "#5fae7a",
 "ethereal":  "#9a7cff",
 "spiritual": "#e6a849",
 "electrical":"#3fd0e0",
}

CATEGORY_COLORS = {
 "nonmetal":        "#4cc38a",
 "noble":           "#7c6cff",
 "alkali":          "#ff6b6b",
 "alkaline":        "#ff9f43",
 "metalloid":       "#2bc4c4",
 "halogen":         "#ffd23f",
 "transition":      "#9aa7b8",
 "post-transition": "#7d8aa0",
 "lanthanide":      "#e07cc0",
 "actinide":        "#d65db1",
}
CATEGORY_LABELS = {
 "nonmetal":"reactive nonmetal","noble":"noble gas","alkali":"alkali metal","alkaline":"alkaline earth metal",
 "metalloid":"metalloid","halogen":"halogen","transition":"transition metal","post-transition":"post-transition metal",
 "lanthanide":"lanthanide","actinide":"actinide",
}

GASES = {"H","He","N","O","F","Ne","Cl","Ar","Kr","Xe","Rn"}
LIQUIDS = {"Br","Hg"}
def phase(sym, Z):
    if sym == "Og": return "gas (predicted)"
    if sym in GASES: return "gas"
    if sym in LIQUIDS: return "liquid"
    if Z >= 100: return "solid (predicted)"
    return "solid"

def block(cat, group):
    if cat in ("lanthanide","actinide"): return "f"
    if group in (1,2) or (group is None): return "s"
    if group is not None and 3 <= group <= 12: return "d"
    return "p"

def slug_of(name): return name.lower()

if __name__ == "__main__":
    from collections import Counter
    assert len(ELEMENTS) == 118, len(ELEMENTS)
    zs = [e[0] for e in ELEMENTS]
    assert zs == list(range(1, 119)), "Z must be contiguous 1..118"
    nat = Counter(gate(z)[1] for z in zs)
    cat = Counter(e[4] for e in ELEMENTS)
    print(f"118 elements OK · Z 1..118 contiguous")
    print("by gate-nature:", dict(nat))
    print("by category:", dict(cat))
