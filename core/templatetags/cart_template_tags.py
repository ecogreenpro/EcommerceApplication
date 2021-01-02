from django import template
from django.utils.safestring import mark_safe

from core.models import CartProducts, Order

register = template.Library()


# register = template.Library()
#
#
# @register.filter
# def cart_item_count(user):
#     if user.is_authenticated:
#         qs = Order.objects.filter(user=user, ordered=False)
#         if qs.exists():
#             return qs[0].items.count()
#     return 0
@register.simple_tag
def cartPage_li():
    items = CartProducts.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
        <td>1</td>
        <td width="35%">
            <div class="display-flex align-center">
                 <div class="img-product">
                    <img src="/media/{}" alt="" class="mCS_img_loaded">
                 </div>
            </div>
        </td>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
         <td>{}</td>
         </tr>
         """.format(
            i.item.mainImage, i.item.name, i.price(), i.quantity, i.get_final_price())
    return mark_safe(items_li)


@register.simple_tag
def cartPage_total():
    items = Order.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
         <td>{}</td>
         </tr>
         """.format(i.get_total())
    return mark_safe(items_li)
