import streamlit as st

st.title("About this project")

st.write()

st.markdown("""
The main goal of this project was to learn how to create and manage a mongodb database and its collections, while also practicing creating secure authentication login process.

I chose streamlit as a framework because of its versatility and easy to create interface components/widgets.

In this article I wanted to dive into the concepts of the project, it’s not my intention to create a “step-by-step” tutorial for it. But you are more then welcome to visit this project’s repo and check out the code I wrote: https://github.com/higuima/todolist

### How I divided this project

I decided to divide the project into two smaller projects and it was very helpfull to understand what I needed to tackle first.

Since I already used streamlit in other projects I was very confortable creating the kanban dashboard first and mix it with the challange I proposed to myself: learn how to use mongodb.

To simplify, the smaller projects were basically:

**Kanban dashboard**

- use python and streamlit to create and vizualise the dashboard
- use mongodb to store all the data from the tasks

**Users login and signup interface**

- using mongodb to store all data from client
- clients can only see their tasks
- create a secure authentication process

### **Now, what exaclty is a kanban dashboard?**

Is an organization method of visualizing all your tasks based on the state of completion they have. In this case, I created a status for each task and gave them a flow of completion from “to do” to “doing” and when the task is finalized, “done”.
""")
st.image('./app/assets/kanban.png')

st.markdown("""
> If you want to learn more about kanban, [here’s a cool guide](https://www.atlassian.com/br/agile/kanban)
> 

So, to create the ilusion of flow I built three streamlit columns and displayed the status of the task. Each column displays cards with information about the tasks in a way that you can interact with:
""")

st.image('./app/assets/kanban_dash.png')


st.markdown("""
This way, each task gets a card and you can move them between columns by changing the status of the task.

### What are the databases I created?

To store the information necessary for each task, I created a non-relational database using JSON structure. This way I can easily upload a new task to mongodb and retrive information in a organized way.

> Also, I really wanted to experiment with a no-SQL structure type of database, so yeah, I could’ve used tables, but I didn’t want to.

""")

st.image('./app/assets/databases.png')

st.markdown("""
For the Users database, I needed information for the login/signup system. It was also necessary for the experience that each user could only access its own tasks. To acomplish this, I used the user_id while filtering the tasks that should render on the page. This user_id is created automatically by Mongodb and it was refreshing being allowed to just integrate the collections with an easy query.

### Finishing touches

There were a lot of fundamental details that I found interesting while building this project. Like the thought of having to manage different users and display different and unique information for each of them.

I really like using streamlit for fast building projects that need visualization but I never used it to create a real interface for the user before. I think the already built in widgets create an amazing UI and it’s very practical. If you take one thing from this article, let it be: **use streamlit!**

If you made it this far, thank you. I hope you enjoyed reading it.


""")

st.write("Here is a link of an article I wrote about this project: https://medium.com/@higuima13/to-do-list-a-project-using-python-mongodb-and-streamlit-4d6db1a04d45")
