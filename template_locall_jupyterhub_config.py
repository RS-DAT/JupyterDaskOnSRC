
# See https://jupyterhub-dockerspawner.readthedocs.io/en/latest/index.html
# docker should be installed on the host machine
# in the .docker/config.json file, se the "credsStore": to "" (empty string)

import sys

c = get_config()

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

c.JupyterHub.admin_access = True
c.Authenticator.admin_users = {'sarah'} # replace with your username
c.JupyterHub.authenticator_class = 'jupyterhub.auth.PAMAuthenticator'
c.Authenticator.allowed_users = {'sarah'} # replace with your username

c.JupyterHub.bind_url = 'https://127.0.0.1:8000'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# replace with your desired image see https://github.com/jupyter/docker-stacks/tree/main/images
# and see https://quay.io/organization/pangeo
c.DockerSpawner.image = 'quay.io/pangeo/base-notebook:latest'

# set c.Spawner.cmd to launch singleuser server with jupyterlab
# this is needed if pangeo image is used
c.Spawner.cmd = ['jupyter-labhub']

# Explicitly set notebook directory because we'll be mounting a volume to it.
# Most `jupyter/docker-stacks` *-notebook images run the Notebook server as
# user `jovyan`, and set the notebook directory to `/home/jovyan/work`.
# We follow the same convention
c.DockerSpawner.notebook_dir = '/home/jovyan/work'

# Mount the real user's Docker volume on the host to the notebook user's
# notebook directory in the container
notebook_mount_dir = '/home/sarah/work'  # replace with your desired mount point
c.DockerSpawner.volumes = {notebook_mount_dir: {"bind": c.DockerSpawner.notebook_dir , "mode": "rw"}}

c.Spawner.default_url = '/lab'
# c.Spawner.notebook_dir = '~'
c.JupyterHub.port = 8000
# c.DockerSpawner.start_timeout = 120
# c.Spawner.http_timeout = 60

c.DockerSpawner.remove_containers = True
c.Authenticator.delete_invalid_users = True

c.JupyterHub.cleanup_servers = True
c.JupyterHub.cleanup_proxy = True

# Remove containers once they are stopped
c.DockerSpawner.remove = True

# For debugging arguments passed to spawned containers
c.DockerSpawner.debug = True

# Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
c.Application.log_level = 'DEBUG'

# TODO check how to remove cached containers