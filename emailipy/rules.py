import clients

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