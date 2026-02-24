#!/bin/bash
# MkDocs 로컬 서버 실행 (심볼릭 링크 자동 생성)

set -e
cd "$(dirname "$0")"

mkdir -p docs

ln -sfn ../dictionary docs/dictionary
ln -sfn ../standards docs/standards
ln -sfn ../glossary docs/glossary
ln -sfn ../governance docs/governance
ln -sfn ../analysis docs/analysis
ln -sfn ../assets docs/assets
ln -sf ../README.md docs/index.md
ln -sf ../project-guide.md docs/project-guide.md

echo "http://127.0.0.1:8000"
python3 -m mkdocs serve
