class Markdown:
    def __init__(self):
        self.__markdown_text = ""  

    def nadpis1(self, text):
        self.__markdown_text += f"# {text}\n\n"
        return self

    def nadpis2(self, text):
        self.__markdown_text += f"## {text}\n\n"
        return self

    def nadpis3(self, text):
        self.__markdown_text += f"### {text}\n\n"
        return self

    def odstavec(self, text):
        self.__markdown_text += f"{text}\n\n"
        return self

    def zobrazit(self):
        print(self.__markdown_text)
        return self

    def ulozit(self, soubor):
        with open(soubor, 'w', encoding='utf-8') as file:
            file.write(self.__markdown_text)
        return self


md = Markdown()
md.nadpis1("Titulní stránka")\
  .odstavec("Toto je úvodní odstavec dokumentu.")\
  .nadpis2("Podnadpis")\
  .odstavec("Tento dokument generujeme pomocí třídy Markdown.")\
  .zobrazit()

md.ulozit("dokument.md")
