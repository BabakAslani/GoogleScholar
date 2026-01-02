from scholarly import scholarly
import json
from datetime import datetime, timezone

author_id = "s60m-LwAAAAJ"

# Fetch profile
author = scholarly.search_author_id(author_id)
author = scholarly.fill(author)

# Overall stats
total_citations = author['citedby']
h_index = author['hindex']
i10_index = author.get('i10index', 0)
cites_per_year = author.get('cites_per_year', {})

# --- Automatic recent window (last 5 years including current) ---
current_year = datetime.now().year
recent_start_year = current_year - 5  # 2026 → 2021, 2027 → 2022, 2028 → 2023, ...

# Collect recent citations per paper
papers = author.get('publications', [])
citations_recent = []

for p in papers:
    pf = scholarly.fill(p)
    cpy = pf.get('cites_per_year', {})
    c_recent = sum(count for year, count in cpy.items() if int(year) >= recent_start_year)
    citations_recent.append(c_recent)

# Compute recent h-index
sorted_cites = sorted(citations_recent, reverse=True)
h_index_recent = 0
for i, c in enumerate(sorted_cites):
    if c >= i + 1:
        h_index_recent = i + 1
    else:
        break

# Compute recent i10-index
i10_index_recent = sum(1 for c in citations_recent if c >= 10)

# Build JSON stats
stats = {
    "total_citations": total_citations,
    "h_index": h_index,
    "i10_index": i10_index,
    "citations_per_year": cites_per_year,
    "h_index_recent": h_index_recent,
    "i10_index_recent": i10_index_recent,
    "recent_start_year": recent_start_year,
    "current_year": current_year,
    "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
}

# Save to JSON
with open("scholar_stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print("Updated scholar_stats.json successfully.")
