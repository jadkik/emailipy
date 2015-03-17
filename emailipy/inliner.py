import tinycss

from lxml import etree
from lxml.cssselect import CSSSelector
from lxml.html import soupparser

from linter import get_clients_without_support


# specificity is represented as a single int at the moment
# so to account for !important we need to make a big int
IMPORTANT_MULTIPLIER = 9000

def inline_css(html, css, strip_unsupported_css=True):
    node_declarations = {}
    try:
        dom = etree.fromstring(html)
    except etree.XMLSyntaxError:
        dom = soupparser.fromstring(html)

    css_rules = tinycss.make_parser().parse_stylesheet(css).rules
    for rule in css_rules:
        css_selector = rule.selector.as_css()
        for node in CSSSelector(css_selector)(dom):
            for declaration in rule.declarations:

                if strip_unsupported_css and get_clients_without_support(declaration):
                    continue # skip invalid rules

                declaration.specificity = _selector_specificity(css_selector, declaration.priority)
                node_declarations.setdefault(node, {})
                active_declaration = node_declarations.get(node, {}).get(declaration.name)
                if active_declaration and active_declaration.specificity > declaration.specificity:
                    continue # skip rules with lower specificity

                node_declarations[node][declaration.name] = declaration
                node.set('style', _get_node_style(node_declarations[node]))

    return etree.tostring(dom, pretty_print=True)


def _get_node_style(declarations):
    stringify_value = lambda value: " ".join([v.as_css() for v in value])
    style = " ".join(["{}: {};".format(declaration.name, stringify_value(declaration.value)) for declaration in declarations.values()])
    return style


def _selector_specificity(selector, priority):
    class_weight = selector.count(".")
    id_weight = selector.count("#")
    element_weight = len([a for a in selector.split(" ") if not (a.startswith(".") or a.startswith("#"))])
    weight = element_weight + class_weight * 10 + element_weight * id_weight * 100
    if priority:
        weight *= IMPORTANT_MULTIPLIER
    return weight
