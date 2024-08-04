import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.acesso_dados import AcessoDados

class ExecutarTransacaoFinanceira(AcessoDados):
    # Logica de principal de tranferecia financeira
    def transferir(self, correlation_id, conta_origem, conta_destino, valor):
        try:
            conta_saldo_origem = self.consultar(conta_origem)
            if conta_saldo_origem.saldo < valor:
                print(f"Transacao numero {correlation_id} foi cancelada por falta de saldo")
            else:
                conta_saldo_destino = self.consultar(conta_destino)
                conta_saldo_origem.saldo -= valor
                conta_saldo_destino.saldo += valor
                print(f"Transacao numero {correlation_id} foi efetivada com sucesso! Novos saldos: Conta Origem: {conta_saldo_origem.saldo} | Conta Destino: {conta_saldo_destino.saldo}")

        except Exception as e:
            print(f"Erro inesperado na transacao numero {correlation_id}: {e}")