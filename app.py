import streamlit as st
from pandas import read_csv

barra = st.sidebar

opcao = barra.selectbox('Menu', ['Inicio', 'Leitor de Arquivos', 'Player de Audio', 'Player de Video'])

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Construção do Menu~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if opcao == 'Inicio':

    st.markdown('''
 
    # Bem-vindo
            
    Algumas aplicações utilizando Streamlit.
    
    ''')

    st.markdown('### Documentação do Framework')

    st.link_button("Streamlit", "https://docs.streamlit.io/")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Construção do Leitor de Arquivos~~~~~~~~~~~~~~~~~~~~~~~

elif opcao == 'Leitor de Arquivos':

    st.markdown('''   
            
    ### Leitor e Visualizador de Arquivos :outbox_tray:

    ''')

    arquivo = st.file_uploader('Suba os arquivos aqui!', type=['jpeg' , 'png' , 'jpg' , 'mp4' , 'mp3' , 'csv' ,  'py'])

    if arquivo:
        print(arquivo.type)
        file_type = arquivo.type.split('/')
        if file_type[0] == 'image':
            st.image(arquivo)
        elif file_type[0] == 'text' and file_type[1] == 'x-python':
            st.code(arquivo.read().decode())
        elif file_type[0] == 'text' and file_type[1] == 'csv':
            df = read_csv(arquivo)
            st.dataframe(df)
    else:
        st.error("Sem arquivos")

    with st.expander('Código Fonte:'):

        st.code('''

            arquivo = st.file_uploader('Suba os arquivos aqui!', type=['jpeg' , 'png' , 'jpg' , 'mp4' , 'mp3' , 'csv' ,  'py'])

            if arquivo:
                print(arquivo.type)
                file_type = arquivo.type.split('/')
                if file_type[0] == 'image':
                    st.image(arquivo)
                elif file_type[0] == 'text' and file_type[1] == 'x-python':
                    st.code(arquivo.read().decode())
                elif file_type[0] == 'text' and file_type[1] == 'csv':
                    df = read_csv(arquivo)
                    st.dataframe(df)
            else:
                st.error("Sem arquivos")
        
        ''', language='python')


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Construção do Player de Audio~~~~~~~~~~~~~~~~~~~~~~~~~~~

elif opcao == 'Player de Audio':


    st.markdown('### Player de Audio :musical_score:')

    st.markdown('Suba um arquivo de audio para poder ouvir')

    arquivo = st.file_uploader('', type=['mp3', 'mpeg'])

    st.audio(arquivo)

    with st.expander('Código Fonte'):

        st.code('''

            st.markdown('### Player de Audio :musical_score:')

            st.markdown('Suba um arquivo de audio para poder ouvir')

            arquivo = st.file_uploader('', type=['mp3', 'mpeg'])

            st.audio(arquivo)

        ''', language='python')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~Construção do Player de Video~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

elif opcao == 'Player de Video':

    st.markdown('### Player de VIdeo :clapper:')

    st.markdown('Suba um arquivo para assistir')


    arquivo = st.file_uploader('', type= ['mp4' , 'mkv', 'webm'])

    st.video(arquivo)

    with st.expander('Código Fonte'):

        st.code('''

        st.markdown('### Player de VIdeo :clapper:')

        st.markdown('Suba um arquivo para assistir')

        arquivo = st.file_uploader('', type= ['mp4' , 'mkv', 'webm'])

        st.video(arquivo)
                
        ''', language='python')
