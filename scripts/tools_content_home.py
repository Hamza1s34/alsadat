# -*- coding: utf-8 -*-
"""Content for the Flooring & Walls and Outdoor pages of /tools/.

These four tools share a shape: an area is measured, a wastage allowance
is applied, and the result is bought in packs. The copy therefore spends
most of its words on why the wastage figure differs between jobs, which
is the part that actually changes the order.
"""

HOME_TOOLS = [

    # ------------------------------------------------------------------
    {
        "slug": "tile-calculator",
        "calc": "tile-calculator",
        "category": "flooring",
        "icon": "◼️",
        "h1": "Tile Calculator",
        "title": "Tile Calculator — How Many Tiles & Boxes Do I Need?",
        "meta_description": "Calculate how many tiles and boxes you need for a floor or wall, with grout joints and cutting waste. Metric or imperial tile sizes, optional cost per box.",
        "meta_keywords": "tile calculator, how many tiles do i need, tile box calculator, floor tile calculator, bathroom tile calculator, tiles per square metre, grout joint calculator",
        "tagline": "Tiles and boxes for a floor or wall, counted with the grout joint included — because joints change the count.",
        "blurb": "Floor and wall tiles by the box, with grout joints and cutting waste included.",
        "intro": [
            "<p>“How many tiles do I need” has a subtly different answer from what most people expect, because tiles are not laid edge to edge. Every tile sits inside a grout joint, so the space one tile actually occupies is its own size plus the joint on each side. On a 600 mm tile with a 3 mm joint that is a 1% difference and barely matters; on a 100 mm mosaic tile with a 3 mm joint it is 6%, which is the difference between one box and two.</p>",
            "<p>This calculator includes the joint, adds a cutting allowance, and converts the result into boxes — since that is how tiles are actually sold, and a part box is not something you can buy.</p>"
        ],
        "formula": "<p><strong>Module area</strong> = (tile length + joint) × (tile width + joint)</p><p><strong>Tiles needed</strong> = area ÷ module area × (1 + waste)</p><p><strong>Boxes</strong> = tiles needed ÷ tiles per box, rounded up</p>",
        "sections": [
            {
                "h": "Why the grout joint is in the formula",
                "body": "<p>A tile plus its joint forms a repeating module, and that module — not the tile itself — is what tiles the floor. Divide the room area by the bare tile area and you will come out slightly short every time, because you have ignored the width the joints take up.</p>"
                        "<p>The effect scales with tile size. A 600 × 600 mm tile with a 3 mm joint occupies 603 × 603 mm, which is 1.0% more than the tile alone — negligible. A 300 × 300 mm tile with a 3 mm joint occupies 303 × 303 mm, 2.0% more. A 100 × 100 mm tile with the same joint occupies 103 × 103 mm, 6.1% more. Small formats and wide joints are exactly where the shortcut goes wrong.</p>"
                        "<p>Joint width itself depends on the tile. Rectified porcelain — cut to an exact size after firing — can take a 2 mm joint, and looks best with one. Standard ceramic wall tiles usually want 5–10 mm, partly because their edges are not perfectly straight and the joint hides the variation. Floor tiles in a busy area sit in the 3–5 mm range.</p>"
            },
            {
                "h": "Cutting waste: the figure that decides your order",
                "body": "<p>Some tiles will be cut. That is unavoidable — rooms are not multiples of tile sizes. The question is only how much of each cut tile is thrown away, and that depends on the layout:</p>"
                        "<ul>"
                        "<li><strong>Straight lay in a plain rectangular room — 10%.</strong> Most offcuts go at the perimeter and many can be used on the opposite wall.</li>"
                        "<li><strong>Diagonal or diamond lay — 15%.</strong> Every perimeter tile is a triangle, so half of every cut tile is waste by definition.</li>"
                        "<li><strong>Herringbone or chevron — 15–20%.</strong> These patterns generate offcuts at both ends of every course.</li>"
                        "<li><strong>Rooms with many obstacles — add 5%.</strong> Pipes, columns, door reveals and awkward returns around a bathroom or kitchen all consume tiles.</li>"
                        "</ul>"
                        "<p>Always keep the surplus. Tiles are made in dye lots and the shade shifts slightly between production runs; a repair in two years' time with a tile from a different batch may not match, and a discontinued tile cannot be matched at all. A spare box in the loft is cheap insurance.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A room 12 feet by 10 feet is 120 square feet, which is 11.15 square metres. With 600 × 600 mm tiles and a 3 mm joint, each module covers 0.3636 square metres, so 11.15 ÷ 0.3636 gives 30.7 tiles before any waste.</p>"
                        "<p>Add 10% for cutting and it becomes 33.7 tiles — 34 tiles. At four tiles per box that is 8.5 boxes, rounded up to 9 boxes, giving 36 tiles and a genuine spare pair plus a few cuts.</p>"
                        "<p>The calculator reports two coverage figures and they are not the same number. The <em>tile area in a box</em> is 1.44 square metres or about 15.5 square feet — that is what the manufacturer prints on the packaging, and it counts the tiles only. The <em>floor a box covers</em> is a little larger, 1.454 square metres, because once the tiles are laid with their joints the grout lines are floor too. Both are correct; they just answer different questions. Use the floor figure to check whether a box will cover the room, and the tile figure to compare packaging between suppliers.</p>"
                        "<p>With 600 mm tiles the gap between the two is about 1%, so it hardly matters. With small mosaics it can exceed 6%, which on a bathroom floor is the difference between one box and two.</p>"
            },
            {
                "h": "Buying, checking and storing",
                "body": "<p>Order the boxes from the same batch in one go, and check the batch code on every box as it is delivered. A mixed delivery is a genuine problem and much easier to refuse at the door than to argue about later.</p>"
                        "<p>Open a box and dry-lay a few tiles before fixing anything. Shade variation between tiles in the same batch is normal and often part of the look, but it needs to be seen before the adhesive is mixed, not after. Check the calibration too — tile sizes are nominal, and laying tiles from two different boxes alternately across a floor is the standard trick for disguising minor variation.</p>"
                        "<p>Store spares flat and dry, and keep the box with the batch code. That one detail is what makes a future repair possible.</p>"
            }
        ],
        "table": {
            "caption": "Tiles per square metre by size (3 mm joint, joint included)",
            "head": ["Tile size", "Tiles per m²", "Tiles per ft²", "Coverage per 10 tiles"],
            "rows": [
                ["100 × 100 mm", "94.2", "8.75", "0.106 m²"],
                ["200 × 200 mm", "24.3", "2.26", "0.412 m²"],
                ["300 × 300 mm", "10.9", "1.01", "0.918 m²"],
                ["300 × 600 mm", "5.47", "0.508", "1.83 m²"],
                ["400 × 400 mm", "6.17", "0.573", "1.62 m²"],
                ["600 × 600 mm", "2.75", "0.256", "3.64 m²"],
                ["600 × 1200 mm", "1.38", "0.128", "7.25 m²"],
                ["800 × 800 mm", "1.55", "0.144", "6.45 m²"]
            ]
        },
        "faqs": [
            ("How many tiles do I need for a 12 × 10 ft room?",
             "With 600 × 600 mm tiles and a 3 mm joint, about 34 tiles including a 10% cutting allowance — 9 boxes at four tiles per box. The room is 120 square feet, or 11.15 square metres, and each tile plus its joint covers 0.3636 square metres."),
            ("How many tiles are in a square metre?",
             "It depends entirely on the tile size: 2.75 per square metre for 600 × 600 mm, 5.47 for 300 × 600 mm, 10.9 for 300 × 300 mm and 94.2 for 100 × 100 mm mosaics. These figures include a 3 mm joint. Smaller tiles need far more per square metre, and the joint becomes a proportionally bigger part of the count."),
            ("How much waste should I allow for tiles?",
             "10% for a straight lay in a plain rectangular room, 15% for a diagonal or diamond pattern, and 15–20% for herringbone. Add another 5% if the room has many pipes, columns or awkward corners. Always keep the surplus — tiles vary between batches and a discontinued tile cannot be matched later."),
            ("Does the grout joint affect how many tiles I need?",
             "Yes, and more than most people expect with small tiles. Tiles tile the floor as tile-plus-joint modules, so the joint width is part of the repeating unit. On 600 mm tiles a 3 mm joint adds 1% to the count; on 100 mm mosaics it adds over 6%, which can be the difference between buying one box and buying two."),
            ("How wide should the grout joint be?",
             "2–3 mm for rectified porcelain, which is cut precisely after firing and can take a tight joint. 5–10 mm for standard ceramic wall tiles, where a wider joint helps hide edge variation. 3–5 mm is typical for floor tiles in normal domestic use."),
            ("How do I compare the price of tiles from different suppliers?",
             "Convert everything to cost per square metre or square foot of finished floor, not per tile, since box sizes and tile counts differ. Enter the price per box in this calculator and it will show the cost per square foot, including the waste allowance — which is the number that actually compares.")
        ],
        "related": ["flooring-calculator", "paint-calculator", "square-footage-calculator", "concrete-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "paint-calculator",
        "calc": "paint-calculator",
        "category": "flooring",
        "icon": "🎨",
        "h1": "Paint Calculator",
        "title": "Paint Calculator — How Much Paint Do I Need for a Room?",
        "meta_description": "Work out how many litres or gallons of paint a room needs, with door and window deductions, coats and your paint's coverage rate. Optional cost per litre.",
        "meta_keywords": "paint calculator, how much paint do i need, paint coverage calculator, litres of paint per room, gallons of paint calculator, wall area calculator, paint estimator",
        "tagline": "Litres or gallons for your room, with doors, windows and the number of coats taken off — not guessed.",
        "blurb": "Litres or gallons per room, with doors, windows and coats deducted properly.",
        "intro": [
            "<p>Paint coverage is quoted per litre on the tin, but the tin's figure is a laboratory number measured on a smooth, sealed, non-absorbent surface. Real walls are none of those things. The gap between the stated coverage and what actually happens is why so many decorating jobs finish one litre short.</p>",
            "<p>This calculator measures the walls, deducts the openings, applies your number of coats, and converts the result into the cans paint is actually sold in — because a paint shop will not sell you 7.1 litres, and knowing you need two 4 litre cans rather than three changes the budget.</p>"
        ],
        "formula": "<p><strong>Wall area</strong> = 2 × (length + width) × height, plus the ceiling if included</p><p><strong>Less openings</strong> — about 2 m² (21 ft²) per door and 1.4 m² (15 ft²) per window</p><p><strong>Paint</strong> = area ÷ coverage rate × number of coats</p>",
        "sections": [
            {
                "h": "Why the tin's coverage figure is optimistic",
                "body": "<p>A coverage rate of 10 square metres per litre assumes a smooth surface with the same porosity throughout, applied at exactly the specified film thickness. Bare plasterboard and fresh plaster absorb paint far more readily than the third coat on an old wall, so the first coat on new work can consume 20–30% more than the tin claims.</p>"
                        "<p>The colour matters too. Going from a dark colour to a light one, or painting red over anything, usually takes three coats rather than two — red and yellow pigments are naturally translucent and simply do not cover opaquely in two passes. If you are making a big jump in tone, plan for an extra coat or use a tinted primer.</p>"
                        "<p>This calculator lets you pick the coverage rate you expect rather than forcing the tin's figure on you. If you are painting new plaster, choose the exterior masonry rate of 8 m²/L as a conservative stand-in, or enter a lower number under the same options — the result will be closer to reality.</p>"
            },
            {
                "h": "Coverage rates for common paints",
                "body": "<p>The defaults in the calculator reflect typical manufacturer figures for a properly prepared surface:</p>"
                        "<ul>"
                        "<li><strong>Interior emulsion — 10 m² per litre.</strong> The general-purpose choice for walls and ceilings. Vinyl and acrylic emulsions are scrub-resistant and are what most interior walls get.</li>"
                        "<li><strong>Gloss and enamel — 14 m² per litre.</strong> Higher coverage because it is applied in a thinner, harder film. Used on trim, doors, skirting and joinery, where durability matters more than a flat finish.</li>"
                        "<li><strong>Exterior masonry — 8 m² per litre.</strong> Lower coverage because masonry is porous and textured and drinks the first coat. Also the right figure to use for bare interior plaster.</li>"
                        "<li><strong>Primer and sealer — 12 m² per litre.</strong> Seals a new or patchy surface so the topcoats behave predictably and cover evenly.</li>"
                        "</ul>"
                        "<p>Always check the tin. Coverage rates vary between manufacturers and between products within one manufacturer's range, and the difference between 8 and 12 square metres per litre on a large room is several litres.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A room 12 feet by 12 feet with 9 foot walls. The wall area is 2 × (12 + 12) × 9 = 432 square feet. Deduct one door at 21 square feet and two windows at 15 square feet each, and the paintable area is 381 square feet — 35.4 square metres.</p>"
                        "<p>At 10 square metres per litre for interior emulsion that is 3.54 litres per coat; two coats need 7.08 litres. In cans, that is two 4 litre cans with a little to spare, or one 20 litre drum. If you buy the same volume as five 1 US gallon (3.785 litre) cans you will pay noticeably more per litre for the same paint — the smaller the container, the higher the price per litre, on essentially every product.</p>"
                        "<p>Now suppose the ceiling is included. Adding 12 × 12 = 144 square feet brings the total to 525 square feet, or 48.8 square metres — 9.75 litres for two coats, which is three 4 litre cans. Including the ceiling changes the order, which is why it is a checkbox rather than an assumption.</p>"
            },
            {
                "h": "Doors, windows and the deduction",
                "body": "<p>Deducting openings is worth doing on a room with several of them, but it is easy to over-deduct. You do not paint the door, but you usually do paint the frame and the architrave around it — and on a standard doorway those edges add back a good part of the area you just removed. Windows likewise come with reveals and sills that need cutting in.</p>"
                        "<p>The calculator uses roughly 2 square metres per door and 1.4 square metres per window, which are the conventional allowances. If you are deducting openings and also painting all the trim in a separate colour, price the trim separately — a trim paint in gloss or enamel over doors, skirting and frames can easily consume a couple of litres on its own.</p>"
            },
            {
                "h": "Buying and storing",
                "body": "<p>Buy all the paint for one room in a single purchase, and mix cans from different batches together in one large container before you start. Paint shade varies slightly between batches, and a wall that changes colour halfway across is a mistake you cannot undo without repainting the whole thing.</p>"
                        "<p>Estimate generously for the first coat on new or repaired surfaces and buy one can more than the calculation suggests. Unopened water-based paint keeps for years in a frost-free store, and leftover paint in the original tin, labelled with the room and the date, is what makes a later touch-up possible. Keep a note of the colour name, the product and the sheen.</p>"
            }
        ],
        "table": {
            "caption": "Paint needed for two coats (interior emulsion at 10 m² per litre)",
            "head": ["Room (ft)", "Wall area", "Paintable area*", "Litres for 2 coats", "4 L cans"],
            "rows": [
                ["10 × 10", "360 ft²", "309 ft²", "5.7 L", "2"],
                ["12 × 12", "432 ft²", "381 ft²", "7.1 L", "2"],
                ["12 × 15", "486 ft²", "435 ft²", "8.1 L", "3"],
                ["15 × 15", "540 ft²", "489 ft²", "9.1 L", "3"],
                ["16 × 20", "648 ft²", "597 ft²", "11.1 L", "3"],
                ["20 × 20", "720 ft²", "669 ft²", "12.4 L", "4"]
            ]
        },
        "faqs": [
            ("How much paint do I need for a 12 × 12 room?",
             "About 7 litres for two coats on the walls — two 4 litre cans. The walls total 432 square feet, less a door and two windows leaves 381 square feet of paintable area, which is 35.4 square metres. At 10 square metres per litre that is 3.54 litres per coat. Add the ceiling and it becomes about 9.75 litres, or three cans."),
            ("How many square metres does a litre of paint cover?",
             "Typically 10 square metres for interior emulsion, 14 for gloss and enamel, 8 for exterior masonry and 12 for primer. These are manufacturer figures for a properly prepared surface, and real coverage on bare or porous material is often 20–30% lower."),
            ("How many coats of paint do I need?",
             "Two coats is standard for a colour change of similar tone onto a prepared surface. Three if you are covering a dark colour with a light one, or painting over red, yellow or a strong orange, since those pigments are naturally translucent. New plaster and repaired patches need a primer or a mist coat first."),
            ("Should I deduct doors and windows from the wall area?",
             "Deduct them if you want a tighter estimate, but do not expect a big saving. The calculator takes about 2 square metres per door and 1.4 per window, which is conventional. On a typical room that removes perhaps 10% of the wall area — and you will add some of it back painting the frames and reveals."),
            ("Is it cheaper to buy a 20 litre drum than 4 litre cans?",
             "Per litre, usually yes, and substantially so. The catch is that you must be able to use it. Water-based paint keeps well for years if the tin is sealed and stored frost-free, so a larger container is worth it if you are painting several rooms in the same colour — and not worth it if you are painting one small room."),
            ("How long should I wait between coats?",
             "Four hours is typical for water-based emulsion, and longer in cold or humid conditions. Solvent-based paints need considerably longer — often overnight. The test is not the clock but the surface: if the first coat is still cool to the touch or feels tacky, it has not dried and the second coat will lift it.")
        ],
        "related": ["tile-calculator", "flooring-calculator", "square-footage-calculator", "square-footage-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "flooring-calculator",
        "calc": "flooring-calculator",
        "category": "flooring",
        "icon": "🪵",
        "h1": "Flooring Calculator",
        "title": "Flooring Calculator — Laminate, Vinyl &amp; Hardwood Boxes",
        "meta_description": "Calculate how many boxes of laminate, vinyl or hardwood flooring you need, with a waste allowance and optional underlayment. Cost per square foot.",
        "meta_keywords": "flooring calculator, laminate calculator, how many boxes of flooring, vinyl plank calculator, hardwood flooring calculator, underlayment calculator, flooring per square foot",
        "tagline": "Boxes of laminate, vinyl or hardwood for your floor — with a wastage figure that matches the pattern you are laying.",
        "blurb": "Laminate, vinyl and hardwood boxes for a room, plus underlayment rolls.",
        "intro": [
            "<p>Flooring is sold by the box, and every manufacturer's box covers a different area — 24 square feet for a typical laminate, 20 for engineered or solid hardwood, and anything the manufacturer chooses if you go with a specialist product. So the useful calculation is not the area, which is easy, but the number of boxes, which is not.</p>",
            "<p>This calculator measures the floor, applies a wastage allowance matched to your laying pattern, and rounds up to whole boxes, since that is the smallest unit you can buy.</p>"
        ],
        "formula": "<p><strong>Floor area</strong> = length × width</p><p><strong>Boxes</strong> = floor area × (1 + waste) ÷ coverage per box, rounded up</p><p><strong>Underlayment rolls</strong> = floor area ÷ roll coverage, rounded up</p>",
        "sections": [
            {
                "h": "Wastage depends on the pattern, not the room",
                "body": "<p>The biggest single influence on how much flooring you buy is not the shape of the room but the pattern you lay it in:</p>"
                        "<ul>"
                        "<li><strong>Straight lay — 10%.</strong> Planks run parallel to one wall, cut at the far edge. The offcut from the last plank of a row starts the next row, so very little is truly wasted.</li>"
                        "<li><strong>Diagonal lay — 15%.</strong> Planks run at 45 degrees to the walls, which means a triangular cut at both ends of every perimeter row. Those triangles are unusable.</li>"
                        "<li><strong>Herringbone or chevron — 15–20%.</strong> Every plank is cut at an angle at the edges of each course, and the pattern consumes far more cuts per square metre than a straight lay.</li>"
                        "</ul>"
                        "<p>Room shape adds to this. A single rectangular room wastes least. A room with alcoves, chimney breasts, awkward returns or a diagonal wall wastes more, because the offcuts at a complex edge rarely fit anywhere else.</p>"
            },
            {
                "h": "Which flooring type, and how much a box covers",
                "body": "<p>The coverage per box varies by material, and the figures this calculator uses are typical rather than universal:</p>"
                        "<ul>"
                        "<li><strong>Laminate — about 2.23 m² (24 ft²) per box.</strong> A rigid click-together board with a photographic top layer and an HDF core. Durable, inexpensive, and unforgiving of a damp floor.</li>"
                        "<li><strong>Vinyl plank / LVT — about 2.23 m² (24 ft²) per box.</strong> Waterproof, warm underfoot and stable in kitchens and bathrooms where laminate is not. Usually glued or clicked, with a wear layer measured in mils or millimetres that determines how well it holds up.</li>"
                        "<li><strong>Engineered wood — about 1.86 m² (20 ft²) per box.</strong> A real wood veneer on a plywood core, so it moves less with humidity than solid timber and can be used over underfloor heating.</li>"
                        "<li><strong>Solid hardwood — about 1.86 m² (20 ft²) per box.</strong> Solid timber throughout. Beautiful, and the most sensitive to moisture — it needs to acclimatise and it should not go below grade or over a concrete slab without careful preparation.</li>"
                        "<li><strong>Cork — about 2.0 m² (21.5 ft²) per box.</strong> Soft, warm and quiet underfoot.</li>"
                        "</ul>"
                        "<p>If your product is not listed, choose the custom option and enter the coverage printed on the box. That is always the authoritative number.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A room 15 feet by 12 feet gives 180 square feet. With laminate at 24 square feet per box and a 10% wastage allowance, that is 180 × 1.1 ÷ 24 = 8.25 boxes — so 9 boxes, giving 216 square feet of material and a genuine spare.</p>"
                        "<p>Lay the same room in herringbone and the allowance rises to 15–20%. At 18%, the calculation is 180 × 1.18 ÷ 24 = 8.85 boxes, which still rounds to 9 — but the margin is now thin, and a single miscut would send you back to the shop for a tenth box. That is the practical argument for buying the spare box up front.</p>"
                        "<p>If you are adding underlayment at 100 square feet per roll, 180 square feet needs two rolls.</p>"
            },
            {
                "h": "Underlayment, expansion gaps and the things that go wrong",
                "body": "<p>Underlayment is not optional on a floating floor. It provides a little give, deadens sound, and allows the boards to expand and contract slightly as humidity changes. Foam is cheapest and thinnest; combination foam-and-foil adds a vapour barrier; cork and rubber are quieter and firmer and last longer underfoot.</p>"
                        "<p>Leave an expansion gap of about 10 mm all round the perimeter, and cover it with skirting or beading. This is the single most common installation mistake with laminate and floating vinyl: the floor is fitted tight to the walls, then it warms up, expands, has nowhere to go and lifts into a ridge down the middle of the room. The gap looks wrong when you fit it and is correct.</p>"
                        "<p>Acclimatise the boxes in the room they will be laid in for at least 48 hours, stacked flat and unopened. Timber and laminate both move with the moisture content of the air, and boards fitted straight from a cold warehouse into a warm room will move after installation rather than before.</p>"
            }
        ],
        "table": {
            "caption": "Boxes needed by room size (10% wastage)",
            "head": ["Floor area", "Laminate (24 ft²/box)", "Engineered (20 ft²/box)", "Cork (21.5 ft²/box)"],
            "rows": [
                ["100 ft²", "5 boxes", "6 boxes", "6 boxes"],
                ["150 ft²", "7 boxes", "9 boxes", "8 boxes"],
                ["180 ft²", "9 boxes", "10 boxes", "10 boxes"],
                ["250 ft²", "12 boxes", "14 boxes", "13 boxes"],
                ["300 ft²", "14 boxes", "17 boxes", "16 boxes"],
                ["500 ft²", "23 boxes", "28 boxes", "26 boxes"]
            ]
        },
        "faqs": [
            ("How many boxes of flooring do I need?",
             "Divide the floor area, plus your wastage allowance, by the coverage per box and round up. A 180 square foot room with 10% waste needs 198 square feet of material, which at 24 square feet per box is 8.25 boxes — 9 boxes. Enter your room dimensions and product above and the calculator does this directly."),
            ("How much waste should I allow for flooring?",
             "10% for a straight lay, 15% for a diagonal lay, and 15–20% for herringbone or chevron. Add a little more if the room has alcoves, chimney breasts or awkward returns, since offcuts at a complex edge rarely fit anywhere else."),
            ("How much does a box of laminate cover?",
             "Typically about 2.23 square metres, or 24 square feet, but it varies by product and manufacturer. Always check the figure printed on the box and use the custom option here if it differs — the difference between a 20 and a 24 square foot box is more than a box over a large room."),
            ("Do I need underlayment for laminate flooring?",
             "Yes. A floating floor needs underlayment for acoustic insulation, a small amount of give underfoot, and to allow the boards to move. Skipping it also voids most manufacturers' warranties. Combination foam-and-foil underlayment adds a moisture barrier, which matters over a concrete slab."),
            ("What is the expansion gap and why does it matter?",
             "A gap of about 10 mm left between the flooring and the wall, hidden by skirting or beading. Laminate and wood both expand as humidity rises, and if the floor is fitted tight to the walls it has nowhere to go and will lift into a ridge. It is the most common installation error with floating floors."),
            ("Can I lay laminate in a bathroom or kitchen?",
             "Not in a bathroom. Laminate has an HDF core that swells permanently once water reaches it. A kitchen is possible with care around the sink and dishwasher, but vinyl plank or luxury vinyl tile is the better choice for both — it is waterproof through its full thickness and looks very similar.")
        ],
        "related": ["tile-calculator", "paint-calculator", "square-footage-calculator", "roofing-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "fence-calculator",
        "calc": "fence-calculator",
        "category": "outdoor",
        "icon": "🚧",
        "h1": "Fence Calculator",
        "title": "Fence Calculator — Posts, Panels, Rails, Pickets & Concrete",
        "meta_description": "Calculate fence posts, bays, panels, rails or pickets from the fence run and post spacing, plus the concrete needed to set each post. Works in feet and metres.",
        "meta_keywords": "fence calculator, fence post calculator, how many fence posts, picket fence calculator, fence panel calculator, post hole concrete calculator, chain link fence calculator",
        "tagline": "Posts, bays, rails or pickets from your fence run — plus the concrete to set every post.",
        "blurb": "Posts, panels, rails or pickets from your fence run, plus post-hole concrete.",
        "intro": [
            "<p>Fence quantities all follow from one decision: the post spacing. Set the posts and everything else is determined — the number of bays, the panels, the rails, the pickets, and the concrete for the holes. Change the spacing and every number changes with it.</p>",
            "<p>This calculator handles panel fences, picket fences, post-and-rail and chain link. It also works out the concrete for the post holes, which is the quantity people most often forget and then guess at, usually low.</p>"
        ],
        "formula": "<p><strong>Posts</strong> = ⌈fence run ÷ post spacing⌉ + 1 &nbsp;·&nbsp; <strong>Bays</strong> = posts − 1</p><p><strong>Rails</strong> = bays × spacing × rails per bay &nbsp;·&nbsp; <strong>Pickets</strong> = run ÷ (picket width + gap)</p><p><strong>Concrete per post</strong> = (π × hole radius² × depth) − (post section² × depth)</p>",
        "sections": [
            {
                "h": "Post spacing sets everything else",
                "body": "<p>Most timber and panel fences use bays of 8 feet, or about 2.4 metres. Chain link often stretches to 10 feet because the fabric is tensioned between posts rather than supported by them. Some decorative or lightweight fence styles go to 6 feet, which adds posts and cost but makes the fence noticeably more rigid.</p>"
                        "<p>The end post matters as much as the spacings. A run of 100 feet at 8 foot bays divides exactly into 12½ bays, so you need 14 posts — 12 full bays plus a shorter final bay, and an extra post to close it. Dividing the run by the spacing and rounding down will leave you one post short every time, which is why the calculator always adds the closing post.</p>"
                        "<p>Angles and ends need more substantial posts than the ones in between. A run of posts in a straight line only has to hold the fence up; an end post has to resist the entire fence pulling on it, and a corner post has to resist it from two directions. By tradition these are set deeper and frequently braced.</p>"
            },
            {
                "h": "Post holes, depth and the one-third rule",
                "body": "<p>A common rule is that a third of the post's total length goes into the ground. An 8 foot post becomes 2 feet 8 inches in the ground with 5 foot 4 inches above. At least 24 inches is usual for a 6 foot fence, and more in sandy or loose ground.</p>"
                        "<p>The depth should also reach below the frost line where ground freezing is a factor. Frost heave lifts an inadequately set post a little each winter, and after a few seasons the fence is visibly leaning. In cold climates this can mean a hole deeper than the one-third rule suggests — check your local building guidance.</p>"
                        "<p>Hole diameter should be about three times the post's width. For a 4 inch post that is a 12 inch hole, which is what the calculator defaults to. A hole that is too tight cannot take enough concrete to hold the post; a hole that is too wide simply uses more material for the same result.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A 100 foot fence run at 8 foot spacing needs 14 posts and creates 13 bays. With two rails per bay that is 200 linear feet of rail — two runs of 100 feet, one per rail line.</p>"
                        "<p>Note that this is <em>not</em> 13 bays × 8 feet × 2, which would give 208 feet. The run is 100 feet, so the last bay is 4 feet rather than 8, and rails are cut to the run, not to the nominal bay width. Estimating rails from bays × spacing over-orders by 4% on this run, and by more whenever the run divides awkwardly by the post spacing. As a panel fence it needs 13 panels.</p>"
                        "<p>Post holes at 12 inches diameter and 24 inches deep, with a 4 inch post. Each hole is π × 0.5² × 2 = 1.571 cubic feet, less the 0.222 cubic feet occupied by the post, so 1.349 cubic feet of concrete — 0.038 cubic metres per post, or 0.535 cubic metres across all 14 posts. At a bag yield of 0.011 cubic metres per 25 kilogram bag, that is 49 bags.</p>"
                        "<p>That last figure surprises people. Setting 14 posts properly takes the best part of a pallet of post-mix, and discovering it halfway through is the difference between finishing the job and making a second trip.</p>"
            },
            {
                "h": "Post-mix, dry mix and what actually holds a post",
                "body": "<p>Fast-setting post-mix is the convenient option: pour it dry into the hole around the post, add water, and leave it. It is more expensive per kilogram than mixing your own, and its advantage is speed and no mess. Where you have many posts, a 1 : 4 cement-to-ballast mix is considerably cheaper.</p>"
                        "<p>Whatever you use, the concrete's job is not to grip the post — it is to be a heavy, wide lump of mass that the post cannot move through. That is why the hole needs both depth and width, and why a wider hole with more concrete resists lateral load far better than a narrow one. Pack the concrete well as you fill; air pockets reduce the mass you are relying on.</p>"
                        "<p>Crown the concrete slightly above ground level so water runs away from the post rather than pooling at its base. And use posts rated for ground contact — timber that is only treated for above-ground use will rot at the soil line long before the rest of the fence fails.</p>"
            },
            {
                "h": "Fence height, planing permission and neighbours",
                "body": "<p>The default height is 6 feet, which is the common limit for a domestic boundary fence without planning permission in many jurisdictions — but the rules differ, and they differ again for a fence at the front of a property, on a corner, or next to a highway. Check locally before building. In many places a 6 foot fence is permitted at the rear but only 3 or 4 feet at the front.</p>"
                        "<p>Wind load rises steeply with height, and a solid 6 foot fence presents a great deal of it. In exposed locations, posts that are simply planted 2 feet into ordinary soil will not survive. Options are deeper holes, more posts, or a design that lets some wind through.</p>"
                        "<p>Finally, if the fence is on a boundary, talk to the neighbour first. It is cheaper and considerably more pleasant than a dispute, and in many places the fence becomes a shared asset with shared obligations.</p>"
            }
        ],
        "table": {
            "caption": "Posts and bays by fence run (8 ft spacing, all four types)",
            "head": ["Fence run", "Posts", "Bays", "Rails at 2 per bay", "Concrete (24 in hole, 4 in post)"],
            "rows": [
                ["20 ft", "4", "3", "40 lin ft", "0.15 m³"],
                ["50 ft", "8", "7", "100 lin ft", "0.31 m³"],
                ["100 ft", "14", "13", "200 lin ft", "0.54 m³"],
                ["150 ft", "20", "19", "300 lin ft", "0.76 m³"],
                ["200 ft", "26", "25", "400 lin ft", "0.99 m³"],
                ["300 ft", "39", "38", "600 lin ft", "1.49 m³"]
            ]
        },
        "faqs": [
            ("How many fence posts do I need?",
             "Divide the fence run by the post spacing, round up, and add one for the closing post. A 100 foot run at 8 foot spacing gives 12.5, which rounds to 13 bays, plus one post — 14 posts in total. Forgetting the extra post is the most common error in fence estimating."),
            ("How far apart should fence posts be?",
             "8 feet (about 2.4 metres) for most timber and panel fences. Chain link often goes to 10 feet, since the fabric is tensioned between posts. Shorter spans of 6 feet add posts and cost but are noticeably more rigid, and are worth it in exposed or windy locations."),
            ("How deep should fence posts be set?",
             "One third of the post's total length is a common rule, so an 8 foot post goes 2 feet 8 inches into the ground. At least 24 inches is usual for a 6 foot fence. The hole must also reach below the frost line, or frost heave will lift the post a little each winter."),
            ("How much concrete do I need per fence post?",
             "About 0.038 cubic metres — roughly two 25 kilogram bags of post-mix — for a 12 inch diameter hole 24 inches deep with a 4 inch post. Across 14 posts that is 0.54 cubic metres, or about 49 bags. Many people underestimate this badly; it is worth ordering in one go."),
            ("How many pickets do I need for a picket fence?",
             "Divide the fence run by the picket width plus the gap, and add one for the closing picket. At 4 inch pickets with a 2 inch gap each picket occupies 6 inches, so a 100 foot run takes 201 — 200 pickets would span 99 feet 10 inches and leave the last gap open. A tighter gap uses more pickets and blocks more wind, which matters on an exposed site."),
            ("How tall can I build a fence without permission?",
             "It varies by country and by location within a country — often 6 feet at the rear and 3 or 4 feet at the front, with stricter limits on corners and next to highways. Check the current local rules before you build, and talk to neighbours if the fence is on a shared boundary.")
        ],
        "related": ["concrete-calculator", "gravel-calculator", "square-footage-calculator", "tile-calculator"]
    }
]
