import scrapy

class PrefectoSpider(scrapy.Spider):
    name = "prefecto"
    start_urls = ['https://es.wikipedia.org/wiki/Prefectos_provinciales_del_Ecuador']


    def parse(self, response):
        l = response.css('.mw-parser-output')
        tablas = l.xpath('//div/table[1]')
        tr = tablas.xpath('tbody/tr')
        for x in tr:
            lista = x.xpath('td')
            if len(lista) > 0:
                nombre = lista[2].xpath('a/text()')
                provincia = lista[3].xpath('a/text()')
                predecesor = lista[4].xpath('a/text()')
                partido = lista[5].xpath('a/text()')
                posecion = lista[6].xpath('a/text()')
                if len(nombre) > 0:
                    nombre = lista[2].xpath('a/text()').extract()[0].strip()
                else:
                    nombre = lista[2].xpath('text()').extract()[0].strip()
                if len(provincia) > 0:
                    provincia = lista[3].xpath('a/text()').extract()[0].strip()
                else:
                    provincia = lista[3].xpath('text()').extract()[0].strip()
                if len(predecesor) > 0:
                    predecesor = lista[4].xpath('a/@href').extract()
                else:
                    predecesor = lista[4].xpath('text()').extract()[0].strip()
                if len(partido) > 0:
                    partido = lista[5].xpath('a/text()').extract()[0].strip()
                else:
                    partido = lista[5].xpath('text()').extract()[0].strip()
                if len(posecion) > 0:
                    posecion = lista[6].xpath('a/text()').extract()[0].strip()
                else:
                    posecion = lista[6].xpath('text()').extract()[0].strip()
                yield {
                    'nombre': nombre,
                    'predecesor': predecesor,
                    'provincia': provincia,
                    'partido': partido,
                    'posecion': posecion,
                        }


# for l in response.css('.mw-parser-output'):
#     for i in l.xpath('//div/table[1]'):
#          provincia = i.xpath('tbody/tr/td[4]/a/text()').extract()
#          predecesor = i.xpath('tbody/tr/td[5]/a/text()').extract()
#          partido = i.xpath('tbody/tr/td[6]/a/text()').extract()
#          posecion = i.xpath('tbody/tr/td[6]/a/text()').extract()
