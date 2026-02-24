import json
d = json.load(open('/home/user/dev/data-dict/raw/column-metadata.json'))
print(f"Tables extracted: {len(d['tables'])}")
for k, v in sorted(d['tables'].items()):
    pk = ','.join(v['pk_columns'])
    print(f"  {k:40s} {v['column_count']:3d}cols  PK={pk:40s}  {v['schema_generation']}")
