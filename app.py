import streamlit as st
from datetime import datetime, time

def main():

    st.title("Nosso Sistema de Input")
    email = st.text_input("Email")
    data = st.date_input("Data", datetime.now())
    hora = st.time_input("Hora", value=time(9, 0)) # Valor Padrão: 09:00
    valor = st.number_input("Valor da venda", min_value=0.0, format="%.2f")
    quantidade = st.number_input("Qantidade de vendas", min_value=1, step=1)
    produto = st.selectbox("Selecionar o produto vendido",options=["CRM","Midias Sociais","Trafego"])

    if st.button("Salvar"):
       data_hora = datetime.combine(data,hora)
       st.write("**Dados da Venda**")
       st.write(f"Email do Vendedor: {email}")
       st.write(f"Data e Hora da compra: {data_hora}")
       st.write(f"Valor da Venda: R$ {valor:.2f}")
       st.write(f"Quantidader de produtos: {quantidade}")
       st.write(f"Produto:{produto}")
       
       
                       
if __name__=="__main__":
    main()