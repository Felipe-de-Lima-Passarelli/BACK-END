import scrapy

class spider(scrapy.Spider): # Definição da classe que representa a Spider.
    name = "q"  # O nome da Spider, usado para identificá-la quando executada.

    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
        "USER_AGENT": "x"
    }

    def start_requests(self):  # Função responsável por fazer as requisições iniciais na primeira página.
        yield scrapy.Request("https://quotes.toscrape.com/page/1")

    def parse(self, response, **kwargs):  # Função que processa a resposta da requisição.
        # Extraímos todos os blocos de citações da página usando XPath.
        blocos = response.xpath('//div[@class="quote"]')

        for bloco in blocos:
            texto = bloco.xpath('.//span[@class="text"]/text()').get()  # O texto da citação.
            autor = bloco.xpath('.//small/text()').get()  # O nome do autor da citação.
            tags = bloco.xpath('.//a[@class="tag"]/text()').getall()  # As tags associadas à citação.

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
