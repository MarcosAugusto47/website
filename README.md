# Personal Website

Personal website built with [Pelican](https://getpelican.com/).

## Credits

Website design and theme copied from [Duarte O. Carmo](https://duarteocarmo.com) ([source](https://github.com/duarteocarmo/duarteocarmo.com)). May be customized in the future.

## Development

```bash
make devserver
```

Visit http://127.0.0.1:8000

## Deployment

Currently deployed to both platforms. Once I purchase a custom domain, I will use Cloudflare Pages only.

### GitHub Pages

- **URL:** https://marcosaugusto47.github.io/website
- **Config:** `publishconf.py`
- **Deploy:** Automatic via GitHub Actions on push to `main`

### Cloudflare Pages

- **URL:** https://website.marcosbsb2014.workers.dev
- **Config:** `publishconf_cloudflare.py`
- **Build command:** `pip install -r requirements.txt && pelican content -s publishconf_cloudflare.py`
- **Output directory:** `output`
