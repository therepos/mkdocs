# MkDocs

This is a template to deploy a basic MkDocs site on GitHub Pages.

## GitHub Pages
To get started:

1. Click the **Use this template** button (top-right).  
2. Choose **Create a new repository**.  
3. Enable GitHub Pages:  
- Trigger the GitHub Actions workflow by editing any Markdown file.  
- **Settings** > **Pages** > **Deploy from Branch** > **gh-pages**  
- **Settings** > **Actions** > **General** > **Workflow permission** > **Read and write permissions**   
4. Visit your published site e.g. https://therepos.github.io/template-mkdocs

## Local Deployment
1\. To deploy it locally::  
```bash
git clone https://github.com/therepos/mkdocs.git
```

2\. Install requirements:
```bash
cd mkdocs
pip install -r requirements.txt
```

3\. Deploy locally:
```bash
mkdocs serve
```

4\. Push to GitHub repo:
```bash
git add . 
git commit -m "Updates"
git push
```

5\. (Optional) Preview site locally only:
```bash
mkdocs build
```

---

## References
[Official MkDocs Guide](https://www.mkdocs.org/)
