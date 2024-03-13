import streamlit as st
import os
from openai import OpenAI

class EvaluacionGenerator:
    def __init__(self, api_key, model_version):
        self.client = OpenAI(api_key=api_key)
        self.templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
        self.model = model_version  

    def _load_template(self, tool_name, template_name):
        template_path = os.path.join(self.templates_dir, tool_name, template_name + '.txt')
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()

    def _generate_text(self, system_message, user_prompt):
        chat_completion = self.client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_message},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0,
            model=self.model,
        )
        return chat_completion.choices[0].message.content

    def generate_evaluation(self, tool_name, actividade):
        system_message = self._load_template(tool_name, 'system_message')
        user_prompt = self._load_template(tool_name, 'prompt').format(
            actividade=actividade,
        )
        return self._generate_text(system_message, user_prompt)

# Interfaz de Streamlit
st.sidebar.title("Configuración da Avaliación")

api_key = st.sidebar.text_input("Introduce a túa API Key de OpenAI:", type="password")
model_version = st.sidebar.selectbox("Selecciona la versión del modelo:", ["GPT 3.5", "GPT 4"])

# Mapear selección del modelo a los identificadores de modelo en OpenAI
model_map = {
    'GPT 3.5': 'gpt-3.5-turbo-0125',
    'GPT 4': 'gpt-4-0125-preview'
}

if not api_key:
    st.error("Por favor, introduce a API Key.")
else:
    st.title("Instrumentos de Avaliación")

    herramienta = st.selectbox("Escolle o tipo de instrumento de avaliación:", ['Escala', 'Rúbrica', 'Lista de cotexo'])
    actividade = st.text_area("Para que debe servir o instrumento?", "Corrixir un texto en forma de artigo de opinión sobre a situación do transporte público en Santiago de Compostela. O texto estará elaborado como unha 'carta ao director' dun xornal.")

    # Convertir nombres para coincidir con las carpetas de templates
    herramienta_map = {
        'Escala': 'escala',
        # 'Rexistro': 'rexistro',
        'Rúbrica': 'rubrica',
        'Lista de cotexo': 'lista_de_cotexo'
    }

    if st.button('Xerar Avaliación'):
        if actividade:
            generator = EvaluacionGenerator(api_key, model_map[model_version])
            resultado = generator.generate_evaluation(herramienta_map[herramienta], actividade)
            st.markdown("### Resultado:")
            st.markdown(resultado, unsafe_allow_html=True)
        else:
            st.error("Por favor, completa o criterio de avaliación e o mínimo de consecución.")
