# -*- coding: utf-8 -*-
"""Content for the Area & Land cluster of /tools/ pages.

Every entry is one page. ``intro``, ``sections`` and the reference table are
what make each page distinct — the calculators behind them share an engine,
but no two pages here should read as the same page with the units swapped.
Text is written for a global audience; the South Asian land units appear as
one supported unit family rather than as the framing of the whole hub.
"""

AREA_TOOLS = [

    # ------------------------------------------------------------------
    {
        "slug": "area-converter",
        "calc": "area-converter",
        "category": "area",
        "icon": "🔁",
        "h1": "Area Converter",
        "title": "Area Converter — ft², m², yd², Acres, Hectares, Marla, Kanal",
        "meta_description": "Free area converter for square feet, square metres, square yards, acres, hectares, marla and kanal. Pick your marla standard and convert every unit at once.",
        "meta_keywords": "area converter, area unit converter, square feet to square metres, acres to hectares, marla converter, kanal converter, convert area units",
        "tagline": "Convert between eleven area units at once — imperial, metric and South Asian land measures, with the marla standard left in your hands.",
        "blurb": "Convert any area into eleven units at once, including marla and kanal.",
        "intro": [
            "<p>This converter takes one area figure and shows it in every unit we support at the same time: square feet, square metres, square yards, square inches, square centimetres, acres, hectares, square kilometres, square miles, marla and kanal. You do not have to run it twice — enter the number once and read the row you need.</p>",
            "<p>Area conversion trips people up for one reason: most units are fixed by international definition, but a few are not. An acre is always 43,560 square feet and a hectare is always 10,000 square metres, everywhere on earth. A <strong>marla</strong> is not. It is a traditional unit that different regions and different housing societies define as 272.25, 250 or 225 square feet, so the same advertised plot can differ by more than 20% depending on whose definition you use. That is why this tool asks you to choose a marla standard instead of quietly assuming one.</p>"
        ],
        "formula": "<p><strong>To convert, multiply by the factor for the target unit</strong></p><p>The calculator converts your input to square feet first, then divides by the factor of every other unit. Square feet is the common meeting point because the imperial and South Asian land units are defined in it, and the metric units convert to it exactly.</p>",
        "sections": [
            {
                "h": "The fixed conversions worth memorising",
                "body": "<ul>"
                        "<li>1 square foot = 0.09290304 square metres (exactly, because 1 foot = 0.3048 m exactly)</li>"
                        "<li>1 square metre = 10.7639104 square feet</li>"
                        "<li>1 square yard = 9 square feet</li>"
                        "<li>1 acre = 43,560 square feet = 4,046.8564 square metres</li>"
                        "<li>1 hectare = 10,000 square metres = 2.4710538147 acres</li>"
                        "<li>1 square mile = 640 acres = 2.589988 square kilometres</li>"
                        "<li>1 square kilometre = 100 hectares = 247.105 acres</li>"
                        "</ul>"
            },
            {
                "h": "Why marla needs a selector and kanal does not",
                "body": "<p>Kanal is defined as exactly 20 marla wherever it is used, and traditionally as 605 square yards — 5,445 square feet. Kanal therefore has a fixed square-foot value and no selector.</p>"
                        "<p>Marla is the variable one. In traditional revenue records and older city schemes it is 272.25 square feet (30.25 square yards), which is what makes 20 marla equal a 5,445 square foot kanal and 8 kanal equal an acre. In many newer housing societies a marla is rounded to 250 square feet, and some regions and older schemes use 225 square feet. If you are buying or selling land, confirm the standard in writing before you agree a price.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>You are comparing two listings: one plots out at 1,200 square feet and the other at 111 square metres. Enter 1,200 with the from-unit set to square feet and the result is 111.484 square metres — so the two plots are the same size, give or take a rounding difference in the listing.</p>"
                        "<p>Now enter 10 with the from-unit set to acres. The table returns 4.0468564 hectares, 43,560 square feet, 4,840 square yards, 160 marla and 8 kanal — the last two only at the 272.25 square foot marla standard. Switch the marla standard to 250 and the same acre reads 174.24 marla.</p>"
            },
            {
                "h": "Where each unit is used",
                "body": "<p><strong>Square feet</strong> dominates residential floor area in the United States, the United Kingdom, India, Pakistan and the Gulf. <strong>Square metres</strong> is the standard for construction drawings and floor plans almost everywhere else, and for any engineering document. <strong>Acres</strong> cover rural and development land in the US, UK, Ireland and the Commonwealth; <strong>hectares</strong> do the same job in most of Europe, Latin America, Africa and Asia. <strong>Marla and kanal</strong> are the working units of residential plot markets in Pakistan and parts of northern India.</p>"
            }
        ],
        "table": {
            "caption": "Common area equivalents",
            "head": ["From", "Equals", "Also equals"],
            "rows": [
                ["1 acre", "43,560 ft²", "0.404686 ha · 160 marla (272.25 ft²)"],
                ["1 hectare", "10,000 m²", "2.471054 ac · 107,639 ft²"],
                ["1 square mile", "640 ac", "2.589988 km² · 2,589,988 m²"],
                ["1 square kilometre", "100 ha", "247.105 ac · 0.386102 mi²"],
                ["1 square yard", "9 ft²", "0.836127 m²"],
                ["1 square metre", "10.763910 ft²", "1.195990 yd²"],
                ["1 kanal", "605 yd²", "5,445 ft² · 20 marla"],
                ["1 marla (272.25 ft²)", "30.25 yd²", "25.2929 m²"],
                ["1 marla (250 ft²)", "27.778 yd²", "23.2258 m²"],
                ["1 marla (225 ft²)", "25 yd²", "20.9032 m²"]
            ]
        },
        "faqs": [
            ("How many square feet are in a marla?",
             "It depends on the standard. The traditional revenue standard is 272.25 square feet (30.25 square yards), many modern housing societies use 250 square feet, and some regions and older schemes use 225 square feet. This converter lets you pick the standard rather than assuming one, because the difference between 272.25 and 225 is over 20% of the plot area."),
            ("How many marla are in an acre?",
             "160 marla at the traditional 272.25 square foot standard, because 43,560 ÷ 272.25 = 160. At the 250 square foot standard the same acre is 174.24 marla, and at 225 square feet it is 193.6 marla. This is the clearest example of why the standard matters."),
            ("Is a hectare bigger than an acre?",
             "Yes. One hectare is 10,000 square metres, which is 2.471054 acres — roughly two and a half acres. Going the other way, one acre is 0.40468564224 hectares, just over two fifths of a hectare."),
            ("How many square metres is 1,000 square feet?",
             "92.90304 square metres. Multiply any figure in square feet by 0.09290304 to get square metres, or divide by 10.7639104. The conversion is exact because the foot is defined as exactly 0.3048 metres."),
            ("How many kanal in an acre?",
             "Eight, at the traditional kanal of 5,445 square feet. That works because 8 × 5,445 = 43,560 square feet, exactly one acre. It also means one kanal is one eighth of an acre, or 0.125 acres."),
            ("Why does the calculator show so many decimal places?",
             "Because rounding early introduces real error when you convert a large area. A single acre in hectares is 0.404686, and rounding that to 0.4 would misstate a 5,000 acre estate by nearly 24 hectares. Convert precisely, then round the final number to whatever your document needs.")
        ],
        "related": ["square-footage-calculator", "land-area-calculator", "plot-area-calculator", "square-feet-to-square-meters"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "square-footage-calculator",
        "calc": "square-footage-calculator",
        "category": "area",
        "icon": "📐",
        "h1": "Square Footage Calculator",
        "title": "Square Footage Calculator — Rectangle, Circle &amp; Triangle",
        "meta_description": "Work out square footage from length and width, or from a circle, triangle or trapezoid. Get the area in ft², m², yd² and acres, with cost per ft².",
        "meta_keywords": "square footage calculator, square foot calculator, how to calculate square feet, area calculator, room square footage, cost per square foot",
        "tagline": "Enter any shape and get square footage — plus square metres, square yards, acres and a cost estimate if you have a price per square foot.",
        "blurb": "Square footage for rectangles, circles, triangles and trapezoids, with a cost estimate.",
        "intro": [
            "<p>Square footage is the unit nearly every flooring, painting, roofing and real-estate figure is quoted in. This calculator works out the area of a rectangle, a circle, a triangle or a trapezoid, converts your measurements to feet first so you can mix units between fields, and gives you the result in square feet along with square metres, square yards, acres and hectares.</p>",
            "<p>If you know the price per square foot — for flooring, land, or a builder's rate — enter it and the total cost appears alongside the area. The price is deliberately left as a plain number with no currency attached, so the tool works the same whether you are pricing in dollars, euros, pounds, rupees or dirhams.</p>"
        ],
        "formula": "<p><strong>Rectangle:</strong> length × width &nbsp;·&nbsp; <strong>Circle:</strong> π × (diameter ÷ 2)² &nbsp;·&nbsp; <strong>Triangle:</strong> ½ × base × perpendicular height &nbsp;·&nbsp; <strong>Trapezoid:</strong> ½ × (side A + side B) × the distance between them</p>",
        "sections": [
            {
                "h": "Choosing the right shape",
                "body": "<p>Most rooms are rectangles, so length × width is usually all you need. Reach for the other shapes when the space is not a clean rectangle:</p>"
                        "<ul>"
                        "<li><strong>Trapezoid</strong> is the one people miss. A room that is wider at one end than the other is a trapezoid, not a rectangle. Measure both widths and the distance between them, and the area will be smaller than simply multiplying the average width by the length — the calculator does that averaging properly.</li>"
                        "<li><strong>Circle</strong> takes the diameter, not the radius, because that is what you can actually measure across a round room or a circular patio.</li>"
                        "<li><strong>Triangle</strong> uses the perpendicular height — the straight-line distance from the base to the opposite corner — not the length of either sloping side.</li>"
                        "</ul>"
                        "<p>For an L-shaped room, split it into two rectangles, work out each one and add them. The calculator's “how many identical areas” field multiplies one shape, so it is the wrong tool for two different rectangles — use it twice instead.</p>"
            },
            {
                "h": "Measure twice, and measure in the middle",
                "body": "<p>Rooms are rarely perfectly square even when the drawing says they are. Measure the length at both ends and the width at both sides; if the two readings differ by more than an inch or two, treat the room as a trapezoid so the error is captured rather than averaged away. Measure at floor level rather than skirting-board height, and take the figure from wall to wall, not to the edge of the carpet.</p>"
                        "<p>For a whole house, measure each room separately and add the results. A single measurement around the outside of the building gives you the footprint including internal and external walls, which is a larger and different number from the usable floor area.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A room measures 15 feet 6 inches by 12 feet 3 inches. Convert to decimal feet first — 15.5 by 12.25 — and the calculator returns 189.88 square feet, or 17.64 square metres. At a flooring price of 4 per square foot, the material cost comes out at 759.50 in the same currency.</p>"
                        "<p>A plot 32 feet wide at the road and 28 feet wide at the back, with 90 feet between the two widths, is a trapezoid: ½ × (32 + 28) × 90 = 2,700 square feet. At the 272.25 square foot marla standard that is 9.92 marla, and the calculator shows the figure for the 250 and 225 standards too.</p>"
            },
            {
                "h": "Square footage is not floor area",
                "body": "<p>The number this calculator produces is a flat, two-dimensional area. It is what you need for flooring, paint, roof covering and land pricing. It is <em>not</em> the same as the built-up area or the sellable area on a floor plan, which are measured differently and may exclude or include walls, balconies and common areas according to local rules. When a listing quotes a built-up area, ask what it includes before comparing it with a square footage figure you calculated yourself.</p>"
            }
        ],
        "table": {
            "caption": "Square footage of common room sizes",
            "head": ["Dimensions (feet)", "Square feet", "Square metres"],
            "rows": [
                ["10 × 10", "100 ft²", "9.29 m²"],
                ["10 × 12", "120 ft²", "11.15 m²"],
                ["12 × 12", "144 ft²", "13.38 m²"],
                ["12 × 15", "180 ft²", "16.72 m²"],
                ["14 × 16", "224 ft²", "20.81 m²"],
                ["15 × 20", "300 ft²", "27.87 m²"],
                ["20 × 20", "400 ft²", "37.16 m²"],
                ["20 × 30", "600 ft²", "55.74 m²"]
            ]
        },
        "faqs": [
            ("How do I calculate square feet from inches?",
             "Multiply the length in inches by the width in inches, then divide by 144. There are 144 square inches in a square foot. This calculator does it for you — set the unit dropdowns beside the length and width fields to inches and enter the raw measurements."),
            ("How do I work out the square footage of an irregular room?",
             "Break it into shapes you can measure. An L-shaped room is two rectangles: measure each and add them. A room that is wider at one end than the other is a trapezoid — measure both widths and the distance between them and use the trapezoid shape here. For a curved bay or an angled corner, a triangle plus a rectangle is usually close enough."),
            ("Is square footage the same as square metres?",
             "No. One square metre is 10.7639104 square feet, so a 100 square metre apartment is about 1,076 square feet. If a floor plan is in square metres and a price is quoted per square foot, convert first — the two numbers differ by more than ten times, which is an easy and expensive mistake to make."),
            ("Why is my calculated area different from the listing?",
             "Listings often quote a built-up or carpet area rather than a true floor area, and rules on what those include vary by country and by developer. Walls, balconies, stairwells and shared corridors are treated differently in each. Treat your own measurement as the accurate one for ordering materials, and the listing figure as a marketing number."),
            ("Do I add a waste allowance for flooring?",
             "Yes, and this calculator gives you the bare area. Add 5–10% for a straightforward rectangular room with a simple laying pattern, and 10–15% for a diagonal or herringbone pattern, a room with many corners, or a large-format tile where every cut wastes more of the tile. The dedicated flooring and tile calculators on this site apply the allowance for you.")
        ],
        "related": ["area-converter", "land-area-calculator", "plot-area-calculator", "tile-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "land-area-calculator",
        "calc": "land-area-calculator",
        "category": "area",
        "icon": "🌍",
        "h1": "Land Area Calculator",
        "title": "Land Area Calculator — Acres, Hectares, Marla &amp; Kanal",
        "meta_description": "Calculate land area from length and width, or enter an area you know, and see it in acres, hectares, square feet, square metres, marla and kanal.",
        "meta_keywords": "land area calculator, plot area calculator, acres calculator, hectares calculator, land measurement, marla kanal calculator, land size conversion",
        "tagline": "Measure a plot, field or site and see it in every land unit — acres and hectares for records, marla and kanal for the local market.",
        "blurb": "Work out land area in acres, hectares, marla and kanal from a simple measurement.",
        "intro": [
            "<p>Land changes hands in units that have almost nothing to do with each other. A rural estate is priced in acres or hectares, a building plot is priced in marla or kanal in South Asia, and a mortgage or survey document will want square feet or square metres. This calculator takes one measurement and puts the answer in all of them at once, so you can check a listing against a title deed without converting by hand.</p>",
            "<p>Enter the dimensions if you have them, or pick “I already know the area” and type in a figure from a survey, a deed or a listing. The tool also accepts a per-marla and a per-acre price so you can see whether two listings quoted in different units are actually the same price.</p>"
        ],
        "formula": "<p><strong>Rectangle:</strong> length × width &nbsp;·&nbsp; <strong>Triangle:</strong> ½ × base × perpendicular height &nbsp;·&nbsp; <strong>Trapezoid:</strong> ½ × (side A + side B) × the distance between them</p>",
        "sections": [
            {
                "h": "What an acre and a hectare actually are",
                "body": "<p>An acre is 43,560 square feet — historically the area a team of oxen could plough in a day. It is 4,046.8564 square metres, roughly 208 feet square, and it is still the working unit for rural and development land in the United States, the United Kingdom, Ireland and across the Commonwealth.</p>"
                        "<p>A hectare is 10,000 square metres — a square 100 metres on each side. It replaced the acre in most of the world because it fits the metric system cleanly, and it is what agricultural, forestry and planning documents use in Europe, Latin America, Africa and most of Asia. One hectare is 2.471054 acres.</p>"
                        "<p>Because both are large, buying a hectare when you meant an acre is an expensive misunderstanding: the hectare is nearly two and a half times bigger.</p>"
            },
            {
                "h": "Marla, kanal and the South Asian plot market",
                "body": "<p>A <strong>kanal</strong> is fixed at 20 marla and, traditionally, 605 square yards — 5,445 square feet. Eight kanal make an acre, and one kanal is one eighth of an acre. That relationship holds only because the traditional marla is 272.25 square feet.</p>"
                        "<p>A <strong>marla</strong> is the variable unit. Traditional revenue records and older city schemes use 272.25 square feet. Many modern housing societies round it to 250 square feet. Some regions and older schemes use 225. The same advertised “10 marla” plot can therefore be 2,722, 2,500 or 2,250 square feet — a difference of up to 21% in what you actually get. Always ask which standard the price is quoted against, and put it in writing.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A plot measures 90 feet by 60 feet. That is 5,400 square feet, 600 square yards, 501.68 square metres, 19.83 marla at the traditional standard, 0.992 kanal and 0.124 acres. The calculator shows 21.6 marla at the 250 square foot standard — the same physical plot, described two different ways.</p>"
                        "<p>Suppose the seller is asking a price per marla. Enter it and the total land value appears; enter a price per acre instead and you get the other total. If both prices are quoted, comparing the two totals against the same plot is the quickest way to see which listing is genuinely cheaper.</p>"
            },
            {
                "h": "Converting a surveyed area",
                "body": "<p>Survey documents rarely give you a neat rectangle. They give a boundary description, a plan drawing, or an area already calculated by a licensed surveyor. If you have that final figure, use the “I already know the area” option and pick the unit the document uses — the calculator converts from there. If you only have a plan drawing with irregular boundaries, the practical approach is to divide the plot into triangles and trapezoids on paper, work out each one here, and add them up.</p>"
            }
        ],
        "table": {
            "caption": "Land unit reference",
            "head": ["Unit", "Square feet", "Square metres", "Acres"],
            "rows": [
                ["1 square yard", "9", "0.8361", "0.000207"],
                ["1 marla (225 ft²)", "225", "20.903", "0.005165"],
                ["1 marla (250 ft²)", "250", "23.226", "0.005740"],
                ["1 marla (272.25 ft²)", "272.25", "25.293", "0.006250"],
                ["1 kanal", "5,445", "505.86", "0.125000"],
                ["1 acre", "43,560", "4,046.86", "1"],
                ["1 hectare", "107,639.1", "10,000", "2.471054"],
                ["1 square kilometre", "10,763,910", "1,000,000", "247.1054"],
                ["1 square mile", "27,878,400", "2,589,988", "640"]
            ]
        },
        "faqs": [
            ("How do I calculate land area from length and width?",
             "Multiply length by width when both are in the same unit, then convert. If you measure in feet the answer is already square feet. This calculator lets you enter each dimension in a different unit — feet, metres, yards, inches or centimetres — and converts both before multiplying, so you can measure a long side with a tape in metres and a short side in feet without doing any arithmetic."),
            ("How many square feet is 1 kanal?",
             "5,445 square feet, which is 605 square yards or 505.86 square metres. Kanal is fixed at 20 marla, and on the traditional 272.25 square foot marla standard that gives 20 × 272.25 = 5,445. If a society defines marla as 250 square feet, its kanal works out at 5,000 square feet instead."),
            ("How many acres is a 10 marla plot?",
             "At the traditional standard, 10 marla is 2,722.5 square feet, which is 0.0625 acres — one sixteenth of an acre, or half a kanal. Under the 250 square foot standard, 10 marla is 2,500 square feet, or 0.0574 acres."),
            ("What is the difference between an acre and a hectare?",
             "An acre is 43,560 square feet (4,046.86 m²) and a hectare is 10,000 square metres (107,639 square feet). A hectare is about 2.47 times larger than an acre. Use acres for land records in the US, UK and Commonwealth countries, and hectares for metric-system countries and scientific or planning documents."),
            ("Should I use the surveyed area or my own measurement?",
             "Use the surveyed area for anything legal or financial — a purchase, a mortgage or a planning application — because a licensed surveyor's figure is the one that stands. Use your own measurement for practical decisions like how much fencing or turf to buy, and expect it to differ slightly from the deed because boundaries are rarely perfectly straight.")
        ],
        "related": ["plot-area-calculator", "area-converter", "square-footage-calculator", "marla-to-square-feet"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "plot-area-calculator",
        "calc": "plot-area-calculator",
        "category": "area",
        "icon": "🏡",
        "h1": "Plot Area Calculator",
        "title": "Plot Area Calculator — Marla, Kanal &amp; Perimeter",
        "meta_description": "Work out a plot's area in square feet, marla and kanal, plus the boundary length for a wall or fence. Handles plots that narrow at one end.",
        "meta_keywords": "plot area calculator, plot size calculator, marla calculator, kanal calculator, plot perimeter, boundary wall length, irregular plot area",
        "tagline": "Plot area in every unit, plus the perimeter you will actually need for a boundary wall or fence.",
        "blurb": "Plot area in marla, kanal and square feet — plus the perimeter for boundary walls.",
        "intro": [
            "<p>This calculator is built for a building plot rather than a field. Alongside the area in square feet, square metres, square yards, marla, kanal, acres and hectares, it returns the <strong>perimeter</strong> — the total run along the edges of the plot, which is the number you need before you can price a boundary wall, a fence or the foundation strip.</p>",
            "<p>Plots are rarely perfect rectangles. Tick the box for a plot that narrows or widens at one end and the calculator switches to the trapezoid formula, measuring the sloping side properly instead of averaging the two widths and hoping the error is small.</p>"
        ],
        "formula": "<p><strong>Rectangular plot:</strong> length × width &nbsp;·&nbsp; <strong>Plot wider at one end:</strong> ½ × (width A + width B) × length &nbsp;·&nbsp; <strong>Perimeter:</strong> the sum of the actual edges, with the sloping side measured as a true diagonal</p>",
        "sections": [
            {
                "h": "Why the perimeter matters as much as the area",
                "body": "<p>Two plots with the same area can have very different perimeters. A 50 × 90 foot plot and a 30 × 150 foot plot are both 4,500 square feet, but the first has a perimeter of 280 feet and the second 360 feet. If you are building a boundary wall at a cost per running foot, the narrow long plot costs nearly 30% more to enclose for exactly the same land area.</p>"
                        "<p>Perimeter also drives the foundation and damp-proof course for the wall, the number of gate piers, and how much of the plot is lost to the wall's own footprint — which matters when local rules cap how much of the plot you may cover.</p>"
            },
            {
                "h": "Measuring a plot that is not rectangular",
                "body": "<p>Stand at the road and measure the frontage. Then walk to the back and measure the rear width. Measure the depth along the side boundary — the perpendicular distance between the front and rear lines, not the distance along the sloping side. Enter those three figures, tick the irregular box, and the calculator applies the trapezoid formula.</p>"
                        "<p>For a plot with a cut corner, or one boundary that runs at an angle, the practical approach is to split the plot into a rectangle plus a triangle on paper, work out each shape here, and add the two areas. It takes an extra minute and gives a figure you can defend.</p>"
            },
            {
                "h": "Worked example",
                "body": "<p>A plot measures 50 feet wide by 90 feet deep. The area is 4,500 square feet — 16.53 marla at the traditional standard, 18 marla at 250 square feet, 0.827 kanal, and 0.1033 acres. The perimeter is 280 feet, so a boundary wall in blockwork needs 280 running feet of wall plus gate piers.</p>"
                        "<p>Now suppose the same plot is 50 feet at the front and 44 feet at the back, still 90 feet deep. It becomes a trapezoid: ½ × (50 + 44) × 90 = 4,230 square feet, or 15.54 marla — about 6% less land than the rectangle it looked like on the plan. The sloping side is measured as a true diagonal, giving a perimeter of 279.8 feet.</p>"
            },
            {
                "h": "Area, covered area and local byelaws",
                "body": "<p>Almost everywhere, the permitted covered area is set as a fraction of the plot area — a floor area ratio or coverage limit. That makes the figure you calculate here the input to a planning question, not just a pricing question. Compute the area first, then check your local authority's table for the maximum ground coverage and the maximum total floor area, because those limits are usually expressed as a percentage of exactly this number.</p>"
            }
        ],
        "table": {
            "caption": "Common plot sizes",
            "head": ["Plot description", "Square feet", "Square metres", "Kanal"],
            "rows": [
                ["5 marla (250 ft² standard)", "1,250 ft²", "116.13 m²", "0.230"],
                ["5 marla (272.25 ft² standard)", "1,361 ft²", "126.46 m²", "0.250"],
                ["10 marla (250 ft² standard)", "2,500 ft²", "232.26 m²", "0.459"],
                ["10 marla (272.25 ft² standard)", "2,722 ft²", "252.93 m²", "0.500"],
                ["1 kanal", "5,445 ft²", "505.86 m²", "1.000"],
                ["2 kanal", "10,890 ft²", "1,011.7 m²", "2.000"],
                ["1 acre", "43,560 ft²", "4,046.9 m²", "8.000"]
            ]
        },
        "faqs": [
            ("How do I calculate plot area in marla?",
             "First work out the area in square feet — length times width for a rectangular plot. Then divide by the marla standard used where the plot is. At the traditional 272.25 square feet, a 2,722 square foot plot is 10 marla. This calculator shows the marla figure for the standard you pick, so you can see how the same plot reads under all three common definitions."),
            ("How do I find the perimeter of an irregular plot?",
             "Add up the length of each actual edge. For a plot that is wider at one end than the other, the two sloping sides are diagonals, not the depth of the plot — the calculator measures each as the hypotenuse of the width difference and the plot depth, which is why the perimeter comes out slightly longer than simply doubling the average width plus the depth."),
            ("What size boundary wall do I need for a 10 marla plot?",
             "Take the perimeter from this calculator and add for gate piers. A 10 marla plot at 250 square feet is typically around 25 × 100 feet, giving a perimeter of 250 feet. Add the return walls at any gate and allow for the thickness of the piers themselves before ordering block, brick or concrete."),
            ("Why is my plot measured differently from the seller's listing?",
             "Listings often quote a rounded or nominal size — “10 marla” rather than an exact measurement — and the marla standard behind it may not be stated. Between the 272.25 and 225 square foot standards that is a difference of more than 20%. Measure the plot yourself or use the surveyed dimensions, and ask in writing which standard the price assumes."),
            ("Does the shape of a plot affect its value?",
             "It affects what you can build. A narrow frontage limits the width of the house and the garage, and a deep narrow plot needs more wall and more driveway per square foot of land. Two plots of identical area can have very different buildable potential, which is why the perimeter this calculator returns is worth reading alongside the area.")
        ],
        "related": ["land-area-calculator", "area-converter", "square-footage-calculator", "fence-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "square-feet-to-square-meters",
        "calc": "square-feet-to-square-meters",
        "category": "area",
        "icon": "↔️",
        "h1": "Square Feet to Square Metres",
        "title": "Square Feet to Square Meters Converter (ft² to m²)",
        "meta_description": "Convert square feet to square metres instantly. One square foot is 0.09290304 m². Includes the formula, a conversion table and worked examples.",
        "meta_keywords": "square feet to square meters, sq ft to sq m, convert square feet to square metres, ft2 to m2, square foot to square metre calculator",
        "tagline": "Convert square feet to square metres exactly — multiply by 0.09290304, or divide by 10.7639104.",
        "blurb": "Convert ft² to m² with the exact factor and a reference table.",
        "intro": [
            "<p>Square feet and square metres are the two units nearly every property transaction and construction drawing is quoted in, and switching between them is one of the most common conversions there is. The factor is exact, not approximate: <strong>one square foot is 0.09290304 square metres</strong>, because the foot is defined as exactly 0.3048 metres and 0.3048² = 0.09290304.</p>",
            "<p>Enter a figure in square feet and the converter returns square metres to seven significant figures, along with square centimetres, square yards, square millimetres, acres and marla for context.</p>"
        ],
        "formula": "<p><strong>square metres = square feet × 0.09290304</strong> &nbsp;·&nbsp; <strong>square feet = square metres ÷ 0.09290304</strong> (or × 10.7639104)</p>",
        "sections": [
            {
                "h": "The two ways to do it, and why one is safer",
                "body": "<p>You can multiply by 0.09290304 or divide by 10.7639104. Both give the same answer, but multiplying by the smaller number is the one to reach for when you are working without a calculator. Dividing by 10.7639104 in your head invites errors, and a slip here is expensive: getting the direction wrong on a 2,000 square foot house misstates it by roughly 1,800 square metres.</p>"
                        "<p>A useful bracket to sanity-check with: one square metre is a little under eleven square feet. So a 1,000 square foot area should come out just under 93 square metres. If your answer is in the hundreds for a figure in the thousands, you have multiplied when you should have divided.</p>"
            },
            {
                "h": "Where this conversion actually comes up",
                "body": "<p>Floor plans from most of the world outside the US and UK are drawn in square metres, while the same property marketed to an international buyer is often advertised in square feet. Builders' rates are quoted per square foot in some markets and per square metre in others, so comparing two quotes means converting one of them first.</p>"
                        "<p>Flooring, tiling and paint coverage are the other frequent case. A box of laminate flooring is usually labelled with its coverage in square metres even in countries that sell houses in square feet, and paint coverage is nearly always given as square metres per litre.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<ul>"
                        "<li>1,000 ft² = 92.90304 m² — a common apartment size</li>"
                        "<li>1,200 ft² = 111.4836 m²</li>"
                        "<li>2,000 ft² = 185.80608 m² — a typical three-bedroom house</li>"
                        "<li>2,722.5 ft² = 252.929 m² — a 10 marla plot at the traditional standard</li>"
                        "<li>43,560 ft² = 4,046.8564 m² — exactly one acre</li>"
                        "</ul>"
                        "<p>Notice the last line: an acre is 4,046.86 square metres, which is why the acre is not a round number in metric and why land registries in metric countries use hectares — 10,000 square metres — instead.</p>"
            },
            {
                "h": "Avoid the classic mistakes",
                "body": "<p><strong>Confusing feet with square feet.</strong> Multiplying a length in feet by 0.3048 converts the length to metres; multiplying an area in square feet by 0.09290304 converts the area to square metres. Mixing the two converts a 100 foot wall into 92.9 square metres, which is meaningless.</p>"
                        "<p><strong>Rounding the factor too early.</strong> Using 0.093 instead of 0.09290304 introduces an error of about 0.1%, which is 2 square metres on a 2,000 square foot house — small, but avoidable.</p>"
                        "<p><strong>Converting when you should not.</strong> If both figures are already in square feet, there is nothing to convert. This sounds obvious and still causes more errors than either of the above.</p>"
            }
        ],
        "table": {
            "caption": "Square feet to square metres",
            "head": ["Square feet (ft²)", "Square metres (m²)"],
            "rows": [
                ["50", "4.645"],
                ["100", "9.290"],
                ["250", "23.226"],
                ["500", "46.452"],
                ["750", "69.677"],
                ["1,000", "92.903"],
                ["1,200", "111.484"],
                ["1,500", "139.355"],
                ["2,000", "185.806"],
                ["2,500", "232.258"],
                ["3,000", "278.709"],
                ["5,000", "464.515"],
                ["10,000", "929.030"],
                ["43,560 (1 acre)", "4,046.856"]
            ]
        },
        "faqs": [
            ("How many square metres is 1 square foot?",
             "Exactly 0.09290304 square metres. This is an exact figure, not a rounded one, because an international foot is defined as precisely 0.3048 metres and 0.3048 × 0.3048 = 0.09290304."),
            ("How many square feet is 1 square metre?",
             "10.7639104 square feet. Divide a square metre figure by 0.09290304 to convert it to square feet, or multiply by 10.7639104 — the same operation either way."),
            ("How do I convert 1,000 square feet to square metres?",
             "Multiply 1,000 by 0.09290304, which gives 92.90304 square metres. If you only need a rough figure, dividing by 10.76 gets you to 92.9 in your head, which is close enough for estimating and not close enough for a quotation."),
            ("Is a square metre bigger than a square foot?",
             "Yes, about ten and three-quarter times bigger. A square metre is a square one metre on each side; a square foot is a square roughly 30.5 centimetres on each side. This is why a figure quoted in square feet is always numerically larger than the same area in square metres."),
            ("How many square metres is an acre?",
             "4,046.8564224 square metres. This is not a round number because the acre predates the metric system; it is defined as 43,560 square feet. In metric countries land is measured in hectares instead, where one hectare is exactly 10,000 square metres and therefore 2.471054 acres.")
        ],
        "related": ["square-meters-to-square-feet", "area-converter", "square-footage-calculator", "land-area-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "square-meters-to-square-feet",
        "calc": "square-meters-to-square-feet",
        "category": "area",
        "icon": "↔️",
        "h1": "Square Metres to Square Feet",
        "title": "Square Meters to Square Feet Converter (m² to ft²)",
        "meta_description": "Convert square metres to square feet instantly. One square metre is 10.7639104 ft². Includes the formula, a conversion table and worked examples.",
        "meta_keywords": "square meters to square feet, sq m to sq ft, convert square metres to square feet, m2 to ft2, square metre to square foot calculator",
        "tagline": "Convert square metres to square feet exactly — multiply by 10.7639104, or divide by 0.09290304.",
        "blurb": "Convert m² to ft² with the exact factor and a reference table.",
        "intro": [
            "<p>Going from square metres to square feet multiplies your number by about ten and three quarters, so the answer is always much larger than the figure you started with. The exact factor is <strong>10.7639104</strong>: one square metre covers 10.7639104 square feet, because one metre is 3.280839895 feet and 3.280839895² = 10.7639104.</p>",
            "<p>This direction is the one you need when a floor plan is drawn in square metres but the market you are selling into quotes prices per square foot, or when a construction rate is given per square metre and you want to compare it with a per-square-foot quote from somewhere else.</p>"
        ],
        "formula": "<p><strong>square feet = square metres × 10.7639104</strong> &nbsp;·&nbsp; <strong>square metres = square feet ÷ 10.7639104</strong> (or × 0.09290304)</p>",
        "sections": [
            {
                "h": "Reading the answer correctly",
                "body": "<p>Because the multiplier is just over ten, a 100 square metre flat becomes 1,076 square feet and a 200 square metre house becomes 2,153 square feet. If your result is smaller than your input, you have divided when you should have multiplied.</p>"
                        "<p>A quick mental check that works well: multiply by 10, then add about 7.6%. For 150 square metres that gives 1,500 plus 114, or 1,614 square feet — the exact answer is 1,614.59. It is a genuinely useful estimate to have in your head when scanning listings.</p>"
            },
            {
                "h": "Metric plans, imperial markets",
                "body": "<p>Most countries design and build in metric. Floor areas on drawings, structural calculations and building-permit documents are in square metres almost everywhere except the United States. But residential property is still advertised in square feet to buyers in the US, the UK, India, Pakistan, Bangladesh and much of the Gulf — so a metric plan frequently has to be presented in imperial units to be understood.</p>"
                        "<p>The same applies to material coverage. A box of tiles or laminate flooring sold into a metric market will state its coverage in square metres per box; the room you are measuring may well be a round number of feet. Convert the room, not the box, and keep the box figure as the manufacturer supplied it.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<ul>"
                        "<li>50 m² = 538.20 ft²</li>"
                        "<li>100 m² = 1,076.39 ft² — a comfortable two-bedroom flat</li>"
                        "<li>150 m² = 1,614.59 ft²</li>"
                        "<li>200 m² = 2,152.78 ft² — a large family house</li>"
                        "<li>500 m² = 5,381.96 ft²</li>"
                        "<li>10,000 m² = 107,639.10 ft² — exactly one hectare</li>"
                        "</ul>"
                        "<p>The last line is worth remembering for land: because a hectare is exactly 10,000 square metres, it is exactly 107,639.1 square feet. That is the bridge between metric land documents and per-square-foot pricing.</p>"
            },
            {
                "h": "Watch the difference between length and area",
                "body": "<p>A metre is 3.28084 feet. A square metre is 10.7639 square feet — the square of that number, as it must be. Using the length factor on an area is the single most common error in this conversion, and it understates the result by a factor of more than three. If you convert a 30 square metre room by multiplying by 3.28 you get 98 square feet, when the true answer is 322.92 square feet.</p>"
            }
        ],
        "table": {
            "caption": "Square metres to square feet",
            "head": ["Square metres (m²)", "Square feet (ft²)"],
            "rows": [
                ["1", "10.764"],
                ["5", "53.820"],
                ["10", "107.639"],
                ["20", "215.278"],
                ["25", "269.098"],
                ["50", "538.196"],
                ["75", "807.293"],
                ["100", "1,076.391"],
                ["150", "1,614.587"],
                ["200", "2,152.782"],
                ["250", "2,690.978"],
                ["500", "5,381.955"],
                ["1,000", "10,763.910"],
                ["10,000 (1 hectare)", "107,639.104"]
            ]
        },
        "faqs": [
            ("How many square feet is 1 square metre?",
             "Exactly 10.7639104 square feet. An international foot is defined as exactly 0.3048 metres, so one metre is 1 ÷ 0.3048 = 3.280839895 feet, and squaring that gives 10.7639104 square feet per square metre."),
            ("How do I convert square metres to square feet quickly?",
             "Multiply by 10.764. For a rough mental estimate, multiply by 10 and add 7.6% — so 100 m² is 1,000 plus 76, or about 1,076 square feet. The exact figure is 1,076.391, so the shortcut is accurate enough for estimating but not for a quotation."),
            ("Is 100 square metres the same as 100 square feet?",
             "No — 100 square metres is 1,076.39 square feet, more than ten times larger. The two units differ by a factor of about 10.76, which is why mistaking one for the other is such an expensive error on a floor plan."),
            ("How many square feet is a hectare?",
             "107,639.104 square feet. A hectare is exactly 10,000 square metres and one square metre is 10.7639104 square feet, so the product is the answer. To go the other way, one acre is 43,560 square feet, or 0.404686 hectares."),
            ("How do I convert square metres to square yards?",
             "Multiply square metres by 1.19599. A square yard is 9 square feet, and 10.7639104 ÷ 9 = 1.19599 square yards per square metre. The square-yard figure will always be about 20% larger than the square-metre figure for the same area.")
        ],
        "related": ["square-feet-to-square-meters", "area-converter", "square-footage-calculator", "flooring-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "acres-to-hectares",
        "calc": "acres-to-hectares",
        "category": "area",
        "icon": "🌾",
        "h1": "Acres to Hectares",
        "title": "Acres to Hectares Converter (ac to ha)",
        "meta_description": "Convert acres to hectares instantly. One acre is 0.40468564224 hectares. Includes the exact formula, a conversion table and worked examples.",
        "meta_keywords": "acres to hectares, ac to ha, convert acres to hectares, acre hectare converter, land conversion acres hectares, farmland area converter",
        "tagline": "Convert acres to hectares exactly — one acre is 0.40468564224 hectares.",
        "blurb": "Convert acres to hectares with the exact factor and a land reference table.",
        "intro": [
            "<p>The acre and the hectare are the two units that divide the world's land records: acres in the United States, the United Kingdom, Ireland and across the Commonwealth; hectares almost everywhere else. Anyone dealing with rural land across that boundary needs the conversion constantly.</p>",
            "<p><strong>One acre is 0.40468564224 hectares.</strong> Put the other way, one hectare is 2.4710538 acres, so a hectare is just under two and a half acres. The acre figure is always the smaller number when both describe the same piece of land, which is a useful check when you are reading a document that quotes both.</p>"
        ],
        "formula": "<p><strong>hectares = acres × 0.40468564224</strong> &nbsp;·&nbsp; <strong>acres = hectares ÷ 0.40468564224</strong> (or × 2.4710538)</p>",
        "sections": [
            {
                "h": "Where both numbers come from",
                "body": "<p>An acre is defined as 43,560 square feet — historically the area one team of oxen could plough in a day, which is why it is not a round number in any modern system. In metric that is 4,046.8564224 square metres, arrived at by converting 43,560 square feet at exactly 0.09290304 square metres per square foot.</p>"
                        "<p>A hectare is exactly 10,000 square metres: a square 100 metres on each side. It was created with the metric system as a land unit, and it divides by ten and a hundred cleanly, which the acre does not. Dividing 4,046.8564224 by 10,000 gives the 0.40468564224 hectares in one acre.</p>"
            },
            {
                "h": "Sizes worth knowing by heart",
                "body": "<ul>"
                        "<li>1 acre = 0.4047 ha · 43,560 ft² · 4,840 yd² · 4,046.86 m²</li>"
                        "<li>10 acres = 4.0469 ha — a smallholding</li>"
                        "<li>100 acres = 40.469 ha — a working farm</li>"
                        "<li>640 acres = 258.999 ha — one square mile</li>"
                        "<li>1 hectare = 2.4711 acres · 10,000 m²</li>"
                        "<li>A square kilometre = 247.105 acres = 100 hectares</li>"
                        "</ul>"
                        "<p>The relationship between the square mile and the acre is exact and worth remembering: a square mile is exactly 640 acres. It is the reason the United States' Public Land Survey System divides land into sections of one square mile.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<p>A 12 acre field converts to 4.856 hectares. A 40 acre plot is 16.187 hectares — very close to the 16 hectare figure a European buyer might be quoted, which is the kind of near-match that makes it easy to think two listings are the same when they are not.</p>"
                        "<p>Working in the other direction for a sanity check: a 100 hectare farm is 247.105 acres, and a 500 hectare estate is 1,235.53 acres. If those numbers feel uncomfortable, you have probably applied the factor in the wrong direction.</p>"
            },
            {
                "h": "Which unit to put in a contract",
                "body": "<p>Put both. Land contracts that cross a jurisdiction boundary — an overseas buyer, a foreign lender, a multinational developer — should state the area in the unit of the local registry <em>and</em> in the other, with the conversion factor written out. An acre/ha discrepancy of a few hundredths looks trivial on paper but is real money on a large parcel, and a single stated figure in the “wrong” unit invites a dispute later.</p>"
                        "<p>For farmland, remember that the area sold and the area cultivated are rarely identical. Hedgerows, ditches, access tracks, woodland strips and building footprints all sit inside the boundary but outside the productive area. Expect the usable area to be several percent smaller than the registered area, and sometimes much more on old irregular parcels.</p>"
            }
        ],
        "table": {
            "caption": "Acres to hectares",
            "head": ["Acres", "Hectares", "Square metres"],
            "rows": [
                ["0.25", "0.1012", "1,011.7"],
                ["0.5", "0.2023", "2,023.4"],
                ["1", "0.4047", "4,046.9"],
                ["2", "0.8094", "8,093.7"],
                ["5", "2.0234", "20,234.3"],
                ["10", "4.0469", "40,468.6"],
                ["20", "8.0937", "80,937.1"],
                ["40", "16.1874", "161,874.3"],
                ["50", "20.2343", "202,342.8"],
                ["100", "40.4686", "404,685.6"],
                ["160", "64.7497", "647,497.0"],
                ["640 (1 sq mile)", "258.9988", "2,589,988.1"],
                ["1,000", "404.6856", "4,046,856.4"]
            ]
        },
        "faqs": [
            ("How many hectares is 1 acre?",
             "Exactly 0.40468564224 hectares. An acre is 43,560 square feet, which is 4,046.8564224 square metres, and a hectare is exactly 10,000 square metres — so dividing one by the other gives the factor."),
            ("Is a hectare bigger than an acre?",
             "Yes, a hectare is about two and a half times larger than an acre. Specifically, one hectare is 2.4710538 acres. If you are converting acres to hectares the number always goes down; converting hectares to acres it always goes up."),
            ("How many acres in a square mile?",
             "Exactly 640 acres. A square mile is one mile by one mile, and a mile is 5,280 feet, so a square mile is 5,280² = 27,878,400 square feet. Dividing by the 43,560 square feet in an acre gives exactly 640."),
            ("How do I convert hectares back to acres?",
             "Multiply by 2.4710538. For example, 5 hectares is 12.355 acres. If you want to be exact, divide the hectares by 0.40468564224 instead — it is the same operation, just expressed the other way round."),
            ("Why do some countries use acres and others hectares?",
             "It is a metrication question, not an agricultural one. The acre is a pre-metric English unit tied to the square foot, so it persisted in the US, UK and Commonwealth. The hectare was introduced with the metric system as a clean 10,000 square metre unit, and countries that metricated their land records moved to it. Both remain legal in many countries, which is why conversion is still needed daily.")
        ],
        "related": ["hectares-to-acres", "area-converter", "land-area-calculator", "plot-area-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "hectares-to-acres",
        "calc": "hectares-to-acres",
        "category": "area",
        "icon": "🌾",
        "h1": "Hectares to Acres",
        "title": "Hectares to Acres Converter (ha to ac)",
        "meta_description": "Convert hectares to acres instantly. One hectare is 2.4710538 acres. Includes the exact formula, a conversion table and worked examples.",
        "meta_keywords": "hectares to acres, ha to ac, convert hectares to acres, hectare acre converter, land conversion hectares to acres, farm size converter",
        "tagline": "Convert hectares to acres exactly — one hectare is 2.4710538 acres.",
        "blurb": "Convert hectares to acres with the exact factor and a land reference table.",
        "intro": [
            "<p>Hectares to acres is the direction you need when a European, African, Asian or Latin American land document meets an American, British or Commonwealth buyer. The hectare is the metric land unit used almost everywhere; the acre survives in a handful of countries that still measure land the pre-metric way.</p>",
            "<p><strong>One hectare is 2.4710538 acres.</strong> The acre figure is always larger than the hectare figure for the same piece of land — nearly two and a half times larger. If your converted number came out smaller than the number you entered, you have used the wrong factor.</p>"
        ],
        "formula": "<p><strong>acres = hectares × 2.4710538147</strong> &nbsp;·&nbsp; <strong>hectares = acres ÷ 2.4710538147</strong> (or × 0.40468564224)</p>",
        "sections": [
            {
                "h": "The exact definition behind the factor",
                "body": "<p>A hectare is exactly 10,000 square metres — a square 100 metres on each side, with no historical baggage at all. An acre is 4,046.8564224 square metres, derived from 43,560 square feet at exactly 0.09290304 square metres per square foot.</p>"
                        "<p>Dividing 10,000 by 4,046.8564224 gives 2.4710538147 acres per hectare. The figure is not round because the acre is not a metric unit; there is no version of this conversion that comes out neat.</p>"
            },
            {
                "h": "Sizes worth knowing by heart",
                "body": "<ul>"
                        "<li>1 hectare = 2.4711 acres (the rounded factor used in conversation)</li>"
                        "<li>2 hectares = 4.9421 acres — roughly a small farm</li>"
                        "<li>10 hectares = 24.7105 acres</li>"
                        "<li>40 hectares = 98.8422 acres — very nearly 100 acres</li>"
                        "<li>100 hectares = 247.105 acres</li>"
                        "<li>1 square kilometre = 100 hectares = 247.105 acres</li>"
                        "</ul>"
                        "<p>The 40 hectare figure is the one to memorise: it is almost exactly 100 acres, and it appears constantly in farm listings on both sides of the metric divide.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<p>A 20 hectare vineyard converts to 49.421 acres. A 150 hectare forestry block is 370.66 acres. A 5 hectare development site is 12.355 acres — and if the planning density is expressed as dwellings per acre rather than per hectare, that conversion is the first step in working out how many units the site can hold.</p>"
                        "<p>For agricultural comparisons, note that yields are quoted differently too: tonnes per hectare against bushels or hundredweight per acre. Converting the area is only half the job when you are benchmarking two farms.</p>"
            },
            {
                "h": "When a hectare is not a hectare",
                "body": "<p>All hectare figures are the same hectare, so the unit itself never varies. What varies is what is being measured. A “hectare” of forest, of arable land, or of a development site are all 10,000 square metres, but the productive or developable portion inside that boundary can differ dramatically from one to the next.</p>"
                        "<p>This is where the hectare differs from the marla, which genuinely has multiple regional definitions. If you are working across both worlds — a hectare-based international deed and a marla-based local listing — the hectare side is the reliable one and the marla side is the one that needs a standard written down.</p>"
            }
        ],
        "table": {
            "caption": "Hectares to acres",
            "head": ["Hectares", "Acres", "Square feet"],
            "rows": [
                ["0.1", "0.2471", "10,763.9"],
                ["0.25", "0.6178", "26,909.8"],
                ["0.5", "1.2355", "53,819.6"],
                ["1", "2.4711", "107,639.1"],
                ["2", "4.9421", "215,278.2"],
                ["5", "12.3553", "538,195.5"],
                ["10", "24.7105", "1,076,391.0"],
                ["20", "49.4211", "2,152,782.1"],
                ["40", "98.8422", "4,305,564.2"],
                ["50", "123.5527", "5,381,955.2"],
                ["100", "247.1054", "10,763,910.4"],
                ["1,000", "2,471.0538", "107,639,104.2"]
            ]
        },
        "faqs": [
            ("How many acres is 1 hectare?",
             "2.4710538147 acres. A hectare is exactly 10,000 square metres and an acre is 4,046.8564224 square metres, so dividing one by the other gives the factor. In everyday use, 2.471 is accurate enough."),
            ("How many hectares is 100 acres?",
             "40.4686 hectares. Divide 100 by 2.4710538, or multiply by 0.40468564224 — the same operation. For estimating in your head, 100 acres is a little over 40 hectares, and 250 acres is just over 100 hectares."),
            ("How many square metres is a hectare?",
             "Exactly 10,000 square metres — a square 100 metres on each side. This is the definition of the hectare, and every other hectare conversion follows from it. Ten thousand square metres is also 107,639.104 square feet."),
            ("Is a hectare the same as an acre?",
             "No. A hectare is 2.4710538 acres, so it is nearly two and a half times larger. Confusing the two is an expensive mistake on land: buying “40” of the wrong unit is the difference between roughly 16 hectares and 40 hectares."),
            ("How many hectares in a square kilometre?",
             "Exactly 100. A square kilometre is 1,000 metres by 1,000 metres, which is 1,000,000 square metres, and a hectare is 10,000 square metres — so 100 hectares fit into a square kilometre exactly. That is 247.105 acres.")
        ],
        "related": ["acres-to-hectares", "area-converter", "land-area-calculator", "plot-area-calculator"]
    }
]
