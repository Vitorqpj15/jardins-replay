Sistema para captura e disponibilização de lances de partidas de futebol.

#Sobre o projeto

O Jardins Replay é um projeto pessoal desenvolvido com o objetivo de facilitar o registro de lances durante partidas de futebol.

A ideia é utilizar uma câmera posicionada na quadra para realizar uma gravação contínua. Quando um jogador identificar um lance que deseja rever, poderá apertar um botão para marcar aquele momento.

O sistema então deverá recuperar os últimos 30 segundos da gravação, permitindo que o lance seja posteriormente visualizado e salvo.

#Objetivo 

Criar um sistema simples que permita aos jogadores:

Assistir novamente a lances que aconteceram durante a partida;
Recuperar automaticamente os segundos anteriores ao acionamento do botão;
Salvar os lances importantes;
Evitar a necessidade de gravar e procurar manualmente toda a partida.

#Funcionamento planejado

O funcionamento inicial será baseado no seguinte fluxo:

Câmera
   ↓
Gravação contínua
   ↓
Jogador aperta o botão
   ↓
Sistema identifica o momento
   ↓
Recupera os últimos 30 segundos
   ↓
Lance fica disponível
   ↓
Usuário pode visualizar e salvar

#Tecnologias
Python
OpenCV
Git
GitHub

#Status do projeto 

O projeto está em desenvolvimento.

Atualmente, o foco está na implementação e nos testes da captura de vídeo utilizando Python e OpenCV.

