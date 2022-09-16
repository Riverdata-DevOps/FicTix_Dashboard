# Bibliotecas para a WEB API
from apps import *

import streamlit as st
import streamlit.components.v1 as components

Navbar = '''
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <style>
        /* The whole sidebar */
        .css-1lcbmhc.e1fqkh3o0{
            margin-top: 3.8rem;
        }  
        /* The display arrow */
        .css-sg054d.e1fqkh3o3 {
            margin-top: 5rem;
        }
        body {
            font-family: 'Trebuchet MS', sans-serif;
            font-weight: bold;
            margin: 0;
            background-color: whitesmoke;
        } 
            
        /* #31333f */
        ul {
            list-style-type: none;
            font-size: large;
            margin: 0;
            padding: 0;
            overflow: hidden;
            position: relative;
            width: 100%;
            height: 2.5rem;
            z-index: 999999;
        }
        li {
            height: 100%;
            float: left;
            list-style-type: none;
        }
        li a.nav {
            display: block;
            color: white;
            text-align: center;
            height: 100%;
            text-decoration: none;
            padding-top: 10px;
            font-family: 'Trebuchet MS', sans-serif;
            font-size: large;
            font-weight: bold;
            border: none;
            display: inline-block;
            pointer-events: auto; 
    
        }
        
        li a.nav2 {
            display: block;
            color: white;
            text-align: center;
            height: 100%;
            text-decoration: none;
            padding-top: 10px;
            font-family: 'Trebuchet MS', sans-serif;
            font-size: large;
            font-weight: bold;
            border: none;
            display: inline-block;
            pointer-events: auto; 
    
        }
        
        li a {
            display: block;
            color: white;
            text-align: center;
            height: 100%;
            text-decoration: none;
            padding-top: 10px;
            font-family: 'Trebuchet MS', sans-serif;
            border: none;
            display: inline-block;
            pointer-events: auto; 
    
        }
            
        li a:hover:not(.active) {
            background-color: #111;
        }
            
        .active {
            background-color: #162746;
        }
            
        .logo-image {
            width: 86px;
            height: 56px;
            overflow: hidden;
            padding-top:5px;
            padding-bottom:5px;
            padding-left:5px
            
                      
        }
            
        .dropbtn {
            background-color: #162746;
            color: white;
            margin-left:2rem;
        font-size: large;
            font-family: 'Trebuchet MS', sans-serif;
            font-weight: bold;
            border: none;
            cursor: pointer;
            height: 3.5rem;
            
        }
            
        .dropdown {
            position: fixed;
            right: 0;
            z-index: 9999999999999;
            padding-right: 2.5rem;
            padding-top: 1rem;
        }
            
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
              
              
            z-index: 9999999;
        }
            
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }
            
        .dropdown-content a:hover {background-color: #f1f1f1}
            
        .dropdown:hover .dropdown-content {
            display: block;
        }
            
        .dropdown:hover .dropbtn {
            background-color: #162746;
        }
        .btn-group li a.nav {
            background-color: #162746; /*#4CAF50 Green */
            border: 1.5px solid green;
            border-top:0;
            border-bottom:0;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: large;
            cursor: pointer;
            float: left;
            padding: 15px 16px;
            transition-duration: 0.4s;
            
            
        }
        
        .btn-group li a.nav2 {
            background-color: #162746; /*#4CAF50 Green */
            border: 1.5px solid green;
            border-top:1.5px solid green;
            border-bottom:1.5px solid green;
            color: white;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: large;
            cursor: pointer;
            float: left;
            padding: 15px 16px;
            transition-duration: 0.4s;
            width:305px;
        }
            
        .btn-group li a.nav:not(:last-child) {
            border-right: none; /* Prevent double borders */
        }
        .btn-group li a.nav2:not(:last-child) {
            border-right: none; /* Prevent double borders */
        }
            
        .btn-group li a.nav:hover {
            background-color: #777777;
        }
        .btn-group li a.nav2:hover {
            background-color: #777777;
        }
        
        /* Fix Navbar padding and margin */
        .css-nlntq9 li {
            margin: 0em 0px 0em 0em;
            padding: 0px 0px 0px 0em;
            font-size: 1rem;
        }
        .navbar {
            padding:0px 0px 0px 0px;
                
        }
        /* Fiz Logo Image on Sidebar padding */
        .css-zbg2rx {
            padding: 3rem 1rem;
        }
        
        .element-container css-1my9fp7 e1tzin5v1 {
            display: None;
        }
        .css-1qcggol{
            display:none
        }
        .css-vl8c1e {
            display: none;
        }
        .css-18e3th9 {
            padding-top:2rem   
        }
        
    </style> 
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #162746;">
        <a class="navbar-brand" href="/">
            <div style="margin:0px 0px 0px 10px;" class="logo-image">
                <img src="https://riverdata.com.br/wp-content/uploads/2022/07/cropped-riverdata_logo_bco_21-1536x831.png" width="100%" height="100%">
            </div>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <div class="dropdown">
                <button class="dropbtn">RiverSensor</button>
                
            </div>
            <ul class="navbar-nav" style="margin-left:15px;padding-top:0;padding-bottm:0; height:3.8rem;;">
                <div class="btn-group">
                    <li>
                        <a.nav  href="#?p=Home" >Home</a>
                    </li>
                                        
                </div>
            </ul>
        </div>
    </nav>  
    '''

app = MultiApp()

# configurar a visualização
# %matplotlib inline   #configurações de notebook#
# %config InlineBackend.figure_format = 'svg' #configurações de notebook#

# configurando página
logo_image = Image.open('Riverlogo.jpg').convert('RGB')
background = Image.open('RiverPaper.jpeg').convert('RGB')
PAGE_CONFIG = {'page_title': 'RiverSensor', 'page_icon': logo_image}
st.set_page_config(**PAGE_CONFIG, layout='wide')



def main():
    """RiverSensor"""
    import streamlit.components.v1 as components
    #st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)
    Navlink = st.markdown(Navbar, unsafe_allow_html=True)

    if 'auth' not in st.session_state:
        st.session_state.auth = None
    if 'page' not in st.session_state:
        st.session_state.page = None

    st.session_state.page = 'Home'

    image = st.sidebar.empty()
    sidebar_image = logo_image
    image.image(sidebar_image)

    menu = ["Login", "Criar Novo Usuário"]
    login_ui = st.sidebar.empty()
    choice = login_ui.selectbox("Menu", menu)

    SideBar = st.sidebar.container()


    if 'user' not in st.session_state:
        st.session_state.user = None
    if 'passw' not in st.session_state:
        st.session_state.passw = ''
    if 'auth' not in st.session_state:
        st.session_state.auth = None

    st.image(background, use_column_width=True)

    c1,c2,c3 = st.columns(3)
    user = c2.empty()
    passw = c2.empty()
    login = c2.empty()

    st.session_state.user = user.text_input("Nome de Usuário")

    password = passw.text_input("Senha", type='password', value = st.session_state.passw)

    booleanLogin = login.button("Entrar")
    username = st.session_state.user
    st.session_state.passw = password

    #if booleanLogin:
        #create_usertable()
        #hashed_pswd = make_hashes(password)
        #result = login_user(username, check_hashes(password, hashed_pswd))
    if password or booleanLogin:

        create_usertable()
        hashed_pswd = make_hashes(st.session_state.passw)

        result = login_user(st.session_state.user, check_hashes(st.session_state.passw, hashed_pswd))
        st.session_state.auth = result

        if st.session_state.auth:
            user.empty()
            passw.empty()
            login.empty()
            login_ui.empty()

            with st.sidebar:
                st.markdown('''
                <html>
                   <div class="btn-group" style="margin-top: .7rem "> 
                        <li>
                            <a.nav2 href="#?p=RiverSensor" onclick="">RiverSensor</a>
                        </li>
                   </div>
                </html>
                ''', unsafe_allow_html=True)

            # Indicador de uma requisição para rodar um dos multi apps
            # Se um botão da Navbar for pressionado selecionamos o aplicativo à ser utilizado pelo sistema, desligando os demais aplicativos

            app.add_app('Home', Home())
            app.run()

        else :
            #   Se os dados de login forem incoerentes, indica que a senha está errada
            st.sidebar.warning("Há algum equívoco em seu nome de usuário ou senha inserida no cadastro, por favor, verifique e tente novamente.")


if __name__ == '__main__':
    main()