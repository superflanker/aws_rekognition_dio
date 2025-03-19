# Reconhecimento de Celebridades com AWS Rekognition

Este projeto utiliza o serviço **AWS Rekognition** para detectar celebridades em imagens e marcar seus rostos com caixas delimitadoras.

## 🚀 Tecnologias Utilizadas
- **Python**
- **AWS Rekognition** (via `boto3`)
- **Pillow (PIL)** para manipulação de imagens
- **Mypy-boto3-rekognition** para tipagem segura

## 📌 Pré-requisitos
Antes de rodar o código, certifique-se de que:
- Você tem uma **conta AWS** e permissões para usar o **Rekognition**.
- As credenciais AWS estão configuradas corretamente (via `aws configure` ou variáveis de ambiente).
- O ambiente tem os pacotes necessários instalados.

## 🛠 Instalação
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-usuario/aws-rekognition-celebridades.git
   cd aws-rekognition-celebridades
   ```
2. Instale as dependências:
    ```sh
    uv install
    ```
3. Configure suas credenciais AWS (caso ainda não tenha feito):
   ```sh
   aws configure
   ```

## 📷 Como Usar
1. Coloque suas imagens no diretório **imagens/**.
2. Execute o script:
   ```sh
   uv aws_rekognition_faces.py
   ```
3. O programa processará as imagens e salvará os resultados com caixas delimitadoras das faces reconhecidas.

## 📁 Estrutura do Projeto
```
├── imagens/
│   ├── bbc.jpg
│   ├── msn.jpg
│   ├── neymar-celebridades.jpg
├── aws_rekognition_faces.py
├── pyproject.toml
├── uv.lock
├── README.md
```

## 🎯 Funcionalidades
✅ Identificação automática de celebridades em imagens
✅ Desenho de caixas delimitadoras sobre as faces detectadas
✅ Salvamento da imagem processada no diretório de saída

## 📌 Exemplo de Uso
Se o programa detectar uma celebridade na imagem `msn.jpg`, ele salvará um novo arquivo `msn-detectado.jpg` com a face destacada.

## 🔍 Erros Comuns e Soluções
- **AccessDeniedException**: Verifique se seu usuário IAM tem permissões para `rekognition:RecognizeCelebrities`.
- **Arquivo não encontrado**: Confirme que as imagens estão na pasta correta.

## 💡 Possíveis Aplicações e Insights
### 🎯 **1. Monitoramento de Mídia e Jornalismo**  
📌 **Uso:** Monitorar notícias, eventos e redes sociais para identificar automaticamente celebridades em imagens e vídeos.  
💡 **Insight:** O projeto pode ser ampliado para processar automaticamente imagens de portais de notícias e categorizar conteúdos com base nas personalidades detectadas.

### 🏆 **2. Aplicações em Esportes**  
📌 **Uso:** Reconhecer jogadores e personalidades esportivas em eventos ao vivo ou em fotos de torcedores.  
💡 **Insight:** Integrar com um sistema de estatísticas esportivas para fornecer detalhes sobre o desempenho e a história do atleta reconhecido.

### 🎥 **3. Reconhecimento em Eventos e Shows**  
📌 **Uso:** Identificar celebridades em eventos públicos, como premiações e festivais.  
💡 **Insight:** Criar um **bot de mídia social** que reconheça e marque automaticamente celebridades em fotos de eventos ao vivo.

### 🛍️ **4. Marketing e Publicidade**  
📌 **Uso:** Rastrear quais celebridades aparecem em campanhas publicitárias ou publicações patrocinadas.  
💡 **Insight:** Integrar com uma ferramenta de análise de engajamento para medir o impacto de uma celebridade na campanha.

### 🔍 **5. Detecção de Deepfakes e Verificação de Autenticidade**  
📌 **Uso:** Validar se uma imagem é realmente de uma celebridade ou se foi manipulada.  
💡 **Insight:** Expandir o projeto para usar inteligência artificial a fim de comparar rostos reconhecidos com possíveis deepfakes.

### 🏛️ **6. Arquivos Históricos e Museus**  
📌 **Uso:** Identificar figuras históricas em imagens antigas e associá-las a bancos de dados de biografias.  
💡 **Insight:** Aplicar técnicas de aprimoramento de imagens para melhorar a qualidade de fotos antigas antes do reconhecimento.

### 📲 **7. Aplicações Móveis e Redes Sociais**  
📌 **Uso:** Criar um app onde usuários possam enviar fotos e verificar se encontraram uma celebridade.  
💡 **Insight:** Implementar um ranking das celebridades mais detectadas e permitir que usuários compartilhem resultados diretamente.

### 🔐 **8. Controle de Acesso VIP**  
📌 **Uso:** Sistemas de segurança podem identificar automaticamente VIPs e celebridades em locais restritos.  
💡 **Insight:** Integrar o sistema com câmeras de segurança para reconhecimento em tempo real.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo conforme necessário!

---
💡 **Dúvidas ou sugestões?** Fique à vontade para abrir um issue ou contribuir! 🚀


