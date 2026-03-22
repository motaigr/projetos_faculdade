# Jogo de Aventura na Floresta Assombrada
# Criatividade: O jogo possui mais de 3 níveis em alguns caminhos, 
# com 3 opções na primeira escolha e múltiplos caminhos alternativos 
# em cada ramificação, totalizando mais de 15 finais possíveis.
#Criado a mensagem de boas-vindas e a primeira escolha do jogador
print ("Bem-vindo ao jogo de aventura! Você está em uma floresta assombrada e precisa encontrar uma vila segura para se refugiar. Para isso, você deve escolher o caminho certo. Boa sorte!")
primeira_escolha = input("Você tem três caminhos à sua frente: o caminho da ESQUERDA, o caminho do MEIO e o caminho da DIREITA. Qual caminho você escolhe? ").upper()
if primeira_escolha == "ESQUERDA":
#Criado a segunda escolha do jogador caso ele escolha o caminho da esquerda
    rio_primeira_escolha = input("Você encontrou um rio! Você pode NADAR, ou construir uma JANGADA. O que você escolhe?").upper()
    if rio_primeira_escolha == "NADAR":
        nadar_primeira_escolha = input("Você está sendo levado pela correnteza, você pode CONTINUAR nadando ou se AGARRAR em um tronco flutuante. O que você escolhe?").upper()
        if nadar_primeira_escolha == "CONTINUAR":
            continuacao_segunda_escolha = input("Você conseguiu nadar até a outra margem e viu um caminho DESCENDO rio abaixo e outro SEGUINDO floresta adentro. Qual caminho você escolhe?").upper()
            if continuacao_segunda_escolha == "DESCENDO":
                escolha_final_descendo = input("Você seguiu o caminho descendo rio abaixo e encontrou um vilarejo tranquilo as margens de uma cachoeira, nela você ve uma ESTALAGEM, e uma TAVERNA. Qual lugar você escolhe para se refugiar?").upper()
                if escolha_final_descendo == "ESTALAGEM":
                    print("Você escolheu a estalagem. O estalajadeiro era um homem gentil que te ofereceu comida, abrigo e informações sobre a região.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                elif escolha_final_descendo == "TAVERNA":
                    print("Você escolheu a taverna. Ao entrar, percebeu que estava cheia de caçadores de recompensa que te reconheceram. Antes que pudesse escapar, você foi capturado e levado de volta para a floresta. Você perdeu!")
                else:
                    print("Escolha inválida. Você perdeu!")
            elif continuacao_segunda_escolha == "SEGUINDO":
                print("Você seguiu o caminho seguindo floresta adentro e encontrou um cabana de caça abandonada, ao entrar percebeu que estava vazia e se sente seguro para se refugiar.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            else:
                print("Escolha inválida. Você perdeu!")
        elif nadar_primeira_escolha == "AGARRAR":
            print("Você se agarrou em um tronco, e seguiu corredeira abaixo e acabou caindo de uma cachoeira.")
            escolha_primeiro_final = input("Ao sair da água, você ve um vilarejo tranquilo, nela você ve uma ESTALAGEM, e uma TAVERNA. Qual lugar você escolhe para se refugiar?").upper()
            if escolha_primeiro_final == "ESTALAGEM":
                    print("Você escolheu a estalagem. O estalajadeiro era um homem gentil que te ofereceu comida, abrigo e informações sobre a região.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif escolha_primeiro_final == "TAVERNA":
                    print("Você escolheu a taverna. Ao entrar, percebeu que estava cheia de caçadores de recompensa que te reconheceram. Antes que pudesse escapar, você foi capturado e levado de volta para a floresta. Você perdeu!")
            else:
                 print("Escolha inválida. Você perdeu!")        
        else:
            print("Escolha inválida. Você perdeu!")    
# continuação da segunda escolha do jogador caso ele escolha fazer uma jangada
    elif rio_primeira_escolha == "JANGADA":
        escolha_jangada = input("Você construiu uma jangada, e ao descer o rio percebeu que estava sendo levado até uma cachoeira. Você se SEGURA na jangada ou tenta PULAR para a margem?").upper()
        if escolha_jangada == "SEGURA":
            escolha_final_jangada = input("Você se segurou na jangada e conseguiu descer a cachoeira sem se machucar. Ao chegar na base da cachoeira, você encontrou um vilarejo tranquilo as margens de uma cachoeira, nela você ve uma ESTALAGEM, e uma TAVERNA. Qual lugar você escolhe para se refugiar?").upper()
            if escolha_final_jangada == "ESTALAGEM":
                    print("Você escolheu a estalagem. O estalajadeiro era um homem gentil que te ofereceu comida, abrigo e informações sobre a região.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif escolha_final_jangada == "TAVERNA":
                    print("Você escolheu a taverna. Ao entrar, percebeu que estava cheia de caçadores de recompensa que te reconheceram. Antes que pudesse escapar, você foi capturado e levado de volta para a floresta. Você perdeu!")
            else:
                print("Escolha inválida. Você perdeu!")
        elif escolha_jangada == "PULAR":
            print("Você tentou pular para a margem, mas acabou caindo na água e se machucando. Você perdeu!")
        else:            
            print("Escolha inválida. Você perdeu!")

# continuação da segunda escolha do jogador caso ele escolha seguir em terra firme
    else:
        print("Escolha inválida. Você perdeu!")

#criado a segunda escolha do jogador caso ele escolha o caminho do meio 
elif primeira_escolha == "MEIO":
    escolha_meio = input("Você chegou em uma encruzilhada, você pode seguir pela TRILHA ou pela ESTRADA. Qual caminho você escolhe?").upper()
    if escolha_meio == "TRILHA":
        primeira_escolha_meio = input("Você seguiu para a direita e a estrada estreita começou a se tornar uma mata fechada. Você CONTINUA ou VOLTA pelo mesmo caminho?").upper()
        if primeira_escolha_meio == "CONTINUA":
            primeira_escolha_continua = input("Você continuou pela mata fechada e achou uma cabana iluminada. Você bate na porta e um velho senhor abre, você pede ABRIGO a ele ou PERGUNTA sobre a vila mais próxima?").upper()
            if primeira_escolha_continua == "ABRIGO":
                print("O velho senhor se assusta com o seu pedido e te expulsa da cabana, você se perde na mata e não consegue encontrar a saída. Você perdeu!")
            elif primeira_escolha_continua == "PERGUNTA":
                print("O velho senhor te dá informações sobre a vila mais próxima e te indica o caminho para chegar lá. Proximo ao por do sol você encontra uma vila com uma estalagem segura para se refugiar.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            else:
                print("Escolha inválida. Você perdeu!")
        elif primeira_escolha_meio == "VOLTA":
            escolha_volta = input("Você voltou e encontrou um VIAJANTE misterioso e uma PLACA indicando uma saída. O que você faz?").upper()
            if escolha_volta == "VIAJANTE":
                print("O viajante misterioso se apresenta como um guia experiente e oferece sua ajuda para encontrar a vila segura. Ele te leva por um caminho alternativo e vocês chegam à vila em segurança.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif escolha_volta == "PLACA":
                print("Você seguiu a placa, mas ela acabou te levando para uma armadilha. Você foi capturado por bandidos e perdeu o jogo!")
            else:
                print("Escolha inválida. Você perdeu!")
        else:
            print("Escolha inválida. Você perdeu!")
    elif escolha_meio == "ESTRADA":
        segunda_escolha_meio = input("Você seguiu para a esquerda e encontrou um grupo de viajantes amigaveis que estavam acampando. Eles te ofereceram comida, abrigo e convidam para se juntar a eles. Você ACEITA o convite ou continua viajando SOZINHO?").upper()
        if segunda_escolha_meio == "ACEITA":
            segunda_escolha_aceita = input("Você aceitou o convite e se juntou ao grupo. Eles te convidam para uma FOGUEIRA para conversar ou uma TENDA para descansar. O que você escolhe?").upper()
            if segunda_escolha_aceita == "FOGUEIRA":
                print("Você se sentou ao redor da fogueira e compartilhou histórias com os viajantes. Eles te deram informações valiosas sobre a região e pegaram no sono em volta da fogueira em segurança.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif segunda_escolha_aceita == "TENDA":
                print("Você entra na tenda e descansa tranquilamente durante a noite.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            else:
                print("Escolha inválida. Você perdeu!")   

        elif segunda_escolha_meio == "SOZINHO":
            segunda_escolha_sozinho = input("Você recusou o convite e continuou andando sozinho pela estrada até anoitecer. Você ve um grupo vindo em sua direção, como está longe não consegue identificar se são amigos ou inimigos. Você entra na FLORESTA para se esconder ou segue em FRENTE?").upper()
            if segunda_escolha_sozinho == "FLORESTA":
                print("Você entrou na floresta para se esconder, mas acabou se perdendo e não conseguiu encontrar a saída. Você perdeu!")
            elif segunda_escolha_sozinho == "FRENTE":
                print("Você seguiu em frente e nota que é um grupo de mercenarios. Eles te reconhecem como um forasteiro e te capturam, levando de volta para a floresta. Você perdeu!")
            else:
                print("Escolha inválida. Você perdeu!")
                    
        else:
            print("Escolha inválida. Você perdeu!")    
    else:   
        print("Escolha inválida. Você perdeu!")    
     
#criado a terceira escolha do jogador caso ele escolha o caminho da direita
else:
    primeira_escolha_direita = input("Você seguiu pelo caminho da direita e encontrou uma montanha à sua frente. Você pode tentar ESCALAR ou contornar pelo VALE. O que você escolhe?").upper()
    if primeira_escolha_direita == "ESCALAR":
        escolha_escalar = input("Você começou a escalar a montanha, mas o terreno é instável e você pode DESCER ou CONTINUAR escalando. O que você escolhe?").upper()
        if escolha_escalar == "DESCER":
            segunda_escolha_descer = input("Você desceu da montanha em segurança, você está se sentindo cansado e desanimado, você para um pouco para DESCANSAR ou CONTINUA caminhando?").upper()
            if segunda_escolha_descer == "DESCANSAR":
                terceira_escolha_descansar = input("Você decidiu descansar por um momento, mas acabou adormecendo e acordou e percebeu que já estava escurecendo. Desesperado, você tenta ESCALAR novamente a montanha ou começa a CORRER para encontrar um lugar seguro antes que anoiteça?").upper()
                if terceira_escolha_descansar == "ESCALAR":
                    print("Você tentou escalar a montanha novamente, mas o terreno estava ainda mais instável e você acabou caindo e se machucando. Você perdeu!")
                elif terceira_escolha_descansar == "CORRER":
                    print("Você começou a correr para encontrar um lugar seguro, mas acabou se perdendo na floresta e não conseguiu encontrar a saída. Você perdeu!")
                else:
                    print("Escolha inválida. Você perdeu!")
            elif segunda_escolha_descer == "CONTINUA":
                terceira_escolha_continua = input("Você conseguiu escalar a montanha com sucesso apesar das dificuldades. No topo da montanha, você encontra um acampamento com alguns viajantes. Você pode se aproximar e pedir ABRIGO ou CONTINUAR seguindo o caminho?").upper()
                if terceira_escolha_continua == "ABRIGO":
                    escolha_final_abrigo = input("Você se aproximou do acampamento e pediu abrigo aos viajantes. Eles eram pessoas amigáveis e te ofereceram comida, abrigo e informações sobre a região. O que você escolhe?").upper()
                    if escolha_final_abrigo == "COMIDA":
                        print("Os viajantes te ofereceram comida, e você se sentiu revigorado para continuar sua jornada. Eles também te deram informações valiosas sobre a região e te indicaram o caminho para chegar à vila segura.")
                        print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                    elif escolha_final_abrigo == "SACO DE DORMIR":
                        print("Os viajantes te ofereceram um saco de dormir, e você passou a noite descansando tranquilamente. No dia seguinte, eles te deram informações valiosas sobre a região e te indicaram o caminho para chegar à vila segura.")
                        print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                    else:
                        print("Escolha inválida. Você perdeu!")
                elif terceira_escolha_continua == "CONTINUAR":
                    print("Você decidiu continuar seguindo o caminho, mas acabou se perdendo na floresta e não conseguiu encontrar a saída. Você perdeu!")
                else:
                    print("Escolha inválida. Você perdeu!")
            else:
                print("Escolha inválida. Você perdeu!")        
        elif escolha_escalar == "CONTINUAR":
            segunda_escolha_continuar = input("Você conseguiu escalar a montanha com sucesso apesar das dificuldades. No topo da montanha, você encontra um acampamento com alguns viajantes. Você pode se aproximar e pedir ABRIGO ou CONTINUAR seguindo o caminho?").upper()
            if segunda_escolha_continuar == "ABRIGO":
                print("Você se aproximou do acampamento e pediu abrigo aos viajantes. Eles eram pessoas amigáveis e te ofereceram comida, abrigo e informações sobre a região.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif segunda_escolha_continuar == "CONTINUAR":
                print("Você decidiu continuar seguindo o caminho, mas acabou se perdendo na floresta e não conseguiu encontrar a saída. Você perdeu!")
            else:
                print("Escolha inválida. Você perdeu!")
        else:
            print("Escolha inválida. Você perdeu!")
    elif primeira_escolha_direita == "VALE":
        segunda_escolha_vale = input("Você decidiu contornar a montanha pelo vale, e se depara com um caminho INGREME e outro PLANO. Qual caminho você escolhe?").upper()
        if segunda_escolha_vale == "INGREME":
            terceira_escolha_ingreme = input("Você escolheu o caminho íngreme, e após uma longa caminhada chegou no topo da montanha. Lá, você encontrou um acampamento com alguns viajantes. Você pode se aproximar e pedir ABRIGO ou CONTINUAR seguindo o caminho?").upper()
            if terceira_escolha_ingreme == "ABRIGO":
                quarta_escolha_abrigo = input("Você se aproximou do acampamento e pediu abrigo aos viajantes. Eles eram pessoas amigáveis e te ofereceram COMIDA ou um SACO DE DORMIR para passar a noite. O que você escolhe?").upper()
                if quarta_escolha_abrigo == "COMIDA":
                    print("Os viajantes te ofereceram comida, e você se sentiu revigorado para continuar sua jornada. Eles também te deram informações valiosas sobre a região e te indicaram o caminho para chegar à vila segura.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                elif quarta_escolha_abrigo == "SACO DE DORMIR":
                    print("Os viajantes te ofereceram um saco de dormir, e você passou a noite descansando tranquilamente. No dia seguinte, eles te deram informações valiosas sobre a região e te indicaram o caminho para chegar à vila segura.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                else:
                    print("Escolha inválida. Você perdeu!")
            elif terceira_escolha_ingreme == "CONTINUAR":
                escolha_final_ingreme = input("Você decidiu continuar seguindo o caminho, mas a floresta começou a ficar mais densa você segue em FRENTE ou volta para o ACAMPAMENTO?").upper()
                if escolha_final_ingreme == "FRENTE":
                    print("Você seguiu em frente e acabou se perdendo na floresta, não conseguiu encontrar a saída e acabou morrendo de fome. Você perdeu!")
                elif escolha_final_ingreme == "ACAMPAMENTO":
                    print("Você decidiu voltar para o acampamento, e os viajantes te receberam de volta com alegria, te ofereceram comida, abrigo e informações sobre a região.")
                    print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
                else:
                    print("Escolha inválida. Você perdeu!")
            else:
                print("Escolha inválida. Você perdeu!")
        elif segunda_escolha_vale == "PLANO":
            terceria_escolha_plano = input("Você escolheu o caminho plano, ao inves de contornar a montanha. No final do vale, você encontra algumas cabanas, você BATE na porta da cabana ou ENTRA na cabana?").upper()
            if terceria_escolha_plano == "BATE":
                print("Você bate na porta da cabana e um velho senhor abre, ele percebe que você está cansado e te oferece abrigo.")
                print("Parabéns, você encontrou um lugar seguro para se refugiar e venceu o jogo!")
            elif terceria_escolha_plano == "ENTRA":
                print("Você entrou na cabana sem bater, e encontrou um velho senhor que se assustou com a sua presença e te atacou. Você perdeu!")    
            else:
                print("Escolha inválida. Você perdeu!")

    else:
        print("Escolha inválida. Você perdeu!")

