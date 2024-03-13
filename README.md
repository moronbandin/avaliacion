# Xerador de Instrumentos de Avaliación

Este proxecto é unha aplicación de Streamlit deseñada para xerar instrumentos de avaliación personalizados utilizando a API de OpenAI.

## Instalación

Para comezar, clona este repositorio na túa máquina local. Podes facelo executando o seguinte comando no terminal:

```bash
git clone https://github.com/moronbandin/avaliacion.git
```

Despois de clonar o repositorio, navega ata o directorio do proxecto:

```bash
cd avaliacion
```

Instala as dependencias necesarias utilizando `pip`. É recomendable facelo dentro dun entorno virtual para evitar conflitos con outras bibliotecas:

```bash
python -m venv venv
source venv/bin/activate  # En Windows usa 'venv\Scripts\activate'
pip install -r requirements.txt
```

## Configuración

Antes de executar a aplicación, necesitarás establecer a túa clave da API de OpenAI como unha variable de entorno. Isto podes facelo no teu terminal ou engadindo a variable ao arquivo `.env` na raíz do proxecto (deberías crear este arquivo se non existe):

```plaintext
OPENAI_API_KEY=túa_clave_api
```

Se prefires establecela directamente no teu entorno:

```bash
export OPENAI_API_KEY=túa_clave_api  # En Windows usa 'set OPENAI_API_KEY=túa_clave_api'
```

## Execución

Unha vez configurado todo, podes iniciar a aplicación de Streamlit executando:

```bash
streamlit run code/code.py
```

Isto abrirá a aplicación nunha nova pestana do teu navegador.

## Uso

Na aplicación, introduce a túa clave da API de OpenAI no campo correspondente e selecciona a versión do modelo que desexas usar. Despois, escolle o tipo de instrumento de avaliación que queres xerar e proporciona os detalles necesarios. Finalmente, preme o botón "Xerar Avaliación" para obter o teu instrumento de avaliación personalizado.

## Contribucións

As contribucións son benvidas! Por favor, revisa o código, crea unha nova `issue` se atopas algún bug ou envía un pull request se queres engadir novas funcionalidades.

## Licenza

Este proxecto está baixo a Licenza MIT. Consulta o arquivo `LICENSE` para máis detalles.