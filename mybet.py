import streamlit as st
import py-parsehub as p
# Get the API key from the config file
api_key = st.get_secret("PARSEHUB_API_KEY")

# Create a client object using the API key
client = p.Client(api_key=api_key)

# Display a form for creating a new project
st.header("Create a new project")
project_name = st.text_input("Enter project name:")
if st.button("Submit"):
    # Create a new project with the given name
    project = client.create_project(name=project_name)
    st.success("Created project: %s" % project.name)

# Display a list of existing projects
st.header("Your projects")
projects = client.get_projects()
if projects:
    for project in projects:
        st.write(project.name)
        # Add buttons for editing and deleting the project
        if st.button("Edit"):
            # Open a form for editing the project name
            project_name = st.text_input("Enter new project name:", value=project.name)
            if st.button("Save"):
                # Update the project name
                project.name = project_name
                project.save()
                st.success("Updated project: %s" % project.name)
        if st.button("Delete"):
            # Delete the project
            project.delete()
            st.success("Deleted project: %s" % project.name)
else:
    st.warning("No projects found.")
