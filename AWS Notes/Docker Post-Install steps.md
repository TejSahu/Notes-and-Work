Docker has the following main components:
containerd, runc, Notary, Swarmkit


To create the docker group and add your user

Create the docker group

sudo groupadd docker

Add your user to the docker group.

sudo usermod -aG docker $USER

Log out and log back in so that your group membership is re-evaluated.

If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.

On Linux, you can also run the following command to activate the changes to groups:

newgrp docker

Verify that you can run docker commands without sudo.

 docker run hello-world

 docker run -d -v jenkins_home:/home/jenkins/ -p 8080:8080 -p 50000:50000 --restart always jenkins/jenkins:lts-jdk11
 -d to run in background, -v to creata a volume jenkins_home: /home/jenkins(inside container) mapping the host port 8080 to container host similarly 50000:50000 --restart always to restart when stopped finally the image name


 docker run -d -v jenkins_home:/home/jenkins -p 8080:8080 -p 50000:50000 --restart always jenkins/jenkins:lts-jdk11

 docker container stop 7888b6f05d1d;docker container rm 7888b6f05d1d

 docker volume ls
 docker volume rm <containerid>
 docker volume prune #to remove all the local unused volumes

docker ps -a shows all the containers


curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/1.23.3txt)/bin/linux/amd64/kubectl.sha256"

docker exec -it d3042625e7ef bash to run bash in already running container

docker container inspect <containerid>

docker update --restart=no <containerid>


$ sudo docker run -d --name discourse_app local_discourse/app to name a container

$ sudo docker rename discourse_app disc_app to rename

docker system info # to display info about the host

docker history <image id> or tag and label

docker container inspect d3042625e7ef # to inspect the containers

docker image ls --digest # to see the hash output of images

docker image pull <registry>/<image>:<tag> default=latest #syntax to pull images for any registry

docker image pull <registry>/<image> -a # to pull all the images in the repo

docker container inspect d3042625e7ef


docker build github.com/creack/docker-firefox # to build with github url

When pushing to a non-default branch, you need to specify the source ref and the target ref:

git push origin branch1:branch2
Or

git push <remote> <branch with new changes>:<branch you are pushing to>


"Multi-Stage build"

Build the base and app layer then copy the builds and if needed remove them after the build is complete.
eg. https://docs.docker.com/develop/develop-images/multistage-build/

Ctrl+P+Q to exit a docker container without stopping the container
Container are given 10 seconds to stop

CMD default instructions to a container. ENTRYPOINT adds to it as additional arguments.

docker port <containername> - gives the port mapping of the container

docker container rm $(docker container ls -aq) -f # to remove all the containers

docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"
-c means to run a command from a string

LOGGING

/var/lib/docker/containers/<container id>/<container id>-json.log default location

docker logs commands

DOCKER SWARM
Two parts 1)secure cluster 2)Orchestrator
Uses Raft consensus to elect a new leader(manager) if one fails

sudo openssl x509 -in /var/lib/docker/swarm/certificates/swarm/swarm-node.crt --text # to view all the certificates of docker SWARM

docker swarm init --autolock or docker swarm update --autolock=true # will give a crypto key, needs to be kept safe
only affects managers not workers

More docs https://docs.docker.com/engine/reference/commandline/swarm/

docker swarm update --cert-expiry 48h # 2 days

DOCKER NETWORKING

https://docs.docker.com/engine/reference/commandline/network/

<<<<<<< HEAD
VOLUMES

docker volume create myvolname

docker volume rm myvolname 

These volumes will be cretaed under /var/lib/docker/volumes/myvol/_data and are managed by docker

DOCKER SECRETS - secure way to deliver passwords and sensitive data to swarm nodes

can only be used in swarm modes

https://docs.docker.com/engine/reference/commandline/secret/
=======
DOCKER STACKS AND SERVICES: Highest layer of Docker hierarchy

docker stack deploy -c <filename> --is done via compose file -c is for compose file

docker service scale voter(servicename)=20
