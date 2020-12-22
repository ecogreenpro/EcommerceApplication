from django import template
from django.utils.safestring import mark_safe

from core.models import Categories, Brands

register = template.Library()


@register.simple_tag
def categories():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<a href="/category/{}" class="list-group-item list-group-item-action bg-danger text-white"><i 
        class="fas fa-th-large"></i> {}</a>""".format(
            i.slug, i.name, i.image)
    return mark_safe(items_li)


@register.simple_tag
def categories_shop():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<li class="list-group-item d-flex justify-content-between align-items-center"><a 
        href="/category/{}" style="text-decoration: none;"> {} <span class="badge badge-primary badge-pill">14</span> </a></li>""".format(
            i.slug, i.name, i.image)
    return mark_safe(items_li)


@register.simple_tag
def categories_home():
    items = Categories.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """ <div class="col-lg-4"> <img class="bd-placeholder-img rounded-circle " width="140" height="140"
                                     src="/media/{}" focusable="false" role="img"/>
                                <h2> {} </h2>
                                <a class="btn btn-success" href="/category/{}" role="button">
                                    Shop &raquo;</a></div>""".format(
            i.image, i.name, i.slug)
    return mark_safe(items_li)


@register.simple_tag
def brand_shop():
    items = Brands.objects.filter(isactive=True).order_by('name')
    items_li = ""
    for i in items:
        items_li += """<li class="list-group-item d-flex justify-content-between align-items-center"><a 
        href="/category/{}" style="text-decoration: none;"> {} <span class="badge badge-primary badge-pill">14</span> </a></li>""".format(
            i.slug, i.name, i.image)
    return mark_safe(items_li)
