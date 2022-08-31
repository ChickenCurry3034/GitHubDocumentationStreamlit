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
         "Push Code" : ["git push origin master","This command allows a user to push their code into their git repository."],
         "Pull Code" : ["git pull origin master","This command allows a user to pull some code from a repository with the permission of the original owner of the GitHub repository."],
         "Remove Origin" : ["git remote remove origin","This command allows the user to remove the existing origin."],
         "Revert" : ["git revert <commit ID>","This command allows the user to revert the git repository to the version based on its commit ID."]
         }
st.subheader("Code of the command selected:")
st.code(dict[choice][0])
st.caption(dict[choice][1])

original_title = '<p style="font-family:Sans-Serif; color:LightBlue; font-size: 30px;">Visual</p>'
st.markdown(original_title, unsafe_allow_html=True)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.pinimg.com/originals/22/e1/85/22e185ea07628c79a4f586d99c8fd454.png");
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
    st.subheader("The software needed to access this information is called git bash. From there, you right click on the folder you want to insert into GitHub, (if you're on Windows 11 or above) click on more options, and select the option saying Git Bash Here which will lead to this window. It is shown that git has been initialized in the folder through this picture. This is a necessary step in order to insert the code into GitHub because without this, none of the functions after this will work. There are three stages of inserting code into GitHub: Modifying, Staging, and Committing. Modifying the code is simply editing the code on your own local computer, and the other two stages will be explained in other screens.")
elif choice =="Status":
    st.image("2.png")
    st.subheader("When the git status command is called, it shows the files that are committed, staged, and neither of these cases. In this sitation, the 5 files have been edited/added without any of them being staged.")
elif choice =="Stage":
    st.image("4.png")
    st.subheader("Despite not showing any response, the user's request to put the files into the staging area have been resolved. The staging area is somewhat of a stage that lets the code prepare for their addition to the remote repository.")
elif choice =="Log":
    st.image("3.png")
    st.subheader("The user asks for the commit log of the git repository, and the given information is shown. In the yellow, the group of random numbers and letters shown form the commit ID. The author of the commit is also shown, as git allows a group to figure out who made certain edits to a code, the date of the edit is also shown along with the commit name. The commit ID can be used for reverting the code back to original versions to prevent any issues with the current code.")
elif choice=="Add Origin":
    st.image("5.png")
    st.subheader("Once again, there is no response, but the request has been granted as now, the origin of the git repository is now set to the link of that repository, This link allows the code from the user's computer to be uploaded into GitHub, or online, for more people to see. Without this command or link, where would the code be uploaded?")
elif choice=="Commit":
    st.image("6.png")
    st.subheader("With this command shown in the image above, the code is official, and all you have left is to push the code into GitHub! This stage is called the commit stage, as it means someone has completed a specific edit or change in the code.")
elif choice=="Push Code":
    st.image("7.png")
    st.subheader("Shown in the image above, the code has been pushed to the repository stated in the add origin stage. From there, you need to reload your GitHub screen on your browser. You will see all of your code in this repository, and you can send the repository to others as one of the benefits of GitHub is collaboration with others when programming.")
elif choice=="Pull Code":
    st.image("9.png")
    st.subheader('''The image above shows a user pulling the code from another's GitHub repository for them to edit on their end. This will allow this user to download the code from the other user, and using a pull request, they can request their changes to be inserted in the original copy. Before this step, however, the origin must be set to the git repository of the other user that the original user wants to copy using the add origin command.
Image Source: https://www.decodingdevops.com/git-pull-command-example/''')
elif choice=="Remove Origin":
    st.image("8.png")
    st.subheader("This function doesn't send a visual message to you, but it does the action of removing the existing origin you set earlier in the add origin phase. This may solve some issues relating to someone not seeing their code on GitHub, as their origin isn't accurate, so removing the origin and adding a new one would fix this issue.")
elif choice=="Revert":
    st.image("10.png")
    st.subheader("By using the git revert function, the function will be reverted back to the commit corresponding with the commit ID stated. This prevents issues with the current code by simply bringing it back to a working version. In this example, the code couldn't be reverted because there was a conflict in commiting the new changes. A conflict in these sitations are multiple changes (additions or deletions) take place within the same line. This is something programmers want to avoid when programming as it could cause major pauses in the process of uploading code to GitHub.")
