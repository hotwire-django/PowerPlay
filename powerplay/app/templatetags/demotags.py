import re
from base64 import b64encode

from django import template

register = template.Library()


@register.filter
def base64(data):
    encoded = b64encode(data)
    return encoded.decode('utf-8')


INPUT_DIV = """
<div class="form-floating mb-2">
  <input class="form-control" \g<3>>
  <label for="\g<1>">\g<2></label>
</div>
"""
TEXT_AREA_DIV = """
<div class="form-floating mb-2">
  <textarea class="form-control" \g<3> style="height: 100px">\g<4></textarea>
  <label for="\g<1>">\g<2></label>
  \g<5>
</div>
"""
SELECTS_DIV = """
<div class="form-floating mb-2">
  <select class="form-select" \g<3> >
    \g<4>
  </select>
  <label for="\g<1>">\g<2></label>
</div>
"""

@register.filter(is_safe=True)
def prettyform(form_text):
    input_regex = r"<p>\W{0,6}<label for=\"(\w+)\">(?P<label>[^\r\n]+?)</label>\W{0,6}<input (?P<attrs>[^\r\n]+?)\>\W+?\<\/p\>"
    textarea_regex = r"<p>\W{0,6}<label for=\"(?P<id>\w+)\">(?P<label>[^\r\n]+?)</label>\W{0,6}<textarea (?P<attrs>[^\r\n]+?)\>(?P<content>.*?)\<\/textarea\>(?P<extra>.*?)\<\/p\>"
    selects_regex = r"<p>\W{0,6}<label for=\"(?P<id>\w+)\">(?P<label>[^\r\n]+?)</label>\W{0,6}<select (?P<attrs>[^\r\n]+?)\>(?P<options>.*?)</select>\W+<\/p\>"

    form_text = re.sub(input_regex, INPUT_DIV, form_text, flags=re.M|re.DOTALL)
    form_text = re.sub(textarea_regex, TEXT_AREA_DIV, form_text, flags=re.M|re.DOTALL)
    form_text = re.sub(selects_regex, SELECTS_DIV, form_text, flags=re.M|re.DOTALL)
    return form_text


