# 📈 Assistente de Investimento

## Visão Geral
Um assistente inteligente para análise de ações brasileiras. Coleta dados de mercado e gera relatórios em Excel para auxiliar investidores na tomada de decisão.

## 🎯 Objetivo Principal
Fornecer análise rápida e estruturada de ações principais do mercado brasileiro, com foco em métricas fundamentalistas e performance histórica.

## 📊 Ações Monitoradas
| Ticker | Empresa | Segmento |
|--------|---------|----------|
| PETR4.SA | Petrobras | Energia |
| VALE3.SA | Vale | Mineração |
| KLBN4.SA | Klabin | Papel e Celulose |
| BBAS3.SA | Banco do Brasil | Financeiro |
| ITUB3.SA | Itau | Financeiro |

## 📋 Métricas Coletadas

1. **Valor Atual (R$)** - Preço em tempo real da ação
2. **Dividend Yield (%)** - Rendimento em dividendos
3. **Mín. 52 Semanas (R$)** - Preço mínimo no último ano
4. **Máx. 52 Semanas (R$)** - Preço máximo no último ano
5. **Valorização 12m (%)** - Ganho percentual em 12 meses

## 🔧 Stack Técnico

- **Linguagem**: Python 3.13
- **Coleta de Dados**: yfinance (Yahoo Finance)
- **Processamento**: pandas
- **Geração de Excel**: openpyxl
- **Formato de Saída**: .xlsx (Excel)

## 🚀 Como Usar

### 1️⃣ Instalação de Dependências
```bash
pip install -r requirements.txt
```

### 2️⃣ Executar o Script
```bash
python investment_assistant.py
```

### 3️⃣ Resultado
- 📊 Resumo exibido no terminal
- 📁 Arquivo `relatorio_investimentos.xlsx` gerado

## 📁 Estrutura de Arquivos

```
agent-Gui/
├── .claude/                      # Configurações do Claude Code
├── agent.md                      # Esta documentação
├── investment_assistant.py       # Script principal
├── requirements.txt              # Dependências Python
├── README.md                     # Documentação completa
└── relatorio_investimentos.xlsx  # Relatório gerado (depois da primeira execução)
```

## 🔄 Fluxo de Execução

```
1. Coleta de Dados
   ↓
   Busca dados de cada ação (ticker, preço, histórico)
   
2. Processamento
   ↓
   Calcula métricas (min/max, dividend yield, valorização)
   
3. Formatação
   ↓
   Cria DataFrame com os dados
   
4. Geração de Excel
   ↓
   Formata e salva o relatório (.xlsx)
   
5. Exibição
   ↓
   Mostra resumo no terminal
```

## 🎨 Formatação do Excel

- ✅ Cabeçalhos com fundo azul escuro
- ✅ Texto branco nos cabeçalhos
- ✅ Bordas em todas as células
- ✅ Centralização de conteúdo
- ✅ Números formatados com 2 casas decimais
- ✅ Largura automática de colunas

## 🔍 Fonte de Dados

**Yahoo Finance via yfinance**
- Dados públicos e gratuitos
- Atualização diária
- Delay de ~15-20 minutos em relação ao mercado real
- Dados confiáveis e históricos

## ⚠️ Limitações Conhecidas

- ⏱️ Delay de 15-20 minutos em relação ao mercado em tempo real
- 📦 Dividend Yield pode não estar disponível para todas as ações
- 🌐 Depende de conexão com internet
- 📊 Dados históricos limitados às informações disponíveis no Yahoo Finance

## 🚧 Melhorias Futuras

- [ ] Interface web interativa
- [ ] Alertas de preço configuráveis
- [ ] Análise técnica (RSI, MACD, Média Móvel)
- [ ] Integração com Status Invest (web scraping)
- [ ] Agendamento automático de relatórios
- [ ] Comparação com benchmarks (IBOVESPA)
- [ ] Gráficos dentro do Excel
- [ ] Análise de rentabilidade
- [ ] Dashboard em tempo real

## 📝 Notas Adicionais

- **Versão**: 1.0
- **Criado em**: Setembro 2026
- **Autor**: Claude Code
- **Licença**: Livre para uso educacional e pessoal
- **Status**: Funcional

## 💡 Dicas de Uso

1. Execute regularmente para acompanhar as ações
2. Mantenha cópias dos relatórios anteriores para comparação
3. Use como uma das ferramentas de análise, não a única
4. Combine com análise técnica e fundamentalista
5. Considere o dividend yield para investimentos de longo prazo

---

**Próximo Passo**: Executar `python investment_assistant.py` para gerar o primeiro relatório!
