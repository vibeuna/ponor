---
layout: default
title: Pretraga
permalink: /pretraga/
description: "Pretražite sve članke na ponor.ba — vodiče, vijesti i tekstove o AI-u i velikim jezičkim modelima na bosanskom jeziku."
---
<section id="main-content" class="pt-10 pb-8 px-4 sm:px-6 lg:px-8 bg-white dark:bg-[#1C1917] border-b border-warmgray dark:border-[#44403C]">
    <div class="max-w-3xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-bold text-ink mb-6">Pretraga</h1>
        <label for="search-input" class="sr-only">Pretražite članke</label>
        <div class="relative">
            <svg class="w-5 h-5 text-stone absolute left-4 top-1/2 -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
            <input id="search-input" type="search" autocomplete="off" autofocus
                placeholder="Pretražite članke — npr. RAG, agenti, EU AI Act…"
                class="w-full pl-12 pr-4 py-3.5 bg-cream dark:bg-[#292524] border border-warmgray dark:border-[#44403C] rounded-xl text-ink dark:text-cream placeholder-stone focus:outline-none focus:ring-2 focus:ring-coffee/50 focus:border-coffee transition-colors">
        </div>
        <p id="search-count" class="mt-3 text-sm text-stone dark:text-[#A8A29E]" role="status" aria-live="polite"></p>
    </div>
</section>

<section class="py-6 px-4 sm:px-6 lg:px-8">
    <div class="max-w-3xl mx-auto">
        <div id="search-results" class="space-y-1"></div>
    </div>
</section>

<script>
(function() {
    var input = document.getElementById('search-input');
    var results = document.getElementById('search-results');
    var count = document.getElementById('search-count');
    var docs = null, ready = false;

    // Fold diacritics so "prakticni" matches "praktični", "ص" aside.
    // NFD handles č/ć/ž/š; đ/Đ don't decompose, so map them explicitly.
    function fold(s) {
        return (s || '').normalize('NFD').replace(/[̀-ͯ]/g, '')
            .replace(/đ/g, 'd').replace(/Đ/g, 'D').toLowerCase();
    }

    function esc(s) {
        return (s || '').replace(/[&<>"]/g, function(c) {
            return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
        });
    }

    function render(matches, q) {
        if (!q) {
            results.innerHTML = '';
            count.textContent = '';
            return;
        }
        if (!matches.length) {
            results.innerHTML = '';
            count.textContent = 'Nema rezultata za „' + q + '”. Pokušajte s drugim pojmom.';
            return;
        }
        count.textContent = matches.length + (matches.length === 1 ? ' rezultat' : (matches.length < 5 ? ' rezultata' : ' rezultata'));
        var html = matches.map(function(d, i) {
            var meta = [];
            if (d.categoryName) meta.push(esc(d.categoryName));
            if (d.dateDisplay) meta.push(esc(d.dateDisplay));
            if (d.readTime) meta.push(d.readTime + ' min');
            var divider = i > 0 ? '<div class="border-b border-warmgray mx-5 md:mx-6"></div>' : '';
            return divider +
                '<a href="' + d.url + '" class="group block p-5 md:p-6 rounded-xl border border-transparent hover:border-warmgray dark:hover:border-[#44403C] transition-colors">' +
                    '<div class="flex items-center gap-2 mb-2 text-xs text-stone dark:text-[#A8A29E]">' +
                        meta.map(function(m, j) {
                            return (j > 0 ? '<span class="opacity-50">•</span>' : '') + '<span>' + m + '</span>';
                        }).join('') +
                    '</div>' +
                    '<h2 class="font-serif text-xl font-bold text-ink group-hover:text-coffee transition-colors mb-2">' + esc(d.title) + '</h2>' +
                    (d.description ? '<p class="text-sm text-stone leading-relaxed line-clamp-2">' + esc(d.description) + '</p>' : '') +
                '</a>';
        }).join('');
        results.innerHTML = html;
    }

    function search(q) {
        var terms = fold(q).split(/\s+/).filter(Boolean);
        if (!terms.length || !docs) return [];
        var scored = [];
        docs.forEach(function(d) {
            var score = 0;
            for (var i = 0; i < terms.length; i++) {
                var t = terms[i];
                if (d._title.indexOf(t) === -1 && d._tags.indexOf(t) === -1 &&
                    d._desc.indexOf(t) === -1 && d._content.indexOf(t) === -1) {
                    return; // AND: every term must appear somewhere
                }
                if (d._title.indexOf(t) !== -1) score += 4;
                if (d._tags.indexOf(t) !== -1) score += 3;
                if (d._desc.indexOf(t) !== -1) score += 2;
                if (d._content.indexOf(t) !== -1) score += 1;
            }
            scored.push({ d: d, score: score });
        });
        scored.sort(function(a, b) {
            return b.score - a.score || (a.d.date < b.d.date ? 1 : -1);
        });
        return scored.map(function(s) { return s.d; });
    }

    function run() {
        var q = input.value.trim();
        // Keep the query shareable/bookmarkable in the URL.
        var url = q ? location.pathname + '?q=' + encodeURIComponent(q) : location.pathname;
        history.replaceState(null, '', url);
        if (!ready) return;
        render(q ? search(q) : [], q);
    }

    var timer;
    input.addEventListener('input', function() {
        clearTimeout(timer);
        timer = setTimeout(run, 120);
    });

    fetch('/search.json')
        .then(function(r) { return r.json(); })
        .then(function(data) {
            docs = data.map(function(d) {
                d._title = fold(d.title);
                d._desc = fold(d.description);
                d._content = fold(d.content);
                d._tags = fold((d.tags || []).join(' '));
                return d;
            });
            ready = true;
            // Honor ?q= on initial load.
            var params = new URLSearchParams(location.search);
            var q0 = params.get('q');
            if (q0) { input.value = q0; }
            if (input.value.trim()) render(search(input.value.trim()), input.value.trim());
        })
        .catch(function() {
            count.textContent = 'Pretraga trenutno nije dostupna. Pokušajte ponovo kasnije.';
        });
})();
</script>
