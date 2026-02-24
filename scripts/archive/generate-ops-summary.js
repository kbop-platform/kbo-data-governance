const fs = require('fs');
const data = JSON.parse(fs.readFileSync('//wsl.localhost/Ubuntu/home/user/dev/data-dict/raw/ops-schema.json', 'utf-8'));

// Filter out "NN" and empty entries from columns
function getRealColumns(columns) {
  return columns.filter(c =>
    c.physical_name &&
    c.physical_name !== 'NN' &&
    c.physical_name.trim() !== '' &&
    c.data_type !== ''
  );
}

// Group by category
const cats = {};
let totalColCount = 0;
data.forEach(t => {
  const cat = t.category || 'UNKNOWN';
  if (!(cat in cats)) cats[cat] = [];
  const cols = getRealColumns(t.columns || []);
  totalColCount += cols.length;
  cats[cat].push({
    physical_name: t.physical_name,
    logical_name: t.logical_name,
    primary_key: t.primary_key || 'N/A',
    detail: t.detail || '',
    columns: cols.map(c => {
      let typeStr = c.data_type;
      if (c.length) typeStr += '(' + c.length + ')';
      return { name: c.physical_name, type: typeStr, nullable: c.nullable };
    }),
    col_count: cols.length
  });
});

// Output summary
const lines = [];
lines.push('# OPS Schema Summary (ops-schema.json)');
lines.push('');
lines.push('## Overview');
lines.push('');
lines.push('| Category | Tables | Description |');
lines.push('|----------|--------|-------------|');

const catOrder = ['MASTER', 'RECORD', 'LIVE', 'ALARM', 'APPROVAL', 'MONITORING', 'OFFICAL', 'USER', '업무관련', 'UNKNOWN'];
const catDesc = {
  'MASTER': '마스터 데이터 (코드, 선수, 팀, 구장, 경기 등)',
  'RECORD': '기록 데이터 (경기 결과, 선수/팀 성적)',
  'LIVE': '실시간 경기 데이터 (문자중계, 매트릭스, 라인업)',
  'ALARM': '알람 수신 관리',
  'APPROVAL': '승인 요청/처리 (선수 등록, 트레이드, FA 등)',
  'MONITORING': '모니터링 (경기영상, 행동강령, 코로나, 부정행위 등)',
  'OFFICAL': '공시업무 (주소록, 서명, 알람 등)',
  'USER': '사용자 관리',
  '업무관련': '업무 관련 (구단 문의, 자료실, 일반요청)',
  'UNKNOWN': '미분류 (원본에 category 없음)'
};

const sortedCats = Object.keys(cats).sort((a, b) => {
  const ai = catOrder.indexOf(a);
  const bi = catOrder.indexOf(b);
  return (ai === -1 ? 999 : ai) - (bi === -1 ? 999 : bi);
});

sortedCats.forEach(cat => {
  lines.push('| ' + cat + ' | ' + cats[cat].length + ' | ' + (catDesc[cat] || '') + ' |');
});
lines.push('| **TOTAL** | **' + data.length + '** | **총 ' + totalColCount + '개 컬럼** |');
lines.push('');

// Detailed listing
sortedCats.forEach(cat => {
  lines.push('---');
  lines.push('');
  lines.push('## ' + cat + ' (' + cats[cat].length + ' tables)');
  lines.push('');

  cats[cat].sort((a, b) => a.physical_name.localeCompare(b.physical_name)).forEach(t => {
    lines.push('### ' + t.physical_name);
    lines.push('- **논리명**: ' + t.logical_name);
    lines.push('- **PK**: `' + t.primary_key + '`');
    if (t.detail) {
      lines.push('- **비고**: ' + t.detail);
    }
    lines.push('- **컬럼 수**: ' + t.col_count);
    lines.push('');
    lines.push('| Column | Type |');
    lines.push('|--------|------|');
    t.columns.forEach(c => {
      const nn = c.nullable === 'NN' ? ' `NN`' : '';
      lines.push('| ' + c.name + ' | ' + c.type + nn + ' |');
    });
    lines.push('');
  });
});

const output = lines.join('\n');
fs.writeFileSync('//wsl.localhost/Ubuntu/home/user/dev/data-dict/analysis/ops-schema-summary.md', output, 'utf-8');
console.log('Written to analysis/ops-schema-summary.md');
console.log('Total tables:', data.length);
console.log('Total columns:', totalColCount);
console.log('Categories:', sortedCats.join(', '));
