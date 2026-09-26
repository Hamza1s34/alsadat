
/* ============================================================
   AL SADAT BUILDERS — Construction & Property Tools
   Shared calculator engine + the maths for every tool page.

   Usage (from a /tools/<slug>/ page):
     <script src="/js/tools.js"></script>
     <script>AlsadatTools.init('concrete-calculator');</script>

   The page supplies two empty containers: #calc-form and
   #calc-output. Everything inside them is rendered here.

   Conventions
   -----------
   * Every length/area/volume input is stored in its own unit and
     converted to a single base unit before calculating:
       length -> feet, area -> square feet, volume -> cubic feet,
       mass -> kilograms, "small" (tile sizes) -> millimetres.
   * Cost fields are unit-price inputs only. No currency symbol is
     printed, so the same tool works in any country: the visitor
     enters the price in their own currency and reads the total in
     the same currency.
   * All figures are estimates. Material calculators add a waste
     allowance the visitor controls.
   ============================================================ */

(function () {
  'use strict';

  /* ----------------------------------------------------------
     Unit tables. Each maps a unit key to its factor in the base
     unit of that dimension.
     ---------------------------------------------------------- */

  var LENGTH = { ft: 1, 'in': 1 / 12, yd: 3, m: 3.280839895013123, cm: 0.03280839895013123, mm: 0.003280839895013123, km: 3280.839895013123, mi: 5280 };
  var AREA = { sqft: 1, sqm: 10.763910416709722, sqyd: 9, sqin: 1 / 144, sqcm: 1 / 929.0304, acre: 43560, hectare: 107639.10416709722, sqkm: 10763910.416709722, sqmi: 27878400 };
  var VOLUME = { cft: 1, cum: 35.31466672148859, cuyd: 27, cuin: 1 / 1728, litre: 0.03531466672148859, gal: 0.13368055555555558 };
  var MASS = { kg: 1, t: 1000, ust: 907.18474, lb: 0.45359237 };
  var SMALL = { mm: 1, cm: 10, 'in': 25.4, ft: 304.8 };

  var DIM = {
    length: { to: LENGTH, base: 'ft', def: 'ft', units: [['ft', 'ft'], ['m', 'm'], ['yd', 'yd'], ['in', 'in'], ['cm', 'cm']] },
    area: { to: AREA, base: 'sqft', def: 'sqft', units: [['sqft', 'ft²'], ['sqm', 'm²'], ['sqyd', 'yd²']] },
    volume: { to: VOLUME, base: 'cft', def: 'cft', units: [['cft', 'ft³'], ['cum', 'm³'], ['cuyd', 'yd³']] },
    mass: { to: MASS, base: 'kg', def: 't', units: [['t', 'tonnes'], ['kg', 'kg'], ['ust', 'US tons'], ['lb', 'lb']] },
    small: { to: SMALL, base: 'mm', def: 'mm', units: [['mm', 'mm'], ['cm', 'cm'], ['in', 'in'], ['ft', 'ft']] }
  };

  var MARLA_STANDARDS = [
    ['272.25', '272.25 sq ft — traditional (1 kanal = 20 marla)'],
    ['250', '250 sq ft — modern housing societies'],
    ['225', '225 sq ft — some regions and older schemes']
  ];

  var AREA_UNITS = [
    ['sqft', 'Square feet (ft²)'],
    ['sqm', 'Square metres (m²)'],
    ['sqyd', 'Square yards (yd²)'],
    ['sqin', 'Square inches (in²)'],
    ['sqcm', 'Square centimetres (cm²)'],
    ['acre', 'Acres'],
    ['hectare', 'Hectares'],
    ['sqkm', 'Square kilometres (km²)'],
    ['sqmi', 'Square miles (mi²)'],
    ['marla', 'Marla'],
    ['kanal', 'Kanal (20 marla)']
  ];

  /* 1 acre = 43,560 sq ft; 1 hectare = 2.4710538147 acres;
     1 square mile = 640 acres. Kanal is derived, not fixed — see below. */
  var SQFT_PER_ACRE = 43560;
  var SQFT_PER_HECTARE = 107639.10416709722;
  var SQFT_PER_SQMI = 27878400;

  /* A kanal is 20 marla — that relationship is fixed; the kanal's size in
     square feet is not, because marla itself varies by region. The familiar
     5,445 ft² kanal (605 yd²) is simply 20 × 272.25, the traditional marla.
     Every tool derives kanal from the marla standard the visitor selected,
     so no two tools on this site can disagree about the same plot. */
  function kanalSqft(std) { return 20 * (std > 0 ? std : 272.25); }

  /* ----------------------------------------------------------
     Formatting + read helpers
     ---------------------------------------------------------- */

  function fmt(x, d) {
    if (!isFinite(x)) return '—';
    if (x === 0) return '0';
    var abs = Math.abs(x);
    if (d === undefined) {
      if (abs >= 10000) d = 0;
      else if (abs >= 1000) d = 1;
      else if (abs >= 100) d = 1;
      else if (abs >= 1) d = 2;
      else if (abs >= 0.01) d = 3;
      else if (abs >= 0.0001) d = 4;
      else d = 6;
    }
    return Number(x).toLocaleString('en-US', { minimumFractionDigits: d, maximumFractionDigits: d });
  }

  /* The numeric whole-unit count. Use this — not whole() — whenever the
     rounded figure feeds further arithmetic: whole() returns a formatted
     string, and "1,024" * 20 evaluates to NaN, so a cost only breaks once
     the count passes a thousand. Exactly the case that escapes testing. */
  function wholeNum(x) {
    if (!isFinite(x)) return 0;
    /* Math.ceil(-1e-9) is -0, and (-0).toLocaleString() renders as "-0" —
       which is how "0 bags of cement" becomes an impossible negative. */
    if (x <= 0) return 0;
    return Math.ceil(x - 1e-9);
  }

  /* Whole units — bricks, bags, tiles, posts. Never shows "1,024.00 bags". */
  function whole(x) {
    if (!isFinite(x)) return '—';
    return wholeNum(x).toLocaleString('en-US');
  }

  /* Significant-figure formatting, for the pure unit converters. A fixed
     decimal count is wrong there in both directions: 1 acre in hectares
     needs 0.404686, while 5,000 acres needs 2,023.43 — one decimal count
     cannot serve both without either hiding precision or inventing it. */
  function sig(x, s) {
    if (!isFinite(x)) return '—';
    if (x === 0) return '0';
    s = s || 6;
    var d = s - Math.floor(Math.log(Math.abs(x)) / Math.LN10) - 1;
    if (d < 0) d = 0;
    if (d > 10) d = 10;
    return Number(x).toLocaleString('en-US', { minimumFractionDigits: 0, maximumFractionDigits: d });
  }

  function n(v, id) {
    var x = parseFloat(v[id]);
    if (!isFinite(x)) return 0;
    /* Every numeric input on this site is a physical quantity — a length,
       area, volume, price, percentage share or count. None can meaningfully
       be negative, and none of the 19 tools is written to reject one, so the
       floor lives here rather than being repeated in every compute(). */
    return x < 0 ? 0 : x;
  }

  /* Read a field in its base unit. Falls back to the dimension default. */
  function base(v, id, dim) {
    var d = DIM[dim];
    var u = v[id + '__unit'] || d.def;
    var f = d.to[u] !== undefined ? d.to[u] : d.to[d.def];
    return n(v, id) * f;
  }

  function mStd(v) {
    var x = parseFloat(v.marla);
    return isFinite(x) && x > 0 ? x : 272.25;
  }

  /* Convert any area value to square feet, resolving marla by standard. */
  function toSqft(value, unit, std) {
    if (unit === 'marla') return value * std;
    if (unit === 'kanal') return value * kanalSqft(std);
    return value * (AREA[unit] !== undefined ? AREA[unit] : 1);
  }

  function pick(v, id) { return v[id]; }

  function card(label, value, unit) { return { label: label, value: value, unit: unit || '' }; }

  /* Card set shared by every area-producing tool: metric first, then
     imperial, then land units. Keeps the global tools consistent. */
  function areaCards(sqft, std) {
    return [
      card('Square metres', fmt(sqft / AREA.sqm, 3), 'm²'),
      card('Square yards', fmt(sqft / AREA.sqyd, 2), 'yd²'),
      card('Acres', fmt(sqft / SQFT_PER_ACRE, 4), 'ac'),
      card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 4), 'ha'),
      card('Marla (' + fmt(std, 2) + ' ft²)', fmt(sqft / std, 2), 'marla'),
      card('Kanal (20 marla)', fmt(sqft / kanalSqft(std), 3), 'kanal')
    ];
  }

  /* ============================================================
     TOOL REGISTRY
     Each entry: fields[] + compute(v) -> {primary, cards, table, note}
     ============================================================ */

  var T = {};

  /* -------------------- Area converter -------------------- */
  T['area-converter'] = {
    fields: [
      { id: 'value', label: 'Area value', type: 'number', def: 1, step: 'any' },
      { id: 'from', label: 'Convert from', type: 'select', def: 'sqft', options: AREA_UNITS },
      { id: 'marla', label: 'Marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS,
        hint: 'Marla has no single definition. Choose the standard used by your local housing society or revenue office.' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var value = n(v, 'value');
      var sqft = toSqft(value, pick(v, 'from'), std);

      var rows = [
        ['Square feet', sig(sqft, 8), 'ft²'],
        ['Square metres', sig(sqft / AREA.sqm, 8), 'm²'],
        ['Square yards', sig(sqft / AREA.sqyd, 8), 'yd²'],
        ['Square inches', sig(sqft * 144, 8), 'in²'],
        ['Square centimetres', sig(sqft / AREA.sqcm, 8), 'cm²'],
        ['Acres', sig(sqft / SQFT_PER_ACRE, 8), 'ac'],
        ['Hectares', sig(sqft / SQFT_PER_HECTARE, 8), 'ha'],
        ['Square kilometres', sig(sqft / AREA.sqkm, 8), 'km²'],
        ['Square miles', sig(sqft / SQFT_PER_SQMI, 8), 'mi²'],
        ['Marla (' + fmt(std, 2) + ' sq ft)', sig(sqft / std, 8), 'marla'],
        ['Kanal (' + fmt(kanalSqft(std), 0) + ' ft², 20 marla)', sig(sqft / kanalSqft(std), 8), 'kanal']
      ];

      return {
        primary: card(fmt(value, 4) + ' ' + labelForUnit(pick(v, 'from')), sig(sqft / AREA.sqm, 6), 'm²'),
        cards: [
          card('Square feet', sig(sqft, 6), 'ft²'),
          card('Square yards', sig(sqft / AREA.sqyd, 6), 'yd²'),
          card('Acres', sig(sqft / SQFT_PER_ACRE, 6), 'ac'),
          card('Hectares', sig(sqft / SQFT_PER_HECTARE, 6), 'ha')
        ],
        table: { caption: 'The same area in every supported unit', head: ['Unit', 'Value', 'Symbol'], rows: rows },
        note: 'Fixed conversions: 1 acre = 43,560 ft², 1 hectare = 10,000 m² = 2.47105 acres, 1 square mile = 640 acres. Two units here are not fixed. Marla varies by region, so pick your standard above. Kanal is always 20 marla, which means its square-foot value follows the marla standard you chose — 5,445 ft² at the traditional 272.25 ft² marla, 5,000 ft² at the modern 250 ft² marla.'
      };
    }
  };

  function labelForUnit(key) {
    for (var i = 0; i < AREA_UNITS.length; i++) if (AREA_UNITS[i][0] === key) return AREA_UNITS[i][1];
    return key;
  }

  /* -------------------- Square footage -------------------- */
  T['square-footage-calculator'] = {
    fields: [
      { id: 'shape', label: 'Shape', type: 'select', def: 'rectangle', options: [
        ['rectangle', 'Rectangle / square'],
        ['circle', 'Circle'],
        ['triangle', 'Triangle'],
        ['trapezoid', 'Trapezoid / irregular plot']
      ] },
      { id: 'length', label: 'Length', type: 'number', def: 20, dim: 'length', showIf: function (v) { return v.shape === 'rectangle' || v.shape === 'trapezoid'; } },
      { id: 'width', label: 'Width', type: 'number', def: 15, dim: 'length', showIf: function (v) { return v.shape === 'rectangle'; } },
      { id: 'width2', label: 'Far-side width', type: 'number', def: 15, dim: 'length',
        showIf: function (v) { return v.shape === 'trapezoid'; },
        hint: 'Use the trapezoid shape when the two ends of a plot or room differ in width.' },
      { id: 'tdepth', label: 'Distance between the two sides', type: 'number', def: 15, dim: 'length', showIf: function (v) { return v.shape === 'trapezoid'; } },
      { id: 'diameter', label: 'Diameter', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.shape === 'circle'; } },
      { id: 'tbase', label: 'Base', type: 'number', def: 16, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'theight', label: 'Perpendicular height', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'count', label: 'How many identical areas?', type: 'number', def: 1, step: '1', min: 1, hint: 'Set to 2 or more for rooms or slabs of the same size.' },
      { id: 'price', label: 'Price per square foot (optional)', type: 'number', def: 0, step: 'any',
        hint: 'Enter the price in your own currency — the total is shown in the same currency.' }
    ],
    compute: function (v) {
      var shape = pick(v, 'shape');
      var L = base(v, 'length', 'length'), W = base(v, 'width', 'length');
      var one, shapeText;

      if (shape === 'circle') {
        var d = base(v, 'diameter', 'length');
        one = Math.PI * Math.pow(d / 2, 2);
        shapeText = 'π × (diameter ÷ 2)²';
      } else if (shape === 'triangle') {
        one = 0.5 * base(v, 'tbase', 'length') * base(v, 'theight', 'length');
        shapeText = '½ × base × perpendicular height';
      } else if (shape === 'trapezoid') {
        one = 0.5 * (L + base(v, 'width2', 'length')) * base(v, 'tdepth', 'length');
        shapeText = '½ × (side A + side B) × the distance between them';
      } else {
        one = L * W;
        shapeText = 'length × width';
      }

      var count = Math.max(1, Math.round(n(v, 'count') || 1));
      var sqft = one * count;
      var price = n(v, 'price');
      var cards = [card('Square metres', fmt(sqft / AREA.sqm, 3), 'm²'), card('Square yards', fmt(sqft / AREA.sqyd, 2), 'yd²')];
      cards = cards.concat(areaCards(sqft, 272.25).slice(2));
      cards.unshift(card('Single area', fmt(one, 2), 'ft²'));

      if (price > 0) cards.push(card('Estimated cost', fmt(sqft * price, 2), ''));

      return {
        primary: card('Total area', fmt(sqft, 2), 'ft²'),
        cards: cards,
        note: 'Formula used: ' + shapeText + (count > 1 ? ', multiplied by ' + count + ' identical areas.' : '.') +
          ' Measurements are converted to feet before the calculation, so you can mix units between fields.'
      };
    }
  };

  /* -------------------- Land area -------------------- */
  T['land-area-calculator'] = {
    fields: [
      { id: 'shape', label: 'Land shape', type: 'select', def: 'rectangle', options: [
        ['rectangle', 'Rectangle / square plot'],
        ['triangle', 'Triangular plot'],
        ['trapezoid', 'Trapezoidal / irregular plot'],
        ['direct', 'I already know the area']
      ] },
      { id: 'length', label: 'Length', type: 'number', def: 90, dim: 'length', showIf: function (v) { return v.shape === 'rectangle' || v.shape === 'trapezoid'; } },
      { id: 'width', label: 'Width', type: 'number', def: 60, dim: 'length', showIf: function (v) { return v.shape === 'rectangle'; } },
      { id: 'depth', label: 'Distance between the two sides', type: 'number', def: 60, dim: 'length', showIf: function (v) { return v.shape === 'trapezoid'; } },
      { id: 'width2', label: 'Far-side width', type: 'number', def: 50, dim: 'length', showIf: function (v) { return v.shape === 'trapezoid'; } },
      { id: 'tbase', label: 'Base', type: 'number', def: 80, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'theight', label: 'Height (perpendicular)', type: 'number', def: 60, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'directValue', label: 'Known area', type: 'number', def: 5, step: 'any', showIf: function (v) { return v.shape === 'direct'; } },
      { id: 'directUnit', label: 'Unit of that area', type: 'select', def: 'marla', options: AREA_UNITS, showIf: function (v) { return v.shape === 'direct'; } },
      { id: 'marla', label: 'Marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS },
      { id: 'pricePerMarla', label: 'Price per marla (optional)', type: 'number', def: 0, step: 'any',
        hint: 'Land is usually priced per marla in South Asia and per acre or hectare elsewhere. Enter either — both totals are shown.' },
      { id: 'pricePerAcre', label: 'Price per acre (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var shape = pick(v, 'shape');
      var sqft, formula;

      if (shape === 'direct') {
        var du = pick(v, 'directUnit');
        sqft = du === 'marla' ? n(v, 'directValue') * std : toSqft(n(v, 'directValue'), du, std);
        formula = 'Area entered directly in ' + labelForUnit(du) + '.';
      } else if (shape === 'triangle') {
        sqft = 0.5 * base(v, 'tbase', 'length') * base(v, 'theight', 'length');
        formula = 'Area = ½ × base × perpendicular height.';
      } else if (shape === 'trapezoid') {
        sqft = 0.5 * (base(v, 'length', 'length') + base(v, 'width2', 'length')) * base(v, 'depth', 'length');
        formula = 'Area = ½ × (side A + side B) × the perpendicular distance between them — the standard method for a plot whose two ends differ.';
      } else {
        sqft = base(v, 'length', 'length') * base(v, 'width', 'length');
        formula = 'Area = length × width.';
      }

      var marla = sqft / std;
      var acres = sqft / SQFT_PER_ACRE;
      var permission = landNote(sqft, std);

      var cards = [
        card('Square feet', fmt(sqft, 2), 'ft²'),
        card('Square metres', fmt(sqft / AREA.sqm, 2), 'm²'),
        card('Square yards', fmt(sqft / AREA.sqyd, 2), 'yd²'),
        card('Marla (' + fmt(std, 2) + ' ft²)', fmt(marla, 2), 'marla'),
        card('Kanal (20 marla)', fmt(sqft / kanalSqft(std), 3), 'kanal'),
        card('Acres', fmt(acres, 4), 'ac'),
        card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 4), 'ha')
      ];

      var pm = n(v, 'pricePerMarla'), pa = n(v, 'pricePerAcre');
      if (pm > 0) cards.push(card('Land value at per-marla rate', fmt(marla * pm, 2), ''));
      if (pa > 0) cards.push(card('Land value at per-acre rate', fmt(acres * pa, 2), ''));

      return {
        primary: card('Total land area', fmt(sqft, 2), 'ft²'),
        cards: cards,
        table: areaTable(sqft, std, 'Land area conversions'),
        note: formula + ' Local building rules: ' + permission
      };
    }
  };

  /* Every land tool repeats the same closing sanity check: the area in the
     units the visitor's local market actually prices land in. */
  function landNote(sqft, std) {
    var marla = sqft / std;
    var kanal = sqft / kanalSqft(std);
    return 'this plot measures ' + fmt(marla, 2) + ' marla (' + fmt(kanal, 3) + ' kanal), which is ' +
      fmt(sqft / SQFT_PER_ACRE, 4) + ' acres. Local byelaws set the maximum covered area from the plot size, so check your authority’s table before designing.';
  }

  function areaTable(sqft, std, caption) {
    return {
      caption: caption,
      head: ['Unit', 'Value'],
      rows: [
        ['Square feet (ft²)', fmt(sqft, 2)],
        ['Square metres (m²)', fmt(sqft / AREA.sqm, 3)],
        ['Square yards (yd²)', fmt(sqft / AREA.sqyd, 3)],
        ['Marla (' + fmt(std, 2) + ' ft²)', fmt(sqft / std, 3)],
        ['Kanal (' + fmt(kanalSqft(std), 0) + ' ft², 20 marla)', fmt(sqft / kanalSqft(std), 4)],
        ['Acres', fmt(sqft / SQFT_PER_ACRE, 5)],
        ['Hectares', fmt(sqft / SQFT_PER_HECTARE, 5)],
        ['Square miles', fmt(sqft / SQFT_PER_SQMI, 7)]
      ]
    };
  }

  /* -------------------- Plot area -------------------- */
  T['plot-area-calculator'] = {
    fields: [
      { id: 'length', label: 'Plot length', type: 'number', def: 50, dim: 'length' },
      { id: 'width', label: 'Plot width', type: 'number', def: 90, dim: 'length' },
      { id: 'irregular', label: 'The plot narrows or widens at one end', type: 'check', def: false },
      { id: 'width2', label: 'Width at the far end', type: 'number', def: 80, dim: 'length', showIf: function (v) { return v.irregular; } },
      { id: 'side1', label: 'Left side length', type: 'number', def: 0, dim: 'length', showIf: function (v) { return v.irregular; },
        hint: 'Optional. Enter both side lengths for an exact boundary run; leave at 0 to use the symmetric estimate.' },
      { id: 'side2', label: 'Right side length', type: 'number', def: 0, dim: 'length', showIf: function (v) { return v.irregular; },
        hint: 'Measured along the actual edge of the plot, not the straight-line distance on the map.' },
      { id: 'marla', label: 'Marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS },
      { id: 'pricePerSqft', label: 'Price per square foot (optional)', type: 'number', def: 0, step: 'any' },
      { id: 'pricePerMarla', label: 'Price per marla (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var L = base(v, 'length', 'length'), W = base(v, 'width', 'length');
      var W2 = v.irregular ? base(v, 'width2', 'length') : W;
      var sqft = v.irregular ? 0.5 * (W + W2) * L : L * W;

      /* Perimeter. A rectangle is fully determined by its two dimensions.
         A quadrilateral is not: the front and back widths alone do not fix
         the side lengths, because the shape can flex. So the two sides are
         taken as inputs when the visitor knows them, and only fall back to
         an equal-slope estimate when they leave them blank. */
      var perimeter, perimExact = false;
      if (v.irregular) {
        var s1 = base(v, 'side1', 'length'), s2 = base(v, 'side2', 'length');
        if (s1 > 0 && s2 > 0) {
          perimeter = W + W2 + s1 + s2;
          perimExact = true;
        } else {
          var slant = Math.sqrt(Math.pow(L, 2) + Math.pow((W2 - W) / 2, 2));
          perimeter = W + W2 + 2 * slant;
        }
      } else {
        perimeter = 2 * (L + W);
      }

      var marla = sqft / std;
      var cards = [
        card('Square metres', fmt(sqft / AREA.sqm, 2), 'm²'),
        card('Square yards', fmt(sqft / AREA.sqyd, 2), 'yd²'),
        card('Marla (' + fmt(std, 2) + ' ft²)', fmt(marla, 2), 'marla'),
        card('Kanal (20 marla)', fmt(sqft / kanalSqft(std), 3), 'kanal'),
        card('Acres', fmt(sqft / SQFT_PER_ACRE, 4), 'ac'),
        card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 4), 'ha'),
        card('Boundary length (perimeter)' + (perimExact ? '' : (v.irregular ? ' — estimated' : '')), fmt(perimeter, 2), 'ft')
      ];

      var p1 = n(v, 'pricePerSqft'), p2 = n(v, 'pricePerMarla');
      if (p1 > 0) cards.push(card('Plot value at per-ft² rate', fmt(sqft * p1, 2), ''));
      if (p2 > 0) cards.push(card('Plot value at per-marla rate', fmt(marla * p2, 2), ''));

      return {
        primary: card('Plot area', fmt(sqft, 2), 'ft²'),
        cards: cards,
        table: areaTable(sqft, std, 'Your plot in every unit'),
        note: 'The area uses the trapezoid rule — half the sum of the two widths multiplied by the distance between them — which is the standard method for a plot that tapers. ' +
          (v.irregular
            ? (perimExact
              ? 'The perimeter is the sum of the two widths and the two side lengths you entered, so it is exact.'
              : 'The perimeter is estimated: your front and back widths do not on their own fix the side lengths, because a four-sided plot with those widths can flex into different shapes. This figure assumes both sides slope equally. Enter the left and right side lengths for an exact boundary run.')
            : 'Tick the irregular box if the plot is wider or narrower at one end.') +
          ' Because a plot’s area drives the maximum permitted covered area, use this figure — not the advertised size — when checking local byelaws.'
      };
    }
  };

  /* -------------------- Square feet <-> square metres -------------------- */
  T['square-feet-to-square-meters'] = {
    fields: [
      { id: 'value', label: 'Area in square feet', type: 'number', def: 1000, step: 'any' },
      { id: 'marla', label: 'Show land units using marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS }
    ],
    compute: function (v) {
      var sqft = n(v, 'value');
      var sqm = sqft / AREA.sqm;
      var std = mStd(v);
      return {
        primary: card(fmt(sqft, 2) + ' ft² equals', sig(sqm, 7), 'm²'),
        cards: [
          card('Square metres', sig(sqm, 7), 'm²'),
          card('Square centimetres', sig(sqm * 10000, 7), 'cm²'),
          card('Square yards', sig(sqft / AREA.sqyd, 7), 'yd²'),
          card('Square millimetres', sig(sqm * 1e6, 7), 'mm²'),
          card('Marla', sig(sqft / std, 5), 'marla'),
          card('Acres', sig(sqft / SQFT_PER_ACRE, 7), 'ac')
        ],
        note: 'One square foot is exactly 0.09290304 square metres, because one foot is defined as exactly 0.3048 metres. Multiply square feet by 0.09290304, or divide by 10.7639104, to get square metres.'
      };
    }
  };

  T['square-meters-to-square-feet'] = {
    fields: [
      { id: 'value', label: 'Area in square metres', type: 'number', def: 100, step: 'any' },
      { id: 'marla', label: 'Show land units using marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS }
    ],
    compute: function (v) {
      var sqm = n(v, 'value');
      var sqft = sqm * AREA.sqm;
      var std = mStd(v);
      return {
        primary: card(fmt(sqm, 3) + ' m² equals', sig(sqft, 8), 'ft²'),
        cards: [
          card('Square feet', sig(sqft, 8), 'ft²'),
          card('Square yards', sig(sqft / AREA.sqyd, 7), 'yd²'),
          card('Square inches', sig(sqft * 144, 7), 'in²'),
          card('Hectares', sig(sqm / 10000, 7), 'ha'),
          card('Acres', sig(sqft / SQFT_PER_ACRE, 7), 'ac'),
          card('Marla', sig(sqft / std, 5), 'marla')
        ],
        note: 'One square metre equals 10.7639104 square feet. Multiply square metres by 10.7639104, or divide by 0.09290304, to get square feet.'
      };
    }
  };

  /* -------------------- Acres <-> hectares -------------------- */
  T['acres-to-hectares'] = {
    fields: [
      { id: 'value', label: 'Area in acres', type: 'number', def: 5, step: 'any' },
      { id: 'pricePerAcre', label: 'Price per acre (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var acres = n(v, 'value');
      var ha = acres * 0.40468564224;
      var sqft = acres * SQFT_PER_ACRE;
      var cards = [
        card('Hectares', sig(ha, 8), 'ha'),
        card('Square metres', sig(ha * 10000, 8), 'm²'),
        card('Square feet', sig(sqft, 8), 'ft²'),
        card('Square yards', sig(sqft / AREA.sqyd, 7), 'yd²'),
        card('Square kilometres', sig(ha / 100, 7), 'km²'),
        card('Square miles', sig(sqft / SQFT_PER_SQMI, 7), 'mi²'),
        card('Ares', sig(ha * 100, 7), 'a')
      ];
      var p = n(v, 'pricePerAcre');
      if (p > 0) {
        cards.push(card('Total value', fmt(acres * p, 2), ''));
        cards.push(card('Price per hectare', fmt(ha > 0 ? acres * p / ha : 0, 2), ''));
      }
      return {
        primary: card(fmt(acres, 4) + ' acres equals', sig(ha, 8), 'ha'),
        cards: cards,
        note: 'One acre is 4,046.8564224 m², and one hectare is exactly 10,000 m². So 1 acre = 0.40468564224 hectares and 1 hectare = 2.4710538147 acres. The acre is a statute measure used in the United States, the United Kingdom and across the Commonwealth; the hectare is the metric land unit used almost everywhere else.'
      };
    }
  };

  T['hectares-to-acres'] = {
    fields: [
      { id: 'value', label: 'Area in hectares', type: 'number', def: 2, step: 'any' },
      { id: 'pricePerHectare', label: 'Price per hectare (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var ha = n(v, 'value');
      var acres = ha * 2.471053814671653;
      var sqm = ha * 10000;
      var cards = [
        card('Acres', sig(acres, 8), 'ac'),
        card('Square metres', sig(sqm, 8), 'm²'),
        card('Square feet', sig(sqm * AREA.sqm, 8), 'ft²'),
        card('Square yards', sig(sqm * AREA.sqm / AREA.sqyd, 7), 'yd²'),
        card('Square kilometres', sig(ha / 100, 7), 'km²'),
        card('Square miles', sig(sqm * AREA.sqm / SQFT_PER_SQMI, 7), 'mi²'),
        card('Ares', sig(ha * 100, 7), 'a')
      ];
      var p = n(v, 'pricePerHectare');
      if (p > 0) {
        cards.push(card('Total value', fmt(ha * p, 2), ''));
        cards.push(card('Price per acre', fmt(acres > 0 ? ha * p / acres : 0, 2), ''));
      }
      return {
        primary: card(fmt(ha, 4) + ' hectares equals', sig(acres, 8), 'ac'),
        cards: cards,
        note: 'One hectare is 10,000 m², which is 2.4710538147 acres — just under two and a half acres. The hectare is the standard unit for agricultural and development land in most of the world; the acre is still used in the United States, the United Kingdom, Ireland and several Commonwealth countries.'
      };
    }
  };

  /* -------------------- Marla <-> square feet -------------------- */
  T['marla-to-square-feet'] = {
    fields: [
      { id: 'value', label: 'Area in marla', type: 'number', def: 10, step: 'any' },
      { id: 'marla', label: 'Marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS,
        hint: 'Always check which standard your seller, society or revenue record uses. The same "10 marla" can mean three different areas.' },
      { id: 'pricePerMarla', label: 'Price per marla (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var marla = n(v, 'value');
      var sqft = marla * std;
      var cards = [
        card('Square metres', fmt(sqft / AREA.sqm, 3), 'm²'),
        card('Square yards', fmt(sqft / AREA.sqyd, 3), 'yd²'),
        card('Kanal (20 marla)', fmt(sqft / kanalSqft(std), 4), 'kanal'),
        card('Acres', fmt(sqft / SQFT_PER_ACRE, 5), 'ac'),
        card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 5), 'ha')
      ];
      var p = n(v, 'pricePerMarla');
      if (p > 0) {
        cards.push(card('Total value', fmt(marla * p, 2), ''));
        cards.push(card('Price per square foot', fmt(std > 0 ? p / std : 0, 4), ''));
      }
      return {
        primary: card(fmt(marla, 3) + ' marla equals', fmt(sqft, 2), 'ft²'),
        cards: cards,
        note: 'Using the ' + fmt(std, 2) + ' sq ft standard, one marla is ' + fmt(std, 2) + ' ft², and one kanal — which is always 20 marla — is ' + fmt(kanalSqft(std), 0) + ' ft². Both figures move together with the standard you select, so the kanal shown here and the kanal shown by every other tool on this site always agree.'
      };
    }
  };

  T['square-feet-to-marla'] = {
    fields: [
      { id: 'value', label: 'Area in square feet', type: 'number', def: 2722.5, step: 'any' },
      { id: 'marla', label: 'Marla standard', type: 'select', def: '272.25', options: MARLA_STANDARDS }
    ],
    compute: function (v) {
      var std = mStd(v);
      var sqft = n(v, 'value');
      var marla = sqft / std;
      var cards = [
        card('Square metres', fmt(sqft / AREA.sqm, 3), 'm²'),
        card('Square yards', fmt(sqft / AREA.sqyd, 3), 'yd²'),
        card('Kanal (20 marla)', fmt(sqft / kanalSqft(std), 4), 'kanal'),
        card('Acres', fmt(sqft / SQFT_PER_ACRE, 5), 'ac'),
        card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 5), 'ha'),
        card('Marla using 250 ft²', fmt(sqft / 250, 3), 'marla'),
        card('Marla using 225 ft²', fmt(sqft / 225, 3), 'marla')
      ];
      return {
        primary: card(fmt(sqft, 2) + ' ft² equals', fmt(marla, 3), 'marla'),
        cards: cards,
        note: 'Divide the area in square feet by ' + fmt(std, 2) + ' (your selected marla standard). The last two cards show how the same plot is described under the other common standards — a plot sold as ' +
          fmt(sqft / 250, 1) + ' marla on a 250 ft² basis is only ' + fmt(sqft / std, 1) + ' marla on the ' + fmt(std, 2) + ' ft² basis, so always confirm which one the price is quoted against.'
      };
    }
  };

  /* -------------------- Kanal to marla -------------------- */
  T['kanal-to-marla'] = {
    fields: [
      { id: 'value', label: 'Area in kanal', type: 'number', def: 1, step: 'any' },
      { id: 'marla', label: 'Marla standard for the square-foot value', type: 'select', def: '272.25', options: MARLA_STANDARDS },
      { id: 'pricePerMarla', label: 'Price per marla (optional)', type: 'number', def: 0, step: 'any' },
      { id: 'pricePerKanal', label: 'Price per kanal (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var kanal = n(v, 'value');
      var marla = kanal * 20;
      var sqft = marla * std;

      var cards = [
        card('Marla', fmt(marla, 3), 'marla'),
        card('Square feet (at ' + fmt(std, 2) + ' ft²/marla)', fmt(sqft, 2), 'ft²'),
        card('Square feet (traditional 272.25 ft² marla)', fmt(kanal * 5445, 2), 'ft²'),
        card('Square metres', fmt(sqft / AREA.sqm, 2), 'm²'),
        card('Square yards', fmt(sqft / AREA.sqyd, 2), 'yd²'),
        card('Acres', fmt(sqft / SQFT_PER_ACRE, 4), 'ac'),
        card('Hectares', fmt(sqft / SQFT_PER_HECTARE, 4), 'ha')
      ];
      var p1 = n(v, 'pricePerMarla'), p2 = n(v, 'pricePerKanal');
      if (p1 > 0) cards.push(card('Value at per-marla rate', fmt(marla * p1, 2), ''));
      if (p2 > 0) cards.push(card('Value at per-kanal rate', fmt(kanal * p2, 2), ''));

      return {
        primary: card(fmt(kanal, 3) + ' kanal equals', fmt(marla, 2), 'marla'),
        cards: cards,
        table: {
          caption: 'Kanal to marla at a glance',
          head: ['Kanal', 'Marla', 'Square feet (272.25 ft² marla)', 'Acres'],
          rows: [0.25, 0.5, 1, 2, 4, 8, 10].map(function (k) {
            return [fmt(k, 2), fmt(k * 20, 2), fmt(k * 20 * 272.25, 2), fmt(k * 20 * 272.25 / SQFT_PER_ACRE, 4)];
          })
        },
        note: 'Kanal is defined as exactly 20 marla everywhere it is used, so the marla figure never changes. What changes is the square-foot value: 20 × 272.25 = 5,445 ft² in the traditional measure (the figure used in CDA and most Punjab revenue records, equal to 605 square yards), or 20 × 250 = 5,000 ft² under the modern society standard. Eight kanal make one acre only under the 272.25 ft² marla.'
      };
    }
  };

  /* -------------------- Concrete -------------------- */
  T['concrete-calculator'] = {
    fields: [
      { id: 'shape', label: 'What are you pouring?', type: 'select', def: 'slab', options: [
        ['slab', 'Slab, footing or pad — rectangular'],
        ['columnSquare', 'Square or rectangular column'],
        ['columnRound', 'Round column'],
        ['stairs', 'Stairs']
      ] },
      { id: 'length', label: 'Length', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'slab'; } },
      { id: 'width', label: 'Width', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'slab'; } },
      { id: 'depth', label: 'Thickness / depth', type: 'number', def: 4, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'slab'; } },
      { id: 'side1', label: 'Column width', type: 'number', def: 12, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'columnSquare'; } },
      { id: 'side2', label: 'Column depth', type: 'number', def: 12, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'columnSquare'; } },
      { id: 'colHeight', label: 'Column height', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'columnSquare' || v.shape === 'columnRound'; } },
      { id: 'diameter', label: 'Column diameter', type: 'number', def: 12, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'columnRound'; } },
      { id: 'steps', label: 'Number of steps', type: 'number', def: 12, step: '1', showIf: function (v) { return v.shape === 'stairs'; } },
      { id: 'rise', label: 'Riser height', type: 'number', def: 6, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'stairs'; } },
      { id: 'tread', label: 'Tread depth', type: 'number', def: 10, dim: 'length', unitDef: 'in', showIf: function (v) { return v.shape === 'stairs'; } },
      { id: 'stairWidth', label: 'Stair width', type: 'number', def: 3, dim: 'length', showIf: function (v) { return v.shape === 'stairs'; } },
      { id: 'mix', label: 'Concrete grade', type: 'select', def: '1:2:4', options: [
        ['1:3:6', 'M10 (1 : 3 : 6) — mass fill, blinding'],
        ['1:2:4', 'M15 (1 : 2 : 4) — general footings and slabs'],
        ['1:1.5:3', 'M20 (1 : 1.5 : 3) — reinforced slabs and columns'],
        ['custom', 'M25 and above — design mix (enter your own ratio)'],
        ['1:4:8', 'M7.5 (1 : 4 : 8) — lean concrete'],
        ['1:5:10', 'M5 (1 : 5 : 10) — bedding and fill']
      ] },
      { id: 'c1', label: 'Cement parts', type: 'number', def: 1, step: 'any', showIf: function (v) { return v.mix === 'custom'; } },
      { id: 'c2', label: 'Sand parts', type: 'number', def: 1.5, step: 'any', showIf: function (v) { return v.mix === 'custom'; } },
      { id: 'c3', label: 'Aggregate parts', type: 'number', def: 3, step: 'any', showIf: function (v) { return v.mix === 'custom'; },
        hint: 'M25 and above are specified as design mixes rather than nominal ratios: the proportions come from testing the materials you actually have, not from a table. Enter the ratio from your engineer’s mix design.' },
      { id: 'waste', label: 'Wastage allowance', type: 'number', def: 5, unitLabel: '%' },
      { id: 'price', label: 'Price per cubic metre of ready-mix (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var shape = pick(v, 'shape');
      var cft = 0, shapeText = '';

      if (shape === 'columnRound') {
        var r = base(v, 'diameter', 'length') / 2;
        cft = Math.PI * r * r * base(v, 'colHeight', 'length');
        shapeText = 'π × radius² × height';
      } else if (shape === 'columnSquare') {
        cft = base(v, 'side1', 'length') * base(v, 'side2', 'length') * base(v, 'colHeight', 'length');
        shapeText = 'width × depth × height';
      } else if (shape === 'stairs') {
        var cnt = Math.max(1, Math.round(n(v, 'steps') || 1));
        cft = 0.5 * base(v, 'rise', 'length') * base(v, 'tread', 'length') * base(v, 'stairWidth', 'length') * cnt;
        shapeText = '½ × riser × tread × stair width × number of steps (the triangular step profile, excluding the waist slab)';
      } else {
        cft = base(v, 'length', 'length') * base(v, 'width', 'length') * base(v, 'depth', 'length');
        shapeText = 'length × width × thickness';
      }

      var cum = cft / VOLUME.cum;
      var waste = n(v, 'waste') / 100;
      var cumWaste = cum * (1 + waste);

      /* Nominal grades come from the standard ratio table. M25 and above are
         design mixes — the ratio has to come from the engineer, so it is
         taken from the three part fields the visitor fills in. */
      var parts;
      if (pick(v, 'mix') === 'custom') {
        parts = [Math.max(0, n(v, 'c1')), Math.max(0, n(v, 'c2')), Math.max(0, n(v, 'c3'))];
      } else {
        parts = pick(v, 'mix').split(':').map(parseFloat);
      }
      var sum = parts[0] + parts[1] + parts[2];
      if (!(sum > 0)) { parts = [1, 2, 4]; sum = 7; }
      var mixLabel = pick(v, 'mix') === 'custom' ? (parts[0] + ' : ' + parts[1] + ' : ' + parts[2] + ' (design mix)') : pick(v, 'mix');
      var dry = cumWaste * 1.54;               /* bulking / voids factor for dry ingredients */
      var cementVol = dry * (parts[0] / sum);
      var sandVol = dry * (parts[1] / sum);
      var aggVol = dry * (parts[2] / sum);
      var cementKg = cementVol * 1440;          /* bulk density of cement */
      var bags = cementKg / 50;                 /* 50 kg bag */
      var sandT = sandVol * 1.6;                /* dry sand ~1,600 kg/m³ */
      var aggT = aggVol * 1.5;                  /* coarse aggregate ~1,500 kg/m³ */
      var water = cementKg * 0.5;               /* 0.5 water-cement ratio */

      var cards = [
        card('Cubic feet', fmt(cft, 2), 'ft³'),
        card('Cubic yards', fmt(cft / VOLUME.cuyd, 3), 'yd³'),
        card('Volume with wastage', fmt(cumWaste, 3), 'm³'),
        card('Cement', whole(bags), 'bags of 50 kg'),
        card('Cement', fmt(cementKg, 0), 'kg'),
        card('Sand', fmt(sandT, 2), 'tonnes'),
        card('Sand volume', fmt(sandVol, 2), 'm³'),
        card('Coarse aggregate', fmt(aggT, 2), 'tonnes'),
        card('Aggregate volume', fmt(aggVol, 2), 'm³'),
        card('Water', fmt(water, 0), 'litres')
      ];

      var p = n(v, 'price');
      if (p > 0) cards.push(card('Ready-mix cost', fmt(cumWaste * p, 2), ''));

      return {
        primary: card(shape === 'stairs' ? 'Concrete for steps (excludes waist slab)' : 'Concrete volume', fmt(cumWaste, 3), 'm³'),
        cards: cards,
        table: {
          caption: 'Ingredient breakdown at ' + mixLabel + ' (per ' + fmt(cumWaste, 3) + ' m³ of placed concrete)',
          head: ['Material', 'Parts', 'Volume', 'Weight'],
          rows: [
            ['Cement', parts[0], fmt(cementVol, 3) + ' m³', fmt(cementKg, 0) + ' kg (' + whole(bags) + ' bags)'],
            ['Sand (fine aggregate)', parts[1], fmt(sandVol, 3) + ' m³', fmt(sandT, 2) + ' tonnes'],
            ['Coarse aggregate', parts[2], fmt(aggVol, 3) + ' m³', fmt(aggT, 2) + ' tonnes'],
            ['Water', '—', fmt(water / 1000, 3) + ' m³', fmt(water, 0) + ' litres']
          ]
        },
        note: 'Wet volume is converted to dry ingredients with a factor of 1.54. That is a bulking allowance, not a claim that concrete shrinks by 54% — loose cement, sand and aggregate contain air voids and are measured before mixing, so it takes roughly 1.54 m³ of dry material to make 1 m³ of placed concrete. It is an estimating convention, not a physical constant. Cement is priced on a 50 kg bag at 1,440 kg/m³ bulk density, sand at 1,600 kg/m³ and coarse aggregate at 1,500 kg/m³, and water is estimated at a 0.5 water-to-cement ratio. ' +
          (shape === 'stairs' ? 'This covers the step profile only. The waist slab and any landing beneath the flight are not included — work those out as a separate slab and add them, or the order will come up well short. ' : '') +
          'These are ordering figures: buy to the nearest whole bag and the nearest half tonne, and confirm the mix design with your structural engineer before pouring. Formula used: ' + shapeText + '.'
      };
    }
  };

  /* -------------------- Brick -------------------- */
  T['brick-calculator'] = {
    fields: [
      { id: 'length', label: 'Wall length', type: 'number', def: 30, dim: 'length' },
      { id: 'height', label: 'Wall height', type: 'number', def: 10, dim: 'length' },
      { id: 'openings', label: 'Area of doors and windows in the wall', type: 'number', def: 0, dim: 'area',
        unitDef: 'sqft', hint: 'Deduct openings so you do not order bricks for wall that will be cut out.' },
      { id: 'thickness', label: 'Wall thickness', type: 'select', def: '9', options: [
        ['4.5', '4.5 in (112 mm) — half-brick / partition'],
        ['9', '9 in (230 mm) — standard external wall'],
        ['13.5', '13.5 in (340 mm) — one-and-a-half brick'],
        ['custom', 'Custom thickness']
      ] },
      { id: 'customThickness', label: 'Custom wall thickness', type: 'number', def: 6, dim: 'length', unitDef: 'in', showIf: function (v) { return v.thickness === 'custom'; } },
      { id: 'brickSize', label: 'Brick size', type: 'select', def: 'std', options: [
        ['std', 'Standard 9 × 4.5 × 3 in (230 × 115 × 75 mm)'],
        ['modular', 'Modular 190 × 90 × 90 mm'],
        ['custom', 'Custom size']
      ] },
      { id: 'bl', label: 'Brick length', type: 'number', def: 230, dim: 'small', unitDef: 'mm', showIf: function (v) { return v.brickSize === 'custom'; } },
      { id: 'bw', label: 'Brick width', type: 'number', def: 115, dim: 'small', unitDef: 'mm', showIf: function (v) { return v.brickSize === 'custom'; } },
      { id: 'bh', label: 'Brick height', type: 'number', def: 75, dim: 'small', unitDef: 'mm', showIf: function (v) { return v.brickSize === 'custom'; } },
      { id: 'joint', label: 'Mortar joint thickness', type: 'number', def: 10, dim: 'small', unitDef: 'mm' },
      { id: 'waste', label: 'Breakage allowance', type: 'number', def: 5, unitLabel: '%' },
      { id: 'mortarMix', label: 'Mortar mix', type: 'select', def: '1:5', options: [
        ['1:4', '1 : 4 cement to sand — strong, load-bearing'],
        ['1:5', '1 : 5 — general purpose'],
        ['1:6', '1 : 6 — non-load-bearing partitions']
      ] },
      { id: 'pricePer1000', label: 'Price per 1,000 bricks (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var dims;
      if (pick(v, 'brickSize') === 'modular') dims = [190, 90, 90];
      else if (pick(v, 'brickSize') === 'custom') dims = [n(v, 'bl') || 230, n(v, 'bw') || 115, n(v, 'bh') || 75];
      else dims = [230, 115, 75];

      var joint = n(v, 'joint') || 10;
      var L = dims[0], W = dims[1], H = dims[2];

      var thickText = pick(v, 'thickness');
      var thicknessFt = thickText === 'custom'
        ? base(v, 'customThickness', 'length')
        : parseFloat(thickText) / 12;

      var areaSqft = Math.max(0, base(v, 'length', 'length') * base(v, 'height', 'length') - base(v, 'openings', 'area'));
      var areaM2 = areaSqft / AREA.sqm;
      var thicknessM = thicknessFt / 3.280839895013123;
      var thicknessMm = thicknessFt * 304.8;
      var wallVolM3 = areaM2 * thicknessM;

      /* Bricks are counted by face area, not by dividing the wall volume by
         a brick-sized cube. A wall is built in whole leaves of brickwork: a
         230 mm wall is two 115 mm leaves, each showing one 230 × 75 mm face.
         The volume method undercounts a half-brick wall by about 9%, because
         the wall's thickness is not a whole multiple of the jointed brick. */
      var leaves = Math.max(1, Math.round(thicknessMm / (W + joint)));
      var bricksPerM2 = leaves / (((L + joint) / 1000) * ((H + joint) / 1000));
      var bricksNet = areaM2 * bricksPerM2;
      var waste = n(v, 'waste') / 100;
      var bricks = bricksNet * (1 + waste);

      var brickActualVolM3 = (L / 1000) * (W / 1000) * (H / 1000);
      var mortarWet = Math.max(0, wallVolM3 - bricksNet * brickActualVolM3);
      var mortarDry = mortarWet * 1.33;
      var mp = pick(v, 'mortarMix').split(':').map(parseFloat);
      var msum = mp[0] + mp[1];
      var cementVol = mortarDry * (mp[0] / msum);
      var cementKg = cementVol * 1440;
      var cementBags = cementKg / 50;
      var sandVol = mortarDry * (mp[1] / msum);
      var sandT = sandVol * 1.6;

      var cards = [
        card('Wall area', fmt(areaSqft, 2), 'ft²'),
        card('Wall area', fmt(areaM2, 3), 'm²'),
        card('Bricks needed', whole(bricks), 'bricks'),
        card('Bricks without waste', whole(bricksNet), 'bricks'),
        card('Bricks per m² of wall', whole(wallVolM3 > 0 ? bricksNet / areaM2 : 0), 'bricks'),
        card('Bricks per ft² of wall', fmt(areaSqft > 0 ? bricksNet / areaSqft : 0, 2), 'bricks'),
        card('Wall volume', fmt(wallVolM3, 3), 'm³'),
        card('Mortar (wet)', fmt(mortarWet, 3), 'm³'),
        card('Mortar (dry mix)', fmt(mortarDry, 3), 'm³'),
        card('Cement for mortar', whole(cementBags), 'bags of 50 kg'),
        card('Sand for mortar', fmt(sandVol, 3), 'm³'),
        card('Sand for mortar', fmt(sandT, 2), 'tonnes')
      ];

      var p = n(v, 'pricePer1000');
      if (p > 0) cards.push(card('Brick cost', fmt(bricks / 1000 * p, 2), ''));

      return {
        primary: card('Bricks required', whole(bricks), 'bricks'),
        cards: cards,
        note: 'Each brick is counted at its own size plus a ' + fmt(joint, 1) + ' mm mortar joint on every face — that is why the count is lower than dividing the wall volume by the bare brick volume. Mortar is the difference between the wall volume and the volume of the bricks themselves, then increased by 33% for the dry mix you actually order. Breakage allowance is set to ' + fmt(n(v, 'waste'), 1) + '%; raise it to 8–10% for hand-made bricks or long carries across site.'
      };
    }
  };

  /* -------------------- Gravel -------------------- */
  T['gravel-calculator'] = {
    fields: [
      { id: 'shape', label: 'Area shape', type: 'select', def: 'rectangle', options: [
        ['rectangle', 'Rectangle'],
        ['circle', 'Circle'],
        ['triangle', 'Triangle']
      ] },
      { id: 'length', label: 'Length', type: 'number', def: 20, dim: 'length', showIf: function (v) { return v.shape === 'rectangle'; } },
      { id: 'width', label: 'Width', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'rectangle'; } },
      { id: 'diameter', label: 'Diameter', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.shape === 'circle'; } },
      { id: 'tbase', label: 'Base', type: 'number', def: 16, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'theight', label: 'Perpendicular height', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.shape === 'triangle'; } },
      { id: 'depth', label: 'Depth of gravel', type: 'number', def: 3, dim: 'length', unitDef: 'in',
        hint: 'A driveway normally takes 4 in of gravel over a compacted base; a decorative bed takes 2 in.' },
      { id: 'material', label: 'Material', type: 'select', def: '1.68', options: [
        ['1.68', 'Gravel / pea gravel — 1.68 t per m³'],
        ['1.60', 'Crushed stone — 1.60 t per m³'],
        ['1.52', 'River rock — 1.52 t per m³'],
        ['1.45', 'Pea gravel (small, rounded) — 1.45 t per m³'],
        ['1.60', 'Sand — 1.60 t per m³'],
        ['0.35', 'Bark mulch or woodchip — 0.35 t per m³ (very variable)'],
        ['custom', 'Custom density']
      ] },
      { id: 'density', label: 'Custom density', type: 'number', def: 1.6, step: 'any', unitLabel: 't/m³', showIf: function (v) { return v.material === 'custom'; } },
      { id: 'waste', label: 'Wastage allowance', type: 'number', def: 10, unitLabel: '%' },
      { id: 'bagSize', label: 'Bag size for bagged material', type: 'select', def: '25', options: [
        ['25', '25 kg bags'],
        ['50', '50 kg bags'],
        ['40', '40 lb bags'],
        ['60', '60 lb bags'],
        ['0', 'Do not show bags']
      ] },
      { id: 'pricePerTonne', label: 'Price per tonne (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var shape = pick(v, 'shape');
      var area;
      if (shape === 'circle') {
        var r = base(v, 'diameter', 'length') / 2;
        area = Math.PI * r * r;
      } else if (shape === 'triangle') {
        area = 0.5 * base(v, 'tbase', 'length') * base(v, 'theight', 'length');
      } else {
        area = base(v, 'length', 'length') * base(v, 'width', 'length');
      }

      var depthFt = base(v, 'depth', 'length');
      var cft = area * depthFt;
      var cum = cft / VOLUME.cum;
      var waste = n(v, 'waste') / 100;
      var cumWaste = cum * (1 + waste);

      var density = pick(v, 'material') === 'custom' ? (n(v, 'density') || 1.6) : parseFloat(pick(v, 'material'));
      var tonnes = cumWaste * density;

      var cards = [
        card('Area to cover', fmt(area, 2), 'ft²'),
        card('Area to cover', fmt(area / AREA.sqm, 2), 'm²'),
        card('Depth', fmt(depthFt * 12, 1), 'in'),
        card('Cubic yards', fmt(cft / VOLUME.cuyd, 3), 'yd³'),
        card('Cubic metres', fmt(cumWaste, 3), 'm³'),
        card('Cubic feet', fmt(cft * (1 + waste), 2), 'ft³'),
        card('Weight', fmt(tonnes, 2), 'tonnes'),
        card('Weight', fmt(tonnes * 1000 / MASS.ust, 3), 'US tons'),
        card('Weight', fmt(tonnes * 1000, 0), 'kg')
      ];

      var bag = parseFloat(pick(v, 'bagSize'));
      if (bag > 0) {
        var bagKg = bag === 40 || bag === 60 ? bag * 0.45359237 : bag;
        cards.push(card('Bags of ' + bag + (bagKg === bag ? ' kg' : ' lb'), whole(tonnes * 1000 / bagKg), 'bags'));
      }

      var p = n(v, 'pricePerTonne');
      if (p > 0) cards.push(card('Material cost', fmt(tonnes * p, 2), ''));

      return {
        primary: card('Gravel required', fmt(tonnes, 2), 'tonnes'),
        cards: cards,
        table: {
          caption: 'Volume and weight at the selected depth',
          head: ['Measure', 'Value'],
          rows: [
            ['Area', fmt(area, 2) + ' ft² (' + fmt(area / AREA.sqm, 2) + ' m²)'],
            ['Volume (as calculated)', fmt(cum, 3) + ' m³ (' + fmt(cft / VOLUME.cuyd, 3) + ' yd³)'],
            ['Volume with ' + fmt(n(v, 'waste'), 0) + '% wastage', fmt(cumWaste, 3) + ' m³ (' + fmt(cft * (1 + waste) / VOLUME.cuyd, 3) + ' yd³)'],
            ['Density used', fmt(density, 2) + ' t/m³'],
            ['Total weight', fmt(tonnes, 2) + ' tonnes (' + fmt(tonnes * 1000 / MASS.ust, 3) + ' US tons)']
          ]
        },
        note: 'Gravel is sold by volume (cubic yards or cubic metres) in most of the world and by weight (tonnes or tons) elsewhere, so both are shown. The density you pick is what links the two: bulk gravel is around 1.68 t/m³, but it varies with moisture and stone size, so treat the weight as an estimate and confirm with your supplier. Bulk density measures the stone plus the air voids between the pieces, which is why a cubic metre of gravel never weighs as much as a solid cubic metre of rock. Light, loose materials vary most — bark mulch and woodchip run anywhere from 0.25 to 0.4 t/m³ depending on moisture and how finely they are shredded, so for a large order ask the supplier for their own figure rather than trusting any published average.'
      };
    }
  };

  /* -------------------- Tile -------------------- */
  T['tile-calculator'] = {
    fields: [
      { id: 'mode', label: 'How do you want to enter the area?', type: 'select', def: 'dims', options: [
        ['dims', 'Room length × width'],
        ['direct', 'I already know the area']
      ] },
      { id: 'length', label: 'Room length', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.mode === 'dims'; } },
      { id: 'width', label: 'Room width', type: 'number', def: 10, dim: 'length', showIf: function (v) { return v.mode === 'dims'; } },
      { id: 'areaValue', label: 'Area', type: 'number', def: 120, step: 'any', showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'areaUnit', label: 'Area unit', type: 'select', def: 'sqft', options: AREA_UNITS, showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'marla', label: 'Marla standard (for land units)', type: 'select', def: '272.25', options: MARLA_STANDARDS, showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'tileL', label: 'Tile length', type: 'number', def: 600, dim: 'small', unitDef: 'mm' },
      { id: 'tileW', label: 'Tile width', type: 'number', def: 600, dim: 'small', unitDef: 'mm' },
      { id: 'gap', label: 'Grout joint width', type: 'number', def: 3, dim: 'small', unitDef: 'mm',
        hint: 'A 2–3 mm joint for rectified porcelain, 5–10 mm for ceramic wall tiles.' },
      { id: 'waste', label: 'Cutting and breakage allowance', type: 'number', def: 10, unitLabel: '%',
        hint: 'Use 10% for a simple rectangular room, 15% for diagonal layouts or many cuts.' },
      { id: 'perBox', label: 'Tiles per box', type: 'number', def: 4, step: '1' },
      { id: 'pricePerBox', label: 'Price per box (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var std = mStd(v);
      var sqft;
      if (pick(v, 'mode') === 'direct') {
        var u = pick(v, 'areaUnit');
        sqft = u === 'marla' ? n(v, 'areaValue') * std : toSqft(n(v, 'areaValue'), u, std);
      } else {
        sqft = base(v, 'length', 'length') * base(v, 'width', 'length');
      }

      var sqm = sqft / AREA.sqm;
      var tl = n(v, 'tileL') / 1000, tw = n(v, 'tileW') / 1000;
      var gapM = (n(v, 'gap') || 0) / 1000;
      var tileArea = (tl + gapM) * (tw + gapM);      /* tile plus half a joint on each side */
      var tileBare = tl * tw;

      var waste = n(v, 'waste') / 100;
      var tilesNet = tileArea > 0 ? sqm / tileArea : 0;
      var tiles = tilesNet * (1 + waste);
      var perBox = Math.max(1, Math.round(n(v, 'perBox') || 1));
      var boxes = tiles / perBox;

      var cards = [
        card('Total area', fmt(sqft, 2), 'ft²'),
        card('Total area', fmt(sqm, 2), 'm²'),
        card('Tiles without waste', whole(tilesNet), 'tiles'),
        card('Tiles to buy', whole(tiles), 'tiles'),
        card('Boxes to buy', whole(boxes), 'boxes'),
        card('Tile area in a box', fmt(perBox * tileBare * AREA.sqm, 2), 'ft²'),
        card('Tile area in a box', fmt(perBox * tileBare, 3), 'm²'),
        card('Floor a box covers', fmt(perBox * tileArea * AREA.sqm, 2), 'ft²'),
        card('Floor a box covers', fmt(perBox * tileArea, 3), 'm²'),
        card('Tiles per m²', fmt(tileArea > 0 ? 1 / tileArea : 0, 2), 'tiles'),
        card('Tiles per ft²', fmt(tileArea > 0 ? 1 / (tileArea * AREA.sqm) : 0, 3), 'tiles')
      ];

      var p = n(v, 'pricePerBox');
      if (p > 0) {
        cards.push(card('Tile cost', fmt(wholeNum(boxes) * p, 2), ''));
        cards.push(card('Cost per ft²', fmt(sqft > 0 ? wholeNum(boxes) * p / sqft : 0, 3), ''));
      }

      return {
        primary: card('Tiles required', whole(tiles), 'tiles'),
        cards: cards,
        note: 'The tile count uses the tile plus one grout joint on each side, because tiles tile a floor as repeating modules and the joints are part of that pattern. A ' + fmt(n(v, 'tileL'), 0) + ' × ' + fmt(n(v, 'tileW'), 0) +
          ' mm tile with a ' + fmt(n(v, 'gap'), 0) + ' mm joint therefore covers ' + fmt(tileArea, 4) + ' m² of floor. That is why the two coverage figures above differ: the tile area in a box is the number printed on the packaging, while the floor a box covers is slightly larger, since the grout lines are floor too. With large tiles the gap between the two is about 1%; with small mosaics it can exceed 6%. Order whole boxes — the calculator rounds up, and the leftover from the last box is your spare for future repairs.'
      };
    }
  };

  /* -------------------- Paint -------------------- */
  T['paint-calculator'] = {
    fields: [
      { id: 'mode', label: 'How do you want to enter the area?', type: 'select', def: 'room', options: [
        ['room', 'Room dimensions'],
        ['direct', 'I already know the wall area']
      ] },
      { id: 'length', label: 'Room length', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.mode === 'room'; } },
      { id: 'width', label: 'Room width', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.mode === 'room'; } },
      { id: 'height', label: 'Wall height', type: 'number', def: 9, dim: 'length', showIf: function (v) { return v.mode === 'room'; } },
      { id: 'ceiling', label: 'Include the ceiling', type: 'check', def: false, showIf: function (v) { return v.mode === 'room'; } },
      { id: 'directValue', label: 'Wall area to paint', type: 'number', def: 400, step: 'any', showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'directUnit', label: 'Area unit', type: 'select', def: 'sqft', options: [['sqft', 'Square feet (ft²)'], ['sqm', 'Square metres (m²)']], showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'doors', label: 'Number of doors', type: 'number', def: 1, step: '1', showIf: function (v) { return v.mode === 'room'; } },
      { id: 'windows', label: 'Number of windows', type: 'number', def: 2, step: '1', showIf: function (v) { return v.mode === 'room'; } },
      { id: 'coats', label: 'Number of coats', type: 'number', def: 2, step: '1' },
      { id: 'paint', label: 'Paint type', type: 'select', def: '10', options: [
        ['10', 'Interior emulsion — 10 m² per litre'],
        ['14', 'Gloss / enamel trim — 14 m² per litre'],
        ['8', 'Exterior masonry — 8 m² per litre'],
        ['12', 'Primer / sealer — 12 m² per litre']
      ] },
      { id: 'pricePerLitre', label: 'Price per litre (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var sqft, deduction = 0;
      if (pick(v, 'mode') === 'direct') {
        var val = n(v, 'directValue');
        sqft = pick(v, 'directUnit') === 'sqm' ? val * AREA.sqm : val;
      } else {
        var L = base(v, 'length', 'length'), W = base(v, 'width', 'length'), H = base(v, 'height', 'length');
        sqft = 2 * (L + W) * H;
        if (v.ceiling) sqft += L * W;
        /* Standard deductions: 21 ft² (~2 m²) per door, 15 ft² (~1.4 m²) per window. */
        var doors = Math.max(0, Math.round(n(v, 'doors') || 0));
        var windows = Math.max(0, Math.round(n(v, 'windows') || 0));
        deduction = doors * 21 + windows * 15;
        sqft = Math.max(0, sqft - deduction);
      }

      var sqm = sqft / AREA.sqm;
      var coverage = parseFloat(pick(v, 'paint')) || 10;
      var coats = Math.max(1, Math.round(n(v, 'coats') || 1));
      var litresPerCoat = sqm / coverage;
      var litres = litresPerCoat * coats;

      var cards = [
        card('Paintable area', fmt(sqft, 2), 'ft²'),
        card('Paintable area', fmt(sqm, 2), 'm²'),
        card('Coverage rate', fmt(coverage, 1), 'm² per litre'),
        card('Litres per coat', fmt(litresPerCoat, 2), 'L'),
        card('Coats', coats, ''),
        card('4 litre cans', whole(litres / 4), 'cans'),
        card('20 litre drums', whole(litres / 20), 'drums'),
        card('1 US gallon cans (3.785 L)', whole(litres / 3.785411784), 'cans')
      ];

      var p = n(v, 'pricePerLitre');
      if (p > 0) cards.push(card('Paint cost', fmt(litres * p, 2), ''));

      return {
        primary: card('Paint required', fmt(litres, 2), 'litres'),
        cards: cards,
        table: {
          caption: 'Paint required at each coat count',
          head: ['Coats', 'Litres', '4 L cans', '20 L drums'],
          rows: [1, 2, 3].map(function (c) {
            var l = litresPerCoat * c;
            return [c, fmt(l, 2), whole(l / 4), whole(l / 20)];
          })
        },
        note: 'Wall area for a room is the perimeter (2 × (length + width)) multiplied by the wall height' +
          (pick(v, 'mode') === 'room' && v.ceiling ? ', plus the ceiling' : '') +
          (deduction > 0 ? ', minus ' + fmt(deduction, 0) + ' ft² for openings' : '') +
          '. Paint coverage depends on the surface: a porous or unpainted wall drinks far more than a previously painted one, so a primer coat first usually costs less overall. Buy slightly more than the figure above — an exact-match top-up months later rarely matches.'
      };
    }
  };

  /* -------------------- Flooring -------------------- */
  T['flooring-calculator'] = {
    fields: [
      { id: 'mode', label: 'Enter the floor as', type: 'select', def: 'dims', options: [
        ['dims', 'Room length × width'],
        ['direct', 'A known area']
      ] },
      { id: 'length', label: 'Room length', type: 'number', def: 15, dim: 'length', showIf: function (v) { return v.mode === 'dims'; } },
      { id: 'width', label: 'Room width', type: 'number', def: 12, dim: 'length', showIf: function (v) { return v.mode === 'dims'; } },
      { id: 'areaValue', label: 'Area', type: 'number', def: 300, step: 'any', showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'areaUnit', label: 'Area unit', type: 'select', def: 'sqft', options: [['sqft', 'Square feet (ft²)'], ['sqm', 'Square metres (m²)']], showIf: function (v) { return v.mode === 'direct'; } },
      { id: 'type', label: 'Flooring type', type: 'select', def: 'laminate', options: [
        ['laminate', 'Laminate — 2.23 m² (24 ft²) per box'],
        ['vinyl', 'Vinyl plank / LVT — 2.23 m² (24 ft²) per box'],
        ['engineered', 'Engineered wood — 1.86 m² (20 ft²) per box'],
        ['solid', 'Solid hardwood — 1.86 m² (20 ft²) per box'],
        ['cork', 'Cork — 2.0 m² (21.5 ft²) per box'],
        ['custom', 'Custom coverage per box']
      ] },
      { id: 'coverage', label: 'Coverage per box', type: 'number', def: 24, step: 'any', unitLabel: 'ft²', showIf: function (v) { return v.type === 'custom'; } },
      { id: 'waste', label: 'Wastage allowance', type: 'number', def: 10, unitLabel: '%',
        hint: '10% for a straight lay, 15% for a diagonal or herringbone pattern.' },
      { id: 'underlay', label: 'Include underlayment', type: 'check', def: false },
      { id: 'rollCoverage', label: 'Underlayment coverage per roll', type: 'number', def: 100, step: 'any', unitLabel: 'ft²', showIf: function (v) { return v.underlay; } },
      { id: 'pricePerBox', label: 'Price per box (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var sqft;
      if (pick(v, 'mode') === 'direct') {
        var val = n(v, 'areaValue');
        sqft = pick(v, 'areaUnit') === 'sqm' ? val * AREA.sqm : val;
      } else {
        sqft = base(v, 'length', 'length') * base(v, 'width', 'length');
      }
      var sqm = sqft / AREA.sqm;

      var coverSqft = pick(v, 'type') === 'custom'
        ? (n(v, 'coverage') || 24)
        : parseFloat({ laminate: 24, vinyl: 24, engineered: 20, solid: 20, cork: 21.5 }[pick(v, 'type')]);

      var waste = n(v, 'waste') / 100;
      var boxes = sqft * (1 + waste) / coverSqft;

      var cards = [
        card('Floor area', fmt(sqft, 2), 'ft²'),
        card('Floor area', fmt(sqm, 2), 'm²'),
        card('Coverage per box', fmt(coverSqft, 2), 'ft²'),
        card('Boxes needed', whole(boxes), 'boxes'),
        card('Boxes without waste', whole(sqft / coverSqft), 'boxes'),
        card('Total coverage bought', fmt(wholeNum(boxes) * coverSqft, 0), 'ft²')
      ];

      if (v.underlay) {
        var rc = n(v, 'rollCoverage') || 100;
        cards.push(card('Underlayment rolls', whole(sqft / rc), 'rolls'));
        cards.push(card('Roll coverage', fmt(rc, 0), 'ft²'));
      }

      var p = n(v, 'pricePerBox');
      if (p > 0) {
        cards.push(card('Flooring cost', fmt(wholeNum(boxes) * p, 2), ''));
        cards.push(card('Cost per ft²', fmt(sqft > 0 ? wholeNum(boxes) * p / sqft : 0, 3), ''));
      }

      return {
        primary: card('Boxes required', whole(boxes), 'boxes'),
        cards: cards,
        note: 'Flooring is bought by the box, so the calculator rounds the box count up — you cannot buy a part box, and the offcuts from the final box are your spares. ' +
          'Measure each room separately and add the areas rather than measuring the whole house at once, because doors and awkward corners create extra cuts. ' +
          'Leave the boxes flat and unopened in the room for 48 hours before fitting so the planks acclimatise to the room’s humidity.'
      };
    }
  };

  /* -------------------- Roofing -------------------- */
  T['roofing-calculator'] = {
    fields: [
      { id: 'length', label: 'Building length', type: 'number', def: 40, dim: 'length' },
      { id: 'width', label: 'Building width (or span)', type: 'number', def: 24, dim: 'length' },
      { id: 'overhang', label: 'Roof overhang beyond the walls', type: 'number', def: 18, dim: 'length', unitDef: 'in',
        hint: 'Measured at the eaves and the gable ends. 12–24 in is typical.' },
      { id: 'shape', label: 'Roof type', type: 'select', def: 'gable', options: [
        ['gable', 'Gable — two sloping planes'],
        ['hip', 'Hip — slopes on all four sides'],
        ['shed', 'Shed / mono-pitch — one plane'],
        ['flat', 'Flat or low-slope']
      ] },
      { id: 'pitch', label: 'Roof pitch (rise over 12 in run)', type: 'number', def: 6, step: 'any',
        hint: 'A 6/12 pitch rises 6 inches for every 12 inches of horizontal run — about 26.6°.' },
      { id: 'material', label: 'Roof covering', type: 'select', def: 'shingle', options: [
        ['shingle', 'Asphalt shingles — 3 bundles per square'],
        ['metal', 'Standing seam metal — 36 in panels'],
        ['tile', 'Clay or concrete tiles'],
        ['membrane', 'Flat membrane — EPDM / TPO']
      ] },
      { id: 'rollSquares', label: 'Roll coverage (roof squares)', type: 'number', def: 10, step: 'any',
        showIf: function (v) { return v.material === 'shingle' || v.material === 'membrane'; },
        hint: '1 square = 100 ft². A 10 × 100 ft roll is 10 squares; a 3 × 50 ft roll is 1.5 squares. Check the roll you are buying — coverage varies.' },
      { id: 'waste', label: 'Wastage allowance', type: 'number', def: 10, unitLabel: '%' },
      { id: 'pricePerSquare', label: 'Price per roof square (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var L = base(v, 'length', 'length'), W = base(v, 'width', 'length');
      var oh = base(v, 'overhang', 'length');
      var eL = L + 2 * oh, eW = W + 2 * oh;
      var footprint = eL * eW;

      var sh = pick(v, 'shape');
      var pitch = n(v, 'pitch');
      var factor = sh === 'flat' ? 1 : Math.sqrt(1 + Math.pow(pitch / 12, 2));
      var angle = sh === 'flat' ? 0 : Math.atan(pitch / 12) * 180 / Math.PI;

      var roofSqft = footprint * factor;
      var waste = n(v, 'waste') / 100;
      var squares = roofSqft / 100;
      var squaresWaste = squares * (1 + waste);

      var cards = [
        card('Roof area', fmt(roofSqft, 0), 'ft²'),
        card('Roof area', fmt(roofSqft / AREA.sqm, 2), 'm²'),
        card('Roof squares', fmt(squares, 2), 'sq'),
        card('Footprint covered', fmt(footprint, 0), 'ft²'),
        card('Pitch factor', fmt(factor, 4), '×'),
        card('Roof angle', fmt(angle, 1), '°'),
        card('With ' + fmt(n(v, 'waste'), 0) + '% waste', fmt(squaresWaste, 2), 'squares')
      ];

      var mat = pick(v, 'material');
      var rollSq = Math.max(0.01, n(v, 'rollSquares') || 10);
      var rollSqft = rollSq * 100;
      var detail = '';
      if (mat === 'shingle') {
        var bundles = squaresWaste * 3;
        cards.push(card('Shingle bundles', whole(bundles), 'bundles'));
        cards.push(card('Underlayment rolls', whole(squaresWaste / rollSq), 'rolls of ' + fmt(rollSqft, 0) + ' ft²'));
        detail = 'Shingles are sold in bundles: three bundles cover one 10 ft × 10 ft square, the unit roofers quote everything in. Underlayment is shown in rolls covering ' + fmt(rollSqft, 0) + ' ft² each — change that figure if your roll is a different size, because these vary more than shingles do. Add starter strip along the eaves (the building length plus both overhangs) and ridge cap along the ridge and hips.';
      } else if (mat === 'metal') {
        if (sh === 'hip') {
          /* A hip roof has four planes, two of them triangular, so its
             panels are cut and tapered. A whole-panel count would be
             fiction; the area to order is the honest figure. */
          cards.push(card('Roof area to order', fmt(roofSqft * (1 + waste), 0), 'ft²'));
          cards.push(card('Roof area to order', fmt(roofSqft * (1 + waste) / AREA.sqm, 2), 'm²'));
          detail = 'A hip roof has four planes — two trapezoids and two triangles — so its metal panels are cut and tapered rather than rectangular. A whole-panel count would not be meaningful, so the area to order is given instead. Give your supplier the roof plan and they will detail the panels and their cut lengths. Add the ridge cap, hip flashings and eave closure strips separately.';
        } else {
          /* Panels run up the slope, so the panel length is the sloping
             distance from eave to ridge and the panel count is driven by
             how long the ridge is. */
          var slopes = sh === 'gable' ? 2 : 1;
          var slopeRun = sh === 'gable' ? eW / 2 : eW;
          var panelLen = slopeRun * factor;
          var panelsPerSlope = Math.ceil(eL / 3);
          cards.push(card('Panels, 36 in wide', whole(panelsPerSlope * slopes), 'panels'));
          cards.push(card('Panel length (cut to length)', fmt(panelLen, 2), 'ft'));
          cards.push(card('Total panel linear ft', fmt(panelsPerSlope * slopes * panelLen, 1), 'ft'));
          detail = 'Metal panels run from eave to ridge, so their length is the sloping distance (' + fmt(panelLen, 2) + ' ft under these dimensions), not the building width. Order them cut to length to avoid end laps, and allow for the ridge cap, eave closure strips and the fasteners at roughly 8 per square metre.';
        }
      } else if (mat === 'tile') {
        cards.push(card('Tiles per m²', 10, 'tiles'));
        cards.push(card('Tiles needed', whole((roofSqft / AREA.sqm) * 10 * (1 + waste)), 'tiles'));
        detail = 'Clay and concrete tiles run about 10 tiles per square metre, but the exact figure depends on the tile profile and headlap — check the manufacturer’s coverage chart and always add a few percent for breakage, as tiles are heavy and brittle.';
      } else {
        cards.push(card('Membrane rolls', whole(squaresWaste / rollSq), 'rolls of ' + fmt(rollSqft, 0) + ' ft²'));
        detail = 'For flat roofs the area is the footprint, with no pitch factor, because the membrane lies flat rather than following a slope. The rolls shown cover ' + fmt(rollSqft, 0) + ' ft² each; lapping at the seams reduces effective coverage, which the wastage allowance above is there to absorb.';
      }

      var ridge = 0, hips = 0;
      if (sh === 'gable') {
        /* The ridge of a gable roof runs along the building's length,
           not across its span — the slopes fall to the two long eaves. */
        ridge = eL;
      } else if (sh === 'hip') {
        var mn = Math.min(eL, eW);
        ridge = Math.abs(eL - eW);
        /* A hip is a sloping line in three dimensions, so the plan-view
           diagonal has to be multiplied by the pitch factor to give the
           true length of flashing the roofer has to order. */
        hips = 4 * Math.sqrt(2 * Math.pow(mn / 2, 2)) * factor;
      }
      if (ridge + hips > 0) cards.push(card('Ridge + hip length', fmt(ridge + hips, 2), 'ft'));

      var p = n(v, 'pricePerSquare');
      if (p > 0) cards.push(card('Roofing cost', fmt(squaresWaste * p, 2), ''));

      return {
        primary: card('Roof surface area', fmt(roofSqft, 0), 'ft²'),
        cards: cards,
        note: detail + ' The pitch factor converts the flat footprint you measured on the ground into the sloped surface the materials actually cover: at ' +
          fmt(pitch, 1) + '/12 the factor is ' + fmt(factor, 3) + ', so a roof that looks like ' + fmt(footprint, 0) +
          ' ft² from above is really ' + fmt(roofSqft, 0) + ' ft² of material. ' +
          'For a hip or gable roof the overhang is added on all four sides, which is why the footprint here is larger than the building itself.'
      };
    }
  };

  /* -------------------- Fence -------------------- */
  T['fence-calculator'] = {
    fields: [
      { id: 'length', label: 'Total fence run', type: 'number', def: 100, dim: 'length' },
      { id: 'height', label: 'Fence height', type: 'number', def: 6, dim: 'length' },
      { id: 'type', label: 'Fence type', type: 'select', def: 'panel', options: [
        ['panel', 'Pre-made panels between posts'],
        ['picket', 'Picket fence'],
        ['rail', 'Post and rail (rural style)'],
        ['chainlink', 'Chain link with line posts']
      ] },
      { id: 'spacing', label: 'Post spacing', type: 'number', def: 8, dim: 'length',
        hint: 'Most timber and panel fences use 8 ft bays; chain link often uses 10 ft.' },
      { id: 'rails', label: 'Rails per bay', type: 'number', def: 2, step: '1' },
      { id: 'picketW', label: 'Picket width', type: 'number', def: 4, dim: 'length', unitDef: 'in', showIf: function (v) { return v.type === 'picket'; } },
      { id: 'picketGap', label: 'Gap between pickets', type: 'number', def: 2, dim: 'length', unitDef: 'in', showIf: function (v) { return v.type === 'picket'; } },
      { id: 'holeDia', label: 'Post hole diameter', type: 'number', def: 12, dim: 'length', unitDef: 'in' },
      { id: 'holeDepth', label: 'Post hole depth', type: 'number', def: 24, dim: 'length', unitDef: 'in',
        hint: 'A common rule is one third of the post length in the ground, below the frost line.' },
      { id: 'postSize', label: 'Post cross-section', type: 'number', def: 4, dim: 'length', unitDef: 'in' },
      { id: 'bagYield', label: 'Concrete per bag', type: 'number', def: 0.011, step: 'any', unitLabel: 'm³',
        hint: 'A 25 kg bag of post-mix yields roughly 0.011 m³ (about 2 bags per post).' },
      { id: 'pricePerPanel', label: 'Price per panel or bay (optional)', type: 'number', def: 0, step: 'any' }
    ],
    compute: function (v) {
      var run = base(v, 'length', 'length');
      var spacing = base(v, 'spacing', 'length');
      var posts = spacing > 0 ? Math.ceil(run / spacing) + 1 : 1;
      var bays = posts - 1;
      var railsPerBay = Math.max(0, Math.round(n(v, 'rails') || 0));
      /* Rails run the full length of the fence, not bays × spacing. On a run
         that does not divide evenly by the spacing the last bay is shorter,
         so bays × spacing overshoots — 100 ft at 8 ft gives 13 bays and
         104 ft of rail per line, when only 100 ft exists. */
      var railLinear = run * railsPerBay;

      var cards = [
        card('Fence run', fmt(run, 2), 'ft'),
        card('Fence run', fmt(run / 3.280839895013123, 2), 'm'),
        card('Posts', posts, 'posts'),
        card('Bays / panels', bays, 'bays'),
        card('Rails', fmt(railLinear, 2), 'linear ft')
      ];

      if (pick(v, 'type') === 'picket') {
        /* n pickets with n−1 gaps between them occupy n × w + (n−1) × g, so
           n = (run + g) / (w + g). Dividing by (w + g) alone drops the final
           picket on any run that does not fit an exact number. */
        var step = base(v, 'picketW', 'length') + base(v, 'picketGap', 'length');
        var gap = base(v, 'picketGap', 'length');
        var pickets = step > 0 ? Math.ceil((run + gap) / step) : 0;
        cards.push(card('Pickets', pickets, 'pickets'));
        cards.push(card('Pickets per ft', fmt(step > 0 ? 1 / step : 0, 2), 'per ft'));
      } else if (pick(v, 'type') === 'chainlink') {
        cards.push(card('Fabric rolls (50 ft)', whole(run / 50), 'rolls'));
        cards.push(card('Tension wire', fmt(run * 2, 2), 'linear ft'));
      } else {
        cards.push(card('Panels needed', bays, 'panels'));
      }

      /* The hole and post are measured in feet, so the difference is a
         volume in cubic feet — it has to be converted before it can be
         compared with a bag yield quoted in cubic metres. */
      var holeR = base(v, 'holeDia', 'length') / 2;
      var holeD = base(v, 'holeDepth', 'length');
      var postSide = base(v, 'postSize', 'length');
      var perPostCft = Math.max(0, Math.PI * holeR * holeR * holeD - postSide * postSide * holeD);
      var perPost = perPostCft / VOLUME.cum;
      var totalConcrete = perPost * posts;
      var bagYield = n(v, 'bagYield') || 0.011;
      cards.push(card('Concrete per post', fmt(perPost, 4), 'm³'));
      cards.push(card('Total concrete', fmt(totalConcrete, 3), 'm³'));
      cards.push(card('Bags of post-mix', whole(totalConcrete / bagYield), 'bags'));

      var p = n(v, 'pricePerPanel');
      if (p > 0) cards.push(card('Estimated material cost', fmt(bays * p, 2), ''));

      var hFt = base(v, 'height', 'length');
      cards.push(card('Fence height', fmt(hFt, 2), 'ft'));
      cards.push(card('Total fence area', fmt(run * hFt, 1), 'ft²'));

      return {
        primary: card('Posts required', posts, 'posts'),
        cards: cards,
        table: {
          caption: 'Cutting list',
          head: ['Item', 'Quantity', 'Notes'],
          rows: [
            ['Posts', posts, 'one more than the number of bays'],
            ['Bays', bays, 'each ' + fmt(spacing, 2) + ' ft wide'],
            ['Rails', fmt(railLinear, 2) + ' linear ft', railsPerBay + ' per bay'],
            ['Concrete', fmt(totalConcrete, 3) + ' m³', whole(totalConcrete / bagYield) + ' bags at ' + fmt(bagYield, 4) + ' m³ each'],
            ['Fence area', fmt(run * hFt, 1) + ' ft²', 'for stain or paint']
          ]
        },
        note: 'Post count is the fence run divided by the spacing, rounded up, plus the final post at the far end — so a 100 ft run at 8 ft centres gives 14 posts and 13 bays. ' +
          'Set the posts in concrete rather than tamping soil around them: the hole should be about three times the post width and deep enough to sit below the frost line, with the concrete sloping away from the post at the top so water runs off. ' +
          'Saw the posts after the concrete has cured, not before, so the tops line up.'
      };
    }
  };

  /* ============================================================
     ENGINE — builds the form, reads values, renders results
     ============================================================ */

  function el(tag, cls, html) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html !== undefined) e.innerHTML = html;
    return e;
  }

  function fieldHtml(f) {
    var wrap = el('div', 'calc-field');
    wrap.setAttribute('data-field', f.id);
    if (f.showIf) wrap.setAttribute('data-showif', f.id);

    if (f.type === 'check') {
      wrap.className = 'calc-field';
      var lab = el('label', 'calc-check');
      var cb = el('input');
      cb.type = 'checkbox';
      cb.id = 'f-' + f.id;
      cb.checked = !!f.def;
      lab.appendChild(cb);
      lab.appendChild(el('span', null, f.label));
      wrap.appendChild(lab);
    } else {
      wrap.appendChild(el('label', null, f.label));
      if (f.type === 'select') {
        var sel = el('select', 'calc-select');
        sel.id = 'f-' + f.id;
        f.options.forEach(function (o) {
          var opt = el('option', null, o[1]);
          opt.value = o[0];
          if (String(o[0]) === String(f.def)) opt.selected = true;
          sel.appendChild(opt);
        });
        wrap.appendChild(sel);
      } else {
        var group = el('div', 'calc-input-group');
        var inp = el('input');
        inp.type = 'number';
        inp.id = 'f-' + f.id;
        inp.value = f.def;
        inp.step = f.step || 'any';
        inp.setAttribute('inputmode', 'decimal');
        /* Floor every numeric field at zero unless a tool asks otherwise.
           The clamp in n() is what actually protects the maths; this is the
           visible affordance that stops the browser's spinner going below it. */
        inp.min = f.min !== undefined ? f.min : 0;
        group.appendChild(inp);

        if (f.dim) {
          var d = DIM[f.dim];
          var us = el('select');
          us.id = 'f-' + f.id + '__unit';
          d.units.forEach(function (u) {
            var o = el('option', null, u[1]);
            o.value = u[0];
            if (u[0] === (f.unitDef || d.def)) o.selected = true;
            us.appendChild(o);
          });
          group.appendChild(us);
        } else if (f.unitLabel) {
          group.appendChild(el('span', 'calc-unit-suffix', f.unitLabel));
        }
        wrap.appendChild(group);
      }
    }

    if (f.hint) wrap.appendChild(el('div', 'calc-hint', f.hint));
    return wrap;
  }

  function slotHtml(slot) {
    if (!slot) return '';
    return slot.value + (slot.unit ? '<span class="rc-unit">' + slot.unit + '</span>' : '');
  }

  function readValues(form, fields) {
    var v = {};
    fields.forEach(function (f) {
      var e = form.querySelector('#f-' + f.id);
      if (!e) return;
      v[f.id] = f.type === 'check' ? e.checked : e.value;
      if (f.dim) {
        var u = form.querySelector('#f-' + f.id + '__unit');
        if (u) v[f.id + '__unit'] = u.value;
      }
    });
    return v;
  }

  function render(out, res) {
    var html = '';
    if (res.primary) {
      html += '<div class="result-cards"><div class="result-card is-primary">' +
        '<span class="rc-label">' + res.primary.label + '</span>' +
        '<span class="rc-value">' + slotHtml(res.primary) + '</span></div></div>';
    }
    if (res.cards && res.cards.length) {
      html += '<div class="result-cards">';
      res.cards.forEach(function (c) {
        html += '<div class="result-card"><span class="rc-label">' + c.label + '</span>' +
          '<span class="rc-value">' + slotHtml(c) + '</span></div>';
      });
      html += '</div>';
    }
    if (res.table) {
      html += '<div class="table-scroll"><table class="data-table">' +
        (res.table.caption ? '<caption>' + res.table.caption + '</caption>' : '') +
        '<thead><tr>' + res.table.head.map(function (h) { return '<th>' + h + '</th>'; }).join('') + '</tr></thead>' +
        '<tbody>' + res.table.rows.map(function (r) {
          return '<tr>' + r.map(function (c, i) { return i === 0 ? '<td><strong>' + c + '</strong></td>' : '<td>' + c + '</td>'; }).join('') + '</tr>';
        }).join('') + '</tbody></table></div>';
    }
    if (res.note) html += '<p class="calc-note">' + res.note + '</p>';
    out.innerHTML = html;
  }

  function update(form, out, tool) {
    var wrappers = form.querySelectorAll('[data-field]');
    var provisional = {};
    tool.fields.forEach(function (f) {
      var e = form.querySelector('#f-' + f.id);
      if (!e) return;
      provisional[f.id] = f.type === 'check' ? e.checked : e.value;
    });

    /* Hide conditional fields, then recompute with whatever is visible. */
    wrappers.forEach(function (w) {
      var id = w.getAttribute('data-field');
      var spec = null;
      tool.fields.forEach(function (f) { if (f.id === id) spec = f; });
      if (spec && spec.showIf) {
        w.style.display = spec.showIf(provisional) ? '' : 'none';
      }
    });

    var v = readValues(form, tool.fields);
    try {
      render(out, tool.compute(v));
    } catch (err) {
      out.innerHTML = '<p class="calc-note">Check your inputs — one of the values could not be calculated.</p>';
    }
  }

  function init(toolId) {
    function boot() {
      var tool = T[toolId];
      var form = document.getElementById('calc-form');
      var out = document.getElementById('calc-output');
      if (!tool || !form || !out) return;

      tool.fields.forEach(function (f) { form.appendChild(fieldHtml(f)); });

      var actions = el('div', 'calc-actions');
      var reset = el('button', 'btn btn-outline', 'Reset values');
      reset.type = 'button';
      reset.addEventListener('click', function () {
        tool.fields.forEach(function (f) {
          var e = form.querySelector('#f-' + f.id);
          if (!e) return;
          if (f.type === 'check') e.checked = !!f.def;
          else e.value = f.def;
          if (f.dim) {
            var u = form.querySelector('#f-' + f.id + '__unit');
            if (u) u.value = f.unitDef || DIM[f.dim].def;
          }
        });
        update(form, out, tool);
      });
      actions.appendChild(reset);
      form.appendChild(actions);

      form.addEventListener('input', function () { update(form, out, tool); });
      form.addEventListener('change', function () { update(form, out, tool); });
      /* A number input inside a <form> submits on Enter, which would reload
         the page and lose the visitor's figures. */
      form.addEventListener('submit', function (e) { e.preventDefault(); });

      update(form, out, tool);
    }

    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
    else boot();
  }

  window.AlsadatTools = { init: init, tools: T, units: { LENGTH: LENGTH, AREA: AREA, VOLUME: VOLUME, MASS: MASS } };
})();
