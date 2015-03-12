import tinycss
import clients

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
# clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.IPHONE, clients.OUTLOOK_COM, clients.APPLE_MAIL, clients.YAHOO, clients.GMAIL, clients.ANDROID
INVALID_RULES = {
    # text & font
    "text-overflow": [clients.OUTLOOK],
    "text-shadow": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.GMAIL],
    "word-wrap": [clients.OUTLOOK, clients.GMAIL, clients.ANDROID],
    "text-fill-color": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.OUTLOOK_COM, clients.YAHOO, clients.GMAIL],
    "text-fill-stroke": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.OUTLOOK_COM, clients.YAHOO, clients.GMAIL],
    # color & background
    "background": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.OUTLOOK_COM, clients.YAHOO, clients.GMAIL],
    "background-image": [clients.OUTLOOK, clients.OUTLOOK_COM],
    "background-position": [clients.OUTLOOK, clients.OUTLOOK_COM, clients.GMAIL],
    "background-repeat": [clients.OUTLOOK, clients.OUTLOOK_COM],
    "background-size": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.OUTLOOK_COM, clients.YAHOO, clients.GMAIL, clients.ANDROID],
    # box model
    "border-color": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.ANDROID],
    "border-image": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.OUTLOOK_COM, clients.YAHOO, clients.GMAIL, clients.ANDROID],
    "border-radius": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.YAHOO, clients.ANDROID],
    "box-shadow": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.YAHOO, clients.GMAIL, clients.ANDROID],
    "margin": [clients.OUTLOOK_COM],
    "max-width": [clients.OUTLOOK],
    "min-width": [clients.OUTLOOK],
    # positioning & display
    "bottom": [clients.ALL],
    "clip": [clients.ALL],
    "cursor": [clients.ALL],
    "left": [clients.ALL],
    "opacity": [clients.OUTLOOK, clients.OUTLOOK_EXPRESS, clients.YAHOO, clients.GMAIL],
    "outline": [clients.ALL],
    "overflow": [clients.ALL],
    "position": [clients.ALL],
    "resize": [clients.ALL],
    "right": [clients.ALL],
    "top": [clients.ALL],
    "visibility": [clients.ALL],
    # lists
    "list-style-image": [clients.ALL],
}


def _get_clients_without_support(declaration):
    return INVALID_RULES.get(declaration.name)
