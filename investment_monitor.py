#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Investment Monitor - Monitora ações no Status Invest
Consulta: Petrobras, Banco do Brasil, Vale, Bradesco, Klabim
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import os
from pathlib import Path

class InvestmentMonitor:
    def __init__(self):
        self.base_url = "https://www.statusinvest.com.br/acoes"
        self.acoes = {
            'PETR4': 'Petrobras',
            'BBDC4': 'Banco do Brasil',
            'VALE3': 'Vale',
            'BRAD3': 'Bradesco',
            'KLBN4': 'Klabim'
        }
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def buscar_dados_acao(self, ticker):
        """
        Busca dados de uma ação específica no Status Invest
        """
        try:
            url = f"{self.base_url}/{ticker}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            # Encontra o price principal
            price_element = soup.find('h1', class_='header-top-title')
            variation_element = soup.find('span', class_='header-top-variation')

            valor = None
            variacao = None

            if price_element:
                valor_text = price_element.get_text(strip=True)
                # Extrai número do valor (ex: "R$ 25,30")
                valor = valor_text.replace('R$', '').strip()

            if variation_element:
                var_text = variation_element.get_text(strip=True)
                variacao = var_text

            return {
                'ticker': ticker,
                'nome': self.acoes.get(ticker, ticker),
                'valor': valor,
                'variacao': variacao
            }

        except Exception as e:
            print(f"Erro ao buscar {ticker}: {str(e)}")
            return {
                'ticker': ticker,
                'nome': self.acoes.get(ticker, ticker),
                'valor': 'Erro',
                'variacao': 'Erro'
            }

    def coletar_todas_acoes(self):
        """
        Coleta dados de todas as ações monitoradas
        """
        print("Coletando dados de investimentos...")
        dados = []

        for ticker in self.acoes.keys():
            print(f"  Consultando {ticker}...")
            info = self.buscar_dados_acao(ticker)
            dados.append(info)

        return dados

    def criar_excel(self, dados, nome_arquivo=None):
        """
        Cria arquivo Excel com os dados coletados
        """
        if nome_arquivo is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nome_arquivo = f"acoes_{timestamp}.xlsx"

        # Garante que o arquivo está no diretório do projeto
        caminho_arquivo = Path(nome_arquivo)
        if not caminho_arquivo.is_absolute():
            caminho_arquivo = Path.cwd() / nome_arquivo

        # Cria DataFrame
        df = pd.DataFrame(dados)

        # Reordena colunas
        df = df[['ticker', 'nome', 'valor', 'variacao']]

        # Renomeia colunas para português
        df.columns = ['Ticker', 'Nome', 'Valor (R$)', 'Variação (%)']

        # Cria escritor do Excel
        with pd.ExcelWriter(caminho_arquivo, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Ações')

            # Formata a planilha
            workbook = writer.book
            worksheet = writer.sheets['Ações']

            # Ajusta largura das colunas
            worksheet.column_dimensions['A'].width = 12
            worksheet.column_dimensions['B'].width = 20
            worksheet.column_dimensions['C'].width = 15
            worksheet.column_dimensions['D'].width = 15

            # Adiciona info de coleta
            info_row = len(df) + 3
            worksheet[f'A{info_row}'] = f"Coletado em: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

        print(f"✓ Arquivo criado: {caminho_arquivo}")
        return str(caminho_arquivo)

    def executar(self):
        """
        Executa a coleta e geração do Excel
        """
        try:
            dados = self.coletar_todas_acoes()
            arquivo = self.criar_excel(dados)

            print("\n" + "="*50)
            print("RESUMO DAS AÇÕES")
            print("="*50)
            for d in dados:
                print(f"{d['nome']:20} - {d['valor']:>10} | {d['variacao']:>10}")
            print("="*50)

            return arquivo

        except Exception as e:
            print(f"Erro na execução: {str(e)}")
            return None


if __name__ == "__main__":
    monitor = InvestmentMonitor()
    monitor.executar()
