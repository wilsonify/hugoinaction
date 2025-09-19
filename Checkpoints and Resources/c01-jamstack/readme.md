# Acme Corporation Website  

Welcome to the **Acme Corporation Website Project**. This repository contains the code for Acme Corporation’s digital presence — a Jamstack-based site built with [Hugo](https://gohugo.io/), enhanced by JavaScript and APIs.  

The final deployed version of the project (as featured in *Hugo in Action*) is hosted at:  
[https://chapter-13-09.hugoinaction.com/](https://chapter-13-09.hugoinaction.com/)  

---

## Project Overview  

We are building a **Jamstack site** that includes:  
- **Company pages** — About, Contact, Terms, Privacy.  
- **Blog** — with support for comments and search.  
- **Shape editor** — a JavaScript-based tool to create and edit digital shapes.  
- **Storefront** — purchase shapes, delivered via email.  

Hugo handles the **markup layer**, while JavaScript and APIs add interactivity and dynamic features.  

---

## Getting Started  

### 1. Prerequisites  

To contribute, you’ll need:  
- A modern operating system (Linux, macOS, or Windows).  
- [Git](https://git-scm.com/) (for version control).  
- [Hugo](https://gohugo.io/getting-started/installing/) (extended version recommended).  
- A web browser (for testing).  
- Basic knowledge of:  
  - **HTML, CSS, JavaScript**  
  - **GitHub workflows**  
  - A template engine (e.g., Mustache, Jade, ERB)  
  - **npm** (optional, for JavaScript dependencies)  

---

### 2. Clone the Repository  

```bash
git clone https://github.com/your-org/acme-website.git
cd acme-website
```

---

### 3. Run the Site Locally  

Start Hugo’s development server:  

```bash
hugo server -D
```

This will:  
- Serve the site at `http://localhost:1313`  
- Watch files for changes and reload automatically  

---

### 4. Project Structure  

```
acme-website/
├── content/        # Markdown files for pages & blog posts
├── layouts/        # Hugo templates and themes
├── static/         # CSS, JavaScript, images
├── themes/         # Shared templates & styles
├── config.toml     # Site configuration
└── package.json    # (optional) JavaScript dependencies
```

---

### 5. Deployment  

We follow a **Jamstack flow**:  
1. Content + templates → compiled into static HTML by Hugo.  
2. Dynamic features (comments, search, storefront) → handled via JavaScript + APIs.  
3. Deployment is automated (CI/CD pipelines push changes to production).  

---

## Learning Resources  

- [Jamstack.org](https://jamstack.org/) – core concepts  
- [Hugo Documentation](https://gohugo.io/documentation/) – reference for templates & content organization  
- [Hugo in Action](https://hugoinaction.com) – book source code and exercises  

---

## Quick Check  

> **Exercise:** Hugo works on the _______ layer of the Jamstack.  

---

## Summary  

- **Jamstack** = Markup + JavaScript + APIs.  
- **Hugo** is the static site generator powering the markup layer.  
- **JavaScript** connects to APIs for interactivity (comments, search, editor, storefront).  
- This approach ensures a fast, cost-effective, and maintainable site.  