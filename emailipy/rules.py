from clients import OUTLOOK, OUTLOOK_EXPRESS, IPHONE, OUTLOOK_COM, APPLE_MAIL, YAHOO, GMAIL, ANDROID

# https://www.campaignmonitor.com/css/
INVALID_RULES = {
    # text & font
    "text-overflow": [OUTLOOK],
    "text-shadow": [OUTLOOK, OUTLOOK_EXPRESS, GMAIL],
    "word-wrap": [OUTLOOK, GMAIL, ANDROID],
    "text-fill-color": [OUTLOOK, OUTLOOK_EXPRESS, OUTLOOK_COM, YAHOO, GMAIL],
    "text-fill-stroke": [OUTLOOK, OUTLOOK_EXPRESS, OUTLOOK_COM, YAHOO, GMAIL],
    # color & background
    "background": [OUTLOOK, OUTLOOK_EXPRESS, OUTLOOK_COM, YAHOO, GMAIL],
    "background-image": [OUTLOOK, OUTLOOK_COM],
    "background-position": [OUTLOOK, OUTLOOK_COM, GMAIL],
    "background-repeat": [OUTLOOK, OUTLOOK_COM],
    "background-size": [OUTLOOK, OUTLOOK_EXPRESS, OUTLOOK_COM, YAHOO, GMAIL, ANDROID],
    # box model
    "border-color": [OUTLOOK, OUTLOOK_EXPRESS, ANDROID],
    "border-image": [OUTLOOK, OUTLOOK_EXPRESS, OUTLOOK_COM, YAHOO, GMAIL, ANDROID],
    "border-radius": [OUTLOOK, OUTLOOK_EXPRESS, YAHOO, ANDROID],
    "box-shadow": [OUTLOOK, OUTLOOK_EXPRESS, YAHOO, GMAIL, ANDROID],
    "margin": [OUTLOOK_COM],
    "max-width": [OUTLOOK],
    "min-width": [OUTLOOK],
    # positioning & display
    "bottom": [OUTLOOK, YAHOO, GMAIL],
    "clip": [ALL],
    "cursor": [ALL],
    "left": [ALL],
    "opacity": [OUTLOOK, OUTLOOK_EXPRESS, YAHOO, GMAIL],
    "outline": [ALL],
    "overflow": [ALL],
    "position": [ALL],
    "resize": [ALL],
    "right": [ALL],
    "top": [ALL],
    "visibility": [ALL],
    # lists
    "list-style-image": [ALL],
}