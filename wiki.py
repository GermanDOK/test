import wikipedia

def get_summary(name):
    try:
        wikipedia.set_lang("ru")
        summary = wikipedia.page(name)
        return summary
    except Exception:
        return ":( Страничка не найдена"



