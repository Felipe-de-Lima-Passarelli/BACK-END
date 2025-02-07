import scrapy
from fake_useragent import UserAgent

USER_AGENT = UserAgent().random

class spider(scrapy.Spider): # Definição da classe que representa a Spider.
    name = "quotes_2"  # O nome da Spider, usado para identificá-la quando executada.

    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
        "USER_AGENT": USER_AGENT
    }

    def start_requests(self):  # Função responsável por fazer as requisições iniciais na primeira página.
        yield scrapy.Request("https://quotes.toscrape.com/tag/love/page/1/")

    def parse(self, response, **kwargs):  # Função que processa a resposta da requisição.
        # Extraímos todos os blocos de citações da página usando XPath.
        blocos = response.xpath('//div[@class="quote"]')

        for bloco in blocos:
            texto = bloco.xpath('.//span[@class="text"]/text()').get()
            autor = bloco.xpath('.//small[@class="author"]/text()').get()
            tags = bloco.xpath('.//div[@class="tags"]/a/text()').getall()

            yield {
                "texto": texto,
                "autor": autor,
                "tags": tags
            }

        # Verifica se existe uma próxima página no site.
        proxima_pagina = response.xpath('//li[@class="next"]/a/@href').get()

        if proxima_pagina:
            yield response.follow(proxima_pagina, callback = self.parse) #Função responsável por trocar de página

# Comandos para rodar a Spider no terminal e salvar os dados coletados:
# Para salvar os dados em formato CSV:
# scrapy runspider "Local_do_Arquivo.py" -o Nome_Salvar.csv:csv

# Para salvar os dados em formato JSON:
# scrapy runspider "Local_do_Arquivo.py" -o Nome_Salvar.json:json

# Para ver os dados coletados diretamente no terminal sem salvar:
# scrapy runspider "Local_do_Arquivo.py" -o -:json
#exemplo -> scrapy runspider "Python\Projetos_Scrapy\Nome_Arquivo.py" -o -:json
