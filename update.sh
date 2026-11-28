commit_if_changed() {
    git diff --cached --quiet || git commit -m "$1"
}

python prepare_webhooks.py

python fetch_mappings_for_today.py

git add data/page_mappings.json
commit_if_changed "🐛 Update page mappings"

git add data/sandbox_ids.json
commit_if_changed "🤖 Update tracked sandbox IDs"

python fetch_data_for_today.py

python monitor_fixed_trophies.py

git add data/20*/*
commit_if_changed "🗃️ Add JSON data snapshot"

git add docs/by_*.md
commit_if_changed "📄 Update Markdown docs"

git push
