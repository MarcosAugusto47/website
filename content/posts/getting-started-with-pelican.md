title: Getting Started with Pelican
date: 2025-01-10
category: blog
description: How I set up this website using Pelican static site generator.

I recently rebuilt my personal website using [Pelican](https://getpelican.com/), a static site generator written in Python. Here's a quick overview of the setup.

## Why Pelican?

There are many static site generators out there (Hugo, Jekyll, Eleventy, etc.), but I chose Pelican because:

- **Python-based** - I'm comfortable with Python and can easily extend it
- **Jinja2 templates** - Flexible and familiar templating
- **Markdown support** - Write content in Markdown, get HTML output
- **Simple** - No complex build process, just generate and deploy

## Basic setup

Getting started is straightforward:

```bash
pip install pelican markdown
pelican-quickstart
```

This creates a basic project structure:

```
website/
├── content/        # Your articles and pages
├── output/         # Generated HTML
├── pelicanconf.py  # Configuration
└── Makefile        # Build commands
```

## Writing content

Articles are just Markdown files with some metadata at the top:

```markdown
title: My Article Title
date: 2025-01-10
category: blog

Your content goes here...
```

## Development workflow

Run the development server with live reload:

```bash
make devserver
```

This watches for changes and regenerates the site automatically.

## Deployment

Since the output is just static HTML, you can deploy anywhere - GitHub Pages, Netlify, Vercel, or your own server.

## Conclusion

Pelican is a solid choice if you want a simple, Python-based static site generator. The learning curve is minimal, and you get full control over your site's design.
