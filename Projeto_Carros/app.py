import streamlit as st
### COLOCAS UM TITULO
# st.title("Carros de Aluguel")

# ### ESCREVE
# st.write("Testando... Esquerda e Direita ")

# ### CRIE UMA BARRA LATERAL
# st.sidebar.title("Barra Lateral")

# ### CRIANDO LISTA 
# # nomes ficticios, qualquer é conhecidencia

# nomes = ["Jeep", "BMW", "Civic", "Yaris, "Fox"]
         
# ## CRIA A CAIXINHA NA BARRA LATERAL 
# st.soidebar.selectbox("Escolha um carro para alugar :", nomes)

# # COLOCA O VIDEO NA PAGINA DO SITE
# st.video("")


st.sidebar.title("Aluguel de Carros")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o carro ideal para você!")

carros = ["Jeep", "BMW", "Civic", "Yaris", "Fox"]
opcao = st.sidebar.selectbox("Selecione o modelo do carro;", carros)

### PRINCIPAL 

st.title('fast - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'##Você alugou o modelo: {opcao}')
st.markdown('---')

#Define a Diária 


dias = st.text_input(f"POr quantos dias você alugou o {opcao} ?")
km = st.number_input(f"Quantos km você rodou?")

if opcao == 'Jeep':
    diaria = 450

elif opcao == 'BMW':
    diaria = 500

elif opcao == 'Civic':
    diaria = 450

elif opcao == 'Yaris':
    diaria = 400

elif opcao == 'Fox':
    diaria = 250

### CALCULAR 

if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_kms = km * 0.15
    aluguel_total = total_dias + total_kms

    st.warning(f'Voce alugou o {opcao} por {dias} dias e rodou {km} km. O valor a pagar é R% {aluguel_total:.2f}')
