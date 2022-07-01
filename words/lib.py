import requests
import urls
from typing import Optional
from typer import style
from typer import colors


def get_request(word: str) -> Optional[dict]:
    request = requests.get(urls.URL + word)
    if request.status_code != 200:
        return None
    else:
        return request.json()


def format_output(req_result: dict, lines: Optional[int]) -> Optional[str]:
    contents = req_result[0]
    tword = style("Word: ", bold=True)
    word = style(contents["word"].title(), fg=colors.GREEN)
    tmeaning = style("Meaning:\n", fg=colors.CYAN, bold=True)
    meaning = ""
    defs = contents.get("meanings")[0]["definitions"]
    if lines is None:
        for i in defs:
            defn = i.get("definition")
            meaning += style(f"{defn}\n", fg=colors.BLUE)
    else:
        i = 0
        while i < lines:
            defn = defs[i].get("definition")
            meaning += style(f"{defn}\n", fg=colors.BLUE)
            i += 1
    return tword + word + "\n" + tmeaning + meaning
