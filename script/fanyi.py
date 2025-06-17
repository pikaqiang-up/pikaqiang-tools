#!/usr/bin/env python3
from urllib.request import urlopen
from urllib.error import URLError
from urllib.parse import quote
from rich import print
from bs4 import BeautifulSoup
import re
import argparse

parser = argparse.ArgumentParser(
    description="A crawler tool.Translate your input by iciba.com"
)
parser.add_argument("text", type=str, help="Text that need to be translated")
parser.add_argument(
    "-e",
    "--with_example",
    action="store_true",
    help="output some example sentences.It usually very loog.",
)
parser.add_argument(
    "-v",
    "--version",
    action="version",
    version="pikaqiang'fanyi 1.0.0 (writen in 2025_04_05)",
    help="Show version",
)
args = parser.parse_args()
word = args.text

p_actions = {
    "yi": lambda word_class, word_meanings: f"[italic dim steel_blue3]{word_class}[/italic dim steel_blue3]  "
    + f"[bright_white]{word_meanings}[/bright_white]",
    "gv": lambda trans: f"[bright_white]{trans}[/bright_white]",
    "li": lambda en, cn: f"\n[bright_white]{en}[/bright_white]\n{cn}",
}


def get_main_content(html, with_example):
    soup = BeautifulSoup(html, "html.parser")
    mean_part = soup.find(re.compile("div|ul"), class_=re.compile("^Mean_part"))
    if mean_part:
        for mean_block in mean_part.find_all("li"):
            if mean_block.i:
                word_class = mean_block.i.text
            elif mean_block.span:
                word_class = mean_block.span.text
            else:
                word_class = "unknown"
            word_meanings = mean_block.div.get_text()
            print(p_actions["yi"](word_class, word_meanings))

    mean_trans = soup.find("div", class_=re.compile("^Mean_trans"))
    if mean_trans:
        print(p_actions["gv"](mean_trans.h3.next_sibling.text))
    if with_example:
        use_scene = soup.find("div", class_=re.compile("^SceneSentence_scene"))
        if use_scene:
            print("[bold deep_sky_blue3]Example sentence[/bold deep_sky_blue3]")
            for sence in use_scene.find_all("div"):
                en = sence.find("span").text
                cn = sence.find("p", re.compile(r".*?_cn.*")).text
                print(p_actions["li"](en, cn))


url = quote(f"https://www.iciba.com/word?w={word}", safe=":/?&=")
try:
    with urlopen(url) as response:
        if response.status == 200:
            content = response.read().decode("utf-8")
            get_main_content(content, args.with_example)
except URLError as e:
    print(f"[bold red]ERROR {e}[/bold red]")
