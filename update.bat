python fetch_mappings_for_today.py

:: https://stackoverflow.com/a/72000317/376454
chcp 65001>nul

git add data/page_mappings.json
git commit -m "💼 Update page mappings"

git add data/sandbox_ids.json
git commit -m "Data: updated sandbox IDs"

python fetch_data_for_today.py

git add data/20*/*
git commit -m "🗃️ Add JSON data snapshot"

git add docs/by_*.md
git commit -m "📄 Update Markdown docs"

git push
