"""Tool copy grounded in the Search Console export reviewed on 2026-10-03.

Keep high-performing converters stable. Give weaker pages a direct answer,
the actual units requested, and examples with stated assumptions.
"""

UPDATES = {
    'square-meters-to-square-feet': {
        'h1': 'Square Meters to Square Feet Converter (m² to ft²)',
        'title': 'Square Meters to Square Feet Calculator (m² to ft²)',
        'meta_description': 'Convert square meters to square feet: 1 m² = approximately 10.7639 ft². Free m2 to ft2 calculator, plus 100, 150 and 200 m² examples and a conversion table.',
        'quick_answer': '<strong>1 square meter ≈ 10.7639 square feet.</strong> Divide m² by 0.09290304 to get ft². For example, 150 m² ≈ 1,614.59 ft² and 200 m² ≈ 2,152.78 ft².',
        'section': ('Does “square meters to feet” mean feet or square feet?', '<p>Square meters measure area, so the matching result is <strong>square feet (ft²)</strong>. Feet measure length. A 1 m² square has sides of about 3.28084 feet, but its area is about 10.7639 ft². You cannot turn an area into a single length without specifying a shape and another dimension.</p><p>For floor plans, use this m² to ft² converter. For the reverse direction, use <a href="/tools/square-feet-to-square-meters">square feet to square meters</a>. The international foot is exactly 0.3048 meters; see <a href="https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors">NIST’s unit definitions</a>.</p>'),
        'faq': ('How many square feet are 150 and 200 square meters?', '150 square meters is approximately 1,614.59 square feet; 200 square meters is approximately 2,152.78 square feet. Divide the square-meter value by 0.09290304, then round the final result.'),
    },
    'paint-calculator': {
        'h1': 'Paint Calculator: How Much Paint for a Room or House?',
        'title': 'Paint Calculator: How Much Paint for a Room or House?',
        'meta_description': 'Calculate paint for a wall, room or house in litres and US gallons. Enter wall area, coats and product coverage; include ceilings or deduct doors and windows.',
        'tagline': 'Estimate litres, US gallons and cans from the area you will paint, the number of coats and your product’s coverage.',
        'quick_answer': '<strong>Paint in litres = paintable area in m² × coats ÷ coverage in m²/L.</strong> A 12 × 12 ft room with 9 ft walls, one door and two windows needs about 7.08 L for two coats at 10 m²/L, excluding its ceiling.',
        'section': ('How much paint do I need for a whole house?', '<p>Add the paintable wall areas of the rooms you will paint. Include ceiling areas only when they are part of the job, and separate surfaces that need a different product or number of coats. Enter the total with <strong>I already know the wall area</strong>. A house’s floor area is not its wall area.</p><p>For example, 200 m² of paintable walls at 10 m² per litre needs 40 litres for two coats. At 8 m² per litre, the same area needs 50 litres. Select <strong>Custom product coverage</strong> to enter the figure on your paint tin. This follows <a href="https://www.dulux.com.pk/en/decorating-tips-and-advice/how-much-paint-do-you-need">Dulux Pakistan’s paint calculation method</a>; surface condition and the chosen product affect the estimate.</p>'),
        'faq': ('How much paint do I need for one wall?', 'Multiply the wall width by its height, deduct openings, then multiply by the number of coats and divide by the product’s coverage per litre. A 4 m wide, 2.5 m high wall has an area of 10 m². At 10 m²/L, two coats need 2 litres before any allowance for the surface.'),
    },
    'gravel-calculator': {
        'h1': 'Gravel Calculator: Volume, Weight & Bulk Density',
        'title': 'Gravel Calculator: Cubic Yards, Tonnes & Density',
        'meta_description': 'Estimate gravel in cubic yards, cubic meters, tonnes and bags. Enter area, depth and bulk density in t/m³; convert kg/m³ and add a waste allowance.',
        'quick_answer': '<strong>Gravel volume = area × depth; weight = volume × bulk density.</strong> The default 1.68 t/m³ equals 1,680 kg/m³. Use your supplier’s bulk density when available.',
        'section': ('Gravel density in kg/m³ and tonnes per cubic meter', '<p>This calculator uses <strong>bulk density</strong>, including air spaces between stones. Its gravel preset is 1.68 t/m³, or 1,680 kg/m³; this is an estimate, not a fixed property of every gravel product. Divide a supplier’s kg/m³ figure by 1,000 before entering it as <strong>Custom density</strong>. For example, 1,600 kg/m³ becomes 1.6 t/m³.</p><p>A 10 m² area at 50 mm depth needs 0.5 m³ before allowance. At 1.68 t/m³, that is 0.84 tonnes. Adding 10% gives 0.55 m³ and 0.924 tonnes. The volume and weight results include the same allowance. Use the <a href="/tools/plot-area-calculator">plot area calculator</a> first for an irregular site.</p>'),
        'faq': ('What gravel density should I enter in kg/m3?', 'Use the supplier’s bulk density for the gravel being delivered. The calculator’s default 1.68 tonnes per cubic meter is 1,680 kg/m³. If the supplier quotes 1,600 kg/m³, select Custom density and enter 1.6 t/m³. Moisture, size and compaction can change the weight.'),
    },
    'square-feet-to-marla': {
        'h1': 'Square Feet to Marla Calculator (Sq Ft to Marla)',
        'title': 'Square Feet to Marla Calculator: 225, 250 & 272.25',
        'meta_description': 'Convert square feet to marla by dividing by 225, 250 or 272.25. Compare 1,000, 1,200 and 9,000 sq ft examples using your plot’s stated marla standard.',
        'quick_answer': '<strong>Marla = square feet ÷ square feet per marla.</strong> 1,200 sq ft is 4.80 marla at 250 sq ft, approximately 4.41 at 272.25, or 5.33 at 225. Choose the standard used for your plot.',
        'section': ('1,000, 1,200 and 9,000 square feet in marla', '<p>At 250 sq ft per marla, 1,000 sq ft = 4 marla, 1,200 sq ft = 4.8 marla and 9,000 sq ft = 36 marla. At 272.25 sq ft per marla, the same areas are approximately 3.67, 4.41 and 33.06 marla. The measured area stays the same; the chosen local unit changes.</p><p>Use the standard stated in the plot documents or by the housing society. If your measurement is in m², first use <a href="/tools/square-meters-to-square-feet">square meters to square feet</a>, or enter the metric area in the <a href="/tools/land-area-calculator">land area calculator</a>. For the reverse conversion, use <a href="/tools/marla-to-square-feet">marla to square feet</a>.</p>'),
        'faq': ('How many marla is 9000 square feet?', '9,000 square feet is 36 marla at 250 square feet per marla, approximately 33.06 marla at 272.25, or 40 marla at 225. Select the standard used in the plot documents before comparing the result with a listing.'),
    },
    'kanal-to-marla': {
        'quick_answer': '<strong>1 kanal = 20 marla; 0.5 kanal = 10 marla; 2 kanal = 40 marla.</strong> Multiply kanal by 20. The square-foot result depends on the selected marla standard.',
        'section': ('How to convert kanal into marla and back', '<p>Multiply kanal by 20 to get marla. Divide marla by 20 to get kanal: 5 marla = 0.25 kanal, 10 marla = 0.5 kanal and 40 marla = 2 kanal. At 250 sq ft per marla, one kanal is 5,000 sq ft; at 272.25, it is 5,445 sq ft.</p><p>Use <a href="/tools/marla-to-square-feet">marla to square feet</a> for a plot quoted in marla, or <a href="/tools/square-feet-to-marla">square feet to marla</a> for a measured area. Both use the same standard selector.</p>'),
        'faq': ('One kanal is equal to how many marla?', 'One kanal equals 20 marla. Its square-foot area follows the marla standard: 5,445 sq ft at 272.25 sq ft per marla, 5,000 at 250, or 4,500 at 225.'),
    },
    'concrete-calculator': {
        'h1': 'Concrete Calculator: How Much Concrete Do I Need?',
        'title': 'Concrete Calculator: Volume, Cubic Yards & Cement Bags',
        'meta_description': 'Calculate concrete volume from length, width and thickness in feet or meters. Estimate cubic yards, m³ and cement bags using your selected mix and allowance.',
        'quick_answer': '<strong>Concrete volume = length × width × thickness.</strong> A 10 × 10 ft slab, 4 inches thick, needs approximately 1.23 yd³ or 0.944 m³ before an allowance. Convert inches to feet before multiplying.',
        'section': ('How much concrete do I need for a slab?', '<p>For a rectangular slab, multiply all three dimensions in the same unit. A 10 × 10 ft slab at 4 inches thick is 10 × 10 × (4 ÷ 12) = 33.33 ft³. Divide by 27 for approximately 1.23 cubic yards, or multiply by 0.028316846592 for approximately 0.944 m³. A 5% allowance raises the order estimate to approximately 0.991 m³.</p><p>Calculate separate slabs, beams or footings separately and add their volumes. Cement and aggregate figures depend on the mix inputs; use the project’s specified mix rather than treating a quantity calculator as a mix design. <a href="https://aciuniversity.concrete.org/Listing/Taking-the-Myth-and-Mystery-out-of-Mix-Design-1779">ACI explains why mixes depend on actual materials and tested performance</a>. For a local project, compare the scope with our <a href="/grey-structure-islamabad">grey structure construction service</a>.</p>'),
        'faq': ('How much concrete is needed for 100 square feet?', 'At 4 inches thick, 100 square feet needs approximately 0.944 cubic meters or 1.23 cubic yards, before allowance. At 6 inches thick, it needs approximately 1.416 cubic meters or 1.85 cubic yards. Floor area alone is not enough; thickness changes the volume.'),
    },
    'flooring-calculator': {
        'h1': 'Flooring Calculator: Area, Boxes & Waste Allowance',
        'title': 'Flooring Calculator: How Many Boxes Do I Need?',
        'meta_description': 'Calculate flooring area and boxes for laminate, vinyl or wood. Enter coverage per box, add cutting allowance and estimate material cost in your currency.',
        'quick_answer': '<strong>Boxes = round up(area × allowance factor ÷ coverage per box).</strong> A 180 sq ft room with 10% allowance and 24 sq ft per box needs 9 boxes.',
        'section': ('How many boxes of flooring do I need?', '<p>A 15 × 12 ft room has 180 sq ft of floor area. Add 10% for cutting to get 198 sq ft. If the product box covers 24 sq ft, divide 198 by 24 to get 8.25, then round up to 9 boxes. Use the coverage printed on your box; pack sizes differ.</p><p>Keep room area and box coverage in matching units. Use <a href="/tools/square-feet-to-square-meters">ft² to m²</a> when the packaging is metric. For ceramic tiles instead of planks, use the <a href="/tools/tile-calculator">tile calculator</a>.</p>'),
        'faq': ('How many boxes of flooring cover a 15 by 12 foot room?', 'The room covers 180 square feet. With a 10% cutting allowance, allow 198 square feet. At 24 square feet per box, buy 9 boxes, because 198 ÷ 24 = 8.25 and boxes must be rounded up. Substitute your product’s actual box coverage.'),
    },
    'tile-calculator': {
        'title': 'Tile Calculator: How Much Tile Do I Need?',
        'quick_answer': '<strong>Tiles = round up(area × allowance factor ÷ area per tile).</strong> For 120 sq ft with 10% allowance, 2 × 2 ft tiles cover 4 sq ft each: 132 ÷ 4 = 33 tiles.',
        'section': ('How much tile do I need for floors and walls?', '<p>Calculate each floor or wall area, then use the tile’s actual dimensions or the coverage per box. A 120 sq ft floor with 10% cutting allowance needs 132 sq ft of tile coverage. With 2 × 2 ft tiles, that is 33 tiles before rounding up to full boxes.</p><p>Bathrooms may need separate floor and wall products. Estimate those surfaces separately, and confirm the cutting allowance for the chosen layout. For local installation, see our <a href="/marble-tile-fixing-islamabad">tile fixing and marble installation service in Islamabad</a>.</p>'),
        'faq': ('How much tile do I need for a 120 square foot floor?', 'With a 10% cutting allowance, allow 132 square feet of coverage. For 2 by 2 foot tiles, each tile covers 4 square feet, so the estimate is 33 tiles. Round up to complete boxes using the tile count or coverage on the packaging.'),
    },
    'brick-calculator': {
        'title': 'Brick Calculator: Bricks for a Wall & Mortar Estimate',
        'quick_answer': '<strong>Brick quantity depends on wall area, wall thickness, brick size and mortar joints.</strong> Deduct openings, choose the actual brick dimensions and add a breakage allowance.',
        'section': ('How many bricks do I need for a wall or house?', '<p>For one wall, enter its length, height and thickness, then choose the brick’s dimensions and mortar joint. A thicker wall uses more bricks even when its visible face area stays the same. Deduct doors and windows before adding breakage.</p><p>For a whole house, estimate each wall separately and total the quantities. Built-up floor area alone does not determine the brick count, because room layout, wall thickness and openings vary. Use our <a href="/tools/concrete-calculator">concrete calculator</a> separately for concrete elements, or review the <a href="/grey-structure-islamabad">grey structure scope</a> for an Islamabad project.</p>'),
        'faq': ('How many bricks are needed to build a house?', 'There is no fixed brick count per house. Add the quantities for the actual walls after accounting for their dimensions, thickness, brick size, mortar joints, doors and windows. Then apply a breakage allowance. A floor-area estimate alone cannot account for the layout.'),
    },
    'square-footage-calculator': {
        'title': 'Square Footage Calculator: Room, House & Plot Area',
        'quick_answer': '<strong>Rectangle area in square feet = length in feet × width in feet.</strong> A 12 × 15 ft room is 180 sq ft. Calculate irregular spaces in sections, then add them.',
        'section': ('How do I figure out the square footage of a house?', '<p>Measure each room in feet, multiply length by width, and add the areas you need. A 12 × 15 ft room contributes 180 sq ft; a 10 × 10 ft room contributes 100 sq ft, for a total of 280 sq ft. Split L-shaped rooms into rectangles instead of measuring a single outer rectangle.</p><p>State whether your total is usable floor area or includes walls and other spaces. For an irregular plot boundary, use the <a href="/tools/plot-area-calculator">plot area calculator</a>. For a metric floor plan, convert using <a href="/tools/square-meters-to-square-feet">square meters to square feet</a>.</p>'),
        'faq': ('How many square feet are in a 12 by 15 room?', 'A rectangular room measuring 12 feet by 15 feet has 180 square feet of floor area. That is approximately 16.72 square meters. If the room has an alcove or an L shape, calculate the additional sections separately.'),
    },
}


def apply_search_content(tools):
    for tool in tools:
        changes = UPDATES.get(tool['slug'], {})
        for key in ('h1', 'title', 'meta_description', 'tagline', 'quick_answer'):
            if key in changes:
                tool[key] = changes[key]
        if 'section' in changes:
            heading, body = changes['section']
            tool['sections'] = [{'h': heading, 'body': body}] + tool['sections']
        if 'faq' in changes:
            tool['faqs'] = [changes['faq']] + tool['faqs']
