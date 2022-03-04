import Language_Country_Abbreviations
from googletrans import Translator


def translate(text, destination, origin=""):
    result = 0
    while result == 0:
        try:
            Trans = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'])
            if origin:
                Trans = str(Trans.translate(text, src=Language_Country_Abbreviations.language_to_code.get(origin), dest=Language_Country_Abbreviations.language_to_code.get(destination)))
            else:
                Trans = str(Trans.translate(text, dest=Language_Country_Abbreviations.language_to_code.get(destination)))
            split = Trans.index("text")
            result = 1
            return Trans[split + 5:Trans.index(", pronunciation")]
        except:
            continue
