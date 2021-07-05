from django import template

register = template.Library()

@register.filter(name='cut_tt')
def cut_tt(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')



# Ugyanaz, mint a fentebbi sor, csak itt nem használok decorator-t
# def cut_tt(value,arg):
#     """
#     This cuts out all values of "arg" from the string!
#     """
#     return value.replace(arg,'')
#
# register.filter('cut_tt',cut_tt)
