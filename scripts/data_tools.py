# -*- coding: utf-8 -*-
"""The tool categories that make up the /tools/ hub.

Imported by both ``build_site.py`` (which only needs the keys and names, to
render the "Tools" navigation dropdown) and ``build_tools.py`` (which builds
the hub page from them). It lives in its own module so neither builder has to
import the other and create a cycle.

Order here is the order on the hub page and in the navigation dropdown.
"""

TOOL_CATEGORIES = [
    ("area", "Area &amp; Land", "🏞️",
     "Convert between square feet, square metres, acres, hectares and the "
     "South Asian land units, or measure an area from its dimensions."),

    ("materials", "Construction Materials", "🧱",
     "Work out how much concrete, brick, sand, aggregate or gravel a job "
     "needs before you order it."),

    ("flooring", "Flooring &amp; Walls", "🎨",
     "Tiles, paint and flooring — the finishing materials where an "
     "over-order is money left in the garage and an under-order is a second "
     "delivery."),

    ("roofing", "Roofing", "🏠",
     "Roof area, pitch, squares, shingle bundles and ridge length for gable, "
     "hip, shed and flat roofs."),

    ("outdoor", "Outdoor &amp; Landscaping", "🌳",
     "Fencing, posts, pickets and boundary-works quantities for the outside "
     "of the property."),

    ("land", "Pakistan Land Units", "🗺️",
     "Marla and kanal conversions for buyers, sellers and anyone reading a "
     "title deed. Every tool lets you choose which marla standard applies."),
]

CATEGORY_NAMES = {key: name for key, name, _icon, _desc in TOOL_CATEGORIES}
CATEGORY_ICONS = {key: icon for key, _name, icon, _desc in TOOL_CATEGORIES}
