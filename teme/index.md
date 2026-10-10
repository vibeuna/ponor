---
layout: default
title: "Sve teme"
description: "Pregled svih tema o kojima piše ponor.ba."
permalink: /teme/
---
<section id="main-content" class="pt-12 pb-8 px-4 sm:px-6 lg:px-8 bg-white dark:bg-[#1C1917] border-b border-warmgray dark:border-[#44403C]">
    <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-bold text-ink mb-3">Sve teme</h1>
        <p class="text-stone text-lg max-w-2xl leading-relaxed">{{ page.description }}</p>
    </div>
</section>

<section class="py-10 px-4 sm:px-6 lg:px-8">
    <div class="max-w-6xl mx-auto">
        {% capture tag_cloud %}{% for tag in site.tags %}{{ tag[1].size | plus: 10000 }}~{{ tag[0] }}|||{% endfor %}{% endcapture %}
        {% assign tag_entries = tag_cloud | split: "|||" | sort | reverse %}
        {% if tag_entries.size > 0 %}
        <div class="flex flex-wrap gap-3">
            {% for entry in tag_entries %}
            {% assign parts = entry | split: "~" %}
            {% assign tag_slug = parts[1] %}
            {% assign tag_count = parts[0] | minus: 10000 %}
            {% assign tag_meta = site.data.tags[tag_slug] %}
            <a href="/teme/{{ tag_slug }}/" class="inline-flex items-center gap-2 px-4 py-2 rounded-full border border-warmgray dark:border-[#44403C] text-sm font-medium text-stone hover:border-coffee hover:text-coffee transition-colors">
                {{ tag_meta.name | default: tag_slug }}
                <span class="text-xs text-stone/60">{{ tag_count }}</span>
            </a>
            {% endfor %}
        </div>
        {% else %}
        <p class="text-stone py-12 text-center">Još nema tema — pojaviće se čim prvi članak bude označen temom.</p>
        {% endif %}
    </div>
</section>
