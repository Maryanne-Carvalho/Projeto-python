from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')
        self.ln(20)

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
        self.ln(10)
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
        self.ln(10)
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 10, label, 0, 1, 'L')
        self.ln(10)

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 7, text)
        self.ln(10)

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)
        

        img_height = self.get_image_height(img, w)
        
        self.ln(img_height + 10)  

    def get_image_height(self, img, w):
        img_size = self.get_image_size(img)
        aspect_ratio = img_size['height'] / img_size['width']
        return w * aspect_ratio

    def get_image_size(self, img):
        with open(img, 'rb') as f:
            from PIL import Image
            im = Image.open(f)
            return {'width': im.width, 'height': im.height}

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()
pdf.titulo("Análise da Desigualdade Educacional no Brasil")
pdf.sub_titulo("Desafios e Desigualdades no Ensino Superior Brasileiro")
pdf.imagem("imagem_capa.jpg", 40, 100, 130)
pdf.ln(20)
pdf.linha_centralizada("Autor: Maryanne L. Carvalho")
pdf.linha_centralizada("Data: 05 de Setembro de 2024")

# ------------- Introdução ------------- 
pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A desigualdade educacional no Brasil é um desafio crítico que afeta o desenvolvimento do país. No nível de ensino superior, essa desigualdade é visível na distribuição de cursos, vagas e modalidades de ensino entre as diferentes regiões. Fatores como a localização geográfica e o tipo de instituição influenciam diretamente o acesso e a qualidade do ensino.")

pdf.paragrafo("Este relatório tem como objetivo examinar essas disparidades através de uma análise dos dados de cursos superiores no Brasil. Utilizando ferramentas de análise de dados fornecidos pelo Ministério da Educação (MEC), identificamos padrões regionais e setoriais que demonstram as desigualdades presentes no sistema educacional. A partir dessa análise, apresentamos uma visão clara e objetiva sobre as diferenças na distribuição do ensino superior no Brasil.")
# ------------- 1ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 1: Número de Cursos por Região")
pdf.paragrafo("Objetivo desta análise é identificar a distribuição de cursos por região no Brasil.")
pdf.imagem("1-grafico.png", 10, 50, 180)
pdf.paragrafo("A análise revela que as regiões Sudeste e Nordeste concentram a maior quantidade de cursos, enquanto a região Norte tem a menor oferta. Isso reflete a desigualdade na oferta de educação superior em diferentes partes do país.")

# ------------- 2ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 2: Distribuição de Vagas por Região")
pdf.paragrafo("Objetivo desta análise é visualizar a distribuição de vagas autorizadas por região no Brasil.")
pdf.imagem("2-grafico.png", 10, 50, 180)
pdf.paragrafo("A distribuição de vagas mostra que as regiões Sudeste e Nordeste têm a maior parte das vagas autorizadas, enquanto a região Norte tem menos oportunidades de acesso ao ensino superior.")

# ------------- 3ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 3: Quantidade de Vagas por Tipo de Curso")
pdf.paragrafo("Esta análise tem como objetivo avaliar a quantidade de vagas disponíveis para os cursos de Bacharelado, Licenciatura e Tecnológico no Brasil.")
pdf.imagem("7-grafico.png", 10, 50, 180)
pdf.paragrafo("A análise mostra que os cursos de Bacharelado têm a maior quantidade de vagas, seguidos pelos cursos de Licenciatura e Tecnológico. Isso pode refletir a demanda e oferta educacional para cada tipo de formação.")
# ------------- 4ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 4: Top Maiores Números de Cursos por Área OCDE")
pdf.paragrafo("Objetivo desta análise é identificar as áreas OCDE(Organização para a Cooperação e Desenvolvimento Econômico ) com o maior número de cursos oferecidos.")
pdf.imagem("3-grafico.png", 10, 50, 180)
pdf.paragrafo("As áreas de Ciências Sociais, Negócios e Direito lideram a oferta de cursos, seguidas por Educação e Saúde. Essas áreas refletem as principais demandas do mercado de trabalho e do sistema educacional brasileiro.")

# ------------- 5ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 5: Instituições por Categoria Administrativa")
pdf.paragrafo("Objetivo desta análise é avaliar a distribuição das instituições de ensino superior por categoria administrativa.")
pdf.imagem("4-grafico.png", 10, 50, 180)
pdf.paragrafo("As instituições privadas com fins lucrativos representam a maior parte das instituições de ensino superior no Brasil, enquanto as instituições públicas representam uma proporção menor.")

# ------------- 6ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 6: Distribuição de Cursos por Modalidade")
pdf.paragrafo("Objetivo desta análise é visualizar a distribuição de cursos por modalidade (presencial e a distância).")
pdf.imagem("5-grafico.png", 10, 50, 180)
pdf.paragrafo("A distribuição de cursos por modalidade mostra uma grande representação da Educação a Distância (EaD) em todas as regiões, refletindo a tendência de democratização do ensino superior.")

# ------------- 7ª página -------------
pdf.add_page()
pdf.titulo_base("Análise 7: Cursos por Região e Modalidade")
pdf.paragrafo("Objetivo desta análise é identificar a distribuição de cursos por região e modalidade.")
pdf.imagem("6-grafico.png", 10, 50, 180)
pdf.paragrafo("Observa-se que a Educação a Distância (EaD) tem grande representação em todas as regiões, o que reflete uma tendência de democratização do ensino superior.")

# ------------- 8ª página -------------
pdf.add_page()
pdf.titulo_base("Conclusão")
pdf.paragrafo("A análise mostra grandes disparidades regionais no ensino superior brasileiro, com o Sudeste e Nordeste concentrando a maioria dos cursos e vagas, enquanto o Norte tem menos oferta. A carga horária dos cursos de Bacharelado é maior do que a dos Tecnológicos e de Licenciatura. A predominância de áreas como Ciências Sociais e Negócios e a crescente importância da Educação a Distância destacam a necessidade de políticas para equilibrar a oferta educacional e expandir o acesso, especialmente nas regiões menos favorecidas.")
# ------------- Gerar o PDF -------------
pdf.output("relatorio_final.pdf")
