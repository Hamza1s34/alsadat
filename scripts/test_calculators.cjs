const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const context = { window: {} };
vm.runInNewContext(fs.readFileSync(path.join(__dirname, '../js/tools.js'), 'utf8'), context);
const tools = context.window.AlsadatTools.tools;

function calculate(slug, overrides = {}) {
  const values = {};
  for (const field of tools[slug].fields) {
    values[field.id] = field.def;
    if (field.dim && field.unitDef) values[field.id + '__unit'] = field.unitDef;
  }
  return tools[slug].compute({ ...values, ...overrides });
}
const number = value => Number(String(value).replaceAll(',', ''));
const close = (actual, expected, tolerance) => assert.ok(Math.abs(actual - expected) <= tolerance, `${actual} versus ${expected}`);
const card = (result, label) => number(result.cards.find(c => c.label === label).value);

for (const slug of Object.keys(tools)) {
  const result = calculate(slug);
  assert.ok(result.primary, slug);
  assert.ok(!/NaN|Infinity/.test(JSON.stringify(result)), slug);
}

// Known international area conversion and the inverse.
close(number(calculate('square-meters-to-square-feet', { value: 200 }).primary.value), 2152.782083, 0.01);
close(number(calculate('square-feet-to-square-meters', { value: 2152.782083 }).primary.value), 200, 0.001);

// Every advertised order volume includes the same 10% allowance.
const gravel = calculate('gravel-calculator');
close(card(gravel, 'Cubic yards'), 2.037037, 0.001);
close(card(gravel, 'Cubic metres'), 1.55742656, 0.001);
close(card(gravel, 'Cubic feet'), 55, 0.001);
close(card(gravel, 'Weight'), 2.61647662, 0.01);

// Manufacturer-specific coverage changes quantity; zero coverage is invalid.
const paint = { mode: 'direct', directValue: 100, directUnit: 'sqm', paint: 'custom', coverage: 8.5, coats: 2 };
close(number(calculate('paint-calculator', paint).primary.value), 23.529411, 0.01);
close(number(calculate('paint-calculator', { ...paint, coats: 3 }).primary.value), 35.294118, 0.01);
assert.equal(calculate('paint-calculator', { ...paint, coverage: 0 }).primary.value, '—');
assert.equal(number(calculate('paint-calculator', { ...paint, directValue: 0 }).primary.value), 0);

for (const standard of [225, 250, 272.25]) {
  const result = calculate('marla-to-square-feet', { value: 20, marla: String(standard) });
  close(number(result.primary.value), standard * 20, 0.01);
  close(card(result, 'Kanal (20 marla)'), 1, 0.001);
}
console.log(`PASS: ${Object.keys(tools).length} calculator smoke checks; conversion, gravel allowance, paint coverage and land-unit regressions`);
