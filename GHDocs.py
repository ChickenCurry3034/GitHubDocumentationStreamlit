import streamlit as st

st.title('GitHub Docs by Aarush')
choice = st.selectbox("Pick the following Git Commands!",["Initialize","Status","Log","Stage","Add Origin","Commit","Pull Code","Remove Origin","Reset"])
dict = { "Initialize" : ["git init","This should be the first command after accessing the folder through git bash. With this command, git will be initialized in the folder."],
         "Status" : ["git status","With this command, the user can access what files are ready for the committing stage and what files still need to be staged."],
         "Log" : ["git log","With this command, the commit history of the files in the folder are shown."],
         "Stage" : ["git add .","This command puts the file into the staging area after the working phase as the next stage is to commit the file."],
         "Add Origin" : ["git remote add origin <link of repository>","This should add the origin link of the git repository, as GitHub should already have access to your account before doing this stage."],
         "Commit" : ["git commit -m 'commit name'","This command puts the file into the git repository for people to access."],
         "Pull Code" : ["git pull origin main","This command allows a user to pull some code from a repository with the permission of the original owner of the GitHub repository."],
         "Remove Origin" : ["git remote remove origin","This command allows the user to remove the existing origin."],
         "Reset" : ["git reset <file>","This command allows the user to reset a certain file to its previous version."]
         }
st.subheader("Code of the command selected:")
st.code(dict[choice][0])
st.caption(dict[choice][1])
