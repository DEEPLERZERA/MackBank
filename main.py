import random
import getpass
from pycpfcnpj import cpfcnpj

contaCliente = []
nomeCliente = []
telefoneCliente = []
emailCliente = []
saldoCliente = []
limiteCreditoCliente = []
senhaCliente = []
historicoOperacoes = []
perguntaSeguranca = []
respostaSeguranca = []
contaCadastrada = 0
qtdErros = 0
cpfCliente = []

def pegueSenha(prompt="SENHA..........: "):
    return getpass.getpass(prompt)

def cadastrarConta():
    global contaCliente, nomeCliente, telefoneCliente, emailCliente, contaCadastrada, saldoCliente, limiteCreditoCliente, senhaCliente, perguntaSeguranca, respostaSeguranca, cpfCliente
    numeroAleatorio = random.randint(1000, 9999)
    print("MACK BANK - CADASTRO DE CONTA")
    print()
    print("NÚMERO DA CONTA:", end=" ")
    print(numeroAleatorio)
    print()
    contaCliente.append(numeroAleatorio)
    nome = input("NOME DO CLIENTE: ")
    print()
    if nome == "":
        print("NOME INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    nomeCliente.append(nome)
    telefone = input("TELEFONE.......: ")
    print()
    if telefone == "":
        print("TELEFONE INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    telefoneCliente.append(telefone)
    email = input("EMAIL.........: ")
    print()
    if email == "":
        print("EMAIL INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    emailCliente.append(email)
    entradaCPF = input("CPF...........: ")
    print()
    if entradaCPF == "":
        print("CPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not cpfcnpj.validate(entradaCPF):
        print("CPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    cpfCliente.append(entradaCPF)
    entradaSaldo = input("SALDO INICIAL...: R$ ")
    print()
    if entradaSaldo == "":
        print("SALDO INICIAL INVÁLIDO (MÍNIMO R$ 1.000,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldo = float(entradaSaldo)
    if saldo < 1000:
        print("SALDO INICIAL INVÁLIDO (MÍNIMO R$ 1.000,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldoCliente.append(saldo)
    entradaLimite = input("LIMITE DE CRÉDITO: R$ ")
    print()
    if entradaLimite == "":
        print("LIMITE DE CRÉDITO INVÁLIDO (MÍNIMO R$ 0,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    limite = float(entradaLimite)
    if limite < 0:
        print("LIMITE DE CRÉDITO INVÁLIDO (MÍNIMO R$ 0,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    limiteCreditoCliente.append(limite)
    senha = pegueSenha("INFORME A SENHA:")
    print()
    if len(senha) < 6 or len(senha) > 6:
        print("SENHA INVÁLIDA (6 DÍGITOS)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    senhaCliente.append(senha)
    confimeSenha = pegueSenha("REPITA A SENHA...: ")
    print()
    if confimeSenha not in senhaCliente:
        print("SENHAS NÃO CONFEREM")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    entradaPergunta = input("PERGUNTA DE SEGURANÇA: ")
    print()
    if entradaPergunta == "":
        print("PERGUNTA DE SEGURANÇA INVÁLIDA")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        perguntaSeguranca = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    perguntaSeguranca.append(entradaPergunta)
    entradaResposta = input("RESPOSTA DA PERGUNTA....: ").lower()
    print()
    if entradaResposta == "":
        print("RESPOSTA INVÁLIDA")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        perguntaSeguranca = []
        respostaSeguranca = []
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    respostaSeguranca.append(entradaResposta)
    input("CADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
    contaCadastrada = 1

def depositarConta():
    print("MACK BANK - DEPÓSITO EM CONTA")
    print()
    entradaConta = input("INFORME O NÚMERO DA CONTA: ")
    print()
    if entradaConta == "":
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("CONTA NÃO CADASTRADA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("NOME DO CLIENTE: ", nomeCliente[indice])
    print()
    entradaDeposito = input("VALOR DO DEPÓSITO: R$ ")
    print()
    if entradaDeposito == "":
        print("VALOR INVÁLIDO")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    deposito = float(entradaDeposito)
    if deposito <= 0:
        print("VALOR INVÁLIDO (DEVE SER MAIOR DO QUE R$ 0,00)")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldoCliente[indice] += deposito
    historicoOperacoes.append(deposito)
    input("DEPÓSITO REALIZADO COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def sacarConta():
    global qtdErros
    print("MACK BANK - SAQUE EM CONTA")
    print()
    entradaConta = input("INFORME O NÚMERO DA CONTA: ")
    print()
    if entradaConta == "":
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("CONTA NÃO CADASTRADA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("NOME DO CLIENTE: ", nomeCliente[indice])
    print()
    entradaSenha = pegueSenha("INFORME A SENHA: ")
    print()
    if entradaSenha != senhaCliente[indice]:
        print("SENHA INCORRETA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    entradaSaque = input("VALOR DO SAQUE..: R$ ")
    print()
    if entradaSaque == "":
        print("VALOR INVÁLIDO")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saque = float(entradaSaque)
    if saque <= 0:
        print("VALOR INVÁLIDO (DEVE SER MAIOR DO QUE R$ 0,00)")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if saque > saldoCliente[indice]:
        if saque > limiteCreditoCliente[indice] + saldoCliente[indice]:
            print("SALDO INSUFICIENTE")
            print()
            input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
            return
        print("VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
        print("SAQUE REALIZADO COM SUCESSO!")
        limiteUtilizado = saque - saldoCliente[indice]
        saldoCliente[indice] = 0
        limiteCreditoCliente[indice] -= limiteUtilizado
        historicoOperacoes.append(-saque)
        return
    saldoCliente[indice] -= saque
    historicoOperacoes.append(-saque)
    input("SAQUE REALIZADO COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
    

def consultarSaldo():
    global qtdErros
    print("MACK BANK - CONSULTA SALDO")
    print()
    entradaConta = input("INFORME O NÚMERO DA CONTA: ")
    print()
    if entradaConta == "":
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("CONTA NÃO CADASTRADA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("NOME DO CLIENTE: ", nomeCliente[indice])
    print()
    senha = pegueSenha("INFORME A SENHA: ")
    print()
    if senha != senhaCliente[indice]:
        print("SENHA INCORRETA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    print(f"SALDO EM CONTA: R$ {saldoCliente[indice]:.2f}")
    print()
    print(f"LIMITE DE CRÉDITO: R$ {limiteCreditoCliente[indice]:.2f}")
    print()
    input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def consultarExtrato():
    global qtdErros
    print("MACK BANK - EXTRATO DA CONTA")
    print()
    entradaConta = input("INFORME O NÚMERO DA CONTA: ")
    print()
    if entradaConta == "":
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("CONTA NÃO CADASTRADA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("NOME DO CLIENTE: ", nomeCliente[indice])
    print()
    senha = pegueSenha("INFORME A SENHA: ")
    print()
    if senha != senhaCliente[indice]:
        print("SENHA INCORRETA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    print(f"LIMITE DE CRÉDITO: R$ {limiteCreditoCliente[indice]:.2f}")
    print()
    print("ÚLTIMAS OPERAÇÕES:")
    print()
    for operacao in historicoOperacoes:
        if operacao < 0:
            print(f"SAQUE: R$ {-operacao:.2f}")
            print()
        else:
            print(f"DEPÓSITO: R$ {operacao:.2f}")
            print()
    print(f"SALDO EM CONTA: R$ {saldoCliente[indice]:.2f}")
    print()
    if saldoCliente[indice] <= 0:
        print("ATENÇÃO AO SEU SALDO, VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO!")
        print()
    input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def recuperarSenha():
    global qtdErros
    print("MACK BANK - RECUPERAÇÃO DE SENHA")
    print()
    entradaConta = input("INFORME O NÚMERO DA CONTA: ")
    print()
    if entradaConta == "":
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("CONTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("CONTA NÃO CADASTRADA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("PERGUNTA DE SEGURANÇA: ", perguntaSeguranca[indice])
    entradaResposta = input("INSIRA A RESPOSTA: ")
    print()
    if entradaResposta == "":
        print("RESPOSTA INVÁLIDA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if entradaResposta.lower() not in respostaSeguranca:
        print("RESPOSTA INCORRETA")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    entradaSenha = pegueSenha("NOVA SENHA: ")
    print()
    if len(entradaSenha) < 6 or len(entradaSenha) > 6:
        print("SENHA INVÁLIDA (6 DÍGITOS)")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    confimeSenha = pegueSenha("REPITA A SENHA: ")
    print()
    if confimeSenha != entradaSenha:
        print("SENHAS NÃO CONFEREM")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    senhaCliente[indice] = entradaSenha
    input("SENHA ALTERADA COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")


while True:
    print("MACK BANK - ESCOLHA UMA OPÇÃO")
    print("   (1)  CADASTRAR CONTA CORRENTE")
    print("   (2)  DEPOSITAR")
    print("   (3)  SACAR")
    print("   (4)  CONSULTAR SALDO")
    print("   (5)  CONSULTAR EXTRATO")
    print("   (6)  RECUPERAR SENHA")
    print("   (7)  FINALIZAR")
    entradaOpcao = input("SUA OPÇÃO: ")

    if entradaOpcao == "":
        print("OPÇÃO INVÁLIDA")
        continue
    
    if not entradaOpcao.isdigit():
        print("OPÇÃO INVÁLIDA")
        continue

    opcao = int(entradaOpcao)

    if opcao < 1 or opcao > 7:
        print("OPÇÃO INVÁLIDA")
        continue

    if opcao == 1 and contaCadastrada == 0:
        cadastrarConta()
        continue 
    elif opcao == 1 and contaCadastrada == 1:
        print("CONTA JÁ CADASTRADA, POR FAVOR SELECIONE OUTRA OPÇÃO")
        continue
    elif opcao == 2:
        depositarConta()
        continue 
    elif opcao == 3 and qtdErros < 3:
        sacarConta()
        continue
    elif opcao == 3 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 4 and qtdErros < 3:
        consultarSaldo()
        continue
    elif opcao == 4 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 5 and qtdErros < 3:
        consultarExtrato()
        continue
    elif opcao == 5 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 6 and qtdErros < 3:
        recuperarSenha()
        continue
    elif opcao == 6 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        print()
        input("PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue

    if opcao == 7:
        print("MACK BANK - SOBRE")
        print()
        print("Este programa foi desenvolvido por")
        print()
        print("Daniel Borges Valentim - 10427564")
        print()
        print("João Vitor Golfieri Mendonça - 10434460")
        break