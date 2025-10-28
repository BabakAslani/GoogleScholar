from scholarly import scholarly
import json
from datetime import datetime

# Replace with your Google Scholar ID
author_id = "s60m-LwAAAAJ"

author = scholarly.search_author_id(author_id)
author = scholarly.fill(author)

# Extract stats
total_citations = author['citedby']
h_index = author['hindex']
i10_index = author.get('i10index', 0)  # fallback to 0 if not present
cites_per_year = author.get('cites_per_year', {})  # dictionary

# Add last updated timestamp
stats = {
    "total_citations": total_citations,
    "h_index": h_index,
    "i10_index": i10_index,
    "citations_per_year": cites_per_year,
    "last_updated": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
}

# Save to JSON
with open("scholar_stats.json", "w") as f:
    json.dump(stats, f, indent=4)

print("Updated scholar_stats.json successfully.")
