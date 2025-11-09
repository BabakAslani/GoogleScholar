# Google Scholar Live Stats

[![Google Scholar](https://upload.wikimedia.org/wikipedia/commons/2/28/Google_Scholar_logo.png)](https://babakaslani.github.io/GoogleScholar/)



This repository provides a **live, weekly-updated visualization of your Google Scholar citations**, including:

- Total citations
- h-index
- i10-index
- Citations per year (interactive bar chart)
- Last updated timestamp

Everything is automatically updated via **GitHub Actions** and displayed beautifully on **GitHub Pages**.

---

## Features

- **Dynamic badges** for total citations, h-index, and i10-index  
- **Interactive bar chart** with hover tooltips showing citations per year  
- **Gradient bars**: darker for recent years  
- **Weekly updates** using GitHub Actions  
- **Cache-busting** ensures your site always shows the latest stats  
- **Responsive and modern layout** with rounded bars  

---

## Demo

Check out the live pages: [My Publications](https://www.babakaslani.com/publications) and [Google Scholar Stats](https://babakaslani.github.io/GoogleScholar/)

---

## Setup & Usage

### 1. Clone this repository

```bash
git clone https://github.com/BabakAslani/GoogleScholar.git
cd GoogleScholar
```

### 2. Install Python dependencies
```bash
pip install scholarly
```

### 3. Configure your Google Scholar ID
```bash
In update_scholar_stats.py, set your Scholar ID:
SCHOLAR_ID = "your_google_scholar_id_here"
```
### 4. Test Python script locally
```bash
python update_scholar_stats.py
```
This generates scholar_stats.json with your citation stats.

### 5. Push to GitHub
```bash
git add scholar_stats.json
git commit -m "Add initial scholar stats"
git push origin main
```

### 6. Self-Hosted GitHub Actions Runner (Recommended)

To avoid Google Scholar rate limits on cloud runners, you can run the workflow on your own machine:

Go to your GitHub repo → Settings → Actions → Runners → New self-hosted runner

Follow the setup commands for your OS (macOS example):

```bash
mkdir actions-runner && cd actions-runner
curl -o actions-runner-osx-x64.tar.gz -L https://github.com/actions/runner/releases/download/v2.329.0/actions-runner-osx-x64-2.329.0.tar.gz
tar xzf ./actions-runner-osx-x64.tar.gz
./config.sh --url https://github.com/<your-username>/GoogleScholar --token <your-token>
./run.sh
```
Update .github/workflows/update.yml to use your runner:
```bash
runs-on: self-hosted
```
The workflow will now execute locally, fetching Scholar stats from your own IP.

### 7. GitHub Actions
The workflow in .github/workflows/update.yml automatically updates your stats weekly.
You can also trigger it manually from the Actions tab in GitHub.

### 8. GitHub Pages
Enable GitHub Pages from Settings → Pages → Source → main / root.
Your live site will be available at:
```bash
https://<your-username>.github.io/GoogleScholar/
```

## Automatic Updates ⚡

Your Google Scholar stats are updated **automatically every week** using **GitHub Actions**.  

- 🤖 The workflow is defined in `.github/workflows/update.yml`  
- 📚 Fetches the latest citation data via the [Scholarly](https://pypi.org/project/scholarly/) Python library  
- 📄 Updates the `scholar_stats.json` file, which is displayed on your GitHub Pages site


### 🔧 How to change the update frequency

The schedule is controlled by a **cron expression** in the YAML file:

```yaml
on:
  schedule:
    - cron: '0 0 * * 0'   # every Sunday at 00:00 UTC
  workflow_dispatch:      # allows manual run from GitHub UI
```

## Customization ✨

- 🎨 **Change chart colors, fonts, or layout** in `index.html`  
- 🏷️ **Add badges or additional metrics** if desired  
- ⚡ **Cache-busting** is built-in for JSON updates  


## 📦 Requirements

- **Python 3.11+**  
- [Scholarly](https://pypi.org/project/scholarly/) Python library:

```bash
pip install scholarly
```

## 📈 Output

The workflow produces a file:
```bash
scholar_stats.json
```

Example contents:
```bash
{
    "total_citations": 283,
    "h_index": 8,
    "i10_index": 8,
    "citations_per_year": {
        "2018": 1,
        "2019": 1,
        "2020": 8,
        "2021": 20,
        "2022": 44,
        "2023": 63,
        "2024": 71,
        "2025": 73
    },
    "h_index_recent": 8,
    "i10_index_recent": 8,
    "last_updated": "2025-11-05 04:35 UTC"
}
```

## 🧠 Future Extensions

Convert this logic into a Python package that outputs embeddable HTML code.

Add visualization charts (citations over time, top publications).

Enable caching for large profiles.

---

## Credits 🙏

- 📚 **Scholarly** – Python library to fetch Google Scholar data  
- 📊 **Chart.js** – Visualization library for interactive charts  

---

## License 📝

This project is licensed under the **MIT License**  

---

## © Copyright

© 2025 Babak Aslani, Ph.D.  
📧 Email: [baslani@gmu.edu](mailto:baslani@gmu.edu)  

---

Enjoy your live Google Scholar stats page! 🎓📊



