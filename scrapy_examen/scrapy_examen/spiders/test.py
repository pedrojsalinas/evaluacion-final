import pandas as pd
import scrapy

#lectura de csv
df=pd.read_csv('datos.csv')
df['predecesor'] ='https://es.wikipedia.org'+df['predecesor']
df= df.dropna()
df1 =df[df['tipo']==1]

class ExamenSpider(scrapy.Spider):
    name = "examen"
    def start_requests(self):
        for url in df['predecesor']:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        # seleccion de tipo de url

        tipo = df.where(df['predecesor'] == response.url)
        tipo= tipo.dropna()
        tipo = tipo['tipo']
        for t in tipo:
            tipo = t
        l = response.css('#mw-content-text')
        tablas = l.xpath('//div/table')
        tr = tablas.xpath('tbody/tr')
        #h1 que contiene nombre de provincia
        provincia = response.css('.firstHeading ::text').extract_first().replace('Anexo:Prefectos de ','')
        #condiciones dependiendo del tipo de url
        for x in tr:
            lista = x.xpath('td')
            if (len(lista) > 0):
                if(tipo==0):
                    nombre = lista[0].xpath('a/text()')
                    inicio = lista[1].xpath('text()')
                    fin = lista[2].xpath('text()').extract()[0].strip()
                    if len(nombre) > 0:
                        nombre = lista[0].xpath('a/text()').extract()[0].strip()
                    else:
                        nombre = lista[0].xpath('text()').extract()[0].strip()
                    if len(inicio) > 0:
                        inicio = lista[1].xpath('text()').extract()[0].strip()
                    else:
                        inicio = lista[1].xpath('text()').extract()[0].strip()
                    if len(fin) > 0:
                        fin = lista[2].xpath('text()').extract()[0].strip()
                    else:
                        fin = lista[2].xpath('text()').extract()[0].strip()
                    yield {
                        'nombre': nombre,
                        'inicio': inicio,
                        'fin': fin,
                        'provincia': provincia,
                            }
                if(tipo==1):
                    lista_th = tr.xpath('th')
                    if (len(lista) > 0):
                        nombre = lista.xpath('a/text()').extract()
                        periodo = lista_th[0].xpath('text()').extract()[0]
                        fin=periodo[7:].replace('?','Actualidad').strip('\n')
                        yield {
                            'nombre': nombre,
                            'inicio': periodo[0:5].strip(),
                            'fin': fin,
                            'provincia': provincia,
                                }
                if(tipo==2):
                    nombre = lista[0].xpath('a/text()')
                    inicio = lista[2].xpath('text()')
                    fin = lista[3].xpath('text()').extract()[0].strip()
                    if len(nombre) > 0:
                        nombre = lista[0].xpath('a/text()').extract()[0].strip()
                    else:
                        nombre = lista[0].xpath('text()').extract()[0].strip()
                    if len(inicio) > 0:
                        inicio = lista[2].xpath('text()').extract()[0].strip()
                    else:
                        inicio = lista[2].xpath('text()').extract()[0].strip()
                    if len(fin) > 0:
                        fin = lista[3].xpath('text()').extract()[0].strip()
                    else:
                        fin = lista[3].xpath('text()').extract()[0].strip()
                    yield {
                        'nombre': nombre,
                        'inicio': inicio,
                        'fin': fin,
                        'provincia': provincia,
                            }
                elif(tipo==3):
                    nombre = lista[1].xpath('a/text()')
                    inicio = lista[2].xpath('text()')
                    fin = lista[3].xpath('text()').extract()[0].strip()
                    if len(nombre) > 0:
                        nombre = lista[1].xpath('a/text()').extract()[0].strip()
                    else:
                        nombre = lista[1].xpath('text()').extract()[0].strip()
                    if len(inicio) > 0:
                        inicio = lista[2].xpath('text()').extract()[0].strip()
                    else:
                        inicio = lista[2].xpath('text()').extract()[0].strip()
                    if len(fin) > 0:
                        fin = lista[3].xpath('text()').extract()[0].strip()
                    else:
                        fin = lista[3].xpath('text()').extract()[0].strip()
                    yield {
                        'nombre': nombre,
                        'inicio': inicio,
                        'fin': fin,
                        'provincia': provincia,
                            }
