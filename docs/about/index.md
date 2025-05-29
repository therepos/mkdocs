# MkDocs
This is a template to deploy a basic [MkDocs](https://squidfunk.github.io/mkdocs-material/getting-started/) documentation site on GitHub Pages.  

## Deployment

### GitHub Pages
To get started, open the [repository](https://github.com/therepos/mkdocs) and follow the steps below:

1. Click the **Use this template** button (top-right).  

2. Choose **Create a new repository**.  

3. Enable GitHub Pages:  
    
    _Settings_ > _Pages_ > _Deploy from Branch_ > **gh-pages**.  

4. Grant read and write permission:  

    _Settings_ > _Actions_ > _General_ > _Workflow permission_ > **Read and write permissions**.

5. Commit any file changes to publish the updates.  

6. Visit your published site e.g. https://therepos.github.io/mkdocs  

### Local Deployment
1\.&nbsp;&nbsp; To deploy it locally:  

```
git clone https://github.com/therepos/mkdocs.git
```

2\.&nbsp;&nbsp; Install dependencies:

```
cd mkdocs  
pip install -r requirements.txt
```

3\.&nbsp;&nbsp; Preview site locally:

```
mkdocs serve
```

4\.&nbsp;&nbsp; Deploy locally:

```
mkdocs build
```

5\.&nbsp;&nbsp; Push to gh-pages:

```
mkdocs gh-deploy
```

6\.&nbsp;&nbsp; Push to GitHub repo:

```
git add . 
git commit -m "Updates"
git push
```

## Guides

To understand more about how to use or customise the site, please refer to the official [MkDocs Guides](https://squidfunk.github.io/mkdocs-material/getting-started/). 

### Structure

```
mkdocs
├── .github/
├── docs/
│   ├── about/                  # your section
│   │   ├── .pages              # set section title here
│   │   └── index.md            # your document
│   └── blog/posts/
│       └── blog.md             # your blog post 
│   ├── css/
│   └── fonts/
├── .gitignore
├── build.py
├── LICENSE
├── mkdocs.yml
├── readme.md
└── requirements.txt
```

## License
This project is licensed under MIT. If you find this template useful, please attribute a link to this repository.

## References
- [MkDocs Catelog](https://github.com/mkdocs/catalog)
