# naranjo_app.py
# Sistema experto simplificado basado en el Algoritmo de Naranjo
# Interfaz: Streamlit
# Autor: Dr. Jekyll (Coordinador del Laboratorio de Innovación)

import streamlit as st

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Evaluador de causalidad - Algoritmo de Naranjo",
    page_icon="💊",
    layout="centered"
)

st.title("💊 Evaluación de causalidad de Reacción Adversa Medicamentosa")
st.caption("Basado en el **Algoritmo de Naranjo**")

# --- PREGUNTAS Y PUNTAJES ---
questions = [
    ("¿Existen informes concluyentes previos sobre esta reacción?", {"si": 1, "no": 0, "no sabe": 0}),
    ("¿Los eventos adversos aparecieron después de la administración del fármaco sospechoso?", {"si": 2, "no": -1, "no sabe": 0}),
    ("¿Mejoró la reacción adversa cuando se suspendió el fármaco o se administró un antagonista específico?", {"si": 1, "no": 0, "no sabe": 0}),
    ("¿Apareció la reacción adversa cuando se volvió a administrar el medicamento?", {"si": 2, "no": -1, "no sabe": 0}),
    ("¿Existen causas alternativas que podrían haber causado la reacción?", {"si": -1, "no": 2, "no sabe": 0}),
    ("¿Reapareció la reacción cuando se administró un placebo?", {"si": -1, "no": 1, "no sabe": 0}),
    ("¿Se detectó el fármaco en algún líquido corporal en concentraciones tóxicas?", {"si": 1, "no": 0, "no sabe": 0}),
    ("¿Fue la reacción más grave cuando se aumentó la dosis o menos grave cuando se redujo?", {"si": 1, "no": 0, "no sabe": 0}),
    ("¿Tuvo el paciente una reacción similar a los mismos medicamentos o similares en exposiciones previas?", {"si": 1, "no": 0, "no sabe": 0}),
    ("¿El evento adverso fue confirmado por evidencia objetiva?", {"si": 1, "no": 0, "no sabe": 0}),
]

# --- FORMULARIO ---
st.subheader("Cuestionario")
responses = {}

with st.form("naranjo_form"):
    for i, (text, opts) in enumerate(questions, start=1):
        responses[f"q{i}"] = st.radio(
            f"{i}. {text}",
            options=list(opts.keys()),
            index=2,  # "no sabe" por defecto
            horizontal=True,
        )
    submitted = st.form_submit_button("Calcular resultado")

# --- CÁLCULO ---
if submitted:
    score = 0
    for i, (_, opts) in enumerate(questions, start=1):
        answer = responses[f"q{i}"]
        score += opts[answer]

    if score >= 9:
        classification = "🟢 Definida (≥ 9)"
    elif 5 <= score <= 8:
        classification = "🟡 Probable (5–8)"
    elif 1 <= score <= 4:
        classification = "🟠 Posible (1–4)"
    elif score == 0:
        classification = "⚪ Dudosa (0)"
    else:
        classification = f"🔴 Improbable (puntaje {score})"

    st.markdown("---")
    st.success(f"**Puntaje total:** {score}")
    st.markdown(f"**Clasificación:** {classification}")

    st.download_button(
        "Descargar resultado",
        data=f"Puntaje total: {score}\nClasificación: {classification}",
        file_name="resultado_naranjo.txt",
        mime="text/plain",
    )

# --- PIE ---
st.markdown("---")
st.caption("Desarrollado con ❤️ utilizando Streamlit y Python. Basado en el Algoritmo de Naranjo (1981).")
