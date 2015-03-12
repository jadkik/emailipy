import tinycss
import rules

from bs4 import BeautifulSoup

def inline_css(html, css, include_invalid=False):
    dom = BeautifulSoup(html)
    css_rules = tinycss.make_parser().parse_stylesheet(css).rules
    for rule in css_rules:
        css_selector = rule.selector.as_css()
        for node in dom.select(css_selector):
            for declaration in rule.declarations:

                if not include_invalid and _get_clients_without_support(declaration):
                    continue # skip invalid rules

                declaration.specificity = _selector_specificity(css_selector, declaration.priority)
                node.declarations = node.declarations or {}
                active_declaration = node.declarations.get(declaration.name)
                if active_declaration and active_declaration.specificity > declaration.specificity:
                    continue # skip rules with lower specificity

                node.declarations[declaration.name] = declaration
                node['style'] = _get_node_style(node)

    return dom.prettify()


def lint_css(css):
    violations = []
    css_rules = tinycss.make_parser().parse_stylesheet(css).rules
    for rule in css_rules:
        for declaration in rule.declarations:
            css_selector = rule.selector.as_css()
            prop = declaration.name
            value = " ".join([v.as_css() for v in declaration.value])
            clients_without_support = _get_clients_without_support(declaration)
            if clients_without_support:
                clients = " | ".join(clients_without_support)
                warning = "Invalid Rule: {} {{ {}: {}; }} -- {}".format(css_selector, prop, value, clients)

                violations.append(warning)

    return violations

def _get_node_style(node):
    stringify_value = lambda value: " ".join([v.as_css() for v in value])
    style = " ".join(["{}: {};".format(declaration.name, stringify_value(declaration.value)) for declaration in node.declarations.values()])
    return style


def _selector_specificity(selector, priority):
    class_weight = selector.count(".")
    id_weight = selector.count("#")
    element_weight = len([a for a in selector.split(" ") if not (a.startswith(".") or a.startswith("#"))])
    weight = element_weight + class_weight * 10 + element_weight * id_weight * 100
    if priority:
        weight *= 90000
    return weight


# https://www.campaignmonitor.com/css/
def _get_clients_without_support(declaration):
    return rules.INVALID_RULES.get(declaration.name)
