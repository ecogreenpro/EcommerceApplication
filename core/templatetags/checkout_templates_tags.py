from django import template
from django.utils.safestring import mark_safe

from core.models import CartProducts, Order, Shipping

register = template.Library()


@register.simple_tag
def checkout_li():
    items = CartProducts.objects.filter(isOrdered=False)
    items_li = ""
    for i in items:
        items_li += """<tr start="1">
     <li class="list-group-item d-flex justify-content-between lh-condensed">
        <div>
             <h6 class="my-0">{}</h6>
             <small class="text-muted">Brief description</small>
         </div>
        <span class="text-muted">{}</span>
     </li>
         """.format(
            i.item.name, i.get_final_price())
    return mark_safe(items_li)


@register.simple_tag
def shipping_li():
    items = Shipping.objects.filter(location='Dhaka')
    shipping_li = ""
    for i in items:
        shipping_li += """<tr start="1">
      <div class="form-group">
         <label for="sel1">Shipping Charge:</label>
            <select class="form-control" id="sel1">
              <option>{}</option>    
            </select>
            <span class="text-muted">{}</span>
      </div>
         """.format(
            i.location, i.charge)
    return mark_safe(shipping_li())
