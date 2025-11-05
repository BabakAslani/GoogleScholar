from scholarly import scholarly
import json
from datetime import datetime, timezone

# Replace with your Google Scholar ID
author_id = "s60m-LwAAAAJ"

# Fetch author profile
author = scholarly.search_author_id(author_id)
author = scholarly.fill(author)

# Extract overall stats
total_citations = author['citedby']
h_index = author['hindex']
i10_index = author.get('i10index', 0)
cites_per_year = author.get('cites_per_year', {})  # dictionary

# Compute "Since 2020" stats
papers = author.get('publications', [])
citations_since_2020_list = []

for p in papers:
    paper_filled = scholarly.fill(p)
    cites_yearly = paper_filled.get('cites_per_year', {})
    # Sum citations from 2020 onward
    c20 = sum(count for year, count in cites_yearly.items() if int(year) >= 2020)
    citations_since_2020_list.append(c20)

# Compute h-index since 2020
sorted_cites = sorted(citations_since_2020_list, reverse=True)
h_index_since_2020 = 0
for i, c in enumerate(sorted_cites):
    if c >= i + 1:
        h_index_since_2020 = i + 1
    else:
        break

# Compute i10-index since 2020
i10_index_since_2020 = sum(1 for c in citations_since_2020_list if c >= 10)

# Add last updated timestamp (timezone-aware UTC)
stats = {
    "total_citations": total_citations,
    "h_index": h_index,
    "i10_index": i10_index,
    "citations_per_year": cites_per_year,
    "h_index_recent": h_index_since_2020,
    "i10_index_recent": i10_index_since_2020,
    "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
}

# Save to JSON
with open("scholar_stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print("Updated scholar_stats.json successfully.")
