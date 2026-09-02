# 💼 Agente de Investimentos - Monitor de Ações

Sistema automatizado para monitorar ações no **Status Invest** e gerar relatórios em Excel.

## 📊 Ações Monitoradas

- **PETR4** - Petrobras
- **BBDC4** - Banco do Brasil
- **VALE3** - Vale
- **BRAD3** - Bradesco
- **KLBN4** - Klabim

## 🚀 Instalação

### 1. Instalar Dependências

```bash
pip install -r requirements.txt
```

Dependências:
- `requests` - Para requisições HTTP
- `beautifulsoup4` - Para parsing HTML
- `pandas` - Para manipulação de dados
- `openpyxl` - Para criar arquivos Excel
- `selenium` - Para JavaScript rendering (opcional)

### 2. Verificar Instalação

```bash
python -c "import requests, bs4, pandas, openpyxl; print('✓ Todas as dependências instaladas')"
```

## 📝 Uso

### Executar o Monitor

```bash
python run_investment_monitor.py
```

Isso irá:
1. Consultar o Status Invest para cada ação
2. Coletar: Ticker, Nome, Valor Atual, Variação (%)
3. Gerar arquivo Excel com timestamp: `acoes_YYYYMMDD_HHMMSS.xlsx`

### Usar Programaticamente

```python
from investment_monitor import InvestmentMonitor

# Criar instância
monitor = InvestmentMonitor()

# Coletar dados
dados = monitor.coletar_todas_acoes()

# Criar Excel
arquivo = monitor.criar_excel(dados, "meu_relatorio.xlsx")

# Ou executar completo
monitor.executar()
```

## 📁 Estrutura de Arquivos

```
.
├── investment_monitor.py       # Classe principal
├── run_investment_monitor.py   # Script de execução
├── requirements.txt            # Dependências
├── INVESTIDOR_README.md        # Este arquivo
└── acoes_*.xlsx                # Arquivos gerados (Excel)
```

## ✨ Funcionalidades

### InvestmentMonitor

- **`buscar_dados_acao(ticker)`** - Busca dados de uma ação específica
  - Retorna: `{ticker, nome, valor, variacao}`

- **`coletar_todas_acoes()`** - Coleta dados de todas as 5 ações
  - Retorna: lista de dicionários com dados

- **`criar_excel(dados, nome_arquivo)`** - Gera arquivo Excel
  - Formata automaticamente
  - Adiciona informação de quando foi gerado

- **`executar()`** - Executa coleta + Excel + exibição

## 📊 Formato do Excel Gerado

| Ticker | Nome             | Valor (R$) | Variação (%) |
|--------|------------------|-----------|--------------|
| PETR4  | Petrobras        | 28,45     | +2,15%       |
| BBDC4  | Banco do Brasil  | 32,10     | -1,30%       |
| VALE3  | Vale             | 60,90     | +0,85%       |
| BRAD3  | Bradesco         | 27,65     | +1,20%       |
| KLBN4  | Klabim           | 18,55     | -0,45%       |

## 🔄 Automação com Agendamento

Para executar automaticamente em horários específicos, você pode usar:

### Windows - Agendador de Tarefas

```bash
# Criar tarefa que executa a cada 15 minutos
schtasks /create /tn "MonitorInvestimentos" /tr "python C:\Users\tom\Documents\agent Gui\run_investment_monitor.py" /sc minute /mo 15
```

### Linux/Mac - Cron

```bash
# Executar a cada 15 minutos
*/15 * * * * cd /caminho/para/pasta && python run_investment_monitor.py
```

## ⚠️ Notas Importantes

- **Rate Limiting**: Respeite o site - não faça mais de 1 requisição por segundo
- **Status Invest**: O site pode ter proteção contra scraping
- **Erros de Conexão**: Verifique sua conexão com internet
- **Bloqueio do Site**: Se receber muitos erros, aguarde alguns minutos antes de tentar novamente

## 🛠️ Troubleshooting

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### "ConnectionError"
- Verifique internet
- Tente novamente em alguns minutos
- O site pode estar bloqueando o IP

### "Erro ao buscar PETR4"
- O Status Invest pode ter mudado sua estrutura HTML
- Verifique se consegue acessar o site manualmente
- Considere usar Selenium para sites dinâmicos

## 📈 Próximas Melhorias

- [ ] Integração com API (mais confiável que scraping)
- [ ] Histórico de preços (sqlite)
- [ ] Gráficos de tendência
- [ ] Alertas quando variação ultrapassa limite
- [ ] Envio automático por email
- [ ] Interface web

## 📧 Suporte

Para problemas com o script ou sugestões, verifique:
- Se o Status Invest mudou seu layout
- Se suas dependências estão atualizadas
- Se há bloqueio do seu IP pelo site

---

**Desenvolvido com ❤️ para investidores brasileiros**
