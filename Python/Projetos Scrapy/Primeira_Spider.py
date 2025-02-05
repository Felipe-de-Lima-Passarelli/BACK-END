import scrapy

class primeira_spider(scrapy.Spider): #propriedade obrigatória
    name = "q" #Nome é obrigatório
    pagina_atual = 1 #Variável para conseguirmos interar o site inteiro

    def start_requests(self): #Função para iniciar a URL do site desejado
        yield scrapy.Request("https://quotes.toscrape.com/page/1") #URL

    def parse(self, response, **kwargs): #Função para fazer a raspagem do site
        blocos = response.xpath('//div[@class="quote"]')
        for bloco in blocos:
            texto = bloco.xpath('./span[@class="text"]/text()').get()
            autor = bloco.xpath('.//small/text()').get()
            tags = bloco.xpath('.//a[@class="tag"]/text()').getall()
            yield {
                "texto": texto,
                "autor": autor,
                "tags": tags
            }
        proxima_pagina = response.xpath('//li[@class="next"]/a')

        if proxima_pagina:
            self.pagina_atual += 1
            yield scrapy.Request('https://quotes.toscrape.com/page/' + str(self.pagina_atual),
                                 callback = self.parse)

#Comandos para executar no terminal e ver os dados adquiridos
#scrapy runspider "Nome_do_Arquivo.py" -o "Nome_para_Salvar."formato":"formato"
#scrapy runspider "Primeira_Spider.py" -o Primeira_Spider.csv:csv
#scrapy runspider "Primeira_Spider.py" -o Primeira_Spider.json:json
