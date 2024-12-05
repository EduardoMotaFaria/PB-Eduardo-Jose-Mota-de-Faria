from functools import reduce


def calcula_saldo(lancamentos) -> float:
    valores_ajustados = map(
        lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    saldo_final = reduce(lambda acc, valor: acc + valor, valores_ajustados, 0)

    return saldo_final
