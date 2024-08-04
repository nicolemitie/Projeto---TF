import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.executar_transacao_financeira import ExecutarTransacaoFinanceira

def main(transacoes):
    executor = ExecutarTransacaoFinanceira()
    # Executar as transações financeiras na ordem do datetime
    transacoes_ordenadas = sorted(transacoes, key=lambda x: x["datetime"])

    for item in transacoes_ordenadas:
        executor.transferir(item["correlation_id"], item["conta_origem"], item["conta_destino"], item["VALOR"])

if __name__ == "__main__":
    pass