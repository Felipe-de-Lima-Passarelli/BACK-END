import scrapy

class spider(scrapy.Spider): # Definição da classe que representa a Spider.
    name = "Top_50_Animes"  # O nome da Spider, usado para identificá-la quando executada.

    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/116.0.0.0"
    }

    def start_requests(self):  # Função responsável por fazer as requisições iniciais na primeira página.
        yield scrapy.Request("https://myanimelist.net/topanime.php")

    def parse(self, response, **kwargs):  # Função que processa a resposta da requisição.
        # Extraímos todos os blocos de citações da página usando XPath.
        blocos = response.xpath('//tr[@class="ranking-list"]')

        for bloco in blocos:
            nome_anime = bloco.xpath('.//td[2]/div/div[2]/h3/a/text()').get()
            quantidade_episodios = bloco.xpath('.//td[2]/div/div[3]/text()[1]').get().strip()
            nota_anime = bloco.xpath('.//td[3]/div/span/text()').get()

            yield {
                "nome_anime": nome_anime,
                "quantidade_episodios": quantidade_episodios,
                "nota_anime": nota_anime
            }

# Comandos para rodar a Spider no terminal e salvar os dados coletados:
# Para salvar os dados em formato CSV:
# scrapy runspider "Local_do_Arquivo.py" -o Nome_Salvar.csv:csv

# Para salvar os dados em formato JSON:
# scrapy runspider "Local_do_Arquivo.py" -o Nome_Salvar.json:json

# Para ver os dados coletados diretamente no terminal sem salvar:
# scrapy runspider "Local_do_Arquivo.py" -o -:json
#exemplo -> scrapy runspider "Python\Projetos_Scrapy\Nome_Arquivo.py" -o -:json
