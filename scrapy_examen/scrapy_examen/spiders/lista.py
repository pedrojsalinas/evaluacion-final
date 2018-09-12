# import scrapy
# import csv
# import pandas as pd
# lista1=[]
# lista2=[]
# listaEnlaces1=[]
# listaEnlaces2=[]
#
# with open('data.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if (row['predecesor']!= ''):
#             if(row['tipo']== '1'):
#                 lista1.append(row['predecesor'])
#             else:
#                 lista2.append(row['predecesor'])
#
#     for l in lista1:
#         listaEnlaces1.append('https://es.wikipedia.org'+l)
#     for l in lista2:
#         listaEnlaces2.append('https://es.wikipedia.org'+l)
#
# # class PrefectoSpider(scrapy.Spider):
# #     name = "lista"
# #     start_urls = listaEnlaces1
# #
# #
# #     def parse(self, response):
# #         l = response.css('#mw-content-text')
# #         tablas = l.xpath('//div/table')
# #         tr = tablas.xpath('tbody/tr')
# #         for x in tr:
# #             lista = x.xpath('td')
# #             if (len(lista) > 0):
# #                 nombre = lista[0].xpath('a/text()')
# #                 inicio = lista[2].xpath('text()')
# #                 fin = lista[3].xpath('text()').extract()[0].strip()
# #                 if len(nombre) > 0:
# #                     nombre = lista[0].xpath('a/text()').extract()[0].strip()
# #                 else:
# #                     nombre = lista[0].xpath('text()').extract()[0].strip()
# #                 if len(inicio) > 0:
# #                     inicio = lista[2].xpath('text()').extract()[0].strip()
# #                 else:
# #                     inicio = lista[2].xpath('text()').extract()[0].strip()
# #                 if len(fin) > 0:
# #                     fin = lista[3].xpath('text()').extract()[0].strip()
# #                 else:
# #                     fin = lista[3].xpath('text()').extract()[0].strip()
# #                 yield {
# #                     'nombre': nombre,
# #                     'inicio': inicio,
# #                     'fin': fin,
# #                     'provincia': response.css('.firstHeading ::text').extract_first().replace('Anexo:Prefectos de ',''),
# #                         }
#
#
# class PrefectoSpider(scrapy.Spider):
#     name = "lista"
#     start_urls = listaEnlaces1
#
#
#     def parse(self, response):
#         l = response.css('#mw-content-text')
#         tablas = l.xpath('//div/table')
#         tr = tablas.xpath('tbody/tr')
#         provincia = response.css('.firstHeading ::text').extract_first().replace('Anexo:Prefectos de ','')
#         l1 = []
#         lista_th = tr.xpath('th')
#         for x in tr:
#             lista = x.xpath('td')
#             if (len(lista) > 0):
#                 nombre = lista.xpath('a/text()').extract()
#                 periodo = lista_th[0].xpath('text()').extract()[0]
#                 # inicio=periodo[0:5].strip()
#                 # inicio = inicio.strip('\n')
#                 fin=periodo[7:].replace('?','Actualidad').strip('\n')
#                 yield {
#                     'nombre': nombre,
#                     'inicio': periodo[0:5].strip(),
#                     'fin': fin,
#                     'provincia': provincia,
#                         }
#
#
# # for l in response.css('.wikitable'):
# #     print(l.xpath('tbody/tr/td[2]/a/text()').extract())
# #     print(l.xpath('tbody/tr/td[3]/text()').extract())
# #     print(l.xpath('tbody/tr/td[4]/text()').extract())
