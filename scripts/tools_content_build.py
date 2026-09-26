# -*- coding: utf-8 -*-
"""Content for the Construction Materials and Roofing pages of /tools/.

Ordering quantities are the point of these pages, so the copy focuses on
what to buy, what the waste allowance is for, and where the industry's
rules of thumb come from. Prices are always left as plain numbers — no
currency is assumed, so the same page reads correctly in any market.
"""

BUILD_TOOLS = [

    # ------------------------------------------------------------------
    {
        "slug": "concrete-calculator",
        "calc": "concrete-calculator",
        "category": "materials",
        "icon": "🧱",
        "h1": "Concrete Calculator",
        "title": "Concrete Calculator — Slabs, Footings, Columns & Stairs",
        "meta_description": "Work out how much concrete a slab, footing, column or stair needs, in m³ and yd³, with cement bags, sand, aggregate and water for your chosen mix.",
        "meta_keywords": "concrete calculator, concrete volume calculator, cement bags calculator, concrete slab calculator, cubic yards concrete, concrete mix ratio calculator, footing calculator",
        "tagline": "Volume in cubic metres and cubic yards, plus cement bags, sand, aggregate and water at the mix you choose.",
        "blurb": "Slabs, footings, columns and stairs — volume plus bags of cement, sand and aggregate.",
        "intro": [
            "<p>Concrete is ordered before you can see whether you got it right. Order short and you are left with a cold joint and a panicked second delivery; order long and you are paying to dispose of set material. This calculator works out the volume of a slab, footing, column or stair, converts it into the units a supplier will quote in, and breaks the volume down into the cement, sand, aggregate and water you need for the mix you selected.</p>",
            "<p>It handles rectangular slabs and footings, round and square columns, and staircase steps. Results are given in cubic metres, cubic feet and cubic yards, because the same pour is quoted differently in different countries — ready-mix plants in metric markets sell by the cubic metre, while suppliers in the United States quote cubic yards.</p>",
            "<p>One scope note before you start: the stair option measures the stepped profile of the flight only. The waist slab underneath it — the sloping slab that carries the steps — is a separate volume and has to be calculated as a slab and added. It is easy to miss, and missing it under-orders the concrete by a third or more on a typical staircase. The same applies to any landing.</p>"
        ],
        "formula": "<p><strong>Slab or footing:</strong> length × width × thickness &nbsp;·&nbsp; <strong>Round column:</strong> π × radius² × height &nbsp;·&nbsp; <strong>Square column:</strong> width × depth × height &nbsp;·&nbsp; <strong>Stairs:</strong> ½ × riser × tread × width × number of steps</p><p>The wet volume is then multiplied by 1.54 to get the dry ingredient volume.</p>",
        "sections": [
            {
                "h": "Why the calculator multiplies by 1.54",
                "body": "<p>Concrete is ordered as a wet volume — the space it will fill — but cement, sand and aggregate are bought as dry materials. Dry materials do not pack to the same volume as the wet concrete they become: the aggregate settles, the cement and sand fill the gaps between stones, and the water occupies space that then leaves as the mix cures.</p>"
                        "<p>The correction factor is conventionally 1.54, meaning you need about 1.54 cubic metres of loose dry material to make 1 cubic metre of finished concrete. Without it, every quantity would come out roughly a third too low. It is a rule of thumb rather than a physical constant, which is another reason to round generously when ordering.</p>"
            },
            {
                "h": "Choosing a grade",
                "body": "<p>The grade describes the compressive strength in newtons per square millimetre, and for the lower grades it also fixes the ratio of cement to sand to aggregate. The ratios this calculator applies are the standard nominal mixes:</p>"
                        "<ul>"
                        "<li><strong>M5 (1 : 5 : 10)</strong> — bedding, fill, non-structural levelling</li>"
                        "<li><strong>M7.5 (1 : 4 : 8)</strong> — lean concrete, blinding under foundations</li>"
                        "<li><strong>M10 (1 : 3 : 6)</strong> — mass fill, kerb backing, light footings</li>"
                        "<li><strong>M15 (1 : 2 : 4)</strong> — general footings, floors, slabs on grade</li>"
                        "<li><strong>M20 (1 : 1.5 : 3)</strong> — reinforced slabs, beams and columns; the default for most domestic structural work</li>"
                        "<li><strong>M25 and above</strong> — design mix</li>"
                        "</ul>"
                        "<p>M25 and everything above it is where the nominal table stops being useful. These grades are specified as <em>design mixes</em>: the proportions are calculated and tested against the materials actually being delivered to your site, not read off a chart. That is why the calculator asks you to enter a ratio rather than guessing one for you — take it from your engineer's mix design. Historic tables sometimes list M25 as 1 : 1 : 2, and it is a reasonable ballpark, but concrete at that grade is doing real structural work and the mix should come from someone who has tested the aggregate.</p>"
                        "<p>Nominal mixes like the rest are fine for domestic and small commercial work. For anything structural beyond that, a designed mix specified by your engineer and verified by cube tests will be both safer and, often, cheaper — nominal mixes deliberately over-specify cement.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A slab 20 feet by 20 feet at 4 inches thick is 400 square feet at one third of a foot, giving 133.33 cubic feet — which is 3.775 cubic metres or 4.94 cubic yards. At M20, that needs 31 bags of 50 kg cement, 1.59 cubic metres of sand, 3.17 cubic metres of coarse aggregate and 761 litres of water.</p>"
                        "<p>The same slab at M15 — a reasonable choice for a slab on grade with light loading — drops the cement to 24 bags, because M15 uses 1 part cement to 6 parts aggregate where M20 uses 1 to 4.5. On a large pour that difference is worth real money, which is exactly why the grade should be specified by someone qualified rather than chosen by habit.</p>"
                        "<p>Note how modest the sand and aggregate volumes are next to the cement count. Only about 1.06 of those 3.775 cubic metres is cement; the rest of the volume is sand, stone and water. That is why cement dominates the cost even though it is the smallest ingredient by volume.</p>"
            },
            {
                "h": "Wastage, over-order and the practical margin",
                "body": "<p>The default 5% wastage allowance covers spillage, an uneven sub-base and the small amount left in the chute. Raise it if your excavation is not flat, if the pour is small, or if you are mixing on site rather than taking ready-mix — in those cases 10% is more realistic.</p>"
                        "<p>For a ready-mix delivery, find out the minimum load and the part-load charge before you order. Many plants have a three cubic metre minimum and charge a surcharge below it, which can make two small pours more expensive than one larger one. If your slab is close to the boundary between two truck sizes, it is usually worth ordering the smaller load and mixing a little extra by hand rather than paying for a part-load of the larger.</p>"
            },
            {
                "h": "Curing is not optional",
                "body": "<p>Concrete gains strength by hydrating, and it only hydrates while there is water available. A slab that dries out in its first week can lose a large part of its design strength even though it looks perfectly fine. Keep the surface damp for at least seven days — a week for ordinary work, longer for structural elements or hot weather — by covering it with polythene, hessian or a curing compound.</p>"
                        "<p>In hot climates that matters more, not less. High temperatures accelerate the loss of moisture and increase the risk of plastic shrinkage cracking, so pour early in the day, keep the mix as cool as you reasonably can, and start curing the moment the surface will take it.</p>"
            }
        ],
        "table": {
            "caption": "Concrete volume for common slabs",
            "head": ["Slab size", "At 4 in thick", "At 6 in thick", "Cubic yards at 4 in"],
            "rows": [
                ["10 × 10 ft", "1.26 m³", "1.88 m³", "1.65 yd³"],
                ["10 × 20 ft", "2.52 m³", "3.77 m³", "3.29 yd³"],
                ["12 × 12 ft", "1.81 m³", "2.72 m³", "2.37 yd³"],
                ["20 × 20 ft", "3.77 m³", "5.66 m³", "4.94 yd³"],
                ["20 × 30 ft", "5.66 m³", "8.50 m³", "7.41 yd³"],
                ["30 × 40 ft", "11.33 m³", "16.99 m³", "14.81 yd³"]
            ]
        },
        "faqs": [
            ("How many bags of cement are in 1 cubic metre of concrete?",
             "About 8.06 bags of 50 kg at the M20 mix (1 : 1.5 : 3), which is the usual figure for reinforced domestic work. At M15 (1 : 2 : 4) it drops to about 6.34 bags. M25 and above are design mixes, so the figure depends on the ratio your engineer specifies — enter that ratio in the calculator and it will work out the bags for you."),
            ("Why doesn't the calculator give a ratio for M25?",
             "Because M25 and above are specified as design mixes rather than nominal ones. The proportions come from testing the actual cement, sand and aggregate being used on the job, not from a published table, so quoting a fixed ratio would be misleading. Historic tables do list M25 as 1 : 1 : 2, and that is a fair starting point, but at this grade the concrete is carrying real structural load and the mix should come from a qualified engineer."),
            ("How wise is it to estimate concrete from a calculator?",
             "For ordering quantities, very — the volumes and bag counts are reliable, and ordering slightly long is far cheaper than running short mid-pour. What a calculator cannot do is choose your grade, because that depends on the loads the element will carry, the reinforcement, the soil and the exposure conditions. Use these figures to buy materials; use your engineer's specification to decide what to buy."),
            ("How do I calculate concrete for a slab?",
             "Multiply length by width by thickness, keeping all three in the same unit. A 20 × 20 foot slab at 4 inches thick is 20 × 20 × (4 ÷ 12) = 133.33 cubic feet, which is 3.775 cubic metres or 4.94 cubic yards. Enter the dimensions here and pick your unit from the dropdown beside each field — the thickness field defaults to inches because slab depths are almost always quoted that way."),
            ("How many cubic yards are in a cubic metre?",
             "1 cubic metre is 1.30795 cubic yards, and 1 cubic yard is 0.764555 cubic metres. So a 3 cubic metre pour is 3.92 cubic yards. If you are converting a quote from a metric supplier to compare with an imperial one, this is the factor to apply."),
            ("What is the 1.54 factor in concrete calculation?",
             "It converts wet concrete volume to dry ingredient volume. One cubic metre of finished concrete requires about 1.54 cubic metres of loose dry cement, sand and aggregate, because the dry materials consolidate and the water leaves voids as the mix cures. Every nominal-mix calculation uses it; without it your material quantities would be roughly a third too low."),
            ("How much water goes into a cubic metre of concrete?",
             "At a water-to-cement ratio of 0.5, roughly 200 litres for the 403 kg of cement in one cubic metre of M20. The ratio matters more than the volume: extra water makes concrete easier to place and permanently weaker, so add water only as the mix design allows and never to loosen a mix that is stiffening up."),
            ("Should I add a waste allowance to the concrete volume?",
             "Yes. Five percent is a sensible default for a flat, well-prepared sub-base and a ready-mix delivery. Use 10% if the ground is uneven, if the pour is small, or if you are mixing on site — spillage and leftover material are proportionally larger on small jobs.")
        ],
        "related": ["brick-calculator", "gravel-calculator", "square-footage-calculator", "tile-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "brick-calculator",
        "calc": "brick-calculator",
        "category": "materials",
        "icon": "🧱",
        "h1": "Brick Calculator",
        "title": "Brick Calculator — How Many Bricks Do I Need for a Wall?",
        "meta_description": "Calculate how many bricks a wall needs from its length, height and thickness, with mortar volume, cement bags and sand. Standard or custom brick sizes.",
        "meta_keywords": "brick calculator, how many bricks do i need, bricks per square metre, brick wall calculator, mortar calculator, bricks per m2, brick quantity calculator",
        "tagline": "Bricks for a wall of any size and thickness — plus the mortar, cement and sand to lay them.",
        "blurb": "Bricks for a wall of any size and thickness, plus the mortar and cement for laying them.",
        "intro": [
            "<p>Brick counts are usually quoted as a rate per square metre or per square foot of wall face, and the rate depends on how thick the wall is. A half-brick wall showing one face of each brick needs roughly half as many bricks per square metre as a full one-brick wall built from two leaves. This calculator works from the wall's actual dimensions and thickness, and lets you set the brick size so it matches what your supplier is actually delivering.</p>",
            "<p>Because bricks always come with mortar, the mortar volume is calculated too, along with the cement and sand needed to mix it. That matters because the cement for mortar is frequently forgotten at ordering time and then bought in a rush at a higher price.</p>"
        ],
        "formula": "<p><strong>Bricks per m² of wall face</strong> = number of brick leaves ÷ ((brick length + joint) × (brick height + joint))</p><p><strong>Number of leaves</strong> = wall thickness ÷ (brick width + joint), rounded to a whole number. <strong>Mortar</strong> = wall volume − the volume of the bricks themselves, then × 1.33 for the dry mix.</p>",
        "sections": [
            {
                "h": "Why we count by wall face, not by volume",
                "body": "<p>A common shortcut is to divide the wall's volume by the volume of one brick. It is quick and it is wrong for most walls, because a wall is built from whole leaves of brickwork and its thickness is never an exact multiple of a single brick plus its joint. A 230 mm wall built from 115 mm bricks is two leaves with a collar joint between them — the volume method treats that collar as part of the bricks and comes out roughly 9% low.</p>"
                        "<p>Counting by face area avoids the problem entirely. Each leaf of brickwork shows one brick face per module, so the rate per square metre is simply the reciprocal of the module area, multiplied by the number of leaves. It is the method estimators use, and it is why a 230 mm wall comes out at about 100 bricks per square metre while a 115 mm wall comes out at about 50.</p>"
            },
            {
                "h": "Standard, modular and imperial bricks",
                "body": "<p>Brick sizes are not universal, and using the wrong one throws the count off by a large margin. The two you will meet most often:</p>"
                        "<ul>"
                        "<li><strong>Standard 230 × 115 × 75 mm</strong> (about 9 × 4½ × 3 in) — the traditional brick across South Asia, the Middle East and much of Africa. At a 10 mm joint it gives roughly 50 bricks per m² as a half-brick wall, or 100 per m² at one brick thick.</li>"
                        "<li><strong>Modular 190 × 90 × 90 mm</strong> — the metric brick used in Europe, Australia and North America, designed so that four bricks plus joints make exactly 800 mm. At a 10 mm joint it gives 50 bricks per m² for a 90 mm wall, and 100 per m² for a 190 mm wall.</li>"
                        "</ul>"
                        "<p>US bricks follow a different convention again — the nominal dimensions include the mortar joint, so a “2¼ × 4 × 8 inch” brick is really 2¼ × 3⅝ × 7⅝ with a ⅜ inch joint. If your supplier quotes nominal sizes, the joint is already baked in; select the closest option and check the per-square-metre rate the calculator shows against the supplier's own figure before ordering.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A garden wall 10 metres long and 3 metres high in 230 mm brickwork. The wall face is 30 square metres. With 230 × 115 × 75 mm bricks at a 10 mm joint, the calculator returns 99 bricks per square metre, which is 2,942 bricks — about 3,090 once the 5% breakage allowance is added.</p>"
                        "<p>The same 30 square metres at 115 mm thick is a single leaf and needs 1,471 bricks, almost exactly half. That difference is the whole point of checking the wall thickness before ordering: guessing wrong on a garden wall is a four-figure mistake in any currency.</p>"
                        "<p>The mortar for the 230 mm wall works out at about 1.02 cubic metres wet, or 1.36 cubic metres of dry mix — roughly 7 bags of 50 kg cement and 1.13 cubic metres of sand at a 1 : 5 mix.</p>"
            },
            {
                "h": "How much waste to allow",
                "body": "<p>Allow 5% for machine-made bricks delivered on pallets and handled carefully. Allow 8–10% where bricks are hand-made, where they are unloaded and carried across a site by hand, or where the wall has many openings, corners and returns that generate cut bricks.</p>"
                        "<p>Keep the surplus. Brick colour and texture vary between kiln batches, and a wall repaired two years later from a different batch will show the join. A few hundred spare bricks stored dry and covered will save a great deal of trouble, and they cost almost nothing relative to the wall.</p>"
            },
            {
                "h": "Mortar mix and joint thickness",
                "body": "<p>A 1 : 5 cement-to-sand mix is the general-purpose choice for most brickwork. Go to 1 : 4 for load-bearing walls and anything exposed to driving rain, because the extra cement improves both strength and weather resistance. Drop to 1 : 6 only for internal non-load-bearing partitions, where strength is not the issue and a softer, more workable mix is easier to lay.</p>"
                        "<p>Keep the joint at about 10 mm. Thicker joints use more mortar and are weaker; thinner joints leave less room for the brick's own dimensional variation, which matters more with hand-made bricks. Consistency across the wall matters as much as the nominal figure — a wall with joints varying between 8 and 15 mm is both weaker and visibly uneven.</p>"
            }
        ],
        "table": {
            "caption": "Bricks per square metre by wall thickness (230 × 115 × 75 mm brick, 10 mm joint)",
            "head": ["Wall thickness", "Leaves", "Bricks per m²", "Bricks per ft²"],
            "rows": [
                ["112 mm (4.5 in)", "1", "50", "4.6"],
                ["230 mm (9 in)", "2", "99", "9.2"],
                ["340 mm (13.5 in)", "3", "148", "13.7"]
            ]
        },
        "faqs": [
            ("How many bricks are in a square metre of wall?",
             "About 50 for a half-brick (115 mm) wall and about 99 for a full one-brick (230 mm) wall, using a 230 × 115 × 75 mm brick with a 10 mm mortar joint. With modular 190 × 90 × 90 mm bricks the figures are 50 per square metre at 90 mm thick and 100 at 190 mm. Always check the wall thickness before ordering, because one answer is exactly double the other."),
            ("How many bricks are in a cubic metre?",
             "About 392 for standard 230 × 115 × 75 mm bricks with 10 mm joints, or 500 for modular 190 × 90 × 90 mm bricks. These figures assume the bricks fill the cubic metre solidly, which real walls rarely do — a 230 mm wall's thickness is not a whole multiple of the jointed brick, which is why this calculator counts by wall face instead."),
            ("How much mortar do I need for a brick wall?",
             "Roughly 15–20% of the finished wall's volume. For 30 square metres of 230 mm wall, that is about 1.02 cubic metres of wet mortar, or 1.36 cubic metres of dry mix — around 7 bags of cement and 1.13 cubic metres of sand at a 1 : 5 mix. The calculator works this out from the brick count and the wall volume, so it accounts for your actual brick size."),
            ("How much cement is in a 1 : 5 mortar mix?",
             "One part cement to five parts sand by volume. A cubic metre of dry mortar at 1 : 5 contains about 0.167 cubic metres of cement, which is 240 kg, or just under 5 bags of 50 kg. Add the water gradually — the workability you want comes from the sand grading, not from extra water."),
            ("Should I add wastage to the brick count?",
             "Yes. Five percent is reasonable for machine-made bricks delivered on pallets, and 8–10% for hand-made bricks, awkward access, or walls with many openings and corners that produce offcuts. Always keep the surplus rather than ordering to the exact figure — brick colour varies between kiln batches and a later repair from a different batch will be visible."),
            ("Does the calculator work for blockwork?",
             "Yes. Enter your block's dimensions under the custom brick size option. Concrete blocks are typically 440 × 215 × 100 mm or 390 × 190 × 190 mm, and with 10 mm joints they give rates of about 12.5 blocks per square metre for the larger face and 10 for the smaller. The mortar calculation works identically.")
        ],
        "related": ["concrete-calculator", "gravel-calculator", "square-footage-calculator", "tile-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "gravel-calculator",
        "calc": "gravel-calculator",
        "category": "materials",
        "icon": "🪨",
        "h1": "Gravel Calculator",
        "title": "Gravel Calculator — How Much Gravel Do I Need?",
        "meta_description": "Calculate how much gravel, crushed stone or pea gravel you need for a driveway, path or bed. Volume in yd³ and m³, weight in tonnes and US tons.",
        "meta_keywords": "gravel calculator, how much gravel do i need, gravel tonnage calculator, crushed stone calculator, cubic yards of gravel, pea gravel calculator, driveway gravel calculator",
        "tagline": "Volume in cubic yards and cubic metres, and the weight in tonnes, so you can order whichever way your supplier sells.",
        "blurb": "Gravel, crushed stone and river rock — volume in yd³ and weight in tonnes.",
        "intro": [
            "<p>Gravel is the material where people most often order the wrong quantity, because suppliers sell it two different ways. Some sell by volume — cubic yards or cubic metres of loose material; others sell by weight — tonnes or US tons. This calculator gives you both, linked by the bulk density of the material you pick.</p>",
            "<p>It covers rectangular, circular and triangular areas, takes a depth in inches or centimetres, and supports the common gravels and stone with their typical densities. There is also a bag option if you are buying in bags rather than having a load tipped.</p>"
        ],
        "formula": "<p><strong>Volume = area × depth</strong> &nbsp;·&nbsp; <strong>Weight = volume × bulk density</strong></p><p>Typical bulk densities: gravel 1.68 t/m³ · crushed stone 1.60 t/m³ · river rock 1.52 t/m³ · pea gravel 1.45 t/m³ · sand 1.60 t/m³</p>",
        "sections": [
            {
                "h": "Bulk density is not the density of rock",
                "body": "<p>A solid cubic metre of granite weighs about 2.7 tonnes. A cubic metre of granite gravel weighs around 1.6 tonnes, and a cubic metre of pea gravel less still. The difference is the air in the gaps between the stones — anything from 30% to 45% of the total volume with loose, rounded material.</p>"
                        "<p>That is why bulk density, not the material's true density, is the number to use. It also means the weight of a given volume shifts with moisture and with how the material has settled in the pile: wet gravel can be 10–15% heavier than the same gravel dry, and material that has been sitting in a stockpile is more compacted than freshly tipped material.</p>"
                        "<p>Treat the weight this calculator delivers as an estimate for budgeting and comparison. For a large order, ask the supplier for their own conversion figure for that specific aggregate.</p>"
            },
            {
                "h": "How deep should gravel be?",
                "body": "<p>Depth is where most driveway and path projects go wrong, and it depends on what the gravel is doing:</p>"
                        "<ul>"
                        "<li><strong>Decorative bed or mulch replacement:</strong> 2 inches (50 mm) is enough to cover the soil and suppress weeds.</li>"
                        "<li><strong>Garden path on a firm base:</strong> 2–3 inches (50–75 mm).</li>"
                        "<li><strong>Foot traffic over soft ground:</strong> 3–4 inches (75–100 mm).</li>"
                        "<li><strong>Driveway over a prepared sub-base:</strong> 4 inches (100 mm) of surface gravel on top of a compacted base course.</li>"
                        "<li><strong>Driveway where vehicles park:</strong> 4–6 inches, laid in two passes and compacted between them.</li>"
                        "</ul>"
                        "<p>A driveway is very rarely just gravel. It is a compacted sub-base of larger crushed stone — typically 4–6 inches of 40 mm stone — with a 2–4 inch surface layer of smaller, finer gravel on top. Pouring decorative pea gravel directly onto soil and driving on it will simply push the stone down into the mud.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A driveway 20 feet long and 10 feet wide, covered 3 inches deep. The area is 200 square feet, the depth is 0.25 feet, giving 50 cubic feet — 1.85 cubic yards, or 1.416 cubic metres. At a bulk density of 1.68 tonnes per cubic metre for gravel, that is 2.38 tonnes, or 2.62 US tons, or about 2,380 kilograms.</p>"
                        "<p>With a 10% wastage allowance — sensible for a driveway, where the sub-base is never perfectly flat — the order becomes about 1.56 cubic metres or 2.62 tonnes. Most suppliers round to the nearest half tonne, so you would ask for 2.5 or 3 tonnes.</p>"
            },
            {
                "h": "Choosing between the types",
                "body": "<p><strong>Pea gravel</strong> is small, rounded and smooth. It drains well, feels good underfoot and looks tidy, and it is the right choice for decorative beds, paths and play areas. It is also the worst choice for a driveway, because rounded stones do not interlock and the surface will shift and rut under vehicle weight.</p>"
                        "<p><strong>Crushed stone</strong> has angular faces that lock together when compacted, giving a stable, load-bearing surface. This is what driveways are built from. <strong>River rock</strong> sits between the two: larger than pea gravel, still rounded, and used for dry stream beds, borders and areas where appearance matters more than load.</p>"
                        "<p>For a driveway surface, a 20 mm crushed stone with fines — often called MOT Type 1, crusher run or road base — compacts to a firm, near-solid surface. For a top dressing, a clean 10–14 mm crushed stone gives a looser decorative finish that needs occasional raking.</p>"
            }
        ],
        "table": {
            "caption": "Gravel required per 100 square feet",
            "head": ["Depth", "Cubic feet", "Cubic yards", "Approx. weight (gravel at 1.68 t/m³)"],
            "rows": [
                ["1 in", "8.33 ft³", "0.31 yd³", "0.40 t"],
                ["2 in", "16.67 ft³", "0.62 yd³", "0.79 t"],
                ["3 in", "25.00 ft³", "0.93 yd³", "1.19 t"],
                ["4 in", "33.33 ft³", "1.23 yd³", "1.59 t"],
                ["6 in", "50.00 ft³", "1.85 yd³", "2.38 t"],
                ["12 in", "100.00 ft³", "3.70 yd³", "4.76 t"]
            ]
        },
        "faqs": [
            ("How much does a cubic yard of gravel weigh?",
             "About 1.4 US tons, or 1.28 metric tonnes, for gravel at a bulk density of 1.68 tonnes per cubic metre. Pea gravel is lighter at roughly 1.2 US tons per cubic yard, and crushed stone sits in between. Because the weight varies with moisture and stone size, treat it as an estimate and confirm with your supplier for a large order."),
            ("How many cubic yards of gravel do I need?",
             "Work out the area, multiply by the depth in feet to get cubic feet, then divide by 27. A 20 × 10 foot driveway at 3 inches deep is 200 × 0.25 = 50 cubic feet, which is 1.85 cubic yards. Add 10% for wastage on a driveway, since the sub-base is never perfectly level."),
            ("How deep should gravel be for a driveway?",
             "Four inches of surface gravel over a compacted sub-base is typical for a domestic driveway, rising to six inches where vehicles park regularly. Laid in two passes with compaction between them, that gives a stable surface. If you are driving on it, do not skip the sub-base — a layer of larger crushed stone underneath is what carries the load."),
            ("How many tonnes of gravel in a cubic metre?",
             "About 1.68 tonnes for gravel at its typical bulk density, 1.6 for crushed stone, 1.52 for river rock and 1.45 for pea gravel. Bulk density accounts for the air gaps between the stones, which is why it is so much lower than the density of solid rock."),
            ("How much area does a tonne of gravel cover?",
             "At a 2 inch depth, one tonne of gravel covers roughly 12 square metres, or about 130 square feet. At 4 inches it covers about 6 square metres, or 65 square feet. Coverage halves as depth doubles, so always fix the depth before you decide the quantity."),
            ("Can I use pea gravel on a driveway?",
             "It is not a good choice. Pea gravel is rounded, so the stones roll over each other instead of locking together, and a driveway surface made from it will rut and migrate under vehicle weight. Use angular crushed stone for anything driven on, and keep pea gravel for paths, beds and play areas.")
        ],
        "related": ["concrete-calculator", "brick-calculator", "square-footage-calculator", "fence-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "roofing-calculator",
        "calc": "roofing-calculator",
        "category": "roofing",
        "icon": "🏠",
        "h1": "Roofing Calculator",
        "title": "Roofing Calculator — Roof Area, Squares, Shingles & Pitch",
        "meta_description": "Calculate roof area from the building footprint and pitch, and get roof squares, shingle bundles, underlayment rolls and ridge length for any roof shape.",
        "meta_keywords": "roofing calculator, roof area calculator, roof pitch calculator, shingle calculator, roofing squares, how many bundles of shingles, hip roof calculator, gable roof area",
        "tagline": "Roof area, squares, bundles and underlayment — from the footprint you can actually measure on the ground.",
        "blurb": "Roof area and materials from the footprint and pitch — gable, hip, shed and flat.",
        "intro": [
            "<p>The area of a roof is not the area of the building underneath it. A sloped roof covers more ground than its footprint, and how much more depends entirely on the pitch. A roof at a 6/12 pitch has about 12% more surface than its footprint; at 12/12 the factor is 1.414, so the roof covers more than 40% extra.</p>",
            "<p>This calculator takes the building footprint you can measure from the ground, adds the overhang, applies the pitch factor, and returns the roof area along with the quantities roofers actually order in: squares, shingle bundles and underlayment rolls.</p>"
        ],
        "formula": "<p><strong>Pitch factor = √(1 + (rise ÷ 12)²)</strong> &nbsp;·&nbsp; <strong>Roof area = footprint × pitch factor</strong> &nbsp;·&nbsp; <strong>Squares = roof area ÷ 100</strong></p><p>The footprint includes the overhang on all sides, because the roof extends beyond the walls.</p>",
        "sections": [
            {
                "h": "What a roof square is",
                "body": "<p>A square is 100 square feet of roof surface — a 10 by 10 foot patch. It is the unit the entire roofing trade quotes in across the United States and Canada, and it exists because a roofer's materials all scale from it: three bundles of asphalt shingles cover one square, and a roll of underlayment covers a neatly stated number of squares.</p>"
                        "<p>Roofers talk in squares rather than square feet for the same reason builders talk in cubic yards of concrete — the unit is the size of the thing being ordered. A “25 square roof” is 2,500 square feet of surface. If a quote arrives in squares and your own measurement is in square feet, divide by 100 before comparing.</p>"
            },
            {
                "h": "Measuring the footprint and adding the overhang",
                "body": "<p>Measure the building's external dimensions at ground level, then add the overhang on each side. The overhang is usually 12 to 24 inches at the eaves, and often 12 inches or less at the gable ends, though it varies by design and by climate — deep overhangs shade walls and shed water well away from the foundation, which is why they are common in hot and wet regions.</p>"
                        "<p>If you can get onto the roof safely, measuring the sloping surface directly removes any doubt. If you cannot, the footprint plus pitch method here is accurate to within a couple of percent, which is well inside the waste allowance you should be applying anyway.</p>"
            },
            {
                "h": "Reading the pitch",
                "body": "<p>Pitch is written as rise over run in twelfths — a 6/12 roof rises 6 inches for every 12 inches of horizontal run, which is a 26.6° angle. The common ones and what they are used for:</p>"
                        "<ul>"
                        "<li><strong>2/12 to 4/12 (9.5°–18.4°)</strong> — low slope, needs a double underlayment or a membrane, common on porches and extensions</li>"
                        "<li><strong>4/12 to 6/12 (18.4°–26.6°)</strong> — the standard range for domestic roofs in most climates</li>"
                        "<li><strong>6/12 to 9/12 (26.6°–36.9°)</strong> — steeper, sheds snow and rain quickly, gives more attic space</li>"
                        "<li><strong>9/12 and above (36.9°+)</strong> — steep, used for snow shedding and architectural effect, and slower and more expensive to roof</li>"
                        "</ul>"
                        "<p>Below about 2/12 the roof is not really pitched at all and needs a membrane system rather than shingles or tiles, because shingles rely on gravity and overlap to shed water and will not do it on a near-flat surface.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A building 40 feet by 24 feet with an 18 inch overhang on all sides has an effective footprint of 43 × 27 = 1,161 square feet. At a 6/12 pitch the factor is √(1 + 0.25) = 1.118, giving a roof area of about 1,298 square feet — 12.98 squares, or 13 squares in trade terms.</p>"
                        "<p>At three bundles per square that is 39 bundles before waste, or 43 with a 10% allowance. Underlayment at 10 squares per roll is two rolls. The ridge on a gable roof of these dimensions runs the building's length, so it is 43 feet — the long dimension, not the 27 foot span the slopes fall across. Mixing those two up is a common estimating error and leaves you short of ridge cap.</p>"
                        "<p>Now change the pitch to 12/12. The factor jumps to 1.414 and the roof area to 1,642 square feet — an extra 344 square feet of covering, or 26% more material, on exactly the same building.</p>"
            },
            {
                "h": "Waste, valleys and the complicated bits",
                "body": "<p>Ten percent waste is a reasonable default for a simple gable roof. Increase it for a hip roof, which has four planes meeting at hips and produces far more offcuts; for any roof with valleys where two planes intersect; for very steep pitches where every cut is awkward; and for complex outlines with dormers, chimneys and changes of direction.</p>"
                        "<p>The calculator does not deduct for chimneys, skylights or vents, and it does not add for valley flashing, starter strip, drip edge or ridge vents. Treat the material figures as the covering quantity only, and price the flashings, fixings and ventilation separately — on a typical roof they add a meaningful percentage to the materials bill.</p>"
            }
        ],
        "table": {
            "caption": "Pitch factor by roof pitch",
            "head": ["Pitch (rise per 12)", "Angle", "Pitch factor", "Roof area per 1,000 ft² footprint"],
            "rows": [
                ["2/12", "9.5°", "1.014", "1,014 ft²"],
                ["3/12", "14.0°", "1.031", "1,031 ft²"],
                ["4/12", "18.4°", "1.054", "1,054 ft²"],
                ["5/12", "22.6°", "1.083", "1,083 ft²"],
                ["6/12", "26.6°", "1.118", "1,118 ft²"],
                ["7/12", "30.3°", "1.158", "1,158 ft²"],
                ["8/12", "33.7°", "1.202", "1,202 ft²"],
                ["9/12", "36.9°", "1.250", "1,250 ft²"],
                ["10/12", "39.8°", "1.302", "1,302 ft²"],
                ["12/12", "45.0°", "1.414", "1,414 ft²"]
            ]
        },
        "faqs": [
            ("How do I calculate roof area?",
             "Multiply the footprint, including the overhang, by the pitch factor. The pitch factor is the square root of 1 plus the rise over 12 squared. For a 6/12 pitch that is √(1 + 0.25) = 1.118, so a 1,000 square foot footprint has a 1,118 square foot roof."),
            ("How many bundles of shingles do I need?",
             "Three bundles cover one square, and a square is 100 square feet of roof surface. So a 13 square roof needs 39 bundles before waste. Add 10% for a simple gable roof and 15% or more for a hip roof, valleys or a steep pitch — the calculator includes a waste field for this."),
            ("What is a roofing square?",
             "A square is 100 square feet of roof surface. It is the standard unit of the roofing trade, chosen because all the material quantities scale from it — three bundles of shingles, and a stated number of squares per roll of underlayment. A 25 square roof is 2,500 square feet."),
            ("Does roof area include the overhang?",
             "Yes, and it must. The roof extends past the walls on all sides, so the correct footprint is the building dimensions plus the overhang at each edge. With an 18 inch overhang on a 40 × 24 foot building, the effective footprint is 43 × 27 feet rather than 40 × 24 — nearly 21% more area before the pitch is even considered."),
            ("How do I work out my roof pitch?",
             "Measure 12 inches horizontally along the roof from a point near the eave, then measure how far the roof has risen vertically over that distance. If it rose 6 inches, your pitch is 6/12. On a drawing or in a specification the pitch is often given directly as a ratio or an angle."),
            ("How much underlayment do I need?",
             "Synthetic underlayment commonly comes in 10 square rolls — a 10 ft × 100 ft roll — so a 13 square roof needs two. Coverage varies between products, and 3 ft wide rolls cover far less, so the calculator lets you enter the figure from the roll you are buying rather than assuming a size. Divide your roof squares by that coverage and round up.")
        ],
        "related": ["square-footage-calculator", "concrete-calculator", "tile-calculator", "fence-calculator"]
    }
]
