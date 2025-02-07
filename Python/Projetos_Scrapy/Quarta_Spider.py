import scrapy

class spider(scrapy.Spider): # Definição da classe que representa a Spider.
    name = "livros"  # O nome da Spider, usado para identificá-la quando executada.

    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
        "USER_AGENT": "x"
    }

    def start_requests(self):  # Função responsável por fazer as requisições iniciais na primeira página.
        yield scrapy.Request("https://books.toscrape.com")

    def parse(self, response, **kwargs):  # Função que processa a resposta da requisição.
        # Extraímos todos os blocos de citações da página usando XPath.
        blocos = response.xpath('//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]')

        for bloco in blocos:
            nome_livro = bloco.xpath('.//article/h3/a/text()').get()
            custo_livro = bloco.xpath('.//article/div[2]/p[1]/text()').get()

            yield {
                "nome_livro": nome_livro,
                "custo_livro": custo_livro
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
