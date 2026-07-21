"""
Space AI 2.0

Spaceman Protocol Constants

Constantes utilizadas por el protocolo de comunicación del juego Spaceman.

Este módulo centraliza todas las cadenas, claves y expresiones regulares
utilizadas por SpacemanProtocolParser.

No contiene lógica de negocio.

Autor: Space AI 2.0
"""

from __future__ import annotations

import re
from typing import Final

#
# Eventos del protocolo
#

STATISTIC_HISTORY_EVENT: Final[str] = "SpaceManStatisticHistory"

#
# Claves JSON
#

HISTORY_KEY: Final[str] = "history"

GAME_ID_KEY: Final[str] = "gameId"

GAME_RESULT_KEY: Final[str] = "gameResult"

#
# Atributos XML
#

ROUND_RESULT_ATTRIBUTE: Final[str] = "result"

ROUND_ID_ATTRIBUTE: Final[str] = "gId"

#
# Expresiones regulares
#

ROUND_RESULT_PATTERN: Final[re.Pattern[str]] = re.compile(
    r"<gr\b"
    r'[^>]*\bgId="(?P<game_id>\d+)"'
    r'[^>]*\bresult="(?P<result>[0-9]+(?:\.[0-9]+)?)"'
)

#
# Mensajes ignorados
#

IGNORED_PREFIXES: Final[frozenset[str]] = frozenset(
    {
        "2",
        "3",
        "40",
        "42",
    }
)

#
# Tipos MIME aceptados
#

JSON_CONTENT_TYPE: Final[str] = "application/json"

#
# Valores por defecto
#

DEFAULT_EVENT_SOURCE: Final[str] = "websocket"
