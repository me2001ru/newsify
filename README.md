# newsify


For overall GitHub stuff:
- make sure you have ssh-key and applied to your host for GitHub
- make sure you have an access token

For project related:

(How to run Jupyter in VS Code: https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

0. Install Selenium
1. Clone repository
2. Create a branch (!! Do not work directly on the main branch !!)
3. Create a pull request (when you want to merge code to main branch)
4. Address review comments
5. Merge your pull request
6. Delete branch (optional)

To be able to run application in container:
- install docker on your local machine. Follow this link: https://docs.docker.com/get-docker/
- enter 'docker build -t <ENTER NAME OF YOUR IMAGE> .'
- enter 'docker run -p 3000:3000 <NAME OF YOUR IMAGE>' (this binds på port 3000 and will occupy your terminal tab)

```
HANDY DOCKER COMMANDS

docker images
docker rmi -f [IMAGE ID] docker image prune (removes images not in use)

docker ps alt. docker ps -a (latter shows containers exited)
docker rm -f [CONTAINER ID] (to remove container)
```




