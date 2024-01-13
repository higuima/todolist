import streamlit as st
from utils.getDatabase import DatabaseConnection
from utils.getUserInfo import UsersConnection

database = DatabaseConnection()
users = UsersConnection()

class Auth():    
    def form_selection(self):
        st.title("Log in or create an account")
        login, signup = st.columns(2)
        with login:
            login_butt = st.button("Log In", use_container_width=True)
            if login_butt:
                st.session_state.form = 'login_form'
                st.rerun()
        with signup:
            sign_up = st.button("Sign Up", use_container_width=True)
            if sign_up:
                st.session_state.form = 'signup_form'
                st.rerun()

    def login(self, email, password):
        client = database.init_connection()
        db = client.todolistdb
        user_info = db.users.find_one({'email':email, 'password': password})
        if user_info:
            st.session_state['user'] = True
            st.session_state['user_id'] = user_info['_id']
            st.session_state['username'] = user_info['name']
            del user_info['password']
            st.rerun()
        else:
            st.session_state['user'] = False
            st.error("😕 User not known or password incorrect")
        return st.session_state['user']

    def logout(self):
        logout = st.sidebar.button(label='Log Out')
        if logout:
            st.session_state.username = ''
            st.session_state.user = ''
            st.session_state.form = ''
            st.rerun()

    def login_form(self):
        with st.form(key='login_user', clear_on_submit=True):
            st.title("Hey there! Welcome back!")
            email = st.text_input("Email", key="login_email")
            password = st.text_input("Password", type="password", key="login_password")
            submit_user_login = st.form_submit_button("Log In",use_container_width=True)
            if submit_user_login:
                user_id = self.login(email, password)

    def signup_form(self):
        with st.form(key='create_user', clear_on_submit=True):
            st.title("Hey there! Welcome!")
            name = st.text_input("Name", key="create_name")
            email = st.text_input("Email", key="create_email")
            company = st.text_input("company", key="create_company")
            password = st.text_input("Password", type="password", key="create_password")
            submit_user = st.form_submit_button("Sign Up",use_container_width=True)
            if submit_user:
                if ''  in [name, email, company, password]:
                    st.error("All fields are required, please fill out the form!")
                else:
                    test_email = users.user_email_exists(email)
                    if test_email == False:
                        user = {
                            "name": name,
                            "email": email,
                            "company": company,
                            "password": password,
                        }
                        user_id = users.insert_user(user)
                        st.success('You have successfully registered!')
                        st.success(f"You are logged in as {name.title()}")
                        user_id = self.login(email, password)

