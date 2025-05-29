# MkDocs
This is a template to deploy a basic [MkDocs](https://www.mkdocs.org/) documentation site on GitHub Pages.  

## 1. Deployment

### 1.1. GitHub Pages
To get started:

1\. Click the **Use this template** button (top-right).  

2\. Choose **Create a new repository**.  

3\. Enable GitHub Pages:  

&nbsp;&nbsp;&nbsp; _Settings_ > _Pages_ > _Deploy from Branch_ > **gh-pages**.  

4\. Grant read and write permission:  

&nbsp;&nbsp;&nbsp; _Settings_ > _Actions_ > _General_ > _Workflow permission_ > **Read and write permissions**.

5\. Commit any file changes to publish the updates.  

6\. Visit your published site e.g. https://therepos.github.io/template-mkdocs  

### 1.2. (Alternative) Local Deployment
1\. To deploy it locally::  
```
git clone https://github.com/therepos/template-mkdocs.git
```

2\. Install dependencies:
```
cd template-mkdocs
pip install -r requirements.txt
```

3\. Preview site locally:
```bash
mkdocs serve
```

4\. Deploy locally:
```bash
mkdocs build
```

5\. Push to gh-pages:
```bash
mkdocs gh-deploy
```

6\. Push to GitHub repo:
```bash
git add . 
git commit -m "Updates"
git push
```

## 2. Guides

To understand more about how to use or customise the site, please refer to the official [MkDocs Guides](https://www.mkdocs.org/). 

### 2.1. Structure

```
template-mkdocs
├── .github/
├── docs/
│   ├── about/                  # your section
│   │   ├── .pages
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

## 3. License
This project is licensed under MIT. If you find this template useful, please attribute a link to this repository.