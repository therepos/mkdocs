# 1. Deployment

### 1.1. GitHub Pages
To get started, open the [repository](https://github.com/therepos/template-mkdocs) and follow the steps below:

1\. Click the **Use this template** button (top-right).  

2\. Choose **Create a new repository**.  

3\. Enable GitHub Pages:  

&nbsp;&nbsp;&nbsp; <em>Settings</em> > <em>Pages</em> > <em>Deploy from Branch</em> > **gh-pages**.  

4\. Grant read and write permission:  

&nbsp;&nbsp;&nbsp; <em>Settings</em> > <em>Actions</em> > <em>General</em> > <em>Workflow permission</em> > **Read and write permissions**.

5\. Commit any file changes to publish the updates.  

6\. Visit your published site e.g. https://therepos.github.io/template-mkdocs  

### 1.2. (Alternative) Local Deployment
1\. To deploy it locally::  
```
git clone https://github.com/therepos/template-mkdocs.git
```

2\. Install npm packages:
```
cd template-mkdocs
npm install
npm run start
```

3\. Deploy locally:
```bash
npm run build
```

4\. Push to GitHub repo:
```bash
git add . 
git commit -m "Updates"
git push
```

5\. (Optional) Preview site locally only:
```bash
npm run serve
```

## 2. Guides

To understand more about how to use or customise the site, please refer to the official [MkDocs Guides](https://www.mkdocs.org/). 

### 2.1 Structure

```
template-docusaurus
├── .github/
├── blog/  
├── └── yyyy-mm-dd-post.md      # your blog post            
├── docs/               
│   └── about/                  # your section
│       └── index.md            # your document
├── src/
├── static/
├── docusaurus.config.js
├── package.json
├── readme.md           
└── sidebars.js
```
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