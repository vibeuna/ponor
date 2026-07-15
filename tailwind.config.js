// Tailwind build config — mirrors the former inline cdn.tailwindcss.com config.
// Rebuild the stylesheet after adding new utility classes to any template:
//   tailwindcss -c tailwind.config.js -i tailwind.input.css -o assets/css/tailwind.css --minify
// (standalone CLI v3.x, no Node needed: github.com/tailwindlabs/tailwindcss/releases)
module.exports = {
  darkMode: 'class',
  content: [
    './_layouts/**/*.html',
    './_includes/**/*.html',
    './_data/**/*.yml',
    './_posts/**/*.md',
    './za/**/*.md',
    './kategorije/**/*.md',
    './*.html',
    './*.md',
  ],
  // category.html composes these at build time (hover:{{ cat.border_class }},
  // group-hover:{{ cat.text_class }}) so the content scanner can't see them.
  // Keep in sync with the *_class values in _data/categories.yml.
  safelist: [
    'hover:border-rose-500', 'hover:border-coffee', 'hover:border-teal',
    'group-hover:text-rose-600', 'group-hover:text-coffee', 'group-hover:text-teal',
  ],
  theme: {
    extend: {
      colors: {
        cream: '#FAF9F6',
        parchment: '#F5F5F0',
        ink: '#1C1917',
        stone: '#78716C',
        coffee: '#B45309',
        'coffee-dark': '#92400E',
        teal: '#0F766E',
        'teal-dark': '#115E59',
        warmgray: '#E7E5E4',
        'warmgray-light': '#F5F5F4',
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        serif: ['Merriweather', 'Georgia', 'serif'],
        mono: ['Fira Code', 'monospace'],
      },
    },
  },
}
