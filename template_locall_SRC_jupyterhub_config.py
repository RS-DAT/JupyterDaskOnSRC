
# This is a template for running jupyetrhub with DockerSpawner "locally" on SRC
# See https://jupyterhub-dockerspawner.readthedocs.io/en/latest/index.html
# 1. choose a catalog item where Docker is installed.
# 2. install packages with sudo, see https://github.com/jupyterhub/jupyterhub
    # Sudo is needed for pam with SRC time-based passwork to work
    # Test it with : sudo python3 -c "import pamela, getpass; print(pamela.authenticate('$USER', getpass.getpass()))"
    # after entering password, it prints "None", otherwise Error.
# 3. The docker instances need access to the Hub, install "jupyter_client" too
# 4. pass ports: ssh -L 8000:localhost:8000 <URL provided by the item>
# 5. run sudo jupyterhub -f template_locall_SRC_jupyterhub_config.py

import sys

c = get_config()

# The docker instances need access to the Hub, so the default loopback port doesn't work:
from jupyter_client.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]

# administrative access to the JupyterHub web interface.
c.JupyterHub.admin_access = True

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
# On SRC, the scratch directory should be mounted and not /home directory
# default mode is  "mode": "rw"
notebook_mount_dir = '/home/falidoost/scratch'  # replace with your username
c.DockerSpawner.volumes = {notebook_mount_dir: {"bind": c.DockerSpawner.notebook_dir}}

c.Spawner.default_url = '/lab?reset'
c.JupyterHub.port = 8000

# TODO how to pause the container when the user is not active?
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
