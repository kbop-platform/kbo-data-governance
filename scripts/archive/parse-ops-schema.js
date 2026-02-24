const fs = require('fs');
const data = JSON.parse(fs.readFileSync('//wsl.localhost/Ubuntu/home/user/dev/data-dict/raw/ops-schema.json', 'utf-8'));

console.log('Total tables:', data.length);
console.log('');

// Group by category
const cats = {};
data.forEach(t => {
  const cat = t.category || 'UNKNOWN';
  if (!(cat in cats)) cats[cat] = [];
  cats[cat].push(t);
});

// Filter out "NN" and empty physical_name entries from columns
function getRealColumns(columns) {
  return columns.filter(c =>
    c.physical_name &&
    c.physical_name !== 'NN' &&
    c.physical_name.trim() !== '' &&
    c.data_type !== ''
  );
}

Object.keys(cats).sort().forEach(cat => {
  console.log('='.repeat(80));
  console.log('CATEGORY:', cat, '(' + cats[cat].length + ' tables)');
  console.log('='.repeat(80));

  cats[cat].sort((a, b) => a.physical_name.localeCompare(b.physical_name)).forEach(t => {
    console.log('');
    console.log('--- ' + t.physical_name + ' ---');
    console.log('  Logical Name: ' + t.logical_name);
    console.log('  Primary Key: ' + (t.primary_key || 'N/A'));
    console.log('  Detail: ' + (t.detail || ''));

    const cols = getRealColumns(t.columns || []);
    console.log('  Columns (' + cols.length + '):');
    cols.forEach(c => {
      let typeStr = c.data_type;
      if (c.length) typeStr += '(' + c.length + ')';
      const nullable = c.nullable === 'NN' ? ' NOT NULL' : '';
      const def = c.default ? ' DEFAULT ' + c.default : '';
      console.log('    ' + c.physical_name + ' : ' + typeStr + nullable + def);
    });
  });
  console.log('');
});
