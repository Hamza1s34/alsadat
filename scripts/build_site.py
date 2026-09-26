#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Al Sadat Builders — static site builder.

Generates dedicated area / sector / overseas landing pages, and patches the
shared navigation, footer and homepage area chips across the existing pages.

Run from the project root:
    python3 scripts/build_site.py
    python3 scripts/build_tools.py

The second command rebuilds the /tools/ pages, which are rendered with the
header and footer this file owns. Any change to the navigation here needs
both, in that order, to reach the tool pages.
"""

import json
import os
import re
import sys
from string import Template

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data_societies import SOCIETIES
from data_sectors import SECTORS
from data_tools import TOOL_CATEGORIES

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://alsadatbuilders.com"
TODAY = "2026-09-22"

# Every page except index.html lives in a "pages/" subfolder. Page links stay
# root-absolute (/pages/contact) so they work from either depth; assets in the
# shared chrome are root-absolute for the same reason, while the area-page
# <head> uses "../" because it is only ever emitted inside pages/.
PAGES_SUBDIR = "pages"

COMPANY = "Al Sadat Builders"
CEO = "Syed Mujtaba Shah"
PHONE_DISPLAY = "0335-5549384"
PHONE_TEL = "0335549384"
WA_NUMBER = "923469607349"
WA_DISPLAY = "0346-9607349"
EMAIL = "info@alsadatbuilders.com"

ALL_AREAS = SOCIETIES + SECTORS
BY_SLUG = {a["slug"]: a for a in ALL_AREAS}

SOCIETY_AREAS = [a for a in SOCIETIES if a["group"] == "society"]
OVERSEAS = [a for a in SOCIETIES if a["group"] == "special"][0]

# ------------------------------------------------------------
# Services (internal linking targets)
# ------------------------------------------------------------
SERVICES = [
    ("construction-company-islamabad", "🏗️", "Construction Company Islamabad",
     "Turnkey residential and commercial construction, managed end to end by the founder."),
    ("house-construction-islamabad", "🏡", "House Construction",
     "Complete 5 Marla to 1 Kanal house construction, from foundation to key handover."),
    ("grey-structure-islamabad", "🧱", "Grey Structure",
     "Grade 60 steel, branded cement and supervised concrete pours for the structural shell."),
    ("house-renovation-islamabad", "🔨", "Renovation &amp; Remodeling",
     "Kitchen and bathroom remodelling, extensions, and full interior modernisation."),
    ("marble-tile-fixing-islamabad", "✨", "Marble &amp; Tile Fixing",
     "Precision marble and large-format porcelain installation for floors, stairs and walls."),
    ("boundary-wall-construction-islamabad", "🧱", "Boundary Wall Construction",
     "Reinforced boundary walls, retaining structures and gate piers built on proper footings."),
    ("plaster-work-islamabad", "🛡️", "Plaster Work &amp; Waterproofing",
     "Internal and external plaster, basement tanking and roof waterproofing systems."),
]

EXISTING_PAGES = [
    ("", "1.0", "weekly", "Al Sadat Builders | Construction Company in Islamabad"),
    ("construction-company-islamabad", "0.9", "weekly", ""),
    ("house-construction-islamabad", "0.9", "weekly", ""),
    ("grey-structure-islamabad", "0.9", "weekly", ""),
    ("house-renovation-islamabad", "0.8", "weekly", ""),
    ("construction-cost-islamabad", "0.8", "weekly", ""),
    ("marble-tile-fixing-islamabad", "0.8", "weekly", ""),
    ("boundary-wall-construction-islamabad", "0.8", "weekly", ""),
    ("plaster-work-islamabad", "0.8", "weekly", ""),
    ("projects", "0.7", "monthly", ""),
    ("contact", "0.6", "monthly", ""),
]

ALL_HTML_PAGES = [
    "index.html",
    "construction-company-islamabad.html",
    "house-construction-islamabad.html",
    "grey-structure-islamabad.html",
    "house-renovation-islamabad.html",
    "construction-cost-islamabad.html",
    "marble-tile-fixing-islamabad.html",
    "boundary-wall-construction-islamabad.html",
    "plaster-work-islamabad.html",
    "projects.html",
    "contact.html",
]


# ============================================================
# Shared chrome
# ============================================================
def nav_areas_dropdown(active_slug):
    """Desktop 'Areas We Serve' dropdown."""
    items = []
    for a in SOCIETY_AREAS + [OVERSEAS]:
        cls = ' class="active"' if a["slug"] == active_slug else ""
        items.append('            <a href="/pages/%s"%s>%s</a>' % (a["slug"], cls, a["short"]))
    if active_slug in BY_SLUG and BY_SLUG[active_slug]["group"] == "sector":
        items.append('            <a href="/pages/construction-company-cda-sectors-islamabad">CDA Sectors (F, G, E, I)</a>')
    else:
        items.append('            <a href="/pages/construction-company-cda-sectors-islamabad">CDA Sectors (F, G, E, I)</a>')
    return (
        '        <div class="nav-item">\n'
        '          <a href="/pages/construction-company-cda-sectors-islamabad">Areas ▾</a>\n'
        '          <div class="dropdown">\n'
        + "\n".join(items) + "\n"
        '          </div>\n'
        '        </div>'
    )


def mobile_nav_links(active_slug):
    lines = [
        ('/', '🏠 Home', ''),
        ('/tools/', '🧮 Free Construction Tools', ''),
        ('/construction-company-islamabad', '🏗️ Construction Company Islamabad', ''),
        ('/house-construction-islamabad', '🏡 House Construction', ''),
        ('/grey-structure-islamabad', '🧱 Grey Structure', ''),
        ('/house-renovation-islamabad', '🔨 Renovation &amp; Remodeling', ''),
        ('/marble-tile-fixing-islamabad', '✨ Marble &amp; Tile Fixing', ''),
        ('/boundary-wall-construction-islamabad', '🧱 Boundary Wall Construction', ''),
        ('/plaster-work-islamabad', '🛡️ Plaster Work &amp; Waterproofing', ''),
        ('/construction-cost-islamabad', '📊 Construction Cost Guide', ''),
        ('/projects', '📸 Projects &amp; Portfolio', ''),
        ('/construction-company-cda-sectors-islamabad', '📍 Areas We Serve', ''),
    ]
    out = []
    for href, label, _ in lines:
        cls = ' class="active"' if href.lstrip('/') == active_slug else ""
        # /tools/ is a canonical URL in its own right, not a proxied page slug,
        # so it is linked as-is rather than through page_link().
        target = href if href.startswith('/tools/') else page_link(href.lstrip('/'))
        out.append('      <a href="%s"%s>%s</a>' % (target, cls, label))
    out.append('      <div class="mobile-nav-sub">Calculators</div>')
    for key, name, _icon, _desc in TOOL_CATEGORIES:
        out.append('      <a href="/tools/#cat-%s" class="mobile-nav-sub-link">%s</a>' % (key, name))
    out.append('      <div class="mobile-nav-sub">Popular Areas</div>')
    for a in SOCIETY_AREAS + [OVERSEAS]:
        cls = ' class="active"' if a["slug"] == active_slug else ""
        out.append('      <a href="/pages/%s" class="mobile-nav-sub-link"%s>%s %s</a>'
                   % (a["slug"], cls, a["icon"], a["short"]))
    out.append('      <div class="mobile-nav-sub">CDA Sectors</div>')
    for a in SECTORS:
        cls = ' class="active"' if a["slug"] == active_slug else ""
        out.append('      <a href="/pages/%s" class="mobile-nav-sub-link"%s>Sector %s</a>'
                   % (a["slug"], cls, a["name"]))
    out.append('      <a href="/pages/contact">📍 Contact &amp; Free Estimate</a>')
    return "\n".join(out)


def nav_tools_dropdown():
    """Desktop 'Tools' dropdown — the six calculator categories on /tools/."""
    items = ['            <a href="/tools/">All Free Tools</a>']
    for key, name, icon, _desc in TOOL_CATEGORIES:
        items.append('            <a href="/tools/#cat-%s">%s %s</a>' % (key, icon, name))
    return (
        '        <div class="nav-item">\n'
        '          <a href="/tools/">Tools ▾</a>\n'
        '          <div class="dropdown">\n'
        + "\n".join(items) + "\n"
        '          </div>\n'
        '        </div>'
    )


def page_link(slug):
    """Root-absolute URL for a page. index.html is the homepage ('/'); every
    other page lives under PAGES_SUBDIR."""
    return "/" if not slug else "/%s/%s" % (PAGES_SUBDIR, slug)


def footer_area_links():
    links = [(page_link(a["slug"]), a["short"]) for a in SOCIETY_AREAS + [OVERSEAS]]
    links += [
        (page_link("construction-company-f-7-islamabad"), "F-7 Islamabad"),
        (page_link("construction-company-f-8-islamabad"), "F-8 Islamabad"),
        (page_link("construction-company-g-6-islamabad"), "G-6 Islamabad"),
    ]
    return "\n".join('          <li><a href="%s">%s</a></li>' % (h, t) for h, t in links)


CONTACT_VARS = dict(
    CEO=CEO,
    PHONE_TEL=PHONE_TEL,
    PHONE_DISPLAY=PHONE_DISPLAY,
    WA_NUMBER=WA_NUMBER,
    WA_DISPLAY=WA_DISPLAY,
    EMAIL=EMAIL,
)


def header_html(active_slug=""):
    return Template(HEADER_TMPL).substitute(
        NAV_AREAS=nav_areas_dropdown(active_slug),
        NAV_TOOLS=nav_tools_dropdown(),
        MOBILE_LINKS=mobile_nav_links(active_slug),
        **CONTACT_VARS
    )


def footer_html():
    return Template(FOOTER_TMPL).substitute(
        FOOTER_AREAS=footer_area_links(),
        **CONTACT_VARS
    )


def top_bar():
    return TOP_BAR


HEADER_TMPL = """  <!-- Top Bar -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div class="top-bar-links">
        <a href="tel:${PHONE_TEL}">📞 Call: ${PHONE_DISPLAY}</a>
        <a href="https://wa.me/${WA_NUMBER}" target="_blank" rel="noopener noreferrer">💬 WhatsApp: ${WA_DISPLAY}</a>
        <a href="mailto:${EMAIL}">✉️ ${EMAIL}</a>
      </div>
      <div class="top-bar-right">
        <span>📍 Islamabad, Rawalpindi, Bani Gala &amp; All Major Societies</span>
        <span>⏱️ Mon - Sat: 8:00 AM - 8:00 PM</span>
      </div>
    </div>
  </div>

  <!-- Header -->
  <header class="header">
    <div class="header-inner">
      <a href="/" class="logo" aria-label="Al Sadat Builders Home">
        <img src="/images/icon.png" alt="Al Sadat Builders Icon" class="logo-icon-img">
        <div class="logo-text">
          <strong>AL SADAT BUILDERS</strong>
          <span>30+ Years Construction Excellence</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav" aria-label="Primary Navigation">
        <a href="/">Home</a>
        <div class="nav-item">
          <a href="/pages/construction-company-islamabad">Services ▾</a>
          <div class="dropdown">
            <a href="/pages/construction-company-islamabad">Construction in Islamabad</a>
            <a href="/pages/house-construction-islamabad">House Construction</a>
            <a href="/pages/grey-structure-islamabad">Grey Structure</a>
            <a href="/pages/house-renovation-islamabad">Renovation &amp; Repairs</a>
            <a href="/pages/marble-tile-fixing-islamabad">Marble &amp; Tile Fixing</a>
            <a href="/pages/boundary-wall-construction-islamabad">Boundary Wall Construction</a>
            <a href="/pages/plaster-work-islamabad">Plaster Work &amp; Waterproofing</a>
          </div>
        </div>
${NAV_AREAS}
${NAV_TOOLS}
        <a href="/pages/construction-cost-islamabad">Construction Cost</a>
        <a href="/pages/projects">Projects</a>
        <a href="/pages/contact">Contact Us</a>
      </nav>

      <!-- Header CTAs -->
      <div class="header-cta">
        <a href="tel:${PHONE_TEL}" class="btn btn-dark" style="padding: 10px 18px; font-size: 0.88rem;">📞 Call Now</a>
        <a href="https://wa.me/${WA_NUMBER}?text=Hello%20Al%20Sadat%20Builders%2C%20I%20would%20like%20a%20free%20site%20visit%20and%20estimate." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp" style="padding: 10px 18px; font-size: 0.88rem;">💬 WhatsApp</a>
      </div>

      <!-- Hamburger -->
      <button class="hamburger" aria-label="Toggle mobile menu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </header>

  <!-- Mobile Nav Overlay -->
  <div class="mobile-nav">
    <div class="mobile-nav-header">
      <div class="logo">
        <img src="/images/icon.png" alt="Al Sadat Builders" class="logo-icon-img">
        <div class="logo-text">
          <strong>AL SADAT BUILDERS</strong>
          <span>Islamabad, Rawalpindi &amp; Bani Gala</span>
        </div>
      </div>
      <button class="mobile-nav-close" aria-label="Close menu">&times;</button>
    </div>
    <div class="mobile-nav-links">
${MOBILE_LINKS}
    </div>
    <div class="mobile-nav-ctas">
      <a href="tel:${PHONE_TEL}" class="btn btn-primary">📞 Call ${PHONE_DISPLAY}</a>
      <a href="https://wa.me/${WA_NUMBER}" class="btn btn-whatsapp" target="_blank" rel="noopener noreferrer">💬 Chat on WhatsApp</a>
    </div>
  </div>"""


TOP_BAR = ""


FOOTER_TMPL = """  <!-- Footer -->
  <footer class="footer">
    <div class="container footer-top">
      <div class="footer-brand">
        <div class="logo">
          <img src="/images/icon.png" alt="Al Sadat Builders" class="logo-icon-img">
          <div class="logo-text">
            <strong>AL SADAT BUILDERS</strong>
            <span>30+ Years Construction Experience</span>
          </div>
        </div>
        <p>
          Construction company in Islamabad, Rawalpindi &amp; Bani Gala. Founded and led by <strong>${CEO}</strong>. Turnkey residential villas, grey structures, renovation and finishing across CDA sectors, DHA, Bahria Town, Gulberg Greens and B-17.
        </p>
        <div class="footer-social">
          <a href="https://wa.me/${WA_NUMBER}" aria-label="WhatsApp" target="_blank" rel="noopener noreferrer">💬</a>
          <a href="tel:${PHONE_TEL}" aria-label="Call Us">📞</a>
          <a href="mailto:${EMAIL}" aria-label="Email Us">✉️</a>
        </div>
      </div>

      <div class="footer-col">
        <h4>Services</h4>
        <ul>
          <li><a href="/pages/construction-company-islamabad">Construction in Islamabad</a></li>
          <li><a href="/pages/house-construction-islamabad">Turnkey House Construction</a></li>
          <li><a href="/pages/grey-structure-islamabad">Grey Structure Construction</a></li>
          <li><a href="/pages/house-renovation-islamabad">Renovation &amp; Remodeling</a></li>
          <li><a href="/pages/marble-tile-fixing-islamabad">Marble &amp; Tile Fixing</a></li>
          <li><a href="/pages/boundary-wall-construction-islamabad">Boundary Wall Construction</a></li>
          <li><a href="/pages/plaster-work-islamabad">Plaster Work &amp; Waterproofing</a></li>
        </ul>
      </div>

      <div class="footer-col">
        <h4>Areas We Serve</h4>
        <ul>
${FOOTER_AREAS}
        </ul>
      </div>

      <div class="footer-col">
        <h4>Contact &amp; Hours</h4>
        <ul>
          <li><strong>CEO:</strong> ${CEO}</li>
          <li><a href="tel:${PHONE_TEL}">📞 ${PHONE_DISPLAY}</a></li>
          <li><a href="https://wa.me/${WA_NUMBER}" target="_blank" rel="noopener noreferrer">💬 WhatsApp: ${WA_DISPLAY}</a></li>
          <li><a href="mailto:${EMAIL}">✉️ ${EMAIL}</a></li>
          <li>📍 Islamabad, Rawalpindi &amp; Bani Gala</li>
          <li>⏱️ Mon - Sat: 8:00 AM - 8:00 PM</li>
        </ul>
      </div>
    </div>

    <div class="container footer-bottom">
      <p>&copy; 2026 Al Sadat Builders. All rights reserved. Construction Company in Islamabad.</p>
      <div class="footer-bottom-links">
        <a href="/">Home</a>
        <a href="/pages/construction-cost-islamabad">Cost Guide</a>
        <a href="/pages/projects">Projects</a>
        <a href="/pages/contact">Contact</a>
        <a href="/sitemap.xml">Sitemap</a>
      </div>
    </div>
  </footer>

  <!-- Floating WhatsApp -->
  <a href="https://wa.me/${WA_NUMBER}?text=Hello%20Al%20Sadat%20Builders%2C%20I%20would%20like%20to%20discuss%20a%20construction%20project." class="float-whatsapp" target="_blank" rel="noopener noreferrer" aria-label="Chat on WhatsApp">
    <span class="tooltip">Chat with ${CEO}</span>
    💬
  </a>

  <!-- JavaScript -->
  <script src="/js/main.js"></script>
</body>
</html>"""


# ============================================================
# Area page template
# ============================================================
AREA_PAGE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title}</title>
  <meta name="description" content="${meta_desc}">
  <meta name="keywords" content="${keywords}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <link rel="canonical" href="${site}/${slug}">
  <link rel="icon" type="image/png" href="../images/icon.png">
  <link rel="apple-touch-icon" href="../images/icon.png">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="${site}/${slug}">
  <meta property="og:title" content="${og_title}">
  <meta property="og:description" content="${meta_desc}">
  <meta property="og:image" content="${site}/images/logo.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="${og_title}">
  <meta name="twitter:description" content="${meta_desc}">

  <!-- Google Fonts: Inter -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

  <link rel="stylesheet" href="../css/style.css">

  <!-- Schema.org JSON-LD -->
  <script type="application/ld+json">
${schema_contractor}
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

  <!-- Page Hero -->
  <section class="page-hero">
    <div class="container">
      <div class="breadcrumb">
        <a href="/">Home</a> <span>/</span> <a href="/pages/construction-company-islamabad">Construction Company Islamabad</a> <span>/</span> <strong>${name}</strong>
      </div>
      <h1>${h1}</h1>
      <p>${hero_sub}</p>
    </div>
  </section>

  <!-- Overview -->
  <section class="section">
    <div class="container why-inner">
      <div class="why-content animate-on-scroll">
        <span class="badge">${badge}</span>
        <h2>${lead_h2}</h2>
${intro_html}

        <div class="info-box">
          ${highlight}
        </div>

        <div class="hero-btns" style="margin-top: 24px;">
          <a href="/pages/contact" class="btn btn-primary">Book Free Site Visit</a>
          <a href="https://wa.me/${wa_number}?text=${wa_text}" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp">💬 WhatsApp Consultation</a>
        </div>
      </div>

      <div class="why-stats animate-on-scroll">
        <div style="border-radius: var(--radius); overflow: hidden; margin-bottom: 18px; border: 2px solid rgba(245,197,24,0.4);">
          <img src="${img}" alt="${img_alt}" style="width: 100%; height: 180px; object-fit: cover; display: block;" loading="lazy">
        </div>
        <div class="why-stats-title">WHY ${upper_name} CLIENTS CHOOSE US</div>
        <div class="big-stats">
${stats_html}
        </div>
        <p style="color: rgba(255,255,255,0.7); font-size: 0.9rem; text-align: center; margin: 0;">
          Direct supervision by ${ceo} on every site.
        </p>
      </div>
    </div>
  </section>

  <!-- Area-specific engineering -->
  <section class="section bg-off-white">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Local Conditions</span>
        <h2>${challenges_h2}</h2>
        <div class="section-line"></div>
        <p>${challenges_sub}</p>
      </div>

      <div class="services-grid">
${challenges_html}
      </div>
    </div>
  </section>

  <!-- Services offered here -->
  <section class="section">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Our Services in ${name}</span>
        <h2>Construction Services We Provide in ${name}</h2>
        <div class="section-line"></div>
        <p>Every stage of your project handled by one team, under one contract and one itemised BOQ.</p>
      </div>

      <div class="services-grid">
${services_html}
      </div>
    </div>
  </section>

  <!-- Plot types -->
  <section class="section bg-off-white">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Project Types</span>
        <h2>${plots_h2}</h2>
        <div class="section-line"></div>
        <p>${plots_sub}</p>
      </div>

      <div class="services-grid">
${plots_html}
      </div>
    </div>
  </section>

  <!-- Approvals + lead form -->
  <section class="section" id="approvals">
    <div class="container why-inner">
      <div class="why-content animate-on-scroll">
        <span class="badge">Approvals &amp; Compliance</span>
        <h2>${bylaws_h2}</h2>
        <p>${bylaws_sub}</p>
        <ul class="service-list" style="margin-bottom: 24px;">
${bylaws_html}
        </ul>
        <a href="/pages/contact" class="btn btn-dark">Ask About Approvals in ${name}</a>
      </div>

      <div class="contact-form-card animate-on-scroll">
        <h3>Get a Free Estimate for ${name}</h3>
        <p style="font-size: 0.9rem; color: var(--gray); margin-bottom: 18px;">
          Send us your plot details and we will prepare an itemised BOQ for ${name} with no obligation.
        </p>
        <form data-lead-form>
          <div class="form-group">
            <label for="${slug}-name">Your Name *</label>
            <input type="text" id="${slug}-name" name="name" placeholder="Name" required>
          </div>
          <div class="form-group">
            <label for="${slug}-phone">Phone / WhatsApp *</label>
            <input type="tel" id="${slug}-phone" name="phone" placeholder="0335-5549384" required>
          </div>
          <div class="form-group">
            <label for="${slug}-location">Plot Location</label>
            <input type="text" id="${slug}-location" name="location" value="${name}" >
          </div>
          <div class="form-group">
            <label for="${slug}-size">Plot Size</label>
            <select id="${slug}-size" name="plot_size">
              <option value="5 Marla">5 Marla</option>
              <option value="7 Marla">7 Marla</option>
              <option value="8 Marla">8 Marla</option>
              <option value="10 Marla">10 Marla</option>
              <option value="1 Kanal" selected>1 Kanal</option>
              <option value="2 Kanal or larger">2 Kanal or larger</option>
            </select>
          </div>
          <div class="form-group">
            <label for="${slug}-service">Service Required</label>
            <select id="${slug}-service" name="service">
              <option value="Complete Turnkey Construction">Complete Turnkey Construction</option>
              <option value="Grey Structure">Grey Structure Only</option>
              <option value="House Renovation">Renovation &amp; Remodeling</option>
              <option value="Second Storey Addition">Second Storey Addition</option>
              <option value="Marble &amp; Tile Fixing">Marble &amp; Tile Fixing</option>
              <option value="Boundary Wall">Boundary Wall Construction</option>
              <option value="Plaster &amp; Waterproofing">Plaster &amp; Waterproofing</option>
            </select>
          </div>
          <button type="submit" class="btn btn-primary" style="width: 100%;">Request Free Estimate</button>
          <div class="success-msg"></div>
        </form>
      </div>
    </div>
  </section>

  <!-- FAQ -->
  <section class="section bg-off-white" id="faq">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Frequently Asked Questions</span>
        <h2>Construction Questions About ${name}</h2>
        <div class="section-line"></div>
      </div>

      <div style="max-width: 800px; margin: 0 auto; display: flex; flex-direction: column; gap: 20px;">
${faq_html}
      </div>
    </div>
  </section>

  <!-- Internal linking: nearby + all areas + services -->
  <section class="section" id="areas">
    <div class="container">
      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Areas We Serve</span>
        <h2>Other Areas We Build In Near ${name}</h2>
        <div class="section-line"></div>
      </div>

      <div class="services-grid" style="margin-bottom: 40px;">
${nearby_html}
      </div>

      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Full Coverage</span>
        <h2>All Areas &amp; CDA Sectors We Cover</h2>
        <div class="section-line"></div>
        <p>Select your sector or society for area-specific guidance on bylaws, terrain and typical plot sizes.</p>
      </div>

      <div class="areas-grid animate-on-scroll" style="margin-bottom: 40px;">
${all_areas_html}
      </div>

      <div class="section-header text-center animate-on-scroll">
        <span class="badge">Popular Services</span>
        <h2>Construction Services in ${name}</h2>
        <div class="section-line"></div>
      </div>

      <div class="areas-grid animate-on-scroll">
${all_services_html}
      </div>
    </div>
  </section>

  <!-- CTA Band -->
  <section class="cta-band">
    <div class="container cta-band-inner">
      <div>
        <h2>${cta_h2}</h2>
        <p>${cta_p}</p>
      </div>
      <div class="cta-band-btns">
        <a href="tel:${phone_tel}" class="btn btn-dark btn-lg">📞 ${phone_display}</a>
        <a href="https://wa.me/${wa_number}?text=${wa_text}" class="btn btn-whatsapp btn-lg" target="_blank" rel="noopener noreferrer">💬 Chat on WhatsApp</a>
      </div>
    </div>
  </section>

${footer}""")


# ============================================================
# Page assembly
# ============================================================
def esc(s):
    """Escape a data string for HTML output.

    Escapes &, < and > but leaves pre-existing entities (e.g. &amp;) intact,
    because the SERVICES list already carries escaped ampersands.
    """
    s = re.sub(r"&(?!(?:amp|lt|gt|quot|apos|nbsp|#\d+|#x[0-9a-fA-F]+);)", "&amp;", s)
    return s.replace("<", "&lt;").replace(">", "&gt;")


def build_intro(area):
    return "\n".join('        <p>\n          %s\n        </p>' % esc(p) for p in area["intro"])


def build_stats(area):
    out = []
    for num, label in area["stats"]:
        out.append(
            '          <div class="big-stat">\n'
            '            <span class="num">%s</span>\n'
            '            <span class="label">%s</span>\n'
            '          </div>' % (esc(num), esc(label))
        )
    return "\n".join(out)


def build_challenges(area):
    out = []
    for icon, title, desc in area["challenges"]:
        out.append(
            '        <div class="service-card animate-on-scroll">\n'
            '          <div class="service-icon">%s</div>\n'
            '          <h3>%s</h3>\n'
            '          <p>%s</p>\n'
            '        </div>' % (icon, esc(title), esc(desc))
        )
    return "\n".join(out)


def build_services(area):
    n = esc(area["name"])
    out = []
    for slug, icon, title, desc in SERVICES:
        out.append(
            '        <a class="service-card animate-on-scroll" href="/pages/%s" style="display:block; text-decoration:none; color:inherit;">\n'
            '          <div class="service-icon">%s</div>\n'
            '          <h3>%s</h3>\n'
            '          <p>%s Available across %s, with site supervision by %s.</p>\n'
            '          <span class="service-link">Learn more →</span>\n'
            '        </a>' % (slug, icon, title, esc(desc), n, CEO)
        )
    return "\n".join(out)


def build_plots(area):
    out = []
    for title, desc in area["plots"]:
        out.append(
            '        <div class="service-card animate-on-scroll">\n'
            '          <h3>%s</h3>\n'
            '          <p>%s</p>\n'
            '        </div>' % (esc(title), esc(desc))
        )
    return "\n".join(out)


def build_bylaws(area):
    return "\n".join('          <li>%s</li>' % esc(b) for b in area["bylaws"])


def build_faqs(area):
    out = []
    for q, a in area["faqs"]:
        out.append(
            '        <div class="testimonial-card animate-on-scroll">\n'
            '          <h4 style="margin-bottom: 8px; color: var(--black);">%s</h4>\n'
            '          <p style="font-size: 0.92rem; color: var(--gray-dark); margin: 0;">\n'
            '            %s\n'
            '          </p>\n'
            '        </div>' % (esc(q), esc(a))
        )
    return "\n".join(out)


def build_nearby(area):
    out = []
    for slug in area["nearby"]:
        other = BY_SLUG.get(slug)
        if not other:
            continue
        out.append(
            '        <a class="service-card animate-on-scroll" href="/pages/%s" style="display:block; text-decoration:none; color:inherit;">\n'
            '          <div class="service-icon">%s</div>\n'
            '          <h3>Construction Company in %s</h3>\n'
            '          <p>%s</p>\n'
            '          <span class="service-link">View %s →</span>\n'
            '        </a>' % (slug, other["icon"], esc(other["name"]), esc(other["hero_sub"]), esc(other["short"]))
        )
    return "\n".join(out)


def build_all_areas(area):
    out = []
    for a in ALL_AREAS:
        cur = ' style="border-color: var(--yellow); font-weight: 700;"' if a["slug"] == area["slug"] else ""
        out.append('        <a class="area-chip" href="/pages/%s"%s>%s %s</a>'
                   % (a["slug"], cur, a["icon"], esc(a["short"])))
    return "\n".join(out)


def build_all_services(area):
    return "\n".join(
        '        <a class="area-chip" href="/pages/%s">%s %s</a>' % (slug, icon, esc(title))
        for slug, icon, title, _ in SERVICES
    )


def schema_contractor(area):
    data = {
        "@context": "https://schema.org",
        "@type": "GeneralContractor",
        "name": "%s — Construction Company in %s" % (COMPANY, area["name"]),
        "url": "%s/%s" % (SITE, area["slug"]),
        "image": "%s/%s" % (SITE, area["img"]),
        "telephone": "+92-335-5549384",
        "email": EMAIL,
        "priceRange": "PKR 2,800 - 9,500 per sq ft",
        "founder": {"@type": "Person", "name": CEO},
        "description": area["meta_desc"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Islamabad",
            "addressRegion": "Islamabad Capital Territory",
            "addressCountry": "PK",
        },
        "areaServed": [{"@type": "Place", "name": "%s, Islamabad" % area["name"]}]
        + [{"@type": "Place", "name": BY_SLUG[s]["name"]} for s in area["nearby"] if s in BY_SLUG],
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
            "opens": "08:00",
            "closes": "20:00",
        },
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_breadcrumb(area):
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Construction Company Islamabad",
             "item": SITE + "/construction-company-islamabad"},
            {"@type": "ListItem", "position": 3, "name": area["name"],
             "item": "%s/%s" % (SITE, area["slug"])},
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def schema_faq(area):
    data = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in area["faqs"]
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def render_area_page(area):
    from urllib.parse import quote
    wa_text = quote(area["wa_text"], safe="")
    return AREA_PAGE.substitute(
        title=esc(area["title"]),
        meta_desc=esc(area["meta_desc"]),
        keywords=esc(area["keywords"]),
        og_title=esc(area["og_title"]),
        site=SITE,
        slug=area["slug"],
        name=esc(area["name"]),
        short=esc(area["short"]),
        h1=esc(area["h1"]),
        hero_sub=esc(area["hero_sub"]),
        badge=esc(area["badge"]),
        upper_name=esc(area["name"].upper()),
        lead_h2=esc(area["lead_h2"]),
        highlight=esc(area["highlight"]),
        intro_html=build_intro(area),
        stats_html=build_stats(area),
        challenges_h2=esc(area["challenges_h2"]),
        challenges_sub=esc(area["challenges_sub"]),
        challenges_html=build_challenges(area),
        services_html=build_services(area),
        plots_h2=esc(area["plots_h2"]),
        plots_sub=esc(area["plots_sub"]),
        plots_html=build_plots(area),
        bylaws_h2=esc(area["bylaws_h2"]),
        bylaws_sub=esc(area["bylaws_sub"]),
        bylaws_html=build_bylaws(area),
        faq_html=build_faqs(area),
        nearby_html=build_nearby(area),
        all_areas_html=build_all_areas(area),
        all_services_html=build_all_services(area),
        cta_h2=esc(area["cta_h2"]),
        cta_p=esc(area["cta_p"]),
        wa_text=wa_text,
        wa_number=WA_NUMBER,
        phone_tel=PHONE_TEL,
        phone_display=PHONE_DISPLAY,
        ceo=CEO,
        img="../" + area["img"],
        img_alt=esc(area["img_alt"]),
        schema_contractor=schema_contractor(area),
        schema_breadcrumb=schema_breadcrumb(area),
        schema_faq=schema_faq(area),
        header=header_html(area["slug"]),
        footer=footer_html(),
    )


# ============================================================
# Patch existing pages
# ============================================================
AREAS_NAV_BLOCK = (
    '        <div class="nav-item">\n'
    '          <a href="/pages/construction-company-cda-sectors-islamabad">Areas ▾</a>\n'
    '          <div class="dropdown">\n'
    '            <a href="/pages/construction-company-bani-gala">Bani Gala</a>\n'
    '            <a href="/pages/construction-company-dha-islamabad">DHA Islamabad</a>\n'
    '            <a href="/pages/construction-company-bahria-town-islamabad">Bahria Town &amp; Enclave</a>\n'
    '            <a href="/pages/construction-company-gulberg-greens-islamabad">Gulberg Greens</a>\n'
    '            <a href="/pages/construction-company-b-17-multi-gardens-islamabad">B-17 Multi Gardens</a>\n'
    '            <a href="/pages/construction-company-cda-sectors-islamabad">CDA Sectors (F, G, E, I)</a>\n'
    '            <a href="/pages/construction-company-overseas-pakistanis">Overseas Pakistanis</a>\n'
    '          </div>\n'
    '        </div>\n'
)


def patch_existing_pages():
    changed = []
    for fname in ALL_HTML_PAGES:
        # index.html stays at the site root; everything else lives in pages/.
        path = (os.path.join(ROOT, fname) if fname == "index.html"
                else os.path.join(ROOT, PAGES_SUBDIR, fname))
        if not os.path.exists(path):
            print("  ! missing, skipped: %s" % fname)
            continue
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        orig = html

        # 1. Desktop nav — insert Areas dropdown before the Construction Cost link
        if 'href="/pages/construction-company-cda-sectors-islamabad">Areas' not in html:
            html, n = re.subn(
                r'([ \t]*)<a href="/pages/construction-cost-islamabad"[^>]*>Construction Cost</a>',
                lambda m: AREAS_NAV_BLOCK.rstrip("\n") + "\n" + m.group(0),
                html,
                count=1,
            )
            if n == 0:
                print("  ! nav anchor not found in %s" % fname)

        # 1b. Desktop nav — insert the Tools dropdown directly after Areas
        if 'href="/tools/">Tools' not in html:
            html, n = re.subn(
                r'([ \t]*)<a href="/pages/construction-cost-islamabad"[^>]*>Construction Cost</a>',
                lambda m: nav_tools_dropdown() + "\n" + m.group(0),
                html,
                count=1,
            )
            if n == 0:
                print("  ! tools nav anchor not found in %s" % fname)

        # 2. Mobile nav — rebuild the link list
        html = re.sub(
            r'(<div class="mobile-nav-links">)(.*?)(\n    </div>\s*\n\s*<div class="mobile-nav-ctas">)',
            lambda m: m.group(1) + "\n" + mobile_nav_links(_active_slug_for(fname)) + m.group(3),
            html,
            count=1,
            flags=re.S,
        )

        # 3. Footer "Key Locations" column -> "Areas We Serve" with real links
        html = re.sub(
            r'<h4>Key Locations</h4>\s*<ul>.*?</ul>',
            '<h4>Areas We Serve</h4>\n        <ul>\n' + footer_area_links() + '\n        </ul>',
            html,
            count=1,
            flags=re.S,
        )

        # 4. Homepage area chips -> real links (line-based: the grid block is a
        #    single-line-per-chip div, so a regex would mis-match the closing tags)
        if fname == "index.html":
            lines = html.split("\n")
            start = next((i for i, ln in enumerate(lines)
                          if ln.strip() == '<div class="areas-grid animate-on-scroll">'), None)
            if start is not None:
                end = next((j for j in range(start + 1, len(lines))
                            if lines[j] == "      </div>"), None)
                if end is not None:
                    lines[start:end + 1] = _homepage_areas_grid().split("\n")
                    html = "\n".join(lines)
                else:
                    print("  ! areas-grid close not found in %s" % fname)
            else:
                print("  ! areas-grid not found in %s" % fname)

        if html != orig:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(html)
            changed.append(fname)
    return changed


def _active_slug_for(fname):
    base = fname.replace(".html", "")
    if base == "index":
        return ""
    if base == "projects":
        return "projects"
    return base


CHIP_MAP = [
    ("⭐ Bani Gala Islamabad", "/construction-company-bani-gala"),
    ("DHA Islamabad (Phases 1-6)", "/construction-company-dha-islamabad"),
    ("Bahria Town Rawalpindi (Phases 1-8)", "/construction-company-bahria-town-islamabad"),
    ("Bahria Enclave Islamabad", "/construction-company-bahria-town-islamabad"),
    ("Gulberg Greens &amp; Residencia", "/construction-company-gulberg-greens-islamabad"),
    ("B-17 Multi Gardens", "/construction-company-b-17-multi-gardens-islamabad"),
    ("Sector E-11 Islamabad", "/construction-company-e-11-islamabad"),
    ("Sector F-6 Islamabad", "/construction-company-f-6-islamabad"),
    ("Sector F-7 Islamabad", "/construction-company-f-7-islamabad"),
    ("Sector F-8 Islamabad", "/construction-company-f-8-islamabad"),
    ("Sector F-10 &amp; F-11", "/construction-company-f-10-islamabad"),
    ("Sector G-6 Islamabad", "/construction-company-g-6-islamabad"),
    ("Sector G-9 Islamabad", "/construction-company-g-9-islamabad"),
    ("Sector G-10 Islamabad", "/construction-company-g-10-islamabad"),
    ("Sector G-11 Islamabad", "/construction-company-g-11-islamabad"),
    ("Park View City Islamabad", "/contact"),
    ("Park Enclave CDA", "/contact"),
    ("Sector G-13 &amp; G-14", "/construction-company-cda-sectors-islamabad"),
    ("Sector G-15 &amp; Jammu &amp; Kashmir", "/construction-company-cda-sectors-islamabad"),
    ("Sector I-8 &amp; I-9", "/construction-company-cda-sectors-islamabad"),
    ("Sector D-12 &amp; E-7", "/construction-company-cda-sectors-islamabad"),
    ("Adyala Road Rawalpindi", "/contact"),
    ("Rawat &amp; Chaklala Scheme 3", "/contact"),
    ("Top City &amp; Mumtaz City", "/contact"),
]


def _homepage_areas_grid():
    lines = ['<div class="areas-grid animate-on-scroll">']
    for label, href in CHIP_MAP:
        star = ' style="border-color: var(--yellow); font-weight: 700;"' if label.startswith("⭐") else ""
        lines.append('        <a class="area-chip" href="%s"%s>%s</a>'
                     % (page_link(href.lstrip('/')), star, label))
    lines.append('      </div>')
    return "\n".join(lines)


# ============================================================
# Sitemap
# ============================================================
def write_sitemap():
    entries = []
    for slug, prio, freq, _ in EXISTING_PAGES:
        loc = "%s/%s" % (SITE, slug) if slug else SITE + "/"
        entries.append((loc, prio, freq))

    for a in SOCIETY_AREAS:
        entries.append(("%s/%s" % (SITE, a["slug"]), "0.9", "weekly"))
    entries.append(("%s/%s" % (SITE, OVERSEAS["slug"]), "0.8", "monthly"))
    for a in SECTORS:
        entries.append(("%s/%s" % (SITE, a["slug"]), "0.8", "monthly"))

    # The /tools/ hub and its calculator pages, taken from what build_tools.py
    # has actually written to pages/tools/. Reading the directory rather than
    # a hand-kept list means this builder cannot drop the tool URLs when it
    # runs after the tools builder — which it will, on any later chrome change.
    tools_dir = os.path.join(ROOT, PAGES_SUBDIR, "tools")
    if os.path.isdir(tools_dir):
        if os.path.exists(os.path.join(tools_dir, "index.html")):
            entries.append(("%s/tools/" % SITE, "0.8", "weekly"))
        for fn in sorted(os.listdir(tools_dir)):
            if fn.endswith(".html") and fn != "index.html":
                entries.append(("%s/tools/%s" % (SITE, fn[:-5]), "0.7", "monthly"))

    body = "\n".join(
        "  <url>\n"
        "    <loc>%s</loc>\n"
        "    <lastmod>%s</lastmod>\n"
        "    <changefreq>%s</changefreq>\n"
        "    <priority>%s</priority>\n"
        "  </url>" % (loc, TODAY, freq, prio)
        for loc, prio, freq in entries
    )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + body + "\n</urlset>\n")
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(xml)
    return len(entries)


# ============================================================
# llms.txt
# ============================================================
def update_llms():
    path = os.path.join(ROOT, "llms.txt")
    if not os.path.exists(path):
        return False
    with open(path, encoding="utf-8") as fh:
        txt = fh.read()

    area_lines = ["## Areas, Sectors &amp; Societies We Serve".replace("&amp;", "&"), ""]
    area_lines.append("### Housing Societies")
    for a in SOCIETY_AREAS:
        area_lines.append("- %s: %s/%s — %s" % (a["name"], SITE, a["slug"], a["hero_sub"]))
    area_lines.append("")
    area_lines.append("### CDA Sectors")
    area_lines.append("- CDA Sectors Hub: %s/%s — overview and sector index" % (SITE, SOCIETY_AREAS[-1]["slug"]))
    for a in SECTORS:
        area_lines.append("- Sector %s Islamabad: %s/%s — %s" % (a["name"], SITE, a["slug"], a["hero_sub"]))
    area_lines.append("")
    area_lines.append("### Overseas Pakistanis")
    area_lines.append("- %s: %s/%s — %s" % (OVERSEAS["name"], SITE, OVERSEAS["slug"], OVERSEAS["hero_sub"]))
    block = "\n".join(area_lines) + "\n"

    marker = "## Pages & Deep Links"
    if marker in txt:
        txt = re.sub(
            r"## Service Coverage \(Societies & Sectors\).*?(?=\n## )",
            "## Service Coverage (Societies & Sectors)\n\n"
            "Islamabad Capital Territory, Rawalpindi and Bani Gala. Dedicated area pages exist for:\n\n"
            + block.split("## Areas, Sectors & Societies We Serve\n\n", 1)[1]
            + "\n",
            txt,
            count=1,
            flags=re.S,
        )
    else:
        txt = txt.replace(marker, block + "\n" + marker, 1)

    # Rebuild the deep-links list with the new pages appended
    deep = ["## Pages & Deep Links", "",
            "- Homepage: %s/" % SITE,
            "- Construction Company Islamabad: %s/construction-company-islamabad" % SITE,
            "- Turnkey House Construction: %s/house-construction-islamabad" % SITE,
            "- Grey Structure Construction: %s/grey-structure-islamabad" % SITE,
            "- House Renovation & Repairs: %s/house-renovation-islamabad" % SITE,
            "- Marble & Tile Fixing Islamabad: %s/marble-tile-fixing-islamabad" % SITE,
            "- Boundary Wall Construction Islamabad: %s/boundary-wall-construction-islamabad" % SITE,
            "- Plaster Work & Waterproofing Islamabad: %s/plaster-work-islamabad" % SITE,
            "- Construction Cost & BOQ Guide 2026: %s/construction-cost-islamabad" % SITE,
            "- Projects & Portfolio: %s/projects" % SITE,
            "- Contact & Free Estimate: %s/contact" % SITE,
            ""]
    for a in SOCIETY_AREAS + [OVERSEAS] + SECTORS:
        deep.append("- Construction Company in %s: %s/%s" % (a["name"], SITE, a["slug"]))
    deep.append("- Sitemap: %s/sitemap.xml" % SITE)
    deep.append("")
    deep_block = "\n".join(deep)

    txt = re.sub(r"## Pages & Deep Links.*?(?=\Z)", deep_block, txt, count=1, flags=re.S)

    with open(path, "w", encoding="utf-8") as fh:
        fh.write(txt)
    return True


# ============================================================
# Main
# ============================================================
def main():
    print("Al Sadat Builders — site build\n")

    print("Generating area pages:")
    out_dir = os.path.join(ROOT, PAGES_SUBDIR)
    os.makedirs(out_dir, exist_ok=True)
    for a in ALL_AREAS:
        out = os.path.join(out_dir, a["slug"] + ".html")
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(render_area_page(a))
        print("  + %-52s %6.1f KB" % (PAGES_SUBDIR + "/" + a["slug"] + ".html",
                                      os.path.getsize(out) / 1024))

    print("\nPatching existing pages:")
    changed = patch_existing_pages()
    for f in changed:
        print("  ~ %s" % f)

    n = write_sitemap()
    print("\nsitemap.xml written — %d URLs" % n)

    if update_llms():
        print("llms.txt updated")

    print("\nDone. %d area pages + %d patched existing pages." % (len(ALL_AREAS), len(changed)))


if __name__ == "__main__":
    main()
