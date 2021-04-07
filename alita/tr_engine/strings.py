#    Hitsuki (A telegram bot project)
#    Copyright (C) 2017-2019 Paul Larsen
#    Copyright (C) 2019-2020 Akito Mizukito (Haruka Network Development)

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import yaml
from codecs import encode, decode

from hitsuki import LOGGER
from alita.plugins.sql.locales_sql import prev_locale

LANGUAGES = ['en-US', 'pt']

strings = {}

for i in LANGUAGES:
    strings[i] = yaml.full_load(open("locales/" + i + ".yml", "r"))


def tld(chat_id, t, show_none=True):
    LANGUAGE = prev_locale(chat_id)

    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('en-US') and t in strings['en-US']:
            result = decode(
                encode(strings['en-US'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result
        elif LOCALE in ('pt') and t in strings['pt']:
            result = decode(
                encode(strings['pt'][t], 'latin-1', 'backslashreplace'),
                'unicode-escape')
            return result

    if t in strings['en-US']:
        result = decode(
            encode(strings['en-US'][t], 'latin-1', 'backslashreplace'),
            'unicode-escape')
        return result

    err = f"No string found for {t}.\nReport it to @Hitalo."
    LOGGER.warning(err)
    return err


def tld_list(chat_id, t):
    LANGUAGE = prev_locale(chat_id)

    if LANGUAGE:
        LOCALE = LANGUAGE.locale_name
        if LOCALE in ('en-US') and t in strings['en-US']:
            return strings['en-US'][t]
        elif LOCALE in ('pt') and t in strings['pt']:
            return strings['pt'][t]

    if t in strings['en-US']:
        return strings['en-US'][t]

    LOGGER.warning(f"#NOSTR No string found for {t}.")
    return f"No string found for {t}.\nReport it to @Hitalo."