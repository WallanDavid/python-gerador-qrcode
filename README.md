# Gerador de QR Code

Este é um aplicativo simples em Python que permite aos usuários gerar códigos QR a partir de texto ou URLs fornecidos. Ele oferece uma interface gráfica intuitiva onde você pode personalizar várias opções para o QR Code gerado.

## Funcionalidades

- **Entrada de Texto ou URL:** Os usuários podem inserir texto ou URLs para serem convertidos em QR Code.
- **Seleção de Modo de Codificação:** Escolha entre os modos de codificação Byte, Numérico, Alfanumérico ou Kanji.
- **Personalização do Tamanho e Borda:** Defina o tamanho do QR Code e a borda em módulos.
- **Visualização de Prévia:** Visualize uma prévia do QR Code antes de gerá-lo.
- **Salvar QR Code:** Salve o QR Code gerado como uma imagem PNG.

## Como Usar

1. Instale as dependências executando `pip install -r requirements.txt`.
2. Execute o aplicativo executando `python main.py`.
3. Insira o texto ou URL desejado na entrada.
4. Escolha as opções de personalização desejadas.
5. Visualize a prévia do QR Code clicando no botão "Visualizar Prévia".
6. Clique no botão "Gerar QR Code" para gerar o QR Code.
7. Clique no botão "Salvar QR Code" para salvar o QR Code como uma imagem PNG.

## Requisitos

- Python 3.x
- tkinter
- qrcode
- Pillow

## Contribuição

Contribuições são bem-vindas! Se você deseja melhorar este aplicativo, sinta-se à vontade para enviar pull requests ou abrir issues.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
