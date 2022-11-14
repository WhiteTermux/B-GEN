import pyfiglet
import rich
import random

from rich.console import Console
from rich.prompt import Prompt

console = Console()

banner = pyfiglet.figlet_format("B-GEN", font="slant")
console.print(
   f"[bold red]{banner}",
   "Creator: @qust0s",
   "Channel: @WhiteTermux",

   sep = "\n",
   style = "bold white"
)


def BannerGeneration():

    banner_text = console.input("[bold red]\nname of your banner[/]> ")
    
    get_fonts = pyfiglet.FigletFont.getFonts()
    
    try:
       count = 0
       
       many = Prompt.ask(
          "[bold red]how many generate?",
          default="10"
       )

       while count < int(many):
             random_fonts = random.choice(get_fonts)
             
             banners = pyfiglet.figlet_format(banner_text, font=random_fonts)

             count += 1
             console.print(f"[bold magenta]Banners generated[/]: [bold white][{count}]")

             file = open("banners.txt", "a")
             file.write(f"{banners}")
             file.close()
             
    except:
          console.print("[bold red][!] Failed to generate banner!")

BannerGeneration()
