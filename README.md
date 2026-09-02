# 📈 Assistente de Investimento

Um assistente inteligente para análise de ações brasileiras com geração automática de relatórios em Excel.

## 🎯 Funcionalidades

- **Consulta de Ações**: Monitora 5 principais ações do mercado brasileiro
  - PETR4 (Petrobras)
  - VALE3 (Vale)
  - KLBN4 (Klabin)
  - BBAS3 (Banco do Brasil)
  - ITUB3 (Itau)

- **Métricas Analisadas**:
  - 💰 Valor Atual
  - 📊 Dividend Yield
  - 📉 Mínimo 52 semanas
  - 📈 Máximo 52 semanas
  - 📊 Valorização 12 meses

- **Relatório em Excel**: Gera arquivo formatado e pronto para análise

## 🚀 Como Usar

### 1. Instalação

```bash
# Clone ou navegue até a pasta do projeto
cd "C:\Users\tom\Documents\agent Gui"

# Instale as dependências
pip install -r requirements.txt
```

### 2. Executar o Script

```bash
python investment_assistant.py
```

O script irá:
1. Buscar dados de todas as ações
2. Exibir um resumo no terminal
3. Gerar um arquivo `relatorio_investimentos.xlsx`

### 3. Analisar o Relatório

Abra o arquivo `relatorio_investimentos.xlsx` em:
- Microsoft Excel
- Google Sheets
- LibreOffice Calc

## 📋 Estrutura do Relatório

| Coluna | Descrição |
|--------|-----------|
| Ticker | Código da ação |
| Empresa | Nome da empresa |
| Valor Atual (R$) | Preço atual da ação |
| Dividend Yield (%) | Rendimento em dividendos |
| Mín. 52 Semanas (R$) | Preço mínimo no último ano |
| Máx. 52 Semanas (R$) | Preço máximo no último ano |
| Valorização 12m (%) | Ganho percentual em 12 meses |

## 🔧 Personalização

### Adicionar Novas Ações

Edite o dicionário `acoes` no arquivo `investment_assistant.py`:

```python
self.acoes = {
    'PETR4.SA': 'Petrobras',
    'VALE3.SA': 'Vale',
    'KLBN4.SA': 'Klabin',
    'BBAS3.SA': 'Banco do Brasil',
    'ITUB3.SA': 'Itau',
    'SUA_ACAO.SA': 'Nome da Empresa'  # Adicione aqui
}
```

### Mudar Nome do Arquivo de Saída

```python
assistente.gerar_relatorio_excel('meu_relatorio.xlsx')
```

## 📊 Fonte de Dados

Os dados são obtidos via **yfinance**, que utiliza dados públicos do Yahoo Finance, oferecendo:
- Preços históricos
- Informações fundamentais
- Dados de dividendos

## ⚠️ Observações Importantes

- Os dados podem sofrer delay de 15-20 minutos em relação ao mercado em tempo real
- Dividend Yield pode estar marcado como "N/A" se não houver informação disponível
- Recomenda-se usar este relatório como uma das ferramentas de análise, não como única fonte

## 🆘 Troubleshooting

### Erro: "No module named 'yfinance'"

```bash
pip install yfinance
```

### Erro: "Nenhum dado disponível"

- Verifique sua conexão com a internet
- Aguarde alguns segundos e tente novamente
- Alguns tickers podem estar indisponíveis temporariamente

### Excel corrompido

Delete o arquivo anterior e execute novamente:

```bash
python investment_assistant.py
```

## 📝 Exemplo de Execução

```
🚀 Iniciando análise de investimentos...

Buscando dados de PETR4.SA...
Buscando dados de VALE3.SA...
Buscando dados de KLBN4.SA...
Buscando dados de BBAS3.SA...
Buscando dados de ITUB3.SA...

====================================================================================================
                                 RELATÓRIO DE ANÁLISE DE AÇÕES
====================================================================================================
   Ticker Empresa  Valor Atual (R$)  Dividend Yield (%)  Mín. 52 Semanas (R$)  Máx. 52 Semanas (R$)  Valorização 12m (%)
  PETR4.SA Petrobras            28.45               8.12                  22.30                  31.20                12.50
...
====================================================================================================

✅ Relatório gerado com sucesso: relatorio_investimentos.xlsx
   Localização: C:\Users\tom\Documents\agent Gui\relatorio_investimentos.xlsx
```

## 🔄 Próximos Passos (Melhorias Futuras)

- [ ] Interface web interativa
- [ ] Alertas de preço
- [ ] Análise técnica (RSI, MACD)
- [ ] Integração com Status Invest
- [ ] Agendamento automático de relatórios
- [ ] Comparação com benchmarks (IBOVESPA)

## 📄 Licença

Livre para uso educacional e pessoal.

---

**Última atualização**: Setembro 2026
