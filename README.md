# ponor.ba

Static Jekyll site publishing AI/LLM content in Bosnian. Deployed via
GitHub Pages at [www.ponor.ba](https://www.ponor.ba).

Content is produced by an editorial-agent workflow that lives one
level up from this directory (`../CLAUDE.md`, `../blackboard/`,
`../prompts/`). This README covers the site itself: how it's built,
how to run it locally, and how to ship it. It does not duplicate the
editorial process.

## Stack

- **Jekyll** (static site generator), **kramdown** (Markdown).
- **Tailwind CSS**, compiled to a static, committed file
  (`assets/css/tailwind.css`) — Jekyll does not run a build step for
  it. See "Editing styles" below; this is the part most likely to trip
  you up.
- No Jekyll plugins are actually used at runtime. `Gemfile` pulls in
  `github-pages` (so a local build matches GH Pages' environment when
  run via Bundler), but feed, sitemap, and SEO/structured-data are all
  hand-rolled in this repo (`feed.xml`, `sitemap.xml`,
  `_includes/structured-data.html`) rather than delegated to
  `jekyll-feed` / `jekyll-seo-tag`. Nothing in the templates calls
  `{% seo %}` or `feed_meta`.
- No JS framework, no client-side build. `pretraga.md` (search) does a
  client-side fetch of `search.json` and filters in plain JS — no
  third-party search service.

## Content model

**Posts** (`_posts/YYYY-MM-DD-slug.md`) — front matter:

```yaml
layout: post
title: "..."
date: YYYY-MM-DD
category: novosti | vodici | ai-u-praksi | ai-za-sve
read_time: 7          # minutes, integer
description: "..."    # used for meta description, card copy, RSS
image: /assets/images/<slug>.svg   # optional; falls back to a
                                    # gradient + icon tile if omitted
tags: [llm, mcp]       # optional, see Tags below
```

Body = Markdown, minus the H1 (the layout renders the title). To embed
a diagram: `{% include diagram.html name="<slug>" caption="..." alt="..." %}`,
with the SVG at `_includes/diagrams/<slug>.svg` — Jekyll's `{% include %}`
can only read from `_includes/`, so that's the only place a diagram
actually renders from. A `diagram:` front-matter key does nothing by
itself.

**Categories** — four, each with two coupled pieces that must stay in
sync:
1. An entry in `_data/categories.yml` (`name`, `description`, and the
   Tailwind color-class set used for badges/cards/icons).
2. A page in `kategorije/<slug>.md` (`layout: category`,
   `category_slug: <slug>`, `permalink: /kategorije/<slug>/`) — this
   is the actual archive/listing page.

Current categories: `novosti`, `vodici`, `ai-u-praksi`, `ai-za-sve`.
Adding a new category means creating both pieces, adding the color
classes to the `safelist` in `tailwind.config.js` (see below), and
adding an icon branch in `_layouts/category.html` (two places) and the
homepage post-card fallback icon in `index.html`.

**Tags** — freeform topic labels, using Jekyll's built-in `site.tags`
(no plugin). Two coupled pieces, same pattern as categories:
1. An entry in `_data/tags.yml` (slug → display `name`).
2. A page in `teme/<slug>.md` (`layout: tag`, `tag_slug: <slug>`,
   `permalink: /teme/<slug>/`).

`teme/index.md` (`/teme/`) lists every tag currently in use, ranked by
post count, entirely dynamically — no per-tag maintenance needed there.
The homepage's "Popularne teme" sidebar does the same ranking for its
top 6. Tag icons live in one place, `_includes/tag-icon.html` (keyed
by slug, with a generic fallback), included from both the sidebar and
`_layouts/tag.html`.

A tag used in a post's front matter but **not yet** in `_data/tags.yml`
still gets counted and ranked correctly (Jekyll's `site.tags` doesn't
care), but its link 404s until you add the matching `teme/<slug>.md`
page and a `_data/tags.yml` entry — same manual-registration model as
categories, because GitHub Pages only allows a fixed plugin whitelist,
so there's no custom generator to auto-create archive pages.

There is no audience/persona segmentation (developers/business/etc.)
— that was removed; don't reintroduce an `audience:` front-matter
convention without checking the editorial workflow's current stance
first (`../CLAUDE.md`).

## Directory structure

```
_config.yml           Site config: url, permalinks, newsletter, analytics
_data/                categories.yml, tags.yml, months.yml (BS month names)
_includes/            header, footer, head, newsletter, structured-data,
                       tag-icon, diagram (+ diagrams/ — actual diagram SVGs)
_layouts/              default, page, post, category, tag
_posts/                Published articles
kategorije/            One page per category (archive/listing)
teme/                  One page per tag, + index.md ("Sve teme")
assets/
  css/                 fonts.css (self-hosted @font-face), tailwind.css (compiled, committed)
  fonts/               Self-hosted woff2 (Inter, Merriweather, Fira Code)
  images/              Post header images + social default
scripts/
  fetch_fonts.py       Regenerates assets/fonts/ + assets/css/fonts.css
index.html             Homepage
404.html, o-nama.md, politika-privatnosti.md, pretraga.md   Standalone pages
feed.xml, sitemap.xml, search.json, robots.txt   Hand-rolled, Liquid-templated
tailwind.config.js, tailwind.input.css   Tailwind build config (see below)
reference_static_web/  Local-only design reference (gitignored, not published)
_diagram-specs/        Local-only diagram reproducibility specs (gitignored)
```

## Local development

The Ruby/Bundler setup here is a bit particular — worth reading before
you fight it.

**The problem:** `Gemfile` pins `gem "github-pages"`, which — if you
actually `bundle install` it — resolves to **Jekyll 3.10**, an old
version, to match GitHub Pages' hosted build environment. If your
system already has a newer Jekyll installed (4.x), you'll get a
version conflict, or `bundle install` will need to pull down dozens of
transitive gems.

**What actually works day-to-day:** this site uses no Jekyll plugins
at runtime (see Stack, above), so a plain system Jekyll install is
sufficient — you don't need the exact `github-pages`-pinned version to
get correct output locally.

```bash
gem install jekyll webrick   # if not already present; webrick was
                              # dropped from Ruby's stdlib in 3.0+
JEKYLL_NO_BUNDLER_REQUIRE=true jekyll serve --host 127.0.0.1
```

`JEKYLL_NO_BUNDLER_REQUIRE=true` is required — without it, Jekyll
detects the `Gemfile` and tries to load your site through Bundler,
which fails immediately with `Could not find gem 'github-pages'`
unless you've actually run `bundle install` for it.

If you'd rather match GitHub Pages' environment exactly (e.g. to
reproduce a build discrepancy), do it the slow way instead:

```bash
bundle install     # pulls the full github-pages gem set — slow, ~200MB+
bundle exec jekyll serve
```

Either way, the server is at `http://127.0.0.1:4000/` with
`--livereload` if you want auto-refresh on save.

## Editing styles (Tailwind)

**`assets/css/tailwind.css` is a committed, precompiled file — not
generated at request time.** Jekyll does not run Tailwind. If you add
or change a Tailwind class in any template and don't rebuild this
file, the class silently won't exist in the shipped CSS.

There's no `package.json` / npm dependency in this repo. Use the
standalone CLI binary (no Node required):

```bash
curl -sL -o tailwindcss https://github.com/tailwindlabs/tailwindcss/releases/download/v3.4.17/tailwindcss-linux-x64
chmod +x tailwindcss
./tailwindcss -c tailwind.config.js -i tailwind.input.css -o assets/css/tailwind.css --minify
```

(Match the platform suffix to your OS/arch — see the
[releases page](https://github.com/tailwindlabs/tailwindcss/releases).
Pin to v3.4.17 specifically, matching what's already compiled in, so a
rebuild doesn't churn the whole file on an unrelated version bump.)

Two gotchas specific to this codebase:

- **Composed classes aren't visible to the scanner.** Anything built
  by concatenating a Liquid variable into a class string — e.g.
  `hover:{{ cat.border_class }}` in `_layouts/category.html` — can't
  be found by Tailwind's static scan. These are hand-listed in the
  `safelist` array in `tailwind.config.js`. If you add a new category
  color, add its `hover:border-*` and `group-hover:text-*` variants
  there too, or the color will compile everywhere *except* those two
  composed spots.
- **`dark:` and `hover:` on the same property can silently lose to
  each other.** `dark:text-[#A8A29E]` and a plain `hover:text-coffee`
  have equal CSS specificity; whichever Tailwind happens to emit later
  in the file wins when both apply (i.e., hovering a link in dark
  mode). If a hover color isn't showing up in dark mode, you almost
  certainly need `dark:hover:text-coffee` explicitly (a compound
  selector with combined specificity beats source order) rather than
  relying on the plain `hover:` class.

## Deploying to GitHub Pages

1. Push to the branch GitHub Pages is configured to build from (check
   the repo's Settings → Pages — typically `main`/`master`, or a
   dedicated `gh-pages` branch).
2. GitHub Pages runs its own hosted Jekyll build using the
   `github-pages` gem version it currently supports — this is
   independent of whatever Jekyll version you used locally. Given
   nothing here depends on a specific plugin or Jekyll-version
   behavior beyond core Liquid/kramdown, this has been reliable, but
   it's worth actually checking the live site after a push that
   touches Liquid logic (not just copy), since it's a different Jekyll
   version than most local dev setups (this repo's own `Gemfile`
   pins `github-pages` to reflect that GH Pages will use it, but only
   bites in bundle mode).
3. `CNAME` in the repo root (`www.ponor.ba`) tells GitHub Pages the
   custom domain — DNS itself (the CNAME/A records at your registrar)
   is out of scope here and already set up.
4. **Nothing rebuilds `assets/css/tailwind.css` on GitHub Pages** — if
   you changed a template's classes locally and forgot to rebuild and
   commit the compiled CSS, the live site ships stale styles even
   though the build "succeeds." Always rebuild Tailwind before
   pushing a template change (see above).
5. No separate deploy step, no artifacts to upload — `git push` is the
   deploy.

## Scripts

- `scripts/fetch_fonts.py` — re-downloads the exact woff2 files Google
  Fonts serves for this site's font stack (Inter, Merriweather, Fira
  Code), keeping only latin + latin-ext (needed for č/ć/ž/š/đ), and
  regenerates `assets/css/fonts.css` pointing at the self-hosted files.
  Only needs re-running if the font stack itself changes.
- `../scripts/publish_lint.py` and `../scripts/gen_article_image.py`
  (one level up, not in this directory) — part of the editorial
  workflow's publish step; see `../CLAUDE.md`.

## Known gaps

- `_posts/` is currently empty and `git status` shows ~224
  pre-existing uncommitted deletions (old posts, diagrams, header
  images) from an in-progress content prune that predates this
  cleanup — not something this pass touched or should touch without
  the editor's say.
- `reference_static_web/` and `_diagram-specs/` are intentionally
  gitignored (see `.gitignore`'s own comments) — local working
  material, not part of the published site.
