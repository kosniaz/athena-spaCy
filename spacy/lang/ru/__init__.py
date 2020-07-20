from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .lex_attrs import LEX_ATTRS
from .lemmatizer import RussianLemmatizer

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ...util import update_exc
from ...language import Language
from ...lookups import Lookups
from ...attrs import LANG


class RussianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: "ru"
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS

    @classmethod
    def create_lemmatizer(cls, nlp=None, lookups=None):
        if lookups is None:
            lookups = Lookups()
        return RussianLemmatizer(lookups)


class Russian(Language):
    lang = "ru"
    Defaults = RussianDefaults


__all__ = ["Russian"]
