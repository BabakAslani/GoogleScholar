from scholarly import scholarly
import json
from collections import defaultdict

SCHOLAR_ID = "s60m-LwAAAAJ"

# Fetch author
author = scholarly.search_author_id(SCHOLAR_ID)
author = scholarly.fill(author, sections=['publications', 'indices'])

# Total citations and h-index
total_citations = author.get('citedby', 0)
h_index = author.get('hindex', 0)

# Compute citations per year
citations_per_year = defaultdict(int)

for pub in author.get('publications', []):
    pub_filled = scholarly.fill(pub)
    if 'cites_per_year' in pub_filled:
        for year, count in pub_filled['cites_per_year'].items():
            citations_per_year[year] += count

# Convert defaultdict to normal dict and sort
citations_per_year = dict(sorted(citations_per_year.items()))

# Save JSON
output = {
    "total_citations": total_citations,
    "h_index": h_index,
    "citations_per_year": citations_per_year
}

with open("scholar_stats.json", "w") as f:
    json.dump(output, f, indent=2)

print("scholar_stats.json generated successfully!")
