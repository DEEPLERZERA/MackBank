import random
import getpass
import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install('pycpfcnpj')
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
    print("\nNÚMERO DA CONTA:", end=" ")
    print(numeroAleatorio)
    contaCliente.append(numeroAleatorio)
    nome = input("\nNOME DO CLIENTE: ")
    if nome == "":
        print("\nNOME INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    nomeCliente.append(nome)
    telefone = input("\nTELEFONE.......: ")
    if telefone == "":
        print("\nTELEFONE INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    telefoneCliente.append(telefone)
    email = input("\nEMAIL.........: ")
    if email == "":
        print("\nEMAIL INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    emailCliente.append(email)
    entradaCPF = input("\nCPF...........: ")
    if entradaCPF == "":
        print("\nCPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not cpfcnpj.validate(entradaCPF):
        print("\nCPF INVÁLIDO")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        cpfCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    cpfCliente.append(entradaCPF)
    entradaSaldo = input("\nSALDO INICIAL...: R$ ")
    if entradaSaldo == "":
        print("\nSALDO INICIAL INVÁLIDO (MÍNIMO R$ 1.000,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldo = float(entradaSaldo)
    if saldo < 1000:
        print("\nSALDO INICIAL INVÁLIDO (MÍNIMO R$ 1.000,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldoCliente.append(saldo)
    entradaLimite = input("\nLIMITE DE CRÉDITO: R$ ")
    if entradaLimite == "":
        print("\nLIMITE DE CRÉDITO INVÁLIDO (MÍNIMO R$ 0,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    limite = float(entradaLimite)
    if limite < 0:
        print("\nLIMITE DE CRÉDITO INVÁLIDO (MÍNIMO R$ 0,00)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    limiteCreditoCliente.append(limite)
    senha = pegueSenha("\nINFORME A SENHA:")
    if len(senha) < 6 or len(senha) > 6:
        print("\nSENHA INVÁLIDA (6 DÍGITOS)")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    senhaCliente.append(senha)
    confimeSenha = pegueSenha("\nREPITA A SENHA...: ")
    if confimeSenha not in senhaCliente:
        print("\nSENHAS NÃO CONFEREM")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    entradaPergunta = input("\nPERGUNTA DE SEGURANÇA: ")
    if entradaPergunta == "":
        print("\nPERGUNTA DE SEGURANÇA INVÁLIDA")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        perguntaSeguranca = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    perguntaSeguranca.append(entradaPergunta)
    entradaResposta = input("\nRESPOSTA DA PERGUNTA....: ").lower()
    if entradaResposta == "":
        print("\nRESPOSTA INVÁLIDA")
        contaCliente = []
        nomeCliente = []
        telefoneCliente = []
        emailCliente = []
        saldoCliente = []
        limiteCreditoCliente = []
        senhaCliente = []
        perguntaSeguranca = []
        respostaSeguranca = []
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    respostaSeguranca.append(entradaResposta)
    input("\nCADASTRO REALIZADO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
    contaCadastrada = 1

def depositarConta():
    print("MACK BANK - DEPÓSITO EM CONTA")
    entradaConta = input("\nINFORME O NÚMERO DA CONTA: ")
    if entradaConta == "":
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("\nCONTA NÃO CADASTRADA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("\nNOME DO CLIENTE: ", nomeCliente[indice])
    entradaDeposito = input("\nVALOR DO DEPÓSITO: R$ ")
    if entradaDeposito == "":
        print("\nVALOR INVÁLIDO")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    deposito = float(entradaDeposito)
    if deposito <= 0:
        print("\nVALOR INVÁLIDO (DEVE SER MAIOR DO QUE R$ 0,00)")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saldoCliente[indice] += deposito
    historicoOperacoes.append(deposito)
    input("\nDEPÓSITO REALIZADO COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def sacarConta():
    global qtdErros
    print("MACK BANK - SAQUE EM CONTA")
    entradaConta = input("\nINFORME O NÚMERO DA CONTA: ")
    if entradaConta == "":
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("\nCONTA NÃO CADASTRADA")
    
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("\nNOME DO CLIENTE: ", nomeCliente[indice])
    entradaSenha = pegueSenha("\nINFORME A SENHA: ")
    if entradaSenha != senhaCliente[indice]:
        print("\nSENHA INCORRETA")      
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    entradaSaque = input("\nVALOR DO SAQUE..: R$ ")
    if entradaSaque == "":
        print("\nVALOR INVÁLIDO")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    saque = float(entradaSaque)
    if saque <= 0:
        print("\nVALOR INVÁLIDO (DEVE SER MAIOR DO QUE R$ 0,00)")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if saque > saldoCliente[indice]:
        if saque > limiteCreditoCliente[indice] + saldoCliente[indice]:
            print("\nSALDO INSUFICIENTE")
            input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
            return
        print("\nVOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO")
        print("\nSAQUE REALIZADO COM SUCESSO!")
        limiteUtilizado = saque - saldoCliente[indice]
        saldoCliente[indice] = 0
        limiteCreditoCliente[indice] -= limiteUtilizado
        historicoOperacoes.append(-saque)
        return
    saldoCliente[indice] -= saque
    historicoOperacoes.append(-saque)
    input("\nSAQUE REALIZADO COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
    

def consultarSaldo():
    global qtdErros
    print("MACK BANK - CONSULTA SALDO")
    entradaConta = input("\nINFORME O NÚMERO DA CONTA: ")
    if entradaConta == "":
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("\nCONTA NÃO CADASTRADA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("\nNOME DO CLIENTE: ", nomeCliente[indice])
    senha = pegueSenha("\nINFORME A SENHA: ")
    if senha != senhaCliente[indice]:
        print("\nSENHA INCORRETA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    print(f"\nSALDO EM CONTA: R$ {saldoCliente[indice]:.2f}")
    print(f"\nLIMITE DE CRÉDITO: R$ {limiteCreditoCliente[indice]:.2f}")
    input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def consultarExtrato():
    global qtdErros
    print("MACK BANK - EXTRATO DA CONTA")
    entradaConta = input("\nINFORME O NÚMERO DA CONTA: ")
    if entradaConta == "":
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("\nCONTA NÃO CADASTRADA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("\nNOME DO CLIENTE: ", nomeCliente[indice])
    senha = pegueSenha("\nINFORME A SENHA: ")
    if senha != senhaCliente[indice]:
        print("\nSENHA INCORRETA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        qtdErros += 1
        return
    print(f"\nLIMITE DE CRÉDITO: R$ {limiteCreditoCliente[indice]:.2f}")
    print("\nÚLTIMAS OPERAÇÕES:")
    for operacao in historicoOperacoes:
        if operacao < 0:
            print(f"\nSAQUE: R$ {-operacao:.2f}")
        else:
            print(f"\nDEPÓSITO: R$ {operacao:.2f}")
    print(f"\nSALDO EM CONTA: R$ {saldoCliente[indice]:.2f}")
    if saldoCliente[indice] <= 0:
        print("\nATENÇÃO AO SEU SALDO, VOCÊ ESTÁ USANDO O SEU LIMITE DE CRÉDITO!")
    input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")

def recuperarSenha():
    global qtdErros
    print("MACK BANK - RECUPERAÇÃO DE SENHA")
    entradaConta = input("\nINFORME O NÚMERO DA CONTA: ")
    if entradaConta == "":
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if not entradaConta.isdigit():
        print("\nCONTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    conta = int(entradaConta)
    if conta not in contaCliente:
        print("\nCONTA NÃO CADASTRADA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    indice = contaCliente.index(conta)
    print("\nPERGUNTA DE SEGURANÇA: ", perguntaSeguranca[indice])
    entradaResposta = input("\nINSIRA A RESPOSTA: ")
    if entradaResposta == "":
        print("\nRESPOSTA INVÁLIDA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    if entradaResposta.lower() not in respostaSeguranca:
        print("\nRESPOSTA INCORRETA")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    entradaSenha = pegueSenha("\nNOVA SENHA: ")
    if len(entradaSenha) < 6 or len(entradaSenha) > 6:
        print("\nSENHA INVÁLIDA (6 DÍGITOS)")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    confimeSenha = pegueSenha("\nREPITA A SENHA: ")
    if confimeSenha != entradaSenha:
        print("\nSENHAS NÃO CONFEREM")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        return
    senhaCliente[indice] = entradaSenha
    input("\nSENHA ALTERADA COM SUCESSO! PRESSIONE UMA TECLA PARA VOLTAR AO MENU...")


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
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 4 and qtdErros < 3:
        consultarSaldo()
        continue
    elif opcao == 4 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 5 and qtdErros < 3:
        consultarExtrato()
        continue
    elif opcao == 5 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue
    elif opcao == 6 and qtdErros < 3:
        recuperarSenha()
        continue
    elif opcao == 6 and qtdErros == 3:
        print("VOCÊ EXCEDEU O NÚMERO DE TENTATIVAS PERMITIDAS, CONTA BLOQUEADA!")
        input("\nPRESSIONE UMA TECLA PARA VOLTAR AO MENU...")
        continue

    if opcao == 7:
        print("MACK BANK - SOBRE")      
        print("\nEste programa foi desenvolvido por")
        print("\nDaniel Borges Valentim - 10427564")
        print("\nJoão Vitor Golfieri Mendonça - 10434460")
        break