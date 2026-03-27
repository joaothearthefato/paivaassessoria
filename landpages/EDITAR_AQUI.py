#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Landing Pages — PAIVA Assessoria & Marketing
Edite apenas o bloco INFLUENCERS abaixo para personalizar cada página.
"""

import os

# ══════════════════════════════════════════════════════════════════════════════
#  ✏️  DADOS DOS INFLUENCERS — EDITE AQUI
#  Cada dicionário = 1 página completa.
# ══════════════════════════════════════════════════════════════════════════════

INFLUENCERS = [

    # ──────────────────────────────────────────────────────────────────────────
    # 1. CAROL
    # ──────────────────────────────────────────────────────────────────────────
    {
        # ── IDENTIDADE ──────────────────────────────────────────────────────
        "id":           "carol",                        # nome do arquivo .html
        "nome":         "Carol",                        # nome exibido no site
        "nome_completo":"Ana Carol Lima",               # nome completo
        "arroba":       "@eu.carollimah",               # @ do Instagram
        "nicho":        "Lifestyle · Rotina",           # nicho principal
        "subtitulo":    "Influencer Digital",           # linha abaixo do nome
        "cidade":       "Manaus · São Paulo · São José dos Campos",

        # ── IMAGENS ─────────────────────────────────────────────────────────
        # Coloque o caminho relativo da imagem (ex: "./img/carol_hero.jpg")
        # Deixe "" para mostrar o placeholder dourado
        "img_hero":      "./img/carol_hero.jpg",        # foto principal (hero)
        "img_sobre":     "./img/carol_sobre.jpg",       # foto seção "Sobre"
        "img_portfolio1":"./img/carol_camp1.jpg",       # campanha 1
        "img_portfolio2":"./img/carol_camp2.jpg",       # campanha 2
        "img_portfolio3":"./img/carol_camp3.jpg",       # campanha 3

        # ── CONTATO ─────────────────────────────────────────────────────────
        "whatsapp":     "5500000000000",                # número com código país
        "email":        "",                             # email comercial (opcional)
        "instagram_url":"https://www.instagram.com/eu.carollimah/",

        # ── BIO ─────────────────────────────────────────────────────────────
        "bio_p1": "Carol é criadora de conteúdo com forte presença digital, gerando 367 mil visualizações por mês e alto engajamento em Reels (até 81%) e Stories (até 67%). Uma voz autêntica que transforma parcerias em resultados mensuráveis.",
        "bio_p2": "Seu público é 62,5% feminino, faixa predominante de 25 a 44 anos, concentrado em Manaus, São Paulo e São José dos Campos.",
        "tagline": "Transforme sua marca com influência real e resultados que aparecem nos números.",

        # ── MÉTRICAS (cards animados) ────────────────────────────────────────
        # "valor" pode ser número inteiro, decimal ou texto fixo
        "metricas": [
            {"icone":"💥", "valor":"25941",  "sufixo":"",  "label":"Interações Totais",   "sub":"Últimos 30 dias"},
            {"icone":"👁️", "valor":"8528",   "sufixo":"",  "label":"Contas Alcançadas",   "sub":"Últimos 30 dias"},
            {"icone":"📈", "valor":"367964", "sufixo":"",  "label":"Visualizações",        "sub":"Últimos 30 dias"},
            {"icone":"💬", "valor":"872",    "sufixo":"",  "label":"Comentários",          "sub":"4.537 curtidas · 8.040 compartilhamentos"},
        ],

        # ── HERO STATS (3 números no card flutuante) ─────────────────────────
        "hero_stats": [
            {"numero":"367,9K", "label":"Visualizações"},
            {"numero":"8,5K",   "label":"Alcance mensal"},
            {"numero":"62,5%",  "label":"Público feminino"},
        ],

        # ── TAGS DO PERFIL ───────────────────────────────────────────────────
        "tags": ["Lifestyle","Moda","Emagrecimento","Rotina","Divulgação","Diversão"],

        # ── PORTFÓLIO (3 cards) ──────────────────────────────────────────────
        "portfolio": [
            {"titulo":"Campanha Verão",       "categoria":"Lifestyle & Moda"},
            {"titulo":"Lançamento de Produto", "categoria":"Divulgação Premium"},
            {"titulo":"Conteúdo de Rotina",   "categoria":"Lifestyle Diário"},
        ],

        # ── SERVIÇOS ─────────────────────────────────────────────────────────
        "servicos": [
            {"icone":"📱", "titulo":"Feed & Publipost",       "desc":"Publicações estratégicas no feed com fotografia de alta qualidade e copy persuasivo, alinhados à identidade visual da sua marca."},
            {"icone":"⚡", "titulo":"Stories Patrocinados",   "desc":"Conteúdo dinâmico e autêntico nos stories com link direto para seu produto ou serviço, gerando conversão imediata."},
            {"icone":"🎬", "titulo":"Reels & TikTok",         "desc":"Vídeos virais criativos com potencial de alcance orgânico exponencial, apresentando sua marca de forma natural e envolvente."},
            {"icone":"💎", "titulo":"Campanha Completa",       "desc":"Pacote completo com planejamento estratégico, produção de conteúdo em múltiplos formatos e relatório de resultados detalhado."},
        ],

        # ── PÚBLICO ─────────────────────────────────────────────────────────
        "publico_genero":"62,5% feminino · 37,5% masculino",
        "publico_idade": "Predominante: 25 a 44 anos",
        "publico_local": "Manaus · São Paulo · São José dos Campos",

        # ── DISTRIBUIÇÃO DE CONTEÚDO ─────────────────────────────────────────
        "conteudo": [
            {"formato":"Stories", "pct":"67%"},
            {"formato":"Reels",   "pct":"81%"},
            {"formato":"Posts",   "pct":"15%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 2. IQUIARA
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "iquiara",
        "nome":         "Iquiara",
        "nome_completo":"Iquiara Machado",
        "arroba":       "@iquiaraa",
        "nicho":        "Plus Size · Dança · Empoderamento",
        "subtitulo":    "Influencer Digital",
        "cidade":       "São José dos Campos – SP",

        "img_hero":      "./img/iquiara_hero.jpg",
        "img_sobre":     "./img/iquiara_sobre.jpg",
        "img_portfolio1":"./img/iquiara_camp1.jpg",
        "img_portfolio2":"./img/iquiara_camp2.jpg",
        "img_portfolio3":"./img/iquiara_camp3.jpg",

        "whatsapp":     "5512982602098",
        "email":        "iquiaramachado@gmail.com",
        "instagram_url":"https://www.instagram.com/iquiaraa/",

        "bio_p1": "Iquiara é influenciadora digital e criadora de conteúdo com foco no nicho plus size, dança e empoderamento. Natural de São José dos Campos, ela conecta marcas a uma audiência apaixonada e altamente engajada.",
        "bio_p2": "Seu objetivo é estimular as pessoas a se amarem como são, independente de julgamentos alheios — e fazer o que gostam sem medo de ser feliz.",
        "tagline": "Se ame como é, dance com alegria e inspire quem está ao seu redor.",

        "metricas": [
            {"icone":"👥", "valor":"27954",  "sufixo":"",   "label":"Seguidores",          "sub":"Instagram"},
            {"icone":"💫", "valor":"10.19",  "sufixo":"%",  "label":"Taxa de Engajamento",  "sub":"Acima da média do setor"},
            {"icone":"📈", "valor":"342848", "sufixo":"",   "label":"Alcance",              "sub":"Últimos 7 dias"},
            {"icone":"💬", "valor":"378",    "sufixo":"",   "label":"Comentários/Post",     "sub":"Média por publicação"},
        ],

        "hero_stats": [
            {"numero":"27,9K", "label":"Seguidores"},
            {"numero":"10,19%","label":"Engajamento"},
            {"numero":"342K",  "label":"Alcance semanal"},
        ],

        "tags": ["Plus Size","Dança","Empoderamento","Moda","Beleza","Eventos e Festivais"],

        "portfolio": [
            {"titulo":"Campanha Plus Size",   "categoria":"Moda & Empoderamento"},
            {"titulo":"Skincare Inclusivo",   "categoria":"Beleza & Autoestima"},
            {"titulo":"Festival de Dança",    "categoria":"Eventos & Cultura"},
        ],

        "servicos": [
            {"icone":"💆", "titulo":"Reviews de Produtos",     "desc":"Avaliações honestas e detalhadas com storytelling envolvente e alta credibilidade junto ao público plus size."},
            {"icone":"📹", "titulo":"Tutoriais Patrocinados",  "desc":"Conteúdo educativo passo a passo apresentando seu produto de forma natural e convertendo seguidoras em clientes."},
            {"icone":"✨", "titulo":"Stories & Reels",         "desc":"Revelações de produtos com alto potencial viral gerando expectativa, desejo imediato e engajamento real."},
            {"icone":"🌟", "titulo":"Embaixadora de Marca",    "desc":"Parceria de longo prazo representando a marca em todos os formatos de conteúdo com autenticidade."},
        ],

        "publico_genero":"Majoritariamente feminino",
        "publico_idade": "18–24 e 25–34 anos (predominante)",
        "publico_local": "São José dos Campos · São Paulo · Rio de Janeiro · Recife · Belo Horizonte",

        "conteudo": [
            {"formato":"Stories", "pct":"~50%"},
            {"formato":"Reels",   "pct":"~35%"},
            {"formato":"Posts",   "pct":"~15%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 3. MARIA EDUARDA
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "maria_eduarda",
        "nome":         "Maria Eduarda",
        "nome_completo":"Maria Eduarda Martins Matos",
        "arroba":       "@dudammatoss",
        "nicho":        "Country · Moda Sertaneja",
        "subtitulo":    "Influencer Digital",
        "cidade":       "Jacareí · São José dos Campos · Guararema",

        "img_hero":      "./img/mariaeduarda_hero.jpg",
        "img_sobre":     "./img/mariaeduarda_sobre.jpg",
        "img_portfolio1":"./img/mariaeduarda_camp1.jpg",
        "img_portfolio2":"./img/mariaeduarda_camp2.jpg",
        "img_portfolio3":"./img/mariaeduarda_camp3.jpg",

        "whatsapp":     "5500000000002",
        "email":        "",
        "instagram_url":"https://www.instagram.com/dudammatoss/",

        "bio_p1": "Maria Eduarda Martins Matos gera mais de 60 mil visualizações por período com alcance crescente — 53,8% do público são não seguidores, indicando forte potencial de descoberta orgânica para marcas.",
        "bio_p2": "Audiência 77,9% feminina, concentrada na faixa 25–34 anos (42,4%) e 18–24 anos (32,7%), em Jacareí, SJC e Guararema — público jovem, ativo e engajado.",
        "tagline": "Inspire sua audiência com autenticidade, estilo e o melhor da cultura sertaneja.",

        "metricas": [
            {"icone":"📈", "valor":"60309",  "sufixo":"",  "label":"Visualizações",       "sub":"Período recente"},
            {"icone":"👁️", "valor":"11175",  "sufixo":"",  "label":"Contas Alcançadas",   "sub":"53,8% não seguidores"},
            {"icone":"🔍", "valor":"1089",   "sufixo":"",  "label":"Visitas ao Perfil",   "sub":"Reels: 31,5% · Stories: 57,5%"},
            {"icone":"👩", "valor":"77",     "sufixo":"%", "label":"Público Feminino",    "sub":"Faixa 25–34 anos: 42,4%"},
        ],

        "hero_stats": [
            {"numero":"60,3K", "label":"Visualizações"},
            {"numero":"11,1K", "label":"Contas alcançadas"},
            {"numero":"77,9%", "label":"Público feminino"},
        ],

        "tags": ["Country","Moda Sertaneja","Artes Marciais","Viagens","Skincare","Eventos e Festivais"],

        "portfolio": [
            {"titulo":"Look Country",         "categoria":"Moda & Estilo"},
            {"titulo":"Festival Sertanejo",   "categoria":"Eventos & Cultura"},
            {"titulo":"Lifestyle do Interior","categoria":"Rotina & Autenticidade"},
        ],

        "servicos": [
            {"icone":"👗", "titulo":"Publipost de Moda",       "desc":"Publicações de moda country e sertaneja com estética autêntica que conecta sua marca ao público apaixonado por essa cultura."},
            {"icone":"🎵", "titulo":"Conteúdo de Eventos",     "desc":"Cobertura de festas, rodeios e festivais sertanejos com alto engajamento e alcance regional estratégico."},
            {"icone":"🎬", "titulo":"Reels & Stories",         "desc":"Vídeos e stories dinâmicos com trilha sertaneja e edição que geram identidade e conexão emocional com o público."},
            {"icone":"💎", "titulo":"Campanha Completa",        "desc":"Pacote com planejamento, produção e relatório, perfeito para marcas de moda, acessórios, farmácia e eventos."},
        ],

        "publico_genero":"77,9% feminino · 22,1% masculino",
        "publico_idade": "25–34 anos: 42,4% · 18–24 anos: 32,7% · 35–44: 16,1%",
        "publico_local": "Jacareí · São José dos Campos · Guararema",

        "conteudo": [
            {"formato":"Stories", "pct":"57,5%"},
            {"formato":"Reels",   "pct":"31,5%"},
            {"formato":"Posts",   "pct":"11%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 4. NICOLAS
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "nicolas",
        "nome":         "Nicolas",
        "nome_completo":"Nicolas Florentino",
        "arroba":       "@nicflorentino",
        "nicho":        "Lifestyle · Cultura Pop",
        "subtitulo":    "Influencer Digital",
        "cidade":       "Jacareí · São José dos Campos · São Paulo · Rio de Janeiro",

        "img_hero":      "./img/nicolas_hero.jpg",
        "img_sobre":     "./img/nicolas_sobre.jpg",
        "img_portfolio1":"./img/nicolas_camp1.jpg",
        "img_portfolio2":"./img/nicolas_camp2.jpg",
        "img_portfolio3":"./img/nicolas_camp3.jpg",

        "whatsapp":     "5500000000004",
        "email":        "",
        "instagram_url":"https://www.instagram.com/nicflorentino/",

        "bio_p1": "Nicolas é criador de conteúdo com alcance extraordinário: 2,29 milhões de visualizações e 305 mil contas alcançadas, com Reels (39,1%) e Stories (46,2%) como principais formatos.",
        "bio_p2": "Audiência 56% masculina e 44% feminina, distribuída por Jacareí, São José dos Campos, São Paulo e Rio de Janeiro — alcance nacional expressivo.",
        "tagline": "Conecte sua marca a 2,29 milhões de visualizações com conteúdo que realmente engaja.",

        "metricas": [
            {"icone":"📈", "valor":"2290000", "sufixo":"",  "label":"Visualizações",        "sub":"2,29 milhões — alcance massivo"},
            {"icone":"👁️", "valor":"305833",  "sufixo":"",  "label":"Contas Alcançadas",    "sub":"305 mil pessoas impactadas"},
            {"icone":"🔍", "valor":"4811",    "sufixo":"",  "label":"Visitas ao Perfil",    "sub":"80 cliques em links"},
            {"icone":"💬", "valor":"2635",    "sufixo":"",  "label":"Interações",           "sub":"2.038 curtidas · 299 comentários · 230 compartilhamentos"},
        ],

        "hero_stats": [
            {"numero":"2,29M", "label":"Visualizações"},
            {"numero":"305K",  "label":"Contas alcançadas"},
            {"numero":"4.811", "label":"Visitas ao perfil"},
        ],

        "tags": ["Lifestyle","Moda","Skincare","Restaurantes","Beleza","Farmácia","Hospedagem","Pet","Viagens"],

        "portfolio": [
            {"titulo":"Lifestyle & Cultura",  "categoria":"Conteúdo Premium"},
            {"titulo":"Review de Produto",    "categoria":"Beleza & Farmácia"},
            {"titulo":"Viagem & Hospedagem",  "categoria":"Travel Content"},
        ],

        "servicos": [
            {"icone":"💻", "titulo":"Publipost & Reviews",    "desc":"Publicações e avaliações com alta credibilidade junto a uma audiência diversa e engajada em múltiplos nichos."},
            {"icone":"🎬", "titulo":"Reels Virais",           "desc":"Vídeos com alto potencial de viralização — formato que representa 39,1% do conteúdo e gera alcance orgânico massivo."},
            {"icone":"📲", "titulo":"Stories & Links",        "desc":"Stories com link direto gerando cliques e conversão — 46,2% do conteúdo, audiência fiel e ativa."},
            {"icone":"🚀", "titulo":"Campanha Completa",      "desc":"Cobertura em múltiplas plataformas e formatos para lançamentos que precisam de impacto máximo."},
        ],

        "publico_genero":"56% masculino · 44% feminino",
        "publico_idade": "Diversificado entre 18 e 35 anos",
        "publico_local": "Jacareí · São José dos Campos · São Paulo · Rio de Janeiro",

        "conteudo": [
            {"formato":"Stories", "pct":"46,2%"},
            {"formato":"Reels",   "pct":"39,1%"},
            {"formato":"Posts",   "pct":"14,7%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 5. RENATA
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "renata",
        "nome":         "Renata",
        "nome_completo":"Renata Porto",
        "arroba":       "@renataporto2212",
        "nicho":        "Produtividade · Maternidade",
        "subtitulo":    "Influencer Digital",
        "cidade":       "São José dos Campos · Rio de Janeiro",

        "img_hero":      "./img/renata_hero.jpg",
        "img_sobre":     "./img/renata_sobre.jpg",
        "img_portfolio1":"./img/renata_camp1.jpg",
        "img_portfolio2":"./img/renata_camp2.jpg",
        "img_portfolio3":"./img/renata_camp3.jpg",

        "whatsapp":     "5500000000003",
        "email":        "",
        "instagram_url":"https://www.instagram.com/renataporto2212/",

        "bio_p1": "Renata gera 79 mil visualizações com audiência fiel (74,8% seguidores) e forte presença em Stories (90,9%). Conteúdo autêntico que cria conexão real e duradoura com o público.",
        "bio_p2": "Audiência concentrada em São José dos Campos e Rio de Janeiro, com 578 interações e 171 novos seguidores conquistados no período analisado.",
        "tagline": "Conexão real, conteúdo autêntico e uma audiência fiel que confia em cada recomendação.",

        "metricas": [
            {"icone":"📈", "valor":"79436",  "sufixo":"",  "label":"Visualizações",       "sub":"Período recente"},
            {"icone":"👁️", "valor":"8163",   "sufixo":"",  "label":"Contas Alcançadas",   "sub":"74,8% seguidores fiéis"},
            {"icone":"💥", "valor":"578",    "sufixo":"",  "label":"Interações",          "sub":"Stories: 90,9% do conteúdo"},
            {"icone":"🌟", "valor":"171",    "sufixo":"",  "label":"Novos Seguidores",    "sub":"942 visitas ao perfil · 21 cliques"},
        ],

        "hero_stats": [
            {"numero":"79,4K", "label":"Visualizações"},
            {"numero":"8,1K",  "label":"Contas alcançadas"},
            {"numero":"74,8%", "label":"Seguidores fiéis"},
        ],

        "tags": ["Saúde","Maternidade","Estudos","Emagrecimento","Lifestyle","Produtividade"],

        "portfolio": [
            {"titulo":"Rotina de Mãe",        "categoria":"Maternidade & Lifestyle"},
            {"titulo":"Produtividade no Dia",  "categoria":"Estudos & Organização"},
            {"titulo":"Saúde em Família",      "categoria":"Bem-Estar & Emagrecimento"},
        ],

        "servicos": [
            {"icone":"🍼", "titulo":"Conteúdo de Maternidade", "desc":"Posts e vídeos sobre rotina de mãe inserindo sua marca de forma natural em um contexto de alta confiança e identificação."},
            {"icone":"📚", "titulo":"Produtividade & Estudos",  "desc":"Conteúdo sobre organização, estudos e rotina que conecta marcas de papelaria, cursos, apps e estilo de vida."},
            {"icone":"⚡", "titulo":"Stories no Cotidiano",    "desc":"Stories diários com 90,9% do conteúdo — o formato mais forte da Renata, com audiência fiel e altamente engajada."},
            {"icone":"💎", "titulo":"Campanha Completa",        "desc":"Planejamento completo para marcas que querem uma parceria imersiva com relatório de resultados ao final."},
        ],

        "publico_genero":"Majoritariamente feminino",
        "publico_idade": "25–44 anos (predominante)",
        "publico_local": "São José dos Campos · Rio de Janeiro",

        "conteudo": [
            {"formato":"Stories", "pct":"90,9%"},
            {"formato":"Posts",   "pct":"7,5%"},
            {"formato":"Reels",   "pct":"1,6%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 6. THIAGO BARCELOS
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "thiago_barcelos",
        "nome":         "Thiago Barcelos",
        "nome_completo":"Thiago Barcelos",
        "arroba":       "@barccelos",
        "nicho":        "Lifestyle · Moda",
        "subtitulo":    "Influencer Digital",
        "cidade":       "São Paulo · Rio de Janeiro · São José dos Campos",

        "img_hero":      "./img/thiago_hero.jpg",
        "img_sobre":     "./img/thiago_sobre.jpg",
        "img_portfolio1":"./img/thiago_camp1.jpg",
        "img_portfolio2":"./img/thiago_camp2.jpg",
        "img_portfolio3":"./img/thiago_camp3.jpg",

        "whatsapp":     "5500000000005",
        "email":        "",
        "instagram_url":"https://www.instagram.com/barccelos/",

        "bio_p1": "Thiago Barcelos gera 186 mil visualizações com 13,2 mil interações e 1.800 novos seguidores por período. Audiência majoritariamente masculina (86%) e altamente engajada com conteúdo de lifestyle e moda.",
        "bio_p2": "Público 86% masculino, faixa 25–34 anos (62,1%) e 18–24 anos (16,7%), distribuído em São Paulo, Rio de Janeiro e São José dos Campos. 10.643 curtidas e 679 salvamentos por período.",
        "tagline": "Estilo, atitude e conteúdo que engaja o público masculino de verdade.",

        "metricas": [
            {"icone":"📈", "valor":"186300",  "sufixo":"",  "label":"Visualizações",        "sub":"186,3 mil no período"},
            {"icone":"💥", "valor":"13200",   "sufixo":"",  "label":"Interações",           "sub":"1.800 novos seguidores"},
            {"icone":"🔍", "valor":"8788",    "sufixo":"",  "label":"Visitas ao Perfil",    "sub":"Posts: 60,4% · Stories: 39,3%"},
            {"icone":"👍", "valor":"11271",   "sufixo":"",  "label":"Curtidas + Saves",     "sub":"10.643 curtidas · 679 salvamentos"},
        ],

        "hero_stats": [
            {"numero":"186,3K","label":"Visualizações"},
            {"numero":"13,2K", "label":"Interações"},
            {"numero":"86%",   "label":"Público masculino"},
        ],

        "tags": ["Lifestyle","Moda","Comida","Viagens","Skincare","Beleza","Dump","Eventos","Artesanato"],

        "portfolio": [
            {"titulo":"Look do Dia",          "categoria":"Moda & Estilo Masculino"},
            {"titulo":"Gastronomia & Viagem", "categoria":"Lifestyle Premium"},
            {"titulo":"Skincare Masculino",   "categoria":"Beleza & Cuidados"},
        ],

        "servicos": [
            {"icone":"👔", "titulo":"Publipost de Moda",       "desc":"Publicações de estilo masculino com estética premium que apresenta sua marca a um público engajado e fiel."},
            {"icone":"🍽️", "titulo":"Food & Lifestyle",        "desc":"Conteúdo de gastronomia, viagens e experiências com alto apelo visual e alcance nacional."},
            {"icone":"🎬", "titulo":"Posts & Stories",         "desc":"Posts no feed (60,4% do conteúdo) e stories com forte engajamento — 302 comentários e 679 salvamentos por período."},
            {"icone":"💎", "titulo":"Campanha Completa",        "desc":"Campanha imersiva com storytelling de lifestyle, cobertura em múltiplos formatos e relatório final detalhado."},
        ],

        "publico_genero":"86% masculino · 14% feminino",
        "publico_idade": "25–34 anos: 62,1% · 18–24 anos: 16,7%",
        "publico_local": "São Paulo · Rio de Janeiro · São José dos Campos",

        "conteudo": [
            {"formato":"Posts",   "pct":"60,4%"},
            {"formato":"Stories", "pct":"39,3%"},
            {"formato":"Reels",   "pct":"~20%"},
        ],
    },

    # ──────────────────────────────────────────────────────────────────────────
    # 7. EGIDIO
    # ──────────────────────────────────────────────────────────────────────────
    {
        "id":           "egidio",
        "nome":         "Egídio",
        "nome_completo":"Egidio Coimbra",
        "arroba":       "@egiih",
        "nicho":        "Fashion · Makeup",
        "subtitulo":    "Influencer Digital",
        "cidade":       "Jacareí · São José dos Campos · São Paulo",

        "img_hero":      "./img/egidio_hero.jpg",
        "img_sobre":     "./img/egidio_sobre.jpg",
        "img_portfolio1":"./img/egidio_camp1.jpg",
        "img_portfolio2":"./img/egidio_camp2.jpg",
        "img_portfolio3":"./img/egidio_camp3.jpg",

        "whatsapp":     "5500000000006",
        "email":        "",
        "instagram_url":"https://www.instagram.com/egiih/",

        "bio_p1": "Egídio é criador de conteúdo com audiência altamente fiel — 73,3% de seguidores — e forte presença em Stories (82,2% do conteúdo). Conecta marcas a um público engajado e regional de alta relevância.",
        "bio_p2": "Sua audiência está concentrada em Jacareí, São José dos Campos e São Paulo — mercado regional estratégico com alto potencial de conversão local.",
        "tagline": "Arte, estilo e expressão que conectam sua marca a uma audiência apaixonada e fiel.",

        "metricas": [
            {"icone":"📈", "valor":"105551",  "sufixo":"",  "label":"Visualizações",       "sub":"Período recente"},
            {"icone":"👁️", "valor":"18828",   "sufixo":"",  "label":"Contas Alcançadas",   "sub":"73,3% seguidores fiéis"},
            {"icone":"🔍", "valor":"2621",    "sufixo":"",  "label":"Visitas ao Perfil",   "sub":"Stories: 82,2% do conteúdo"},
            {"icone":"🖱️", "valor":"21",      "sufixo":"",  "label":"Cliques em Links",    "sub":"Jacareí · SJC · São Paulo"},
        ],

        "hero_stats": [
            {"numero":"105,5K","label":"Visualizações"},
            {"numero":"18,8K", "label":"Contas alcançadas"},
            {"numero":"73,3%", "label":"Seguidores fiéis"},
        ],

        "tags": ["Lifestyle","Estilo","Vlog","Maquiagem","Fashion","Artista"],

        "portfolio": [
            {"titulo":"Editorial de Moda",    "categoria":"Fashion & Estilo"},
            {"titulo":"Tutorial de Makeup",   "categoria":"Beleza & Arte"},
            {"titulo":"Vlog do Cotidiano",    "categoria":"Lifestyle & Expressão"},
        ],

        "servicos": [
            {"icone":"💄", "titulo":"Reviews de Makeup",       "desc":"Avaliações criativas de produtos de maquiagem com alto engajamento e credibilidade junto ao público de beleza e moda."},
            {"icone":"👗", "titulo":"Editorial de Moda",       "desc":"Conteúdo de fashion com estética artística e autoral — ideal para marcas de roupas, acessórios e lifestyle."},
            {"icone":"📱", "titulo":"Stories no Dia a Dia",    "desc":"82,2% do conteúdo em stories com audiência fiel, engajada e regional — conversão local de alto potencial."},
            {"icone":"🎨", "titulo":"Campanha Artística",      "desc":"Parceria criativa para marcas que buscam posicionamento diferenciado com estética única e impacto visual."},
        ],

        "publico_genero":"Diversificado · alta identificação com arte e moda",
        "publico_idade": "18–35 anos (predominante)",
        "publico_local": "Jacareí · São José dos Campos · São Paulo",

        "conteudo": [
            {"formato":"Stories", "pct":"82,2%"},
            {"formato":"Reels",   "pct":"16,9%"},
            {"formato":"Posts",   "pct":"0,9%"},
        ],
    },

]  # fim de INFLUENCERS


# ══════════════════════════════════════════════════════════════════════════════
#  GERADOR DE HTML — não precisa editar abaixo desta linha
# ══════════════════════════════════════════════════════════════════════════════

def img_block(path, alt, css_class="", style=""):
    """Retorna img se path definido, senão placeholder."""
    cls = f' class="{css_class}"' if css_class else ''
    sty = f' style="{style}"' if style else ''
    if path:
        return f'<img{cls}{sty} src="{path}" alt="{alt}" loading="lazy">'
    else:
        return f'''<div class="ph{" " + css_class if css_class else ""}"{sty}>
  <span class="ph-icon">✦</span>
  <span class="ph-text">{alt}</span>
</div>'''

def make_page(d):
    wa_msg = f"Ol%C3%A1!%20Tenho%20interesse%20em%20contratar%20{d['nome'].replace(' ','%20')}%20para%20uma%20campanha."
    wa_url = f"https://wa.me/{d['whatsapp']}?text={wa_msg}"

    # hero stats
    hs = d["hero_stats"]
    hero_stats_html = "".join([
        f'<div class="hs-item"><span class="hs-num">{s["numero"]}</span><span class="hs-lbl">{s["label"]}</span></div>'
        for s in hs
    ])

    # métricas
    met_html = ""
    for i, m in enumerate(d["metricas"]):
        delay = f'style="transition-delay:{i*0.1}s"'
        is_float = "." in str(m["valor"])
        suf = m["sufixo"]
        val = m["valor"]
        met_html += f'''
      <div class="met-card fade-in" {delay}>
        <div class="met-icon">{m["icone"]}</div>
        <span class="met-num" data-target="{val}" data-suffix="{suf}">0</span>
        <span class="met-lbl">{m["label"]}</span>
        <span class="met-sub">{m["sub"]}</span>
      </div>'''

    # tags
    tags_html = "".join([f'<span class="tag">{t}</span>' for t in d["tags"]])

    # portfólio
    port_html = ""
    for i, p in enumerate(d["portfolio"]):
        delay = f'style="transition-delay:{i*0.12}s"'
        key = f"img_portfolio{i+1}"
        img = img_block(d.get(key,""), p["titulo"], "port-img", "width:100%;height:100%;object-fit:cover;object-position:center;")
        port_html += f'''
      <div class="port-card fade-in" {delay}>
        <div class="port-thumb">{img}</div>
        <div class="port-overlay">
          <h3>{p["titulo"]}</h3>
          <p>{p["categoria"]}</p>
        </div>
        <div class="port-border"></div>
      </div>'''

    # serviços
    serv_html = ""
    for i, s in enumerate(d["servicos"]):
        delay = f'style="transition-delay:{i*0.1}s"'
        serv_html += f'''
      <div class="srv-item fade-in" {delay}>
        <div class="srv-icon">{s["icone"]}</div>
        <div class="srv-body">
          <h3>{s["titulo"]}</h3>
          <p>{s["desc"]}</p>
          <span class="srv-cta">Consulte disponibilidade →</span>
        </div>
      </div>'''

    # conteúdo distribuição
    cont_html = "".join([
        f'<div class="dist-item"><span class="dist-fmt">{c["formato"]}</span><span class="dist-pct">{c["pct"]}</span></div>'
        for c in d["conteudo"]
    ])

    # imagem hero e sobre
    hero_img  = img_block(d.get("img_hero",""),  f'Foto principal de {d["nome"]}',  "hero-img",  "width:100%;height:100%;object-fit:cover;object-position:top center;")
    sobre_img = img_block(d.get("img_sobre",""), f'Foto secundária de {d["nome"]}', "sobre-img", "width:100%;height:100%;object-fit:cover;object-position:top center;")

    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["nome_completo"]} | Influencer Digital Premium</title>
<meta name="description" content="{d["bio_p1"][:120]}...">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;0,900;1,400&family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;1,300;1,400&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   VARIÁVEIS GLOBAIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
:root {{
  --gold:      #C9A84C;
  --gold-lt:   #E8C97A;
  --black:     #080808;
  --dark:      #111111;
  --dark2:     #1A1A1A;
  --dark3:     #222222;
  --graph:     #2D2D2D;
  --text:      #E8E0D5;
  --muted:     #9A9080;
}}
/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   RESET & BASE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth}}
body{{background:var(--black);color:var(--text);font-family:"Montserrat",sans-serif;font-weight:300;line-height:1.75;overflow-x:hidden}}
img{{display:block;max-width:100%}}
a{{text-decoration:none;color:inherit}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   PLACEHOLDER (quando não há imagem)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.ph{{
  width:100%;height:100%;
  display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:14px;
  background:linear-gradient(160deg,var(--dark2) 0%,var(--graph) 40%,var(--dark3) 100%);
  position:relative;
}}
.ph::before{{
  content:"";position:absolute;inset:0;
  background:repeating-linear-gradient(45deg,transparent,transparent 28px,rgba(201,168,76,.03) 28px,rgba(201,168,76,.03) 29px);
}}
.ph-icon{{font-size:3rem;opacity:.25;position:relative}}
.ph-text{{font-size:.65rem;letter-spacing:.3em;text-transform:uppercase;color:var(--muted);position:relative}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   LOADER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
#loader{{
  position:fixed;inset:0;z-index:9999;
  background:var(--black);
  display:flex;align-items:center;justify-content:center;
  flex-direction:column;gap:20px;
  transition:opacity .8s ease,visibility .8s ease;
}}
#loader.hidden{{opacity:0;visibility:hidden;pointer-events:none}}
.ld-name{{
  font-family:"Playfair Display",serif;
  font-size:clamp(1.8rem,6vw,3.5rem);
  color:var(--gold);letter-spacing:.3em;
  animation:pulse 2s ease-in-out infinite;
}}
.ld-bar{{width:180px;height:1px;background:var(--graph);position:relative;overflow:hidden}}
.ld-bar::after{{
  content:"";position:absolute;top:0;left:-100%;
  width:100%;height:100%;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  animation:bar 1.5s ease-in-out infinite;
}}
@keyframes bar{{to{{left:100%}}}}
@keyframes pulse{{0%,100%{{opacity:.7}}50%{{opacity:1;text-shadow:0 0 30px rgba(201,168,76,.5)}}}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   NAVEGAÇÃO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
nav#topnav{{
  position:fixed;top:0;left:0;right:0;z-index:100;
  padding:18px 5vw;
  display:flex;align-items:center;justify-content:space-between;
  transition:all .4s ease;
}}
nav#topnav.scrolled{{
  background:rgba(8,8,8,.96);
  backdrop-filter:blur(20px);
  padding:12px 5vw;
  border-bottom:1px solid rgba(201,168,76,.08);
  box-shadow:0 4px 30px rgba(0,0,0,.4);
}}
.nav-logo{{font-family:"Playfair Display",serif;font-size:1.4rem;color:var(--gold);letter-spacing:.15em}}
.nav-links{{display:flex;gap:32px;list-style:none}}
.nav-links a{{color:var(--muted);font-size:.72rem;letter-spacing:.15em;text-transform:uppercase;transition:color .3s}}
.nav-links a:hover{{color:var(--gold)}}
.nav-btn{{
  background:transparent;border:1px solid var(--gold);
  color:var(--gold);padding:9px 22px;
  font-size:.68rem;letter-spacing:.2em;text-transform:uppercase;
  transition:all .3s;cursor:pointer;
}}
.nav-btn:hover{{background:var(--gold);color:var(--black)}}
/* hamburger */
.hamburger{{
  display:none;flex-direction:column;gap:5px;
  background:none;border:none;cursor:pointer;padding:6px;
}}
.hamburger span{{display:block;width:22px;height:1.5px;background:var(--gold);transition:all .3s}}
.hamburger.open span:nth-child(1){{transform:rotate(45deg) translate(4px,4px)}}
.hamburger.open span:nth-child(2){{opacity:0}}
.hamburger.open span:nth-child(3){{transform:rotate(-45deg) translate(4px,-4px)}}
/* mobile menu */
.mob-menu{{
  display:none;position:fixed;inset:0;z-index:99;
  background:var(--dark);
  flex-direction:column;align-items:center;justify-content:center;gap:28px;
  opacity:0;transition:opacity .4s;
}}
.mob-menu.open{{display:flex;opacity:1}}
.mob-menu a{{font-family:"Playfair Display",serif;font-size:clamp(1.5rem,6vw,2rem);color:var(--muted);transition:color .3s}}
.mob-menu a:hover{{color:var(--gold)}}
.mob-close{{position:absolute;top:22px;right:22px;background:none;border:none;color:var(--gold);font-size:1.6rem;cursor:pointer;line-height:1}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   HERO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.hero{{
  min-height:100vh;
  display:grid;grid-template-columns:1fr 1fr;
  position:relative;overflow:hidden;
}}
.hero::before{{
  content:"";position:absolute;inset:0;
  background:radial-gradient(ellipse at 70% 50%,rgba(201,168,76,.04) 0%,transparent 70%);
  pointer-events:none;
}}
.hero-left{{
  display:flex;flex-direction:column;justify-content:center;
  padding:140px 5vw 80px;
  position:relative;
}}
.hero-eyebrow{{
  font-size:.62rem;letter-spacing:.4em;text-transform:uppercase;
  color:var(--gold);margin-bottom:28px;
  display:flex;align-items:center;gap:14px;
}}
.hero-eyebrow::before{{content:"";width:36px;height:1px;background:var(--gold)}}
.hero-name{{
  font-family:"Playfair Display",serif;
  font-size:clamp(3rem,7vw,6.5rem);
  font-weight:700;line-height:.92;
  color:#fff;margin-bottom:12px;
}}
.hero-name em{{color:var(--gold);font-style:italic}}
.hero-sub{{
  font-size:.72rem;letter-spacing:.3em;text-transform:uppercase;
  color:var(--muted);margin-bottom:28px;
}}
.hero-tagline{{
  font-family:"Cormorant Garamond",serif;
  font-size:clamp(1rem,1.6vw,1.4rem);
  font-weight:300;color:var(--muted);
  line-height:1.7;margin-bottom:48px;max-width:420px;
}}
.hero-actions{{display:flex;gap:16px;align-items:center;flex-wrap:wrap}}
.btn-primary{{
  background:linear-gradient(135deg,var(--gold),var(--gold-lt));
  color:var(--black);padding:15px 36px;
  font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;
  font-weight:700;display:inline-block;transition:all .3s ease;
  position:relative;overflow:hidden;cursor:pointer;border:none;
  text-decoration:none;
}}
.btn-primary::after{{
  content:"";position:absolute;top:0;left:-100%;
  width:100%;height:100%;
  background:rgba(255,255,255,.2);
  transform:skewX(-20deg);transition:left .4s;
}}
.btn-primary:hover::after{{left:150%}}
.btn-primary:hover{{transform:translateY(-2px);box-shadow:0 10px 40px rgba(201,168,76,.4)}}
.btn-ghost{{
  color:var(--muted);font-size:.68rem;letter-spacing:.15em;
  text-transform:uppercase;display:flex;align-items:center;gap:8px;
  transition:color .3s;text-decoration:none;
}}
.btn-ghost:hover{{color:var(--gold)}}

/* hero imagem */
.hero-right{{
  position:relative;display:flex;align-items:center;justify-content:center;
}}
.hero-frame{{
  position:relative;
  width:min(76%,420px);aspect-ratio:3/4;
  margin-top:80px;
}}
.hero-frame::before{{
  content:"";position:absolute;top:-18px;right:-18px;
  width:100%;height:100%;
  border:1px solid rgba(201,168,76,.3);
  pointer-events:none;z-index:1;
}}
.hero-frame::after{{
  content:"";position:absolute;bottom:-18px;left:-18px;
  width:100%;height:100%;
  border:1px solid rgba(201,168,76,.12);
  pointer-events:none;
}}
.hero-frame-inner{{
  width:100%;height:100%;
  overflow:hidden;
  position:relative;
}}
.hero-frame-inner img,
.hero-frame-inner .ph{{
  width:100%;height:100%;
  object-fit:cover;object-position:top center;
}}

/* hero stats card */
.hero-stats{{
  position:absolute;bottom:36px;left:-36px;
  background:rgba(8,8,8,.92);
  border:1px solid rgba(201,168,76,.18);
  backdrop-filter:blur(20px);
  padding:18px 26px;
  display:flex;gap:24px;
  z-index:10;
}}
.hs-item{{text-align:center}}
.hs-num{{
  font-family:"Playfair Display",serif;
  font-size:1.4rem;color:var(--gold);display:block;
}}
.hs-lbl{{font-size:.58rem;letter-spacing:.15em;text-transform:uppercase;color:var(--muted)}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SEÇÕES COMUNS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
section{{padding:110px 5vw}}
.sec-tag{{
  font-size:.62rem;letter-spacing:.4em;text-transform:uppercase;
  color:var(--gold);margin-bottom:18px;
  display:flex;align-items:center;gap:14px;
}}
.sec-tag::before{{content:"";width:28px;height:1px;background:var(--gold)}}
.sec-title{{
  font-family:"Playfair Display",serif;
  font-size:clamp(2.2rem,5vw,3.8rem);
  font-weight:700;line-height:1.1;margin-bottom:20px;
}}
.sec-title em{{color:var(--gold);font-style:italic}}
.gold-line{{width:50px;height:1px;background:linear-gradient(90deg,var(--gold),transparent);margin:26px 0}}
.divider{{height:1px;background:linear-gradient(90deg,transparent,rgba(201,168,76,.1),transparent);margin:0 5vw}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SOBRE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.sobre{{background:var(--dark)}}
.sobre-grid{{
  display:grid;grid-template-columns:1fr 1fr;
  gap:70px;align-items:center;
  max-width:1280px;margin:0 auto;
}}
.sobre-img-wrap{{
  position:relative;aspect-ratio:4/5;overflow:hidden;
}}
.sobre-img-wrap::after{{
  content:"";position:absolute;bottom:-14px;right:-14px;
  width:66%;height:66%;
  border:1px solid rgba(201,168,76,.22);
  pointer-events:none;
}}
.sobre-img-wrap img,
.sobre-img-wrap .ph{{
  width:100%;height:100%;
  object-fit:cover;object-position:top center;
}}
.bio-text{{
  font-family:"Cormorant Garamond",serif;
  font-size:1.2rem;font-weight:300;
  color:var(--muted);line-height:1.85;
  margin-bottom:28px;
}}
.tags-wrap{{display:flex;flex-wrap:wrap;gap:10px;margin-top:6px}}
.tag{{
  border:1px solid rgba(201,168,76,.28);
  padding:6px 18px;font-size:.63rem;
  letter-spacing:.18em;text-transform:uppercase;
  color:var(--gold);transition:background .3s;
}}
.tag:hover{{background:rgba(201,168,76,.08)}}

/* público */
.pub-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;margin-top:40px}}
.pub-card{{
  background:var(--dark2);padding:22px 18px;text-align:center;
}}
.pub-card h4{{font-size:.6rem;letter-spacing:.2em;text-transform:uppercase;color:var(--gold);margin-bottom:8px}}
.pub-card p{{font-size:.78rem;color:var(--muted);line-height:1.5}}

/* distribuição */
.dist-wrap{{display:flex;gap:24px;margin-top:32px;flex-wrap:wrap}}
.dist-item{{
  display:flex;flex-direction:column;align-items:center;
  padding:14px 20px;
  border:1px solid rgba(201,168,76,.15);
}}
.dist-fmt{{font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}}
.dist-pct{{font-family:"Playfair Display",serif;font-size:1.6rem;color:var(--gold)}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   MÉTRICAS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.metricas{{background:var(--black)}}
.met-head{{max-width:640px;margin:0 auto 70px;text-align:center}}
.met-grid{{
  display:grid;grid-template-columns:repeat(4,1fr);
  gap:2px;max-width:1280px;margin:0 auto;
}}
.met-card{{
  background:var(--dark2);padding:44px 24px;text-align:center;
  position:relative;overflow:hidden;transition:all .4s ease;
}}
.met-card::before{{
  content:"";position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
  transform:scaleX(0);transition:transform .4s;
}}
.met-card:hover::before{{transform:scaleX(1)}}
.met-card:hover{{background:var(--dark3);transform:translateY(-4px)}}
.met-icon{{font-size:1.8rem;margin-bottom:18px}}
.met-num{{
  font-family:"Playfair Display",serif;
  font-size:2.8rem;color:var(--gold);
  font-weight:700;display:block;line-height:1;margin-bottom:10px;
}}
.met-lbl{{font-size:.62rem;letter-spacing:.2em;text-transform:uppercase;color:var(--muted);display:block;margin-bottom:6px}}
.met-sub{{font-family:"Cormorant Garamond",serif;font-size:.85rem;color:rgba(154,144,128,.55);line-height:1.4}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   PORTFÓLIO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.portfolio{{background:var(--dark)}}
.port-head{{max-width:640px;margin:0 auto 56px;text-align:center}}
.port-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);
  gap:18px;max-width:1280px;margin:0 auto;
}}
.port-card{{
  position:relative;aspect-ratio:4/5;
  overflow:hidden;cursor:pointer;background:var(--dark2);
}}
.port-thumb{{width:100%;height:100%;position:relative}}
.port-thumb img,.port-thumb .ph{{
  width:100%;height:100%;
  object-fit:cover;object-position:center;
  transition:transform .5s;
}}
.port-card:hover .port-thumb img,
.port-card:hover .port-thumb .ph{{transform:scale(1.05)}}
.port-overlay{{
  position:absolute;inset:0;
  background:linear-gradient(to top,rgba(8,8,8,.95) 0%,transparent 50%);
  display:flex;flex-direction:column;justify-content:flex-end;
  padding:26px;opacity:0;transition:opacity .4s;
}}
.port-card:hover .port-overlay{{opacity:1}}
.port-overlay h3{{font-family:"Playfair Display",serif;font-size:1.1rem;color:#fff;margin-bottom:6px}}
.port-overlay p{{font-size:.7rem;color:var(--gold);letter-spacing:.1em}}
.port-border{{
  position:absolute;inset:0;
  border:1px solid transparent;transition:border-color .4s;pointer-events:none;
}}
.port-card:hover .port-border{{border-color:rgba(201,168,76,.4)}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   SERVIÇOS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.servicos{{background:var(--black)}}
.srv-head{{max-width:640px;margin:0 auto 70px;text-align:center}}
.srv-grid{{
  display:grid;grid-template-columns:repeat(2,1fr);
  gap:2px;max-width:1280px;margin:0 auto;
}}
.srv-item{{
  background:var(--dark2);padding:44px;
  display:flex;gap:26px;align-items:flex-start;
  transition:all .3s;position:relative;overflow:hidden;
}}
.srv-item::after{{
  content:"";position:absolute;bottom:0;left:0;
  width:0;height:1px;background:var(--gold);transition:width .4s;
}}
.srv-item:hover::after{{width:100%}}
.srv-item:hover{{background:var(--dark3)}}
.srv-icon{{
  width:54px;height:54px;flex-shrink:0;
  border:1px solid rgba(201,168,76,.28);
  display:flex;align-items:center;justify-content:center;
  font-size:1.4rem;transition:all .3s;
}}
.srv-item:hover .srv-icon{{background:rgba(201,168,76,.1);border-color:var(--gold)}}
.srv-body h3{{font-family:"Playfair Display",serif;font-size:1.2rem;color:#fff;margin-bottom:10px}}
.srv-body p{{font-size:.83rem;color:var(--muted);line-height:1.7}}
.srv-cta{{
  display:inline-block;margin-top:14px;
  font-family:"Cormorant Garamond",serif;
  font-size:.88rem;color:var(--gold);
}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   DIFERENCIAIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.diferenciais{{background:var(--dark);position:relative;overflow:hidden}}
.diferenciais::before{{
  content:"";position:absolute;top:50%;left:50%;
  transform:translate(-50%,-50%);
  width:700px;height:700px;border-radius:50%;
  background:radial-gradient(circle,rgba(201,168,76,.04) 0%,transparent 70%);
  pointer-events:none;
}}
.diff-head{{text-align:center;margin-bottom:72px}}
.diff-grid{{
  display:grid;grid-template-columns:repeat(3,1fr);
  gap:28px;max-width:1280px;margin:0 auto;
}}
.diff-card{{
  padding:44px 36px;
  border:1px solid rgba(201,168,76,.1);
  transition:all .4s;position:relative;overflow:hidden;
}}
.diff-card::before{{
  content:"";position:absolute;top:0;left:0;
  width:0;height:100%;background:rgba(201,168,76,.04);transition:width .4s;
}}
.diff-card:hover::before{{width:100%}}
.diff-card:hover{{border-color:rgba(201,168,76,.28);transform:translateY(-5px)}}
.diff-n{{
  font-family:"Playfair Display",serif;font-size:3.5rem;
  color:rgba(201,168,76,.12);font-weight:900;line-height:1;margin-bottom:18px;
}}
.diff-card h3{{font-family:"Playfair Display",serif;font-size:1.2rem;color:#fff;margin-bottom:12px}}
.diff-card p{{font-size:.83rem;color:var(--muted);line-height:1.7}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   CTA FINAL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.cta-final{{
  background:var(--black);text-align:center;
  position:relative;overflow:hidden;
}}
.cta-final::before{{
  content:"";position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--gold),transparent);
}}
.cta-glow{{
  position:absolute;inset:0;
  background:radial-gradient(ellipse at center,rgba(201,168,76,.06) 0%,transparent 60%);
}}
.cta-inner{{position:relative;max-width:780px;margin:0 auto}}
.cta-kicker{{
  font-size:.62rem;letter-spacing:.4em;text-transform:uppercase;
  color:var(--gold);margin-bottom:28px;display:block;
}}
.cta-title{{
  font-family:"Playfair Display",serif;
  font-size:clamp(2.2rem,6vw,4.8rem);
  font-weight:700;line-height:1.1;margin-bottom:22px;
}}
.cta-title em{{color:var(--gold);font-style:italic}}
.cta-sub{{
  font-family:"Cormorant Garamond",serif;
  font-size:1.2rem;color:var(--muted);
  margin-bottom:52px;line-height:1.6;
}}
.cta-btn{{
  display:inline-flex;align-items:center;gap:14px;
  background:linear-gradient(135deg,var(--gold),var(--gold-lt));
  color:var(--black);padding:20px 52px;
  font-size:.76rem;letter-spacing:.25em;
  text-transform:uppercase;font-weight:700;
  text-decoration:none;transition:all .4s;
}}
.cta-btn:hover{{transform:translateY(-3px);box-shadow:0 20px 60px rgba(201,168,76,.4)}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   FOOTER
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
footer{{
  background:var(--dark);
  border-top:1px solid rgba(201,168,76,.08);
  padding:52px 5vw;
  display:flex;align-items:center;justify-content:space-between;
  gap:20px;flex-wrap:wrap;
}}
.ft-logo{{font-family:"Playfair Display",serif;font-size:1.4rem;color:var(--gold);letter-spacing:.15em}}
.ft-txt{{font-size:.68rem;letter-spacing:.1em;color:var(--muted)}}
.ft-agency{{font-size:.66rem;letter-spacing:.15em;text-transform:uppercase;color:rgba(154,144,128,.4)}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   WHATSAPP FLUTUANTE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.wa-float{{
  position:fixed;bottom:36px;right:36px;z-index:999;
  width:58px;height:58px;
  background:#25D366;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 20px rgba(37,211,102,.4);
  text-decoration:none;
  animation:wafloat 3s ease-in-out infinite;
  transition:transform .3s,box-shadow .3s;
}}
.wa-float:hover{{animation:none;transform:scale(1.1);box-shadow:0 8px 30px rgba(37,211,102,.5)}}
@keyframes wafloat{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-6px)}}}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   ANIMAÇÕES DE SCROLL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
.fade-in{{opacity:0;transform:translateY(28px);transition:opacity .8s ease,transform .8s ease}}
.fade-in.visible{{opacity:1;transform:none}}
.fade-left{{opacity:0;transform:translateX(-28px);transition:opacity .8s ease,transform .8s ease}}
.fade-left.visible{{opacity:1;transform:none}}
.fade-right{{opacity:0;transform:translateX(28px);transition:opacity .8s ease,transform .8s ease}}
.fade-right.visible{{opacity:1;transform:none}}

/* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   RESPONSIVIDADE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
@media(max-width:1100px){{
  .met-grid{{grid-template-columns:repeat(2,1fr)}}
  .port-grid{{grid-template-columns:repeat(2,1fr)}}
}}
@media(max-width:900px){{
  .hero{{grid-template-columns:1fr;min-height:auto}}
  .hero-left{{padding:120px 5vw 50px}}
  .hero-right{{padding:0 5vw 70px}}
  .hero-frame{{width:100%;max-width:100%;margin-top:0}}
  .hero-stats{{left:0;bottom:20px}}
  .sobre-grid{{grid-template-columns:1fr;gap:40px}}
  .diff-grid{{grid-template-columns:1fr 1fr}}
  .pub-grid{{grid-template-columns:1fr}}
  .srv-grid{{grid-template-columns:1fr}}
}}
@media(max-width:768px){{
  section{{padding:80px 5vw}}
  .nav-links{{display:none}}
  .nav-btn{{display:none}}
  .hamburger{{display:flex}}
  .hero-left{{padding:100px 5vw 40px}}
  .hero-frame{{aspect-ratio:1/1}}
  .met-grid{{grid-template-columns:1fr 1fr}}
  .port-grid{{grid-template-columns:1fr 1fr}}
  .diff-grid{{grid-template-columns:1fr}}
  footer{{flex-direction:column;text-align:center;gap:14px}}
}}
@media(max-width:480px){{
  section{{padding:64px 4vw}}
  .hero-left{{padding:88px 4vw 36px}}
  .hero-frame{{aspect-ratio:3/4}}
  .hero-stats{{gap:14px;padding:14px 18px}}
  .hs-num{{font-size:1.1rem}}
  .met-grid{{grid-template-columns:1fr}}
  .port-grid{{grid-template-columns:1fr}}
  .srv-item{{flex-direction:column;gap:16px;padding:28px 22px}}
  .dist-wrap{{gap:12px}}
  .wa-float{{bottom:22px;right:22px;width:50px;height:50px}}
}}
</style>
</head>
<body>

<!-- LOADER -->
<div id="loader">
  <div class="ld-name">{d["nome"].upper()}</div>
  <div class="ld-bar"></div>
</div>

<!-- WHATSAPP FLUTUANTE -->
<a href="{wa_url}" class="wa-float" target="_blank" aria-label="WhatsApp">
  <svg width="26" height="26" viewBox="0 0 24 24" fill="white">
    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
  </svg>
</a>

<!-- NAVEGAÇÃO -->
<nav id="topnav">
  <div class="nav-logo">{d["nome"]}</div>
  <ul class="nav-links">
    <li><a href="#sobre">Sobre</a></li>
    <li><a href="#metricas">Métricas</a></li>
    <li><a href="#portfolio">Portfólio</a></li>
    <li><a href="#servicos">Serviços</a></li>
  </ul>
  <a href="{wa_url}" class="nav-btn" target="_blank">Contratar</a>
  <button class="hamburger" id="ham" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
</nav>

<!-- MENU MOBILE -->
<div class="mob-menu" id="mobmenu">
  <button class="mob-close" id="mobclose">✕</button>
  <a href="#sobre">Sobre</a>
  <a href="#metricas">Métricas</a>
  <a href="#portfolio">Portfólio</a>
  <a href="#servicos">Serviços</a>
  <a href="{wa_url}" target="_blank">Contratar</a>
</div>

<!-- ══ HERO ══ -->
<section class="hero">
  <div class="hero-left">
    <div class="hero-eyebrow fade-in">{d["nicho"]}</div>
    <h1 class="hero-name fade-in">
      {d["nome"]}<br><em>{d["subtitulo"]}</em>
    </h1>
    <div class="hero-sub fade-in">{d["arroba"]} &nbsp;·&nbsp; {d["cidade"]}</div>
    <p class="hero-tagline fade-in">{d["tagline"]}</p>
    <div class="hero-actions fade-in">
      <a href="{wa_url}" class="btn-primary" target="_blank">Contratar Agora</a>
      <a href="#sobre" class="btn-ghost">
        Conhecer mais
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M12 5v14M5 12l7 7 7-7"/>
        </svg>
      </a>
    </div>
  </div>
  <div class="hero-right">
    <div class="hero-frame fade-right">
      <div class="hero-frame-inner">
        {hero_img}
      </div>
    </div>
    <div class="hero-stats fade-in">
      {hero_stats_html}
    </div>
  </div>
</section>

<!-- ══ SOBRE ══ -->
<section class="sobre" id="sobre">
  <div class="sobre-grid">
    <div class="sobre-img-wrap fade-left">
      {sobre_img}
    </div>
    <div class="fade-right">
      <div class="sec-tag">Quem é</div>
      <h2 class="sec-title">{d["nome"]}<br><em>em detalhes</em></h2>
      <div class="gold-line"></div>
      <p class="bio-text">{d["bio_p1"]}</p>
      <p class="bio-text">{d["bio_p2"]}</p>
      <div class="tags-wrap">{tags_html}</div>

      <div class="pub-grid">
        <div class="pub-card">
          <h4>Gênero</h4>
          <p>{d["publico_genero"]}</p>
        </div>
        <div class="pub-card">
          <h4>Faixa Etária</h4>
          <p>{d["publico_idade"]}</p>
        </div>
        <div class="pub-card">
          <h4>Localização</h4>
          <p>{d["publico_local"]}</p>
        </div>
      </div>

      <div class="dist-wrap">
        {cont_html}
      </div>
    </div>
  </div>
</section>

<div class="divider"></div>

<!-- ══ MÉTRICAS ══ -->
<section class="metricas" id="metricas">
  <div class="met-head fade-in">
    <div class="sec-tag" style="justify-content:center">Resultados Reais</div>
    <h2 class="sec-title" style="text-align:center">Números que<br><em>impressionam</em></h2>
  </div>
  <div class="met-grid">
    {met_html}
  </div>
</section>

<div class="divider"></div>

<!-- ══ PORTFÓLIO ══ -->
<section class="portfolio" id="portfolio">
  <div class="port-head fade-in">
    <div class="sec-tag" style="justify-content:center">Trabalhos</div>
    <h2 class="sec-title" style="text-align:center">Campanhas que<br><em>marcaram</em></h2>
  </div>
  <div class="port-grid">
    {port_html}
  </div>
</section>

<div class="divider"></div>

<!-- ══ SERVIÇOS ══ -->
<section class="servicos" id="servicos">
  <div class="srv-head fade-in">
    <div class="sec-tag" style="justify-content:center">O que Ofereço</div>
    <h2 class="sec-title" style="text-align:center">Serviços <em>premium</em></h2>
  </div>
  <div class="srv-grid">
    {serv_html}
  </div>
</section>

<div class="divider"></div>

<!-- ══ DIFERENCIAIS ══ -->
<section class="diferenciais">
  <div class="diff-head fade-in">
    <div class="sec-tag" style="justify-content:center">Por Que Escolher</div>
    <h2 class="sec-title" style="text-align:center">Meus <em>diferenciais</em></h2>
  </div>
  <div class="diff-grid">
    <div class="diff-card fade-in">
      <div class="diff-n">01</div>
      <h3>Audiência Qualificada</h3>
      <p>Seguidores reais e engajados com perfil alinhado ao público-alvo, garantindo campanhas com resultado mensurável e conversão real.</p>
    </div>
    <div class="diff-card fade-in" style="transition-delay:.1s">
      <div class="diff-n">02</div>
      <h3>Alta Conversão</h3>
      <p>Histórico comprovado de campanhas com retorno acima da média do mercado, com marcas de diferentes segmentos e tamanhos.</p>
    </div>
    <div class="diff-card fade-in" style="transition-delay:.2s">
      <div class="diff-n">03</div>
      <h3>Estratégia Personalizada</h3>
      <p>Cada parceria é planejada de forma única, respeitando a identidade da marca e maximizando o impacto de cada campanha.</p>
    </div>
  </div>
</section>

<!-- ══ CTA FINAL ══ -->
<section class="cta-final">
  <div class="cta-glow"></div>
  <div class="cta-inner fade-in">
    <span class="cta-kicker">Pronto para crescer?</span>
    <h2 class="cta-title">Leve sua marca<br>para outro <em>nível</em></h2>
    <p class="cta-sub">Entre em contato agora e descubra como uma parceria com {d["nome"]} pode transformar sua presença digital.</p>
    <a href="{wa_url}" class="cta-btn" target="_blank">
      Falar no WhatsApp
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <path d="M5 12h14M12 5l7 7-7 7"/>
      </svg>
    </a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="ft-logo">{d["nome"]}</div>
  <div class="ft-txt">© 2025 · Todos os direitos reservados</div>
  <div class="ft-agency">PAIVA Assessoria & Marketing</div>
</footer>

<script>
/* ── LOADER ── */
window.addEventListener("load", () => {{
  setTimeout(() => document.getElementById("loader").classList.add("hidden"), 1600);
}});

/* ── NAV SCROLL ── */
const nav = document.getElementById("topnav");
let lastY = 0;
window.addEventListener("scroll", () => {{
  nav.classList.toggle("scrolled", window.scrollY > 60);
  lastY = window.scrollY;
}}, {{passive:true}});

/* ── HAMBURGER ── */
const ham = document.getElementById("ham");
const mob = document.getElementById("mobmenu");
const cls = document.getElementById("mobclose");
const open = () => {{ ham.classList.add("open"); mob.classList.add("open"); document.body.style.overflow="hidden"; }};
const close = () => {{ ham.classList.remove("open"); mob.classList.remove("open"); document.body.style.overflow=""; }};
ham.addEventListener("click", () => ham.classList.contains("open") ? close() : open());
cls.addEventListener("click", close);
mob.querySelectorAll("a").forEach(a => a.addEventListener("click", close));
mob.addEventListener("click", e => {{ if(e.target===mob) close(); }});
document.addEventListener("keydown", e => {{ if(e.key==="Escape") close(); }});

/* ── SCROLL ANIMATIONS ── */
const observer = new IntersectionObserver((entries) => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      entry.target.classList.add("visible");
      const counter = entry.target.querySelector("[data-target]");
      if (counter && !counter.dataset.done) animCounter(counter);
    }}
  }});
}}, {{ threshold: 0.12, rootMargin: "0px 0px -40px 0px" }});
document.querySelectorAll(".fade-in,.fade-left,.fade-right").forEach(el => observer.observe(el));

/* ── COUNTER ── */
function animCounter(el) {{
  el.dataset.done = "1";
  const raw    = el.dataset.target;
  const suffix = el.dataset.suffix || "";
  const target = parseFloat(raw);
  const isFloat = raw.includes(".");
  const dur = 2000;
  const start = performance.now();

  function fmt(val) {{
    if (target >= 1000000) return (val/1000000).toFixed(2).replace(".",",") + " Mi";
    if (target >= 100000)  return Math.floor(val/1000) + "K";
    if (target >= 10000)   return (val/1000).toFixed(1).replace(".",",") + "K";
    if (isFloat)           return val.toFixed(2).replace(".",",") + suffix;
    return Math.floor(val).toLocaleString("pt-BR") + suffix;
  }}

  (function tick(now) {{
    const progress = Math.min((now - start) / dur, 1);
    const ease = 1 - Math.pow(1 - progress, 3);
    el.textContent = fmt(target * ease);
    if (progress < 1) requestAnimationFrame(tick);
    else el.textContent = fmt(target);
  }})(start);
}}

/* ── PARALLAX HERO ── */
window.addEventListener("scroll", () => {{
  const frame = document.querySelector(".hero-frame");
  if (frame && window.scrollY < window.innerHeight) {{
    frame.style.transform = `translateY(${{window.scrollY * 0.08}}px)`;
  }}
}}, {{passive:true}});

/* ── SMOOTH SCROLL ── */
document.querySelectorAll("a[href^='#']").forEach(a => {{
  a.addEventListener("click", e => {{
    const t = document.querySelector(a.getAttribute("href"));
    if (t) {{ e.preventDefault(); t.scrollIntoView({{behavior:"smooth"}}); }}
  }});
}});
</script>
</body>
</html>'''

# ── GERAR ARQUIVOS ──
os.makedirs("/home/claude/landing-pages-v2", exist_ok=True)

for inf in INFLUENCERS:
    html = make_page(inf)
    path = f'/home/claude/landing-pages-v2/{inf["id"]}.html'
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {inf['nome']:20s} → {inf['id']}.html")

print(f"\n🎉 {len(INFLUENCERS)} páginas geradas em /home/claude/landing-pages-v2/")
