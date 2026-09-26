#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Al Sadat Builders — /tools/ hub and calculator page builder.

Generates the Construction & Property Tools hub (``pages/tools/index.html``)
and one page per calculator (``pages/tools/<slug>.html``), then wires them
into the rest of the site:

  * ``_redirects``     — a 200-proxy rule per tool, so /tools/<slug> works
  * ``sitemap.xml``    — the hub and every tool URL
  * ``llms.txt``       — a calculator section for AI crawlers

Run order matters — the tool pages are rendered with the shared header and
footer from ``build_site.py``, so run that first after any chrome change:

    python3 scripts/build_site.py
    python3 scripts/build_tools.py

Every tool page is rewritten from scratch on each run, so re-running this
after a chrome change is enough to refresh the tool pages themselves; the
checked-in marketing pages are refreshed by ``build_site.py``.
"""

import json
import os
import re
import sys
from string import Template
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_site import (  # noqa: E402  (path is set up above)
    ROOT, SITE, TODAY, PAGES_SUBDIR, COMPANY, CEO, WA_NUMBER,
    esc, header_html, footer_html,
)
from data_tools import TOOL_CATEGORIES, CATEGORY_NAMES  # noqa: E402
from tools_content_area import AREA_TOOLS  # noqa: E402
from tools_content_build import BUILD_TOOLS  # noqa: E402
from tools_content_home import HOME_TOOLS  # noqa: E402
from tools_content_land import LAND_TOOLS  # noqa: E402

TOOLS_SUBDIR = "tools"
OUT_REL = PAGES_SUBDIR + "/" + TOOLS_SUBDIR          # pages/tools
OUT_DIR = os.path.join(ROOT, PAGES_SUBDIR, TOOLS_SUBDIR)

# Canonical URL for the hub. Tool URLs are SITE + "/tools/" + slug.
HUB_URL = SITE + "/tools/"
HUB_SLUG = "tools"

ALL_TOOLS = AREA_TOOLS + BUILD_TOOLS + HOME_TOOLS + LAND_TOOLS
BY_SLUG = {t["slug"]: t for t in ALL_TOOLS}


def tools_in(cat):
    """Tools of one category, in content-file order."""
    return [t for t in ALL_TOOLS if t["category"] == cat]


def url_for(slug):
    return "%s/tools/%s" % (SITE, slug)


def attr(s):
    """Escape for a double-quoted HTML attribute. esc() covers &, < and >;
    a quote is the one thing it does not, and it would end the attribute."""
    return esc(s).replace('"', "&quot;")


# ============================================================
# Page templates
# ============================================================
TOOL_PAGE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${meta_desc}">
  <meta name="keywords" content="${keywords}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${url}">
  <link rel="icon" type="image/png" href="/images/icon.png">
  <link rel="apple-touch-icon" href="/images/icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="${url}">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${meta_desc}">
  <meta property="og:image" content="${site}/images/logo.png">
  <meta property="og:site_name" content="Al Sadat Builders">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${meta_desc}">

  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/tools.css">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
${schema_app}
  </script>

  <!-- Breadcrumbs Schema -->
  <script type="application/ld+json">
${schema_breadcrumb}
  </script>

  <!-- FAQ Schema -->
  <script type="application/ld+json">
${schema_faq}
  </script>
</head>
<body>

${header}

  <!-- Tool Hero -->
  <section class="tool-hero">
    <div class="container">
      <nav class="tool-crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>/</span> <a href="/tools/">Tools</a> <span>/</span> <a href="/tools/#cat-${catkey}">${catname}</a> <span>/</span> <strong>${h1}</strong>
      </nav>
      <h1>${h1}</h1>
      <p>${tagline}</p>
    </div>
  </section>

  <!-- Calculator -->
  <section class="section">
    <div class="container calc-layout">
      <div class="calc-card">
        <h2>Enter your measurements</h2>
        <p class="calc-sub">Every result updates as you type — there is no button to press. Use <strong>Reset values</strong> to start again.</p>
        <div id="calc-form"></div>
      </div>
      <div class="calc-results">
        <h2>Results</h2>
        <div id="calc-output" aria-live="polite"></div>
      </div>
    </div>
  </section>

  <!-- How it works -->
  <section class="section bg-off-white">
    <div class="container">
      <div class="tool-content">
${intro_html}

        <div class="formula-box"><strong>The formula</strong>${formula_html}</div>
${sections_html}${table_html}
      </div>
    </div>
  </section>

  <!-- FAQ, related tools and a note about who publishes this -->
  <section class="section">
    <div class="container">
      <div class="tool-content">
        <h2>Frequently asked questions</h2>
        <div class="tool-faq">
${faq_html}
        </div>

        <h2>Related tools</h2>
        <div class="related-grid">
${related_html}
        </div>

        <div class="tool-cta">
          <h3>About the company that publishes these tools</h3>
          <p>Al Sadat Builders is a construction contractor based in Islamabad, Pakistan, led on site by <strong style="color:#fff;">${ceo}</strong>. These calculators are free to use wherever you are — they print no currency and assume no country. If you are building in Islamabad, Rawalpindi or Bani Gala, we can survey the plot, price the job and hand you an itemised BOQ.</p>
          <div class="tool-cta-btns">
            <a href="/contact" class="btn btn-primary">Book a free site visit</a>
            <a href="https://wa.me/${wa_number}?text=${wa_text}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">💬 WhatsApp us</a>
          </div>
        </div>
      </div>
    </div>
  </section>

${footer}""")


HUB_PAGE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${meta_desc}">
  <meta name="keywords" content="${keywords}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${url}">
  <link rel="icon" type="image/png" href="/images/icon.png">
  <link rel="apple-touch-icon" href="/images/icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="${url}">
  <meta property="og:title" content="${title}">
  <meta property="og:description" content="${meta_desc}">
  <meta property="og:image" content="${site}/images/logo.png">
  <meta property="og:site_name" content="Al Sadat Builders">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${title}">
  <meta name="twitter:description" content="${meta_desc}">

  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="/css/style.css">
  <link rel="stylesheet" href="/css/tools.css">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
${schema_list}
  </script>

  <!-- Breadcrumbs Schema -->
  <script type="application/ld+json">
${schema_breadcrumb}
  </script>

  <!-- FAQ Schema -->
  <script type="application/ld+json">
${schema_faq}
  </script>
</head>
<body>

${header}

  <!-- Hub Hero -->
  <section class="tool-hero">
    <div class="container">
      <nav class="tool-crumbs" aria-label="Breadcrumb">
        <a href="/">Home</a> <span>/</span> <strong>Tools</strong>
      </nav>
      <h1>Free Construction, Property &amp; Area Calculators</h1>
      <p>${tagline}</p>
    </div>
  </section>

  <!-- Intro -->
  <section class="section">
    <div class="container">
      <div class="tool-content">
${intro_html}
      </div>
    </div>
  </section>

  <!-- Category blocks -->
  <section class="section bg-off-white">
    <div class="container">
${categories_html}
    </div>
  </section>

  <!-- How these work -->
  <section class="section">
    <div class="container">
      <div class="tool-content">
${sections_html}
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section bg-off-white">
    <div class="container">
      <div class="tool-content">
        <h2>Frequently asked questions</h2>
        <div class="tool-faq">
${faq_html}
        </div>

        <div class="tool-cta">
          <h3>About the company that publishes these tools</h3>
          <p>Al Sadat Builders is a construction contractor based in Islamabad, Pakistan, led on site by <strong style="color:#fff;">${ceo}</strong>. These calculators are free to use wherever you are — they print no currency and assume no country. If you are building in Islamabad, Rawalpindi or Bani Gala, we can survey the plot, price the job and hand you an itemised BOQ.</p>
          <div class="tool-cta-btns">
            <a href="/contact" class="btn btn-primary">Book a free site visit</a>
            <a href="https://wa.me/${wa_number}?text=${wa_text}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">💬 WhatsApp us</a>
          </div>
        </div>
      </div>
    </div>
  </section>

${footer}""")


# ============================================================
# Hub copy
# ============================================================
HUB_TITLE = "Free Construction, Property & Area Calculators"
HUB_META_DESC = ("19 free construction calculators for area, land, concrete, "
                 "brick, gravel, tiles, paint, flooring, roofing and fencing. "
                 "No sign-up, no currency assumed.")
HUB_META_KEYWORDS = ("construction calculator, property calculator, area calculator, "
                     "building materials calculator, free construction tools, "
                     "land area calculator, marla calculator")

HUB_TAGLINE = ("Twenty calculators for measuring land, pricing materials and checking "
               "quantities before you order. Free, no sign-up, and written to work in "
               "any country — no currency is assumed and no price is hard-coded.")

HUB_INTRO = [
    "<p>This is a set of working calculators for the questions that come up while "
    "you are measuring a plot, planning a build or standing in a builders' yard. "
    "Each one takes the dimensions you actually have — a plot's front and back "
    "widths, a wall's height, a room's floor area — and returns the quantity you "
    "need to order, in the units you think in.</p>",

    "<p>Two things shape how they are written. The first is that <strong>these "
    "tools are not tied to one country</strong>. Every cost field is a plain unit "
    "price: you enter the price in your own currency and read the total back in "
    "the same one, and nothing on the page assumes dollars, pounds, rupees or "
    "euros. Material densities, mix ratios and wastage allowances are stated "
    "openly rather than buried, so you can substitute your own local figures "
    "where they differ.</p>",

    "<p>The second is that <strong>estimates are labelled as estimates</strong>. "
    "A calculator can tell you how much concrete fits in a footing; it cannot "
    "tell you how much your ground will absorb, or whether your engineer will "
    "specify a richer mix. Where a number depends on a supplier's packaging — "
    "the coverage on a roll of roofing underlayment, the area in a box of tiles "
    "— the tool asks you for that figure instead of inventing one. Several of "
    "the pages explain where a calculation stops being reliable, which is "
    "usually more useful than a falsely precise answer.</p>",
]

HUB_SECTIONS = [
    {
        "h": "How these calculators work",
        "body": "<p>Each calculator takes your measurements, converts them to a single "
                "base unit — feet for length, square feet for area, cubic feet for volume "
                "— and works from there. That is why the unit badge next to every input "
                "matters: entering 3 metres where the tool expects 3 feet gives an answer "
                "that is wrong by a factor of ten, and the arithmetic will not warn you.</p>"
                "<p>A waste allowance is applied to material quantities, and you control "
                "it. The default differs by material because materials differ: cutting "
                "tiles produces more offcuts than pouring concrete produces spillage. "
                "Leave it at the default if you are unsure, and raise it for a room with "
                "awkward corners, several doorways, or a diagonal layout.</p>"
    },
    {
        "h": "What a calculator can and cannot tell you",
        "body": "<p>A calculator is arithmetic. It knows nothing about your site. It "
                "cannot know that your sub-base is soft, that the ground falls away "
                "across the plot, that the merchant only sells rebar in fixed lengths, "
                "or that your local code requires a richer concrete mix than the one "
                "you picked.</p>"
                "<p>So use these figures to plan and to sanity-check a quotation, not to "
                "replace a site visit or an engineer's specification. Where a tool's "
                "result depends on a supply assumption, the page says so and the note "
                "under the results repeats it. If a number matters enough to argue "
                "about, it matters enough to check against a real measurement.</p>"
    },
    {
        "h": "Choosing the right units",
        "body": "<p>Three unit families appear across the hub, and you can switch "
                "freely between them on any input. <strong>Imperial</strong> — feet, "
                "square feet, cubic yards, cubic feet — dominates construction in the "
                "United States, the United Kingdom and much of the Commonwealth. "
                "<strong>Metric</strong> — metres, square metres, cubic metres — is the "
                "standard almost everywhere else and is what engineering drawings use. "
                "<strong>South Asian land units</strong> — marla and kanal — are how "
                "residential plots are bought and sold in Pakistan and parts of "
                "northern India, and they appear in their own section below.</p>"
                "<p>Mix units within one calculation if that matches reality. Surveying "
                "a plot in feet while ordering concrete in cubic metres is ordinary, and "
                "the calculators handle it: each input carries its own unit selector, and "
                "the results come back in every unit that matters for that quantity.</p>"
    },
    {
        "h": "Why marla and kanal ask you to choose a standard",
        "body": "<p>An acre is always 43,560 square feet and a hectare is always 10,000 "
                "square metres — those are fixed by definition. A <strong>marla</strong> "
                "is not. The traditional revenue standard is 272.25 square feet, many "
                "modern housing societies sell on 250 square feet, and several regions "
                "and older schemes use 225.</p>"
                "<p>The difference is not academic. A plot advertised at 10 marla is "
                "2,722.5 square feet on one standard and 2,250 on another — more than "
                "20% of the land, for the same three words. So every tool here that "
                "touches marla asks which standard applies, and <strong>kanal follows "
                "from your answer</strong>, because a kanal is always 20 marla. That "
                "single rule is applied across the whole hub, which means no two "
                "calculators on this site can give you a different answer for the "
                "same plot.</p>"
    },
]

HUB_FAQS = [
    ("Are these calculators free?",
     "Yes, all of them, with no sign-up, no email address and no limit on how many "
     "times you use them. There is nothing to download and nothing to install."),
    ("How accurate are the results?",
     "The arithmetic is accurate; the inputs and the assumptions are where the "
     "uncertainty lives. Conversions between defined units — feet to metres, acres "
     "to hectares — are exact to the digits shown. Material quantities are "
     "estimates built on stated assumptions: a waste allowance you control, and "
     "standard densities, mix ratios and coverage rates that you can see on the "
     "page. Always order against a real measurement rather than an advertised one "
     "where you can."),
    ("Can I use these tools outside Pakistan?",
     "Yes — that is what they are written for. No cost field has a currency symbol, "
     "so you enter a price in your own currency and read the total in the same one. "
     "Metric and imperial units sit side by side on every input. The marla and "
     "kanal tools are the only ones tied to a particular part of the world, and "
     "they are grouped in their own section for that reason."),
    ("Why do the marla and kanal tools ask me to pick a marla size?",
     "Because marla has no single definition. The traditional standard is 272.25 "
     "square feet, many housing societies use 250, and some regions and older "
     "schemes use 225. The gap between the largest and smallest is over 20% of the "
     "plot area, so a converter that quietly picked one would be unreliable for "
     "everyone else. Choose the standard your seller or your society uses."),
    ("Do the results replace a professional estimate?",
     "No, and they are not meant to. They are for planning, for comparing quotes "
     "and for checking that a quantity someone has given you is plausible. A "
     "contractor's or engineer's estimate accounts for your site, your ground "
     "conditions and your local building code, none of which a web page can see."),
    ("Why is no price shown for materials?",
     "Because material prices differ hugely between countries, between cities and "
     "between months, and a hard-coded price would be wrong almost everywhere. "
     "Every tool that reports a cost takes a unit price you type in, so the total "
     "comes back in your own currency and stays correct as prices move."),
]


# ============================================================
# Rendering helpers
# ============================================================
def intro_html(t):
    return "\n".join('        %s' % p for p in t["intro"])


def sections_html(t):
    out = []
    for s in t["sections"]:
        out.append('        <h2>%s</h2>\n        %s' % (esc(s["h"]), s["body"]))
    return "\n\n".join(out) + "\n"


def table_html(t):
    tbl = t.get("table")
    if not tbl:
        return ""
    head = "".join("<th>%s</th>" % esc(h) for h in tbl["head"])
    rows = []
    for row in tbl["rows"]:
        cells = []
        for i, c in enumerate(row):
            cells.append("<td><strong>%s</strong></td>" % esc(c) if i == 0
                         else "<td>%s</td>" % esc(c))
        rows.append("          <tr>%s</tr>" % "".join(cells))
    return (
        '\n        <div class="table-scroll">\n'
        '          <table class="data-table">\n'
        '            <caption>%s</caption>\n'
        '            <thead><tr>%s</tr></thead>\n'
        '            <tbody>\n%s\n            </tbody>\n'
        '          </table>\n'
        '        </div>\n' % (esc(tbl["caption"]), head, "\n".join(rows))
    )


def faq_html(faqs, indent="          "):
    out = []
    for q, a in faqs:
        out.append(
            '%s<details>\n'
            '%s  <summary>%s</summary>\n'
            '%s  <div class="faq-body">%s</div>\n'
            '%s</details>' % (indent, indent, esc(q), indent, esc(a), indent)
        )
    return "\n".join(out)


def related_html(t):
    out = []
    for slug in t["related"]:
        other = BY_SLUG.get(slug)
        if not other:
            continue
        out.append(
            '          <a class="related-link" href="/tools/%s">\n'
            '            <span class="rl-icon">%s</span>\n'
            '            <span class="rl-text">%s</span>\n'
            '          </a>' % (slug, other["icon"], esc(other["h1"]))
        )
    return "\n".join(out)


def tool_card(t):
    return (
        '        <a class="tool-card" href="/tools/%s">\n'
        '          <span class="tc-badge">%s</span>\n'
        '          <span class="tc-icon">%s</span>\n'
        '          <h3>%s</h3>\n'
        '          <p>%s</p>\n'
        '        </a>' % (t["slug"], CATEGORY_NAMES[t["category"]],
                        t["icon"], esc(t["h1"]), esc(t["blurb"]))
    )


def categories_html():
    blocks = []
    for key, name, icon, desc in TOOL_CATEGORIES:
        cards = "\n".join(tool_card(t) for t in tools_in(key))
        blocks.append(
            '      <div class="tool-cat-block">\n'
            '        <div class="tool-cat-head" id="cat-%s">\n'
            '          <h2>%s %s</h2>\n'
            '        </div>\n'
            '        <p class="tool-cat-desc">%s</p>\n'
            '        <div class="tools-grid">\n%s\n        </div>\n'
            '      </div>' % (key, icon, name, desc, cards)
        )
    return "\n\n".join(blocks)


# ============================================================
# JSON-LD
# ============================================================
def schema_webapp(t):
    data = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": t["h1"],
        "url": url_for(t["slug"]),
        "description": t["meta_description"],
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "Any",
        "browserRequirements": "Requires JavaScript",
        "isAccessibleForFree": True,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "publisher": {"@type": "Organization", "name": COMPANY,
                      "url": SITE + "/", "founder": {"@type": "Person", "name": CEO}},
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_breadcrumb(t):
    cat = t["category"]
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Construction & Property Tools",
             "item": HUB_URL},
            {"@type": "ListItem", "position": 3,
             "name": CATEGORY_NAMES[cat].replace("&amp;", "&"),
             "item": "%s#cat-%s" % (HUB_URL, cat)},
            {"@type": "ListItem", "position": 4, "name": t["h1"], "item": url_for(t["slug"])},
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_faq(faqs):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in faqs
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_hub_list():
    data = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": HUB_TITLE,
        "url": HUB_URL,
        "numberOfItems": len(ALL_TOOLS),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": t["h1"],
             "url": url_for(t["slug"])}
            for i, t in enumerate(ALL_TOOLS)
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_hub_breadcrumb():
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Construction & Property Tools",
             "item": HUB_URL},
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


# ============================================================
# Render
# ============================================================
def wa_text_for(label):
    return quote("Hello Al Sadat Builders, I was using the %s on your website "
                 "and would like to discuss a construction project." % label,
                 safe="")


def tool_footer(tool_id):
    """The shared footer, with the calculator engine loaded just before
    </body>. tools.js renders every control inside #calc-form and every result
    inside #calc-output, so the page carries no field markup of its own — which
    is why a tool page works the moment its id exists in the registry."""
    scripts = (
        '\n  <!-- Calculator engine — builds the form and the results panel -->\n'
        '  <script src="/js/tools.js"></script>\n'
        "  <script>AlsadatTools.init('%s');</script>\n" % tool_id
    )
    return footer_html().replace("</body>", scripts + "</body>", 1)


def render_tool(t):
    cat = t["category"]
    return TOOL_PAGE.substitute(
        title=attr(t["title"]),
        meta_desc=attr(t["meta_description"]),
        keywords=attr(t["meta_keywords"]),
        url=url_for(t["slug"]),
        site=SITE,
        h1=esc(t["h1"]),
        tagline=esc(t["tagline"]),
        catkey=cat,
        catname=CATEGORY_NAMES[cat],
        intro_html=intro_html(t),
        formula_html=t["formula"],
        sections_html=sections_html(t),
        table_html=table_html(t),
        faq_html=faq_html(t["faqs"]),
        related_html=related_html(t),
        schema_app=schema_webapp(t),
        schema_breadcrumb=schema_breadcrumb(t),
        schema_faq=schema_faq(t["faqs"]),
        header=header_html(t["slug"]),
        footer=tool_footer(t["calc"]),
        ceo=CEO,
        wa_number=WA_NUMBER,
        wa_text=wa_text_for(t["h1"]),
    )


def render_hub():
    return HUB_PAGE.substitute(
        title=attr(HUB_TITLE),
        meta_desc=attr(HUB_META_DESC),
        keywords=attr(HUB_META_KEYWORDS),
        url=HUB_URL,
        site=SITE,
        tagline=esc(HUB_TAGLINE),
        intro_html="\n".join('        %s' % p for p in HUB_INTRO),
        categories_html=categories_html(),
        sections_html=sections_html({"sections": HUB_SECTIONS}),
        faq_html=faq_html(HUB_FAQS),
        schema_list=schema_hub_list(),
        schema_breadcrumb=schema_hub_breadcrumb(),
        schema_faq=schema_faq(HUB_FAQS),
        header=header_html(HUB_SLUG),
        footer=footer_html(),
        ceo=CEO,
        wa_number=WA_NUMBER,
        wa_text=wa_text_for("free construction calculators"),
    )


# ============================================================
# Site wiring
# ============================================================
def tool_urls():
    """(url_path, source_path) for the hub and every tool page."""
    out = [("/tools/", "/pages/tools/"), ("/tools", "/pages/tools/")]
    for t in ALL_TOOLS:
        out.append(("/tools/%s" % t["slug"], "/pages/tools/%s" % t["slug"]))
    return out


def patch_redirects():
    """Insert a 200-proxy rule for the hub and every tool.

    The existing rules are re-sorted rather than appended, and the file's own
    header and trailing comment blocks are preserved verbatim — including the
    warning against a blanket /* splat, which would break every static asset.
    """
    path = os.path.join(ROOT, "_redirects")
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    rule_idx = [i for i, ln in enumerate(lines) if ln.startswith("/")]
    if not rule_idx:
        print("  ! _redirects has no rules — skipped")
        return 0
    first, last = rule_idx[0], rule_idx[-1]
    head, tail = lines[:first], lines[last + 1:]

    existing = {}
    for ln in lines[first:last + 1]:
        if not ln.startswith("/"):
            continue
        parts = ln.split()
        if len(parts) >= 2:
            existing[parts[0]] = ln

    added = 0
    for source, dest in tool_urls():
        if source not in existing:
            added += 1
        existing[source] = "%s  %s  200" % (source, dest)

    rules = [existing[k] for k in sorted(existing)]
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(head + rules + tail))
    return added


def patch_sitemap():
    """Add the hub and every tool URL to sitemap.xml, replacing any tool
    entries already there so re-runs do not duplicate them."""
    path = os.path.join(ROOT, "sitemap.xml")
    with open(path, encoding="utf-8") as fh:
        xml = fh.read()

    # Drop previously generated tool entries, leaving the rest of the file
    # byte-identical.
    xml = re.sub(r"[ \t]*<url>\s*<loc>%s/tools[^<]*</loc>.*?</url>\n" % re.escape(SITE),
                 "", xml, flags=re.S)

    # Sorted by slug so this list is byte-identical to the one build_site.py
    # produces by reading pages/tools/ off disk — otherwise every run of one
    # builder would reshuffle the other's output for no reason.
    entries = [("tools/", "0.8", "weekly")]
    for t in sorted(ALL_TOOLS, key=lambda x: x["slug"]):
        entries.append(("tools/%s" % t["slug"], "0.7", "monthly"))

    body = "\n".join(
        '  <url>\n'
        '    <loc>%s/%s</loc>\n'
        '    <lastmod>%s</lastmod>\n'
        '    <changefreq>%s</changefreq>\n'
        '    <priority>%s</priority>\n'
        '  </url>' % (SITE, loc, TODAY, freq, p)
        for loc, p, freq in entries
    )
    xml = xml.replace("</urlset>", body + "\n</urlset>")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(xml)
    return len(entries)


def update_llms():
    """Add a calculators section to llms.txt, just above the deep-links list.

    It is inserted before '## Pages & Deep Links' on purpose: build_site.py
    rewrites that section from its own template, so anything placed after it
    would be wiped the next time the site builder runs.
    """
    path = os.path.join(ROOT, "llms.txt")
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()

    lines = ["## Free Construction & Property Calculators", "",
             "A hub of %d free calculators at %s — no sign-up, no currency assumed, "
             "usable in any country." % (len(ALL_TOOLS), HUB_URL), ""]
    for key, name, _icon, desc in TOOL_CATEGORIES:
        lines.append("### %s" % name.replace("&amp;", "&"))
        for t in tools_in(key):
            lines.append("- %s: %s — %s" % (
                t["h1"],
                "%s/tools/%s" % (SITE, t["slug"]),
                " ".join(t["blurb"].split())))
        lines.append("")
    block = "\n".join(lines)

    # Rebuild the section from scratch each run: take everything before the
    # deep-links heading, drop any tools section already sitting there, then
    # re-emit it with exactly two newlines on either side. Stripping and
    # re-inserting around a fixed marker (rather than a regex replace) is what
    # keeps repeated runs from accumulating blank lines.
    marker = "## Pages & Deep Links"
    head, sep, tail = txt.partition(marker)
    if not sep:
        return False
    head = re.sub(r"## Free Construction & Property Calculators.*?(?=\n*$)", "",
                  head, count=1, flags=re.S).rstrip("\n")

    txt = head + "\n\n" + block.rstrip("\n") + "\n\n" + sep + tail
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(txt)
    return True


# ============================================================
# Main
# ============================================================
def main():
    print("Al Sadat Builders — tools build\n")

    os.makedirs(OUT_DIR, exist_ok=True)

    print("Generating tool pages:")
    for t in ALL_TOOLS:
        out = os.path.join(OUT_DIR, t["slug"] + ".html")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render_tool(t))
        print("  + %-56s %6.1f KB" % ("%s/%s.html" % (OUT_REL, t["slug"]),
                                      os.path.getsize(out) / 1024))

    hub = os.path.join(OUT_DIR, "index.html")
    with open(hub, "w", encoding="utf-8") as fh:
        fh.write(render_hub())
    print("  + %-56s %6.1f KB" % (OUT_REL + "/index.html", os.path.getsize(hub) / 1024))

    n = patch_redirects()
    print("\n_redirects updated — %d new rule(s)" % n)

    n = patch_sitemap()
    print("sitemap.xml updated — %d tool URL(s)" % n)

    if update_llms():
        print("llms.txt updated")

    print("\nDone. %d tool pages + 1 hub." % len(ALL_TOOLS))


if __name__ == "__main__":
    main()
