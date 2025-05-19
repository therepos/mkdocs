# MkDocs

This is a template to get a basic MkDocs site up and running quickly.  
By default, it deploys via GitHub Actions to GitHub Pages.

## GitHub Pages
To get started:

1\. Click the `Use this template` button (top-right).  
2\. Choose `Create a new repository`.  
3\. Enable GitHub Pages from `Settings` > `Pages` > `Deploy from Branch` > `gh-pages`  
4\. Grant workflow permission from `Settings` > `Actions` > `General` > `Workflow permission` > `Read and write permissions`  
5\. Trigger the GitHub Actions workflow by editing any Markdown file.  
6\. Visit your published site at: `https://<your-username>.github.io/<your-repo-name>/`  
7\. For example: https://therepos.github.io/mkdocs

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

## References
[Official MkDocs Guide](https://www.mkdocs.org/)
