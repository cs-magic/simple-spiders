import re

from project_deepl.scripts.alfred.ds import AlfredResult, AlfredItem
from project_deepl.src.const import TERMINOLOGY_PATH
from project_deepl.src.core import callTranslationViaDeepL
from project_deepl.src.ds import TranslateInput


def inferLanguage(to_translate: str) -> TranslateInput:
    chCharsCnt = len(re.findall(r'[\u4e00-\u9fff]', to_translate))
    enCharsCnt = len(re.findall(r'[a-zA-Z]', to_translate))
    fromLang = "ZH" if chCharsCnt > enCharsCnt else "EN"
    toLang = "EN" if chCharsCnt <= enCharsCnt else "ZH"
    return {
        "text": to_translate,
        "fromLang": fromLang,
        "toLang": toLang
    }


def parseToAlfred(to_translate: str) -> AlfredResult:
    lang = inferLanguage(to_translate)
    result = callTranslationViaDeepL(
        to_translate,
        target_lang=lang["toLang"],
        from_lang=lang["fromLang"],
        terminology=TERMINOLOGY_PATH,
        plain_text=True
    )
    if result:
        item: AlfredItem = {
            "title": result
        }
        return {
            "items": [
                item
            ]
        }
