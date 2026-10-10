source "https://rubygems.org"

# Pins Jekyll + dependencies to whatever GitHub Pages' own build environment
# runs, so a local `bundle exec jekyll serve` matches the hosted build.
gem "github-pages", group: :jekyll_plugins

# Ruby 3.0+ dropped webrick from the standard library; Jekyll's local
# dev server needs it back for `jekyll serve` to work.
gem "webrick", "~> 1.8"
