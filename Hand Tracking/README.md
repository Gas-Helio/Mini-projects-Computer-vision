# Hand Traking

Nesse projeto fiz um hand traking em tempo real pegando as imagens diretas da webcam. Para isso utilizei o mediapipe para detectar a mão e o opencv para obter as imagens da webcam, desenhar os pontos e exibir o resultado.

## Instalação

Use o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/) para instalar os requisitos.

```bash
pip install requirements.txt
```

## Execução

Você pode escolher qual webcam usar para detectar a mão, mudando o parâmetro da função `VideoCapture` na linha 5 do arquivo `main.py`

```bash
python main.py
```

No gif abaixo podemos ver o resultado.

![Exemplo](img/hand.gif)