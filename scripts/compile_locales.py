#!/usr/bin/env python
import os
import sys

import config

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from babel.messages.frontend import main as pybabel

if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == 'mdtable':
        from libretranslate.locales import get_available_locales
        locales = get_available_locales(only_reviewed=False, sort_by_name=True)
        print("Language | Reviewed | Weblate Link")
        print("-------- | -------- | ------------")

        for l in locales:
            link = config.locales_url + "%s/" % l['code']
            if l['code'] == 'en':
                link = config.locales_url
            print("{} | {} | {}".format(l['name'], ':heavy_check_mark:' if l['reviewed'] else '', "[Edit](%s)" % link))
    else:
        if not os.path.isdir(config.locales_dir):
            os.makedirs(config.locales_dir)

        print("Compiling locales")
        sys.argv = ["", "compile", "-f", "-d", config.locales_dir]
        pybabel()



