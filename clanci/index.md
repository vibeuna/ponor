---
layout: default
title: "Svi članci"
description: "Svi članci objavljeni na ponor.ba, od najnovijeg: vodiči, AI u praksi i AI za svakoga, na bosanskom jeziku."
permalink: /clanci/
---
{% comment %}
  Posts live at /clanci/<slug>/ (_config.yml permalink), so /clanci/ itself
  needs a page or visitors trimming the URL hit a 404.
{% endcomment %}
<section id="main-content" class="pt-12 pb-8 px-4 sm:px-6 lg:px-8 bg-white dark:bg-[#1C1917] border-b border-warmgray dark:border-[#44403C]">
    <div class="max-w-6xl mx-auto">
        <h1 class="text-3xl md:text-4xl font-bold text-ink mb-3">Svi članci</h1>
        <p class="text-stone text-lg max-w-2xl leading-relaxed">{{ page.description }}</p>
        <div class="mt-4 text-sm text-stone dark:text-[#A8A29E]">
            {% include count.html n=site.posts.size one="članak" few="članka" many="članaka" %}
        </div>
    </div>
</section>

<section class="py-8 px-4 sm:px-6 lg:px-8">
    <div class="max-w-6xl mx-auto">
        {% if site.posts.size > 0 %}
        <div class="space-y-1">
            {% for post in site.posts %}
            {% assign month_num = post.date | date: "%m" %}
            {% assign cat = site.data.categories[post.category] %}
            <a href="{{ post.url }}" class="group block p-5 md:p-6 rounded-xl border border-transparent hover:border-warmgray dark:hover:border-[#44403C] transition-colors">
                <div class="flex flex-col md:flex-row md:items-center gap-4">
                    <div class="flex-1">
                        <div class="flex flex-wrap items-center gap-3 mb-2">
                            {% if cat %}<span class="px-2 py-0.5 {{ cat.badge_class }} text-xs rounded-full font-medium">{{ cat.name }}</span>{% endif %}
                            <span class="text-xs text-stone dark:text-[#A8A29E]">{{ post.date | date: "%-d." }} {{ site.data.months[month_num] }} {{ post.date | date: "%Y." }}</span>
                            {% if post.read_time %}<span class="text-xs text-stone dark:text-[#A8A29E]">•</span><span class="text-xs text-stone">{{ post.read_time }} min</span>{% endif %}
                        </div>
                        <h2 class="font-serif text-xl font-bold text-ink {{ cat.hover_text | default: 'group-hover:text-coffee' }} transition-colors mb-2">{{ post.title }}</h2>
                        {% if post.description %}<p class="text-sm text-stone leading-relaxed line-clamp-2">{{ post.description }}</p>{% endif %}
                    </div>
                    <div class="flex-shrink-0 hidden md:block">
                        <svg class="w-5 h-5 text-warmgray transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
                    </div>
                </div>
            </a>
            {% unless forloop.last %}<div class="border-b border-warmgray mx-5 md:mx-6"></div>{% endunless %}
            {% endfor %}
        </div>
        {% else %}
        <p class="text-stone py-12 text-center">Još nema objavljenih članaka.</p>
        {% endif %}
    </div>
</section>

{% include newsletter.html %}
