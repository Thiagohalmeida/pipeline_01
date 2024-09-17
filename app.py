import streamlit as st
from contrato import *
from datetime import datetime, time
from pydantic import ValidationError

def main():
    st.title("Nosso Sistema de Input")
    email = st.text_input("Email")
    data = st.date_input("Data", datetime.now())
    hora = st.time_input("Hora", value=time(9, 0))  # Valor Padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Quantidade de vendas", min_value=1, step=1)
    produto = st.selectbox("Selecionar o produto vendido", options=["CRM", "Midias Sociais", "Trafego"])

    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email=email,
                data=data_hora,
                valor=valor,
                quantidade=quantidade,
                produto=produto
            )
            st.write(venda)
        except ValidationError as e:
            st.error(f"Erro: {e}")

if __name__ == "__main__":
    main()