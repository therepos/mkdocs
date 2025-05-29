# MkDocs

This is a template to deploy a basic MkDocs site on GitHub Pages.

## GitHub Pages
To get started:

1\.  Click the **Use this template** button (top-right).  
2\.  Choose **Create a new repository**.  
3\.  Enable GitHub Pages:  
- Trigger the GitHub Actions workflow by editing any Markdown file.  
- <em>Settings</em> > <em>Pages</em> > <em>Deploy from Branch</em> > **gh-pages**.
- <em>Settings</em> > <em>Actions</em> > <em>General</em> > <em>Workflow permission</em> > **Read and write permissions**.  

4\.  Visit your published site e.g. https://therepos.github.io/template-mkdocs

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

## Licence
This project is licensed under MIT. If you find this template useful and use it in your own project, a link back to the original repo would be appreciated!

## References
[Official MkDocs Guide](https://www.mkdocs.org/)
