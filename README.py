
import webbrowser
from time import sleep
import os
from datetime import date 

os.system('cls')

login_idade=[]
login_cpf=[]
login_senha=[]
login_email=[]
login_idade=[]
login_telefone=[]
login_nome=[]
login_cidade=[]


print('='*35)
print('\033[36mSEJA BEM-VINDO AO SISTEMA PRO SÁUDE\033[m')
print('='*35)
op=0
while op!=3:
    print(''' 
    [1] LOGIN
    [2] CADASTRAR
    [3] SAIR''')
    op=int(input('ESCOLHA A OPÇÃO: '))
    os.system('cls')

    if op==1:
        cpf=int(input('CPF: '))
        senha=int and str(input('SENHA: '))
        if cpf in login_cpf:
            print('\033[32mLogin Efetuado!\033[m')
            sleep(1)
            print(f'\033[32mSeja bem-vindo, {nome}!\033[m')
            sleep(3)
            os.system('cls') 
        
            op2=0
            while op2!=5:
                print('''INFORMAÇÕES SOBRE AS ENFERMIDADES
                [1]- EPIDEMIA DE AIDS
                [2]- HANSENÍASE
                [3]- TUBERCULOSE
                [4]- MARCAR CONSULTA
                [5]- Voltar
                ''')
                op2=int(input('ESCOLHA A OPÇÃO: '))
                os.system('cls')

                if op2==1:
                    print('*'*60)
                    print('SINTOMAS:  febre, fraqueza, emagrecimento e diarreia prolongada. Na fase inicial da doença, outros sintomas começam aparecer, como: candidíase oral, aparecimento de gânglios na virilha, axilas e pescoço, diarreia e febre, perda de 10% do peso do corpo e transpirações noturnas.')
                    print('*'*60)
                    print('TRATAMENTO: O tratamento da AIDS é feito com o uso de medicamentos antirretrovirais oferecidos pelo SUS que são capazes de impedir a multiplicação do vírus HIV e, assim, evitar o enfraquecimento do corpo humano.')
                    print('*'*60)
                    print('ESPECIALSITAS: Psicólogo Clínico | Infectologista | Clínico Geral')
                    resp=str(input(f'\033[33m{nome} você deseja ser redirecionado para um site com informações sobre tratamento da AIDS [Sim/Não]?\033[m')).upper()
                        
                        
                        
                    if login_cidade[0]=='s':
                        if resp[0]=='S':
                            sleep(2)
                            webbrowser.open('https://www.saoluis.ma.gov.br/semus/conteudo/1259')
                           
                        else:
                            os.system('cls')


                          
                    if login_cidade[0]=='p':
                         if resp[0]=='S':
                            sleep(3)
                            print('\033[33mCLIQUE EM UNIDADES DE SAÚDE NO SITE\033[m')
                            sleep(2)
                            webbrowser.open('https://www.pacodolumiar.ma.gov.br/secretaria.php?sec=13')
                            os.system('cls')

                    if login_cidade[0]=='i':
                         if resp[0]=='S':
                            sleep(3)
                            webbrowser.open('http://novo.imperatriz.ma.gov.br/media/site/download/enderecos-e-telefones-ubs/ENDERE%C3%87O_UBS_2022.pdf')
                            os.system('cls')
                if op2==2:
                    print('*'*60)
                    print('SINTOMAS: Uma doença crônica, causada pela bactéria Mycobacterium leprae, que pode afetar qualquer pessoa. Caracteriza-se por alteração, diminuição ou perda da sensibilidade térmica, dolorosa, tátil e força muscular, principalmente em mãos, braços, pés, pernas e olhos e pode gerar incapacidades permanentes..')
                    print('*'*60)
                    print('TRATAMENTO: O tratamento é feito por meio do uso de antibióticos. A lepra pode ser curada com 6 a 12 meses de terapia com vários medicamentos. O tratamento precoce evita deficiência..')
                    print('*'*60)
                    print('ESPECIALISTA: Dermatologista | Infectologista | Imunologista')
                    resp=str(input(f'\033[33m{nome} você deseja ser redirecionado para um site com informações sobre tratamento da Hanseníase [Sim/Não]?\033[m')).upper()

                    if login_cidade[0]=='s':
                         if resp[0]=='S':
                            sleep(3)
                            webbrowser.open('http://www.emserh.ma.gov.br/hospital-aquiles-lisboa-2/')
                            os.system('cls')

                    elif login_cidade[0]=='p':
                        print('\033[31mPaço do Lumiar não detém de um local apropiado para cuidados de hanseníase, referência é São Luís!\033[m')
                        sleep(6)
                        os.system('cls')

                    elif login_cidade[0]=='i':
                         if resp[0]=='S':
                            sleep(3)
                            webbrowser.open('https://postosdesaude.com.br/ma/imperatriz/centro-de-saude-dr-milton-lopes-do-nascimento')
                if op2==3:
                    print('*'*60)
                    print('SINTOMAS: A maioria das pessoas infectadas com a bactéria que causa a tuberculose não apresenta sintomas. Quando ocorrem, os sintomas geralmente incluem tosse (às vezes, com sangue), perda de peso, sudorese noturna e febre..')
                    print('*'*60)
                    print('TRATAMENTO:O tratamento nem sempre é necessário para pacientes assintomáticos. Os pacientes com sintomas manifestos precisam de um longo tratamento com vários antibióticos.')
                    print('*'*60)
                    print('ESPECIALISTA: Pneumologista | Infectologista | Clínico geral')
                    resp=str(input(f'\033[33m{nome} você deseja ser redirecionado para um site com informações sobre tratamento da Tuberculose [Sim/Não]?\033[m')).upper()
                    if login_cidade[0]=='s':
                         if resp[0]=='S':
                            sleep(3)
                            webbrowser.open('http://www.emserh.ma.gov.br/unidade-hospital-presidente-vargas/')

                    if login_cidade[0]=='p':
                        print('\033[31mPaço do Lumiar não detém de um local apropiado para cuidados de tuberculose, referência é São Luís!\033[m')
                        sleep(6)
                        os.system('cls')

                    if login_cidade[0]=='i':
                         if resp[0]=='S':
                            sleep(3)
                            webbrowser.open('https://www.portalsaude.com.br/especialidades/infectologista')
                if op2==4:
                    if login_cidade[0]=='s':
                        doenca=str(input('Qual a enfermidade [Aids / Hanseníase / Tuberculose ]?')).lower()
                        if doenca=='aids':
                            print('''Alemanha / Bairro de Fátima / Lira / Anil.''')
                            opcao=str(input('Qual a opção:')).lower()
                            if opcao=='alemanha':
                                dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                                horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                                prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                                print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                                if prioridade[0]=='s':
                                    print(f'\033[32mEndereço: Av. dos Franceses, 131 - Alemanha/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: Sim.\033[m')
                                else:
                                    print(f'\033[32mEndereço: Av. dos Franceses, 131 - Alemanha/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                                sleep(8)
                                os.system('cls')
                                break
                            if opcao=='bairro de fatima':
                                dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                                horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                                prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                                print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                                if prioridade[0]=='s':
                                    print(f'\033[32mEndereço: Rua gardênia Gonçalves, s/n – Bairro de Fátima/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                                else:
                                     print(f'\033[32mEndereço: Rua gardênia Gonçalves, s/n – Bairro de Fátima/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}\033[m')
                                sleep(8)
                                os.system('cls')
                                break
                            if opcao=='lira':
                                dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                                horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                                prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                                print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                                if prioridade[0]=='s':
                                     print(f'\033[32mEndereço: Praça São Roque, s/n - Lira/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                                else:
                                    print(f'\033[32mEndereço: Praça São Roque, s/n - Lira/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                                sleep(8)
                                os.system('cls')
                                break
                            if opcao=='anil':
                                dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                                horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                                prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                                print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                                if prioridade[0]=='s':
                                    print(f'\033[32mEndereço: Av. São Sebastião, s/n - Anil/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                                else:
                                    print(f'\033[32mEndereço: Av. São Sebastião, s/n - Anil/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                                sleep(8)
                                os.system('cls')
                                break 
                        if doenca=='hanseniase' or 'hanseníase':
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                print(f'\033[32mAv. José Sarney S/N, Bairro Vila Nova – Ponta do Bonfim, São Luís-MA/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:    
                                print(f'\033[32mAv. José Sarney S/N, Bairro Vila Nova – Ponta do Bonfim, São Luís-MA/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 
                        if doenca=='tuberculose':
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if print[0]=='s':
                                print(f'\033[32m Endereço: Rua Cinco de Janeiro, Nº 166/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:
                                print(f'\033[32m Endereço: Rua Cinco de Janeiro, Nº 166/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 

                    if login_cidade[0]=='p':
                        doenca=str(input('Qual a enfermidade [Aids / Hanseníase / Tuberculose ]?')).lower()
                        if doenca=='aids':
                            print('''\033[33mUBS: todas de Paço do Lumiar fazem a consulta, contudo, a medicação especializada é feita no CSU Maiobão.\033[m''')
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if print[0]=='s':
                                print(f'\033[32mEndereço: Próximo ao Supermercado Maciel, Av. 13, S/N/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:
                                print(f'\033[32mEndereço: Próximo ao Supermercado Maciel, Av. 13, S/N/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break
                        if doenca=='hanseniase' or 'hanseníase':
                            print('\033[33mMedicações no CSU MAIOBÃO!\033[m')
                            print('\033[31mPaço do Lumiar não detém de um local apropiado para consulta e cuidados de tuberculose, referência é São Luís!\033[m')
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower()
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                print(f'\033[32mAv. José Sarney S/N, Bairro Vila Nova – Ponta do Bonfim, São Luís-MA/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:
                                print(f'\033[32mAv. José Sarney S/N, Bairro Vila Nova – Ponta do Bonfim, São Luís-MA/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 
                        if doenca=='tuberculose':
                            print('\033[31mPaço do Lumiar não detém de um local apropiado para cuidados de tuberculose, referência é São Luís!\033[m')
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower() 
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                print(f'\033[32m Endereço: Rua Cinco de Janeiro, Nº 166/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:   
                                print(f'\033[32m Endereço: Rua Cinco de Janeiro, Nº 166/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 
                    if login_cidade[0]=='i':
                        doenca=str(input('Qual a enfermidade [Aids / Hanseníase / Tuberculose ]?')).lower()
                        if doenca=='aids':
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower() 
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                print(f'\033[32mEndereço: 164, R. Projetada G, 70 - Bacuri, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:
                                print(f'\033[32mEndereço: 164, R. Projetada G, 70 - Bacuri, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 
                        if doenca=='hanseniase' or 'hanseníase':
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower() 
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                 print(f'\033[32mRUA LEONCIO PIRES DOURADO - 967, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:  
                                print(f'\033[32mRUA LEONCIO PIRES DOURADO - 967, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break 
                        if doenca=='tuberculose':
                            dia=str(input('Qual dia da semana [Segunda à Sexta]?'))
                            horario=int and str(input(f'Qual o melhor horário para a sua consulta no {opcao}[8:00 às 18:00]?'))
                            prioridade=str(input('Se encaixa em algum dessas situações: pessoas portadoras de deficiência física, os idosos com idade igual ou superior a sessenta e cinco anos, as gestantes, as lactantes e as pessoas acompanhadas por crianças de colo [SIM/NÃO]?'))[0].lower() 
                            print(f'\033[32m{nome}, sua consulta foi marcada com sucesso!\033[m')
                            if prioridade[0]=='s':
                                print(f'\033[32mRUA LEONCIO PIRES DOURADO - 967, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}/ Prioridade: sim.\033[m')
                            else:
                                print(f'\033[32mRUA LEONCIO PIRES DOURADO - 967, Imperatriz/ Horário: {horario}/ Enfermidade: {doenca}/ Dia: {dia}.\033[m')
                            sleep(8)
                            os.system('cls')
                            break


                if op2==5:
                    break
                        
        else:
            print('\033[31mLOGIN NEGADO, TENTE NOVAMENTE!\033[m')
            print('\033[31mCPF OU SENHA NÃO CADASTRADO!\033[m')


    if op==2:
            nome=str(input('DIGITE SEU NOME: ')).capitalize()
            login_nome.append(nome)

            cpf=int(input('DIGITE SEU CPF: '))
            login_cpf.append(cpf)
            
        
            senha=int(input('DIGITE SUA SENHA [OBS: APENAS NÚMEROS]: '))
            login_senha.append(senha)
    
            cidade=str(input('REGIÃO [São Luís / Paço do Lumiar / Imperatriz] ? '))[0].lower()
            login_cidade.append(cidade)
        
            email=str(input('Digite seu email: ')).lower()
            login_email.append(email)

            telefone=int(input('Telefone: '))
            login_telefone.append(telefone)

            current_date = date.today()
            data_nascimento= int(input("Ano de nascimento:"))
            data_actual = current_date.year
            idade =data_actual-data_nascimento
            login_idade.append(idade)

            



            print('\033[32m CADASTRO REALIZADO COM SUCESSO! \033[m ')
            sleep(3)
            os.system('cls')
            
    if op==3:
        print('\033[32m SAINDO DO SISTEMA, CUIDE-SE :D !\033[m')
        sleep(5)
        os.system('cls')
