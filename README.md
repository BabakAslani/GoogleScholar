# Google Scholar Live Stats

![Google Scholar](https://babakaslani.github.io/GoogleScholar/)  

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

Check out the live page:  
https://www.babakaslani.com/publications

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

### 6. GitHub Actions
The workflow in .github/workflows/update_scholar.yml automatically updates your stats weekly.
You can also trigger it manually from the Actions tab in GitHub.

### 7. GitHub Pages
Enable GitHub Pages from Settings → Pages → Source → main / root.
Your live site will be available at:
```bash
https://<your-username>.github.io/GoogleScholar/
```

## Customization ✨

- 🎨 **Change chart colors, fonts, or layout** in `index.html`  
- 🏷️ **Add badges or additional metrics** if desired  
- ⚡ **Cache-busting** is built-in for JSON updates  

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



