import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.contas_saldo import ContasSaldo
class AcessoDados:
    # Iniciando os dados das contas e saldos
    def __init__(self):
        self.TABELA_SALDOS = [
            ContasSaldo(938485762, 180),
            ContasSaldo(347586970, 1200),
            ContasSaldo(2147483649, 0),
            ContasSaldo(675869708, 4900),
            ContasSaldo(238596054, 478),
            ContasSaldo(573659065, 787),
            ContasSaldo(210385733, 10),
            ContasSaldo(674038564, 400),
            ContasSaldo(563856300, 1200)
        ]

    # Consultar saldo
    def consultar(self, id):
        try:
            saldo = next((x for x in self.TABELA_SALDOS if x.conta == id), None)
            if saldo is None:
                raise ValueError(f"Conta {id} não encontrada.")
            return saldo
        except Exception as e:
            print(f"Erro ao consultar saldo para a conta {id}: {e}")
            return None

    # Atualizar saldo
    def atualizar(self, dado):
        try:
            self.TABELA_SALDOS = [x for x in self.TABELA_SALDOS if x.conta != dado.conta]
            self.TABELA_SALDOS.append(dado)
            return True
        except Exception as e:
            print(f"Erro ao atualizar a conta {dado.conta}: {e}")
            return False