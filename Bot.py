from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Bot')

conversa = ['Oi', 'Olá',

'Tudo bem?','Tudo ótimo',

'Onde é realizado um jogo de futebol?',
'Um jogo de futebol é realizado em estádios.',

'Quantos jogadores um time pode substituir por jogo?',
'Antes da pandemia podia fazer até 3 substituições em um jogo, porém quando o futebol voltou no meio da pandemia foi autorizado fazer ate 5 substituições por time ao longo da partida.',

'Onde foi a primeira copa do mundo de futebol?',
'A primeira copa do mundo foi realizada no Uruguai, no ano de 1930.',

'Quem ganhou a primeira copa do mundo?',
'O ganhador da primeira copa do mundo foi o Uruguai vencendo a Argentina na grande final.',

'Qual foi o único país que disputou todas as copas do mundo?',
'Desde 1930, o único país que participou de todas as edições de mundial foi o Brasil.',

'Quem marcou o primeiro gol do Brasil em uma copa?',
'O primeiro gol do Brasil em uma copa foi marcado pelo jogador Preguinho contra a Lugoslávia, em 1930.',

'Qual foi o material utilizado na primeira bola de futebol?', 
'A primeira bola de futebol foi feita de couro curtido (capotão) e a câmara de ar era uma bexiga de boi.',

'Quando foi criado os cartões amarelo e vermelho no futebol?',
'Após uma confusão na Copa do Mundo em 1966, a FIFA implantou os cartões amarelo e vermelho, inspirado nas cores do semáforo, amarelo para reduzir a velocidade e vermelhor para parar, o inglês Keen Aston teve a ideia de usar as cores para sinalizar as penalidades.',

'Como os árbitros marcavam as penalidades antes da criação dos cartões?',
'Os árbitros usavam apenas o apito, a voz e gestos para fazer as marcações das penalidades.',

'Qual o clube de futebol mais antigo e que ainda esta em atividade no Brasil?',
'O clube mais antigo e que ainda esta em atividade no Brasil é o Sport Club Rio Grande, fundado em 19 de julho de 1900.',

'Qual foi o maior número de expulsões já visto em uma partida de futebol?',
'O maior número de expulsões já visto em uma partida ocorreu entre o time Portuguesa-SP e Botafogo-RJ em 1954, foram 22 jogadores expulsos após uma briga entre as duas equipes.',

'Qual foi o jogamos mais novo a vencer uma copa do mundo?',
'O jogador mais novo a vencer uma copa do mundo foi Edson Arantes do Nascimento, o Pelé. Com apenas 17 anos, Pelé foi campeão do mundo 1958.',

'Quem é conhecido como o Rei do Futebol?',
'Edson Arantes do Nascimento, mais conhecido como Pelé.',

'Quem é a Rainha do Futebol?',
'A rainha do futebol é a brasileira Marta, eleita seis vezes a melhor do mundo.',

'Quem é conhecido como "Rei dos Dribles"?',
'Ronaldinho Gaúcho.',

'Qual o maior estádio do mundo?',
'O maior estádio do mundo é o Rungrado Primeiro de Maio e está localizado em Pyongyang, capital da Coréia do Norte.',

'Qual o maior estádio do Brasil?',
'O maior estádio do Brasil é o Maracanã, comporta atualmente 78,838 tocedores e está localizado no Rio de Janeiro.',

'Qual a definição de "Impedimento"?',
'Um jogador estará impedido quando estiver no campo de ataque e à frente do último adversário, sem contar o goleiro.',

'Qual o tempo total de uma partida?',
'A partida se divide em dois tempos de 45 minutos, com um intervalo de 15 minutos.',

'Quanto jogadores tem uma partida ?',
'A partida será jogada por duas equipes formadas por um máximo de 11 jogadores cada uma, dos quais um jogará como goleiro. A partida não se iniciará se uma as equipes tiver menos e sete jogadores.',

'Como definimos uma equipe ganhadora de uma partida?',
'Defenimos uma equipe vencedora aquela que pontuar o maior número de gols na partida.',

'Quantos jogadores tem em uma equipe ?',
'Cada equipe é formadas por um máximo de 11 jogadores, dos quais um jogará como goleiro. A partida não se iniciará se uma das equipes tiver menos e sete jogadores.',

'Quais as dimensões em campo de futebol?',
'Comprimento: mínimo 90 m e máximo 120 m / Largura: mínima 45 m e máxima 90 m',

'Quais as marcações do campo de jogo?',
'O campo e jogo será marcado com linhas. As ditas linhas pertencem as áreas que demarcam. As duas linhas de marcação mais compridas denominam-se linhas laterais. As duas mais curtas chamam-se linhas de meta. Todas as linhas terão uma largura de 12 cm como máximo. O campo do jogo estará dividido em duas metades por uma linha média. O centro do campo estará marcado com um ponto na metade a linha média, ao redor do qual se traçara um círculo com um raio e 9,15 m.',

'Quais os times que mais foram rebaixados para a serie B do Brasileirão?',
'Os times que mais foram rebaixados para a serie B do brasileirão foram o América-MG e o Vitória, com 6 rebaixamentos no total.',

'Quais times brasileiros que mais venceram a Libertadores?',
'Os times que mais venceram a libertadores foram São Paulo, Grêmio e santos, ambos com 3 títulos no total.',

'O que é a área de meta?',
'A área de meta, situada em ambos extremos do campo de jogo, será demarcada a seguinte maneira:',

'O que são as bandeiras nos cantos do campo?',
'As bandeiras são usadas para definir se vai ser cobrado escanteio ou lance lateral de acordo com a tragetória da bola, dessa forma a bola bate na bandeira e vai para um dos lados, evitando a indecisão na hora da marcação.',

'Quais são os esquemas táticos mais usados no futebol atualmente?',
'Os esquemas mais usados atualmente são o 4-4-2 e o 3-5-2, pois na visão dos treinadores são os esquemas táticos que possuem uma melhor distribuição entre os setores ofensivo e defensivo.',

'Qual foi o time campeão do Brasileirão de 2020?',
'O time campeão foi o Flamengo pela 7° vez na sua história.',

'Quando foi criado a numeração das camisetas dos jogadores de futebol no Brasil?',
'A ideia de enumerar as camisetas dos jogadores implantada em 1947 com o intuito de facilitar a identificação dos jogadores para os locutores, árbitros e fotógrafos.',

'Quantos árbitros trabalham em uma partida de futebol?',
'As equipes de árbitros são compostas por no mínimo 3 árbitros, sendo eles um árbitro de campo e 2 assitentes, também conhecidos como "bandeirinhas".',

'Quais são as propriedades e medidas de uma bola?',
'A bola ela é esférica, feita de couro ou outro material adequado. Terá uma circuferencia não superior a 70 cm e não inferiror a 68 cm. Terá um peso não superior a 450 g e nao inferior 410 g',

'Como é realizado uma susbtituição?',
'Para substituir-se um jogador por um substituto deverão ser observadas as seguintes condições: - o árbitro deverá ser informado da substituição proposta antes que esta seja efetuada. - o substituto não poderá entrar em campo e jogo até que o jogador o qual substituirá tenha abandonado o campo de jogo e recebido o sinal do árbitro. - o substituto entrará em campo unicamente pela linha central e durante uma interrupção do jogo. - uma substituição ficará consumada quando o substituto entra em campo de jogo - a partir desse momento o substituto se converte em jogador, e o jogador ao qual substitui deixa de ser jogador - um jogador que tenha sido substituído não poderá participar mais da partida - todos os substitutos estão submetidos à autoridade e jurisdição do árbitro, sejam chamados ou não a participar do jogo',

'O que é o VAR?',
'O Video Assistant Referee (VAR) é uma nova tecnologia utilizada para tentar solucionar as jogadas polêmicas que acabam acontecendo no futebol.',

'Quais são as funcionalidades do VAR?',
'Com essa ferramenta tecnológica, é possível rever os lances do jogo por mais de trinta câmeras diferentes, porém os árbitros de vídeo, que são os árbitros responsáveis pela revisão dos lances, só podem interferir no jogo em quatro momentos, para anular ou validar um gol, em situação de pênalti, quando um jogador pode ser expulso e ajudar o arbitro de campo a identificar o infrator correto para aplicar a devida punição.',

'Como é realizado a troca de goleiro?',
'Qualquer dos jogadores poderá trocar a posição com o goleiro, sempre que: O árbitro tenha sido previamente informado, a troca se efetue durante uma interrupção do jogo',

'Como é realizado o reinicio de um jogo?',
'Se o árbitro interromper o jogo para advertir o infrator, o jogo será reiniciado por meio de um tiro livre indireto executado por um jogador da equipes adversária do lugar onde a bola se encontrava quando o árbitro interrompeu a partida.',

'O que é o árbrito?',
'Cada partida será controlada por um árbitro, que terá a autoridade total para fazer cumprir as regras de jogo na partida para a qual tenha sido designado.',

'Como é realizado a recuperação do tempo perdido durante uma partida?',
'Cada período deverá prolongar-se para recuperar todo o tempo perdido por: substituições, avaliação da lesão de jogadores, transporte dos jogadores lesionados para fora do campo de jogo para serem atendidos, perda de tempo ou de qualquer outro motivo, a recuperação do tempo perdido ficará a cargo do árbitro.',

'Quando a bola estará fora de jogo?',
'A bola estará fora de jogo quando: tiver ultrapassado completamente uma linha e lateral ou de meta, seja por terra ou pelo ar',

'Qual o time que mais ganhou a Libertadores?',
'O time que mais ganhou título da Libertadores na história é o Independiente da Argentina com um total de 7 títulos.',

'Qual o time brasileiro que mais venceu mundiais?',
'O time brasileiro que mais venceu mundiais foi o São Paulo, com um total de 3 títulos, conquistados nos anos de 1992, 1993 e 2005.',

'Qual o time que mais venceu mundiais?',
'O time que mais venceu mundiais foi o Real Madrid, com um total de 7 títulos, conquistados nos anos de 1960, 1998, 2002, 2014, 2016, 2017 e 2018.',

'Qual é o jogador mais vitorioso da história do futebol?',
'O jogador mais vitorioso do futebol é o lateral-direito Daniel Alves, da Seleção Brasileira, que já levantou 42 troféus ao longo da sua carreira profissional, sem contar o Mundial sub-20, conquistado com o Brasil em 2003.',

'Quando o cartão vermelhor deve ser aplicado em uma partida de futebol?',
'O cartão vermelho deve ser aplicado ao jogador quando aplica força excessiva ou brutalidade contra seu adversário no momento de disputar a bola.',

'O que acontece com o jogador após receber um cartão vermelho?',
'Após o jogador ser expulso, ele é obrigado a deixar o campo e ir direto para o vestiário, não é permitido ficar nem no banco de reserva do seu time.',

'Tem como um jogador ser expulso de uma partida sem tomar um cartão vermelho?',
'Sim, quando o jogador recebe dois cartões amarelos na mesma partida ele recebe automaticamente um cartão vermelho e é expulso de campo.',

'O treinador de um time também pode ser punido com os cartões amarelo e vermelho?',
'Sim, quando o treinador interfere negativamento no andamento do jogo, ele pode ser advertido com os cartões igual um jogador.',

'O treinador de um time também pode ser expulso?',
'Sim, quando um treinador esta na beira do gramado e reclama muito da arbitragem ou interfere no jogo, ele é advertido com os cartões e se continuar a interferir no jogo, pode receber dois cartões amarelos ou um vermelho direto e ser expulso.',

'',
'',

'',
'',

]

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário: ")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta')