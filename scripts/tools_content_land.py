# -*- coding: utf-8 -*-
"""Content for the Pakistan Land Units cluster of /tools/.

Marla and kanal are the units most South Asian land is actually bought and
sold in, and marla has no single definition — 225, 250 and 272.25 sq ft are
all in daily use. Every page here therefore leads with the standard selector
rather than hard-coding one figure, and each page takes a different angle on
the same family of units so they do not read as one page with the words
swapped:

  marla-to-square-feet  -> the conversion itself and common plot sizes
  square-feet-to-marla  -> reading a survey or a title deed back into marla
  kanal-to-marla        -> the 20-marla relationship and larger land parcels

Kanal is always 20 marla, so it moves with the marla standard: 5,445 ft² at
272.25, 5,000 ft² at 250 and 4,500 ft² at 225. That rule is applied by every
tool on the site, not just these three.
"""

LAND_TOOLS = [

    # ------------------------------------------------------------------
    {
        "slug": "marla-to-square-feet",
        "calc": "marla-to-square-feet",
        "category": "land",
        "icon": "📐",
        "h1": "Marla to Square Feet",
        "title": "Marla to Square Feet Converter — 225, 250 & 272.25 Standards",
        "meta_description": "Convert marla to square feet, square metres and square yards using the 225, 250 or 272.25 sq ft standard. Includes a table of common plot sizes.",
        "meta_keywords": "marla to square feet, 1 marla in square feet, marla to sq ft, 5 marla in square feet, 10 marla in square feet, marla conversion, 272.25 marla, 250 sq ft marla",
        "tagline": "Convert marla to square feet — and pick which marla standard the conversion uses.",
        "blurb": "The conversion itself, with a table of the plot sizes buyers actually ask about.",
        "intro": [
            "<p>Marla is the unit most residential land in Pakistan is bought and sold in, and it is the one unit here that has no single fixed size. The traditional marla is 272.25 square feet, which makes a kanal exactly 5,445 square feet and an acre exactly 160 marla. But newer housing societies often sell on a 250 square foot marla, and older schemes in some regions use 225.</p>",
            "<p>That matters because the difference is large. A plot advertised as 10 marla is 2,722.5 square feet on the traditional standard, 2,500 on the 250 standard and 2,250 on the 225 standard — a spread of more than 20% for the same three words. Choose your standard above before you read the result, and check which one your seller is using before you agree a price.</p>"
        ],
        "formula": "<p><strong>Square feet = marla × standard</strong></p><p>Where the standard is 272.25 (traditional), 250 (modern societies) or 225 (older schemes).</p>",
        "sections": [
            {
                "h": "The three marla standards",
                "body": "<p><strong>272.25 square feet — traditional.</strong> The historic revenue measure, still used in most of Punjab and by the capital's development authority. It is not arbitrary: 272.25 square feet is exactly 30.25 square yards, and 30.25 is 5.5 squared. A kanal is 20 of these, or 605 square yards, and eight kanal make one acre.</p>"
                        "<p><strong>250 square feet — modern housing societies.</strong> A rounder figure that many private developments sell against, because it makes plot arithmetic easy: 10 marla is 2,500 square feet, 20 marla is 5,000. It is smaller than the traditional marla by about 8%, so the same plot number buys you less land.</p>"
                        "<p><strong>225 square feet — some regions and older schemes.</strong> Used in parts of Khyber Pakhtunkhwa, in some older developments and in a number of Indian states. It is 17% smaller than the traditional marla, the biggest gap between any two of the three.</p>"
                        "<p>None of these is wrong. What is wrong is not knowing which one applies to your transaction.</p>"
            },
            {
                "h": "Kanal and acre move with marla",
                "body": "<p>One relationship is fixed everywhere: a kanal is 20 marla. What follows from that is that the kanal's size in square feet depends on which marla you are using — 5,445 square feet at the traditional 272.25, 5,000 at 250, and 4,500 at 225.</p>"
                        "<p>Only the traditional marla lines up with the acre. Because 272.25 × 160 = 43,560, exactly one acre, an acre is 160 traditional marla and therefore exactly eight traditional kanal. Switch to the 250 square foot marla and an acre is no longer a whole number of kanal — it is 8.71 of them. That is not a flaw in the arithmetic; it is the reason the traditional standard exists in the form it does.</p>"
                        "<p>The calculator applies this consistently. If you change the marla standard, the kanal figure changes with it, so the two never contradict each other.</p>"
            },
            {
                "h": "Common plot sizes",
                "body": "<p>Most residential plots are sold in a small set of sizes, and knowing the square footage for each on the traditional standard is useful when comparing listings:</p>"
                        "<ul>"
                        "<li><strong>3 marla</strong> — 816.75 ft², about 75.9 m². The smallest common urban plot.</li>"
                        "<li><strong>5 marla</strong> — 1,361.25 ft², about 126.5 m². The standard small family house plot, and by far the most traded size.</li>"
                        "<li><strong>7 marla</strong> — 1,905.75 ft², about 177.1 m².</li>"
                        "<li><strong>10 marla</strong> — 2,722.5 ft², about 252.9 m². The standard mid-size plot.</li>"
                        "<li><strong>1 kanal (20 marla)</strong> — 5,445 ft², about 505.9 m². A large house or small commercial plot.</li>"
                        "<li><strong>2 kanal (40 marla)</strong> — 10,890 ft², about 1,011.7 m².</li>"
                        "</ul>"
                        "<p>On the 250 square foot standard those become 750, 1,250, 1,750, 2,500, 5,000 and 10,000 square feet — rounder numbers, which is precisely why societies adopted it.</p>"
            },
            {
                "h": "Checking which standard a listing uses",
                "body": "<p>Ask for the dimension in square feet or square metres as well as marla, and see which standard the two figures imply. Divide the stated square footage by the marla figure: 2,722.5 ÷ 10 is 272.25, so that listing is traditional; 2,500 ÷ 10 is 250, so that one is not. It takes a moment and it settles the question.</p>"
                        "<p>On a title deed or mutation document, look for the measurement in square feet, square yards or kanal — revenue records usually carry the physical measurement alongside the local unit. If the document mentions kanal, remember it is 20 marla, and check which kanal size the square footage implies.</p>"
                        "<p>If the two figures disagree by more than a few percent, ask before you proceed. A plot described as 10 marla that measures 2,500 square feet on the ground is not being misrepresented if the society sells on a 250 square foot marla — but it is 222 square feet less land than the same words mean elsewhere.</p>"
            }
        ],
        "table": {
            "caption": "Marla to square feet at all three standards",
            "head": ["Marla", "Traditional (272.25 ft²)", "Modern (250 ft²)", "Older (225 ft²)", "Traditional in m²"],
            "rows": [
                ["1", "272.25 ft²", "250.00 ft²", "225.00 ft²", "25.29 m²"],
                ["2", "544.50 ft²", "500.00 ft²", "450.00 ft²", "50.59 m²"],
                ["3", "816.75 ft²", "750.00 ft²", "675.00 ft²", "75.88 m²"],
                ["5", "1,361.25 ft²", "1,250.00 ft²", "1,125.00 ft²", "126.46 m²"],
                ["7", "1,905.75 ft²", "1,750.00 ft²", "1,575.00 ft²", "177.05 m²"],
                ["10", "2,722.50 ft²", "2,500.00 ft²", "2,250.00 ft²", "252.93 m²"],
                ["15", "4,083.75 ft²", "3,750.00 ft²", "3,375.00 ft²", "379.39 m²"],
                ["20 (1 kanal)", "5,445.00 ft²", "5,000.00 ft²", "4,500.00 ft²", "505.86 m²"],
                ["40 (2 kanal)", "10,890.00 ft²", "10,000.00 ft²", "9,000.00 ft²", "1,011.71 m²"],
                ["160 (1 acre)", "43,560.00 ft²", "40,000.00 ft²", "36,000.00 ft²", "4,046.86 m²"]
            ]
        },
        "faqs": [
            ("How many square feet is 1 marla?",
             "272.25 square feet on the traditional standard, 250 on the standard used by many modern housing societies, and 225 in some older schemes and regions. There is no single answer — the marla you are being quoted is the one that matters, so check with the seller or the society before converting."),
            ("How many square feet is 5 marla?",
             "1,361.25 square feet on the traditional 272.25 standard, which is about 126.5 square metres. On a 250 square foot marla it is 1,250 square feet, and on 225 it is 1,125 — a difference of over 200 square feet, which is a room, for the same five marla."),
            ("How many square feet is 10 marla?",
             "2,722.5 square feet traditionally, about 252.9 square metres. At 250 square feet per marla it is 2,500, and at 225 it is 2,250. Ten marla is one of the most common mid-size plot descriptions, so it is worth confirming which standard a listing uses before comparing two properties."),
            ("How many marla are in 1 acre?",
             "160 marla on the traditional 272.25 square foot standard, because 160 × 272.25 = 43,560, exactly one acre. That also makes an acre exactly eight traditional kanal. On the 250 square foot marla an acre is 174.24 marla, and it no longer divides into whole kanal."),
            ("How many square feet is 1 kanal?",
             "5,445 square feet on the traditional standard, which is 605 square yards or about 505.9 square metres. Because a kanal is always 20 marla, it follows the marla standard you choose: 5,000 square feet at 250 per marla and 4,500 at 225."),
            ("Which marla standard should I use?",
             "Use whichever standard your seller, your society or your local revenue office uses, because that is the basis the price was set against. If you are converting for information rather than for a transaction, 272.25 is the safest default — it is the historic measure and the only one that makes an acre come out as exactly 160 marla.")
        ],
        "related": ["square-feet-to-marla", "kanal-to-marla", "land-area-calculator", "plot-area-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "square-feet-to-marla",
        "calc": "square-feet-to-marla",
        "category": "land",
        "icon": "📏",
        "h1": "Square Feet to Marla",
        "title": "Square Feet to Marla Converter — Convert a Measured Area",
        "meta_description": "Convert square feet to marla for any measured area, comparing the 225, 250 and 272.25 sq ft standards side by side — the same plot described three ways.",
        "meta_keywords": "square feet to marla, sq ft to marla, convert square feet to marla, 2722.5 sq ft in marla, 1361 sq ft in marla, land measurement converter, plot size converter",
        "tagline": "Turn a measured area back into marla — and see what the same plot is called under each standard.",
        "blurb": "A measured area read back into marla, compared across all three standards.",
        "intro": [
            "<p>This is the reverse of the usual conversion, and it is the one you need when you have a real measurement. A survey, a title deed, a building plan or a tape measure all give you square feet or square metres. Marla is the unit the market prices in. Converting between the two is how you find out what a plot you have actually measured is worth.</p>",
            "<p>The complication is that the answer depends entirely on which marla standard applies to your area — and this calculator shows all three at once, so you can see straight away how differently the same piece of ground can be described. A plot of 2,722.5 square feet is 10 marla on the traditional standard, 10.89 marla at 250 square feet, and 12.1 marla at 225.</p>"
        ],
        "formula": "<p><strong>Marla = square feet ÷ standard</strong></p><p>Where the standard is 272.25 (traditional), 250 (modern societies) or 225 (older schemes).</p>",
        "sections": [
            {
                "h": "Why this direction is the harder one",
                "body": "<p>Going from marla to square feet is a single multiplication and the answer is always a whole, tidy number when the marla figure is tidy. Going the other way produces fractions, and that is where disagreements between buyers and sellers come from: a plot measured at 2,600 square feet is not a round number of marla on any standard, so both parties reach for whichever figure suits them.</p>"
                        "<p>The calculator therefore shows all three standards side by side rather than the one you selected. Seeing 9.55, 10.40 and 11.56 marla for the same plot is what makes the risk concrete. If a seller describes the plot as 10 marla and you measure 2,600 square feet, you now know which standard they are working on — the 250 square foot one — and you can price accordingly.</p>"
            },
            {
                "h": "Reading a survey or a title deed",
                "body": "<p>Revenue documents, sale deeds and mutation papers nearly always carry the physical measurement alongside the local unit, and the physical measurement is the one to trust. Look for square feet, square yards, square metres or kanal, then convert from that.</p>"
                        "<p>Note that old revenue records often give the measurement in <em>kanal and marla</em> rather than square feet — for example, “1 kanal 5 marla”. Since a kanal is 20 marla, that is 25 marla in total, which at the traditional standard is 6,806.25 square feet. Adding the parts before converting is the step people miss.</p>"
                        "<p>If the document gives square yards, divide by 30.25 to get traditional marla, because 272.25 square feet is exactly 30.25 square yards. That is a quick mental check: a plot of 302.5 square yards is 10 traditional marla.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<p><strong>A plot measuring 1,361 square feet.</strong> Divided by 272.25 that is 5.00 marla — as close to exactly 5 as a real measurement ever gets. On the 250 standard it would be 5.44 marla. This is the classic 5 marla plot, and the measurement confirming 1,361.25 square feet is a good sign the plot is the traditional size.</p>"
                        "<p><strong>A plot measuring 2,722.5 square feet.</strong> Exactly 10 marla traditionally, 10.89 at 250 square feet, and 12.10 at 225. If a listing calls this 10 marla and the price is set per marla, you are being sold the traditional standard.</p>"
                        "<p><strong>A plot measuring 1,200 square feet.</strong> That is 4.41 traditional marla, 4.80 at 250 and 5.33 at 225. Nothing rounds to a whole marla, which is normal for a plot that was measured rather than sold by unit. Price it on the square footage, not on the nearest marla figure.</p>"
            },
            {
                "h": "Covered area and floor area ratio",
                "body": "<p>Once you have the plot area, the next number that matters is how much you are allowed to build on it. Local byelaws set a maximum covered area and a floor area ratio (FAR) or floor space index as a multiple of plot area, and both are defined against the plot's measured area — not against its advertised marla size.</p>"
                        "<p>That is a practical reason to convert from measurement rather than from the listing. If the byelaw allows a floor area of twice the plot, the difference between 2,500 and 2,722.5 square feet of plot is 445 square feet of permitted building — a room and a half, decided by which marla standard the plot is on.</p>"
                        "<p>Use this calculator to get the measured area right, then read your authority's byelaw table against that figure. Building without checking is the expensive mistake here, because an illegal covered area can be ordered demolished.</p>"
            }
        ],
        "table": {
            "caption": "Square feet to marla — common measured areas",
            "head": ["Square feet", "Traditional (272.25)", "Modern (250)", "Older (225)", "Square metres"],
            "rows": [
                ["500 ft²", "1.84 marla", "2.00 marla", "2.22 marla", "46.45 m²"],
                ["750 ft²", "2.75 marla", "3.00 marla", "3.33 marla", "69.68 m²"],
                ["1,000 ft²", "3.67 marla", "4.00 marla", "4.44 marla", "92.90 m²"],
                ["1,250 ft²", "4.59 marla", "5.00 marla", "5.56 marla", "116.13 m²"],
                ["1,361.25 ft²", "5.00 marla", "5.45 marla", "6.05 marla", "126.46 m²"],
                ["1,800 ft²", "6.61 marla", "7.20 marla", "8.00 marla", "167.23 m²"],
                ["2,500 ft²", "9.18 marla", "10.00 marla", "11.11 marla", "232.26 m²"],
                ["2,722.50 ft²", "10.00 marla", "10.89 marla", "12.10 marla", "252.93 m²"],
                ["5,000 ft²", "18.37 marla", "20.00 marla", "22.22 marla", "464.52 m²"],
                ["5,445 ft²", "20.00 marla", "21.78 marla", "24.20 marla", "505.86 m²"]
            ]
        },
        "faqs": [
            ("How do I convert square feet to marla?",
             "Divide the area in square feet by the marla standard you are using. For the traditional standard, divide by 272.25: 2,722.5 ÷ 272.25 = 10 marla. For a modern society using 250 square feet, divide by 250: the same plot is 10.89 marla. Always establish which standard applies before you divide."),
            ("How many marla is 1,000 square feet?",
             "3.67 traditional marla, 4.00 marla at the 250 square foot standard, and 4.44 at 225. Notice that 1,000 square feet is a round 4 marla only on the 250 standard — which is exactly the sort of round number that reveals which standard a description was written against."),
            ("How many marla is 2,722.5 square feet?",
             "Exactly 10 marla on the traditional 272.25 standard. It works out to 10.89 marla at 250 square feet and 12.10 marla at 225. If you have measured 2,722.5 square feet, the plot was almost certainly sold as 10 traditional marla."),
            ("How do I know which marla standard my plot uses?",
             "Divide the square footage you have measured by the marla figure in the listing. If 2,600 square feet is described as 10 marla, the implied standard is 260 — close to the 250 used by modern societies. If it comes out at 272.25, the listing is traditional. Repeat this for any two plots you are comparing, since a mixed set of standards makes the marla figures meaningless."),
            ("What if the plot is described in kanal and marla?",
             "Add them first. One kanal is 20 marla, so “1 kanal 5 marla” is 25 marla, which at the traditional standard is 6,806.25 square feet. Converting the kanal and marla parts separately and adding the results also works, but adding them in marla first is less error-prone."),
            ("Is marla used outside Pakistan?",
             "Yes. Marla and kanal are used across northern India and in parts of Bangladesh, and the same variation in size applies — 272.25 square feet is the common North Indian figure, while 225 appears in several states and in some older schemes. The 250 square foot marla is largely a Pakistani housing society convention.")
        ],
        "related": ["marla-to-square-feet", "kanal-to-marla", "plot-area-calculator", "land-area-calculator"]
    },

    # ------------------------------------------------------------------
    {
        "slug": "kanal-to-marla",
        "calc": "kanal-to-marla",
        "category": "land",
        "icon": "🗺️",
        "h1": "Kanal to Marla",
        "title": "Kanal to Marla Converter — 1 Kanal = 20 Marla",
        "meta_description": "Convert kanal to marla, square feet, square metres and acres. One kanal is always 20 marla, so the square-foot value follows the marla standard you choose.",
        "meta_keywords": "kanal to marla, 1 kanal in marla, kanal to square feet, how many marla in 1 kanal, kanal to acre, 4 kanal in marla, kanal land measurement",
        "tagline": "Kanal to marla, square feet and acres — with the marla standard that decides the area.",
        "blurb": "The 20-marla relationship, for larger parcels priced by the kanal.",
        "intro": [
            "<p>Kanal is the unit of larger land — farm plots, blocks bought for development, and the big residential plots that are too large to describe in marla without the number getting unwieldy. Its definition is refreshingly simple: <strong>one kanal is exactly 20 marla</strong>, everywhere it is used. That part never varies.</p>",
            "<p>What does vary is how many square feet that comes to, because marla itself varies by region. On the traditional 272.25 square foot marla, a kanal is 5,445 square feet — the familiar figure, equal to 605 square yards. On the 250 square foot marla used by modern housing societies, a kanal is 5,000 square feet. Ten percent less land for the same word.</p>"
        ],
        "formula": "<p><strong>Marla = kanal × 20</strong> &nbsp;·&nbsp; <strong>Square feet = kanal × 20 × marla standard</strong></p><p>At 272.25 ft² per marla: 1 kanal = 20 marla = 5,445 ft² = 605 yd² = 0.125 acre.</p>",
        "sections": [
            {
                "h": "The relationships worth memorising",
                "body": "<p>South Asian land measurement is built on a chain of round numbers, and knowing the chain makes most conversions doable in your head:</p>"
                        "<ul>"
                        "<li><strong>1 kanal = 20 marla</strong> — fixed, in every region.</li>"
                        "<li><strong>1 marla = 272.25 ft² = 30.25 yd²</strong> — on the traditional standard. 30.25 is 5.5², which is where the odd-looking figure comes from.</li>"
                        "<li><strong>1 kanal = 5,445 ft² = 605 yd²</strong> — because 20 × 272.25 = 5,445 and 605 = 5 × 121.</li>"
                        "<li><strong>8 kanal = 1 acre</strong> — because 8 × 5,445 = 43,560, exactly an acre.</li>"
                        "<li><strong>1 acre = 160 marla</strong> — the same fact from the other direction.</li>"
                        "<li><strong>4 kanal = 0.5 acre</strong>, and <strong>2 kanal = 0.25 acre</strong> — the sizes most often traded for development.</li>"
                        "</ul>"
                        "<p>Those last few only hold on the traditional standard. Switch to a 250 square foot marla and an acre becomes 8.71 kanal rather than a tidy eight.</p>"
            },
            {
                "h": "When land is priced by the kanal",
                "body": "<p>Small residential plots are priced per marla. Larger parcels — agricultural land, development blocks, and plots of a kanal and above — are often priced per kanal or per acre, and knowing both figures is what lets you compare two listings that quote differently.</p>"
                        "<p>The calculator gives you the per-marla and per-kanal values together when you enter a rate for either, so you can put a per-marla plot and a per-kanal block on the same footing. Be careful to check which rate basis a listing uses: a price that looks like a bargain per kanal may simply be quoted on the 250 square foot standard, where a kanal is 10% smaller.</p>"
                        "<p>For anything at this scale, also check the actual measurements against the deed. Large parcels are frequently described in round kanal figures that the physical survey does not quite support, and on a multi-kanal purchase a small discrepancy is a large amount of money.</p>"
            },
            {
                "h": "Worked examples",
                "body": "<p><strong>1 kanal.</strong> 20 marla. At the traditional standard, 5,445 square feet — 605 square yards, 505.86 square metres, 0.125 acre, or one eighth of an acre.</p>"
                        "<p><strong>4 kanal.</strong> 80 marla, 21,780 square feet, half an acre, 2,023.4 square metres. A common size for a large house plot or a small development parcel.</p>"
                        "<p><strong>10 kanal.</strong> 200 marla, 54,450 square feet, 1.25 acres, 5,058.6 square metres. At this scale the acre figure is usually the more useful one, and the calculator shows it alongside.</p>"
                        "<p><strong>Half a kanal.</strong> 10 marla — the point where the two units meet and the same plot can be described either way. Half a kanal is a standard mid-size residential plot in most cities.</p>"
            },
            {
                "h": "Marla standards and larger parcels",
                "body": "<p>The marla standard matters more, not less, as the parcel gets bigger. On a single 5 marla house plot the difference between standards is about 222 square feet — annoying, but survivable. On 10 kanal it is 4,450 square feet, which is a substantial building's worth of land.</p>"
                        "<p>So for anything measured in kanal, insist on the square footage in writing. That is the figure that can be checked against a survey and against the deed, and it is the one a court would look at if a dispute arose. A kanal figure without a stated marla standard is an incomplete description.</p>"
                        "<p>Agricultural land has a further complication in some areas, where the local unit is the <em>murabba</em> (25 acres) or the <em>bigha</em> — and bigha in particular has no single definition, varying between roughly 1,600 and 2,700 square yards depending on the region. The calculator does not convert bigha for that reason: a conversion factor that is wrong by 60% is worse than no conversion at all.</p>"
            }
        ],
        "table": {
            "caption": "Kanal to marla and square feet (traditional 272.25 ft² marla)",
            "head": ["Kanal", "Marla", "Square feet", "Square metres", "Acres"],
            "rows": [
                ["0.25", "5", "1,361.25 ft²", "126.46 m²", "0.0313 ac"],
                ["0.5", "10", "2,722.50 ft²", "252.93 m²", "0.0625 ac"],
                ["1", "20", "5,445.00 ft²", "505.86 m²", "0.1250 ac"],
                ["2", "40", "10,890.00 ft²", "1,011.71 m²", "0.2500 ac"],
                ["3", "60", "16,335.00 ft²", "1,517.57 m²", "0.3750 ac"],
                ["4", "80", "21,780.00 ft²", "2,023.43 m²", "0.5000 ac"],
                ["5", "100", "27,225.00 ft²", "2,529.29 m²", "0.6250 ac"],
                ["8", "160", "43,560.00 ft²", "4,046.86 m²", "1.0000 ac"],
                ["10", "200", "54,450.00 ft²", "5,058.57 m²", "1.2500 ac"],
                ["20", "400", "108,900.00 ft²", "10,117.14 m²", "2.5000 ac"]
            ]
        },
        "faqs": [
            ("How many marla is 1 kanal?",
             "Exactly 20 marla. This is fixed in every region and under every standard, which makes it the most reliable relationship in South Asian land measurement. Two kanal is 40 marla, five kanal is 100 marla, and so on."),
            ("How many square feet is 1 kanal?",
             "5,445 square feet on the traditional 272.25 square foot marla, which is 605 square yards or about 505.9 square metres. Because a kanal is 20 marla, its square footage follows the marla standard in use: 5,000 square feet at 250 per marla and 4,500 at 225."),
            ("How many kanal are in 1 acre?",
             "Exactly 8 kanal on the traditional standard, because 8 × 5,445 = 43,560 square feet, which is one acre. That also makes an acre 160 traditional marla. On the 250 square foot marla an acre is 8.71 kanal and no longer divides evenly."),
            ("How many marla is half a kanal?",
             "10 marla. Half a kanal is a standard residential plot size in most Pakistani cities, and it is the point where the two units are used interchangeably — the same plot is advertised as either 10 marla or half kanal depending on the market."),
            ("Why is 1 kanal 5,445 square feet?",
             "Because a kanal is 20 marla and the traditional marla is 272.25 square feet: 20 × 272.25 = 5,445. The 272.25 itself is 30.25 square yards, and 30.25 is 5.5 squared. The figure looks arbitrary but it is the product of a consistent traditional system, and it is the only marla standard that makes an acre come out as exactly 160 marla."),
            ("Does the calculator handle bigha or murabba?",
             "It handles murabba indirectly — one murabba is 25 acres, so multiply your acre figure by 25. It does not convert bigha, because bigha has no single definition: it ranges from roughly 1,600 to 2,700 square yards depending on the region and the historical land revenue system. A conversion that may be wrong by 60% is worse than no conversion.")
        ],
        "related": ["marla-to-square-feet", "square-feet-to-marla", "land-area-calculator", "hectares-to-acres"]
    }
]
