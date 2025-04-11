---
layout: default
title: Все инструменты
---

<section class="tools">
  {% for tool in site.data.tools %}
    {% include tool.html tool=tool %}
  {% endfor %}
</section>

<style>
.tool-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px;
  border-radius: 8px;
}
</style>