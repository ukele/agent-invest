#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para executar o monitoramento de ações
Cria um arquivo Excel com os dados das ações consultadas
"""

from investment_monitor import InvestmentMonitor
import sys

def main():
    print("\n" + "="*60)
    print("MONITOR DE AÇÕES - STATUS INVEST")
    print("="*60 + "\n")

    monitor = InvestmentMonitor()

    try:
        arquivo_gerado = monitor.executar()

        if arquivo_gerado:
            print(f"\n✓ Sucesso! Arquivo gerado: {arquivo_gerado}")
            return 0
        else:
            print("\n✗ Erro ao gerar arquivo")
            return 1

    except KeyboardInterrupt:
        print("\n\nOperação cancelada pelo usuário")
        return 1
    except Exception as e:
        print(f"\n✗ Erro inesperado: {str(e)}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
