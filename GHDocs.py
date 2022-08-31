import streamlit as st
st.set_page_config(layout="wide")
from PIL import Image

st.title('GitHub Docs by Aarush')
choice = st.selectbox("Pick the following Git Commands!",["Initialize","Status","Log","Stage","Add Origin","Commit","Push Code","Pull Code","Remove Origin","Revert"])
dict = { "Initialize" : ["git init","This should be the first command after accessing the folder through git bash. With this command, git will be initialized in the folder."],
         "Status" : ["git status","With this command, the user can access what files are ready for the committing stage and what files still need to be staged."],
         "Log" : ["git log","With this command, the commit history of the files in the folder are shown."],
         "Stage" : ["git add .","This command puts the file into the staging area after the working phase as the next stage is to commit the file."],
         "Add Origin" : ["git remote add origin <link of repository>","This should add the origin link of the git repository, as GitHub should already have access to your account before doing this stage."],
         "Commit" : ["git commit -m 'commit name'","This command puts the file into the git repository for people to access."],
         "Push Code" : ["git push origin main","This command allows a user to push their code into their git repository."],
         "Pull Code" : ["git pull origin main","This command allows a user to pull some code from a repository with the permission of the original owner of the GitHub repository."],
         "Remove Origin" : ["git remote remove origin","This command allows the user to remove the existing origin."],
         "Revert" : ["git revert <commit ID>","This command allows the user to revert the git repository to the version based on its commit ID."]
         }
st.subheader("Code of the command selected:")
st.code(dict[choice][0])
st.caption(dict[choice][1])

original_title = '<p style="font-family:Serif; color:LightBlue; font-size: 30px;">Visual</p>'
st.markdown(original_title, unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://freellustrustrations.s3.us-east-2.amazonaws.com/free-images/thumbimg_25361957thumbejpg.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

if choice=="Initialize":
    st.image("1.png")
elif choice =="Status":
    st.image("2.png")
elif choice =="Stage":
    st.image("4.png")
elif choice =="Log":
    st.image("3.png")
elif choice=="Add Origin":
    st.image("5.png")
elif choice=="Commit":
    st.image("6.png")
elif choice=="Push Code":
    st.image("7.png")
elif choice=="Remove Origin":
    st.image("8.png")
elif choice=="Pull Code":
    st.image("9.png")
