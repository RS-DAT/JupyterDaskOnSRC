Conda 
=====

[Conda](https://docs.conda.io) role for the JupyterDask deployment on SURF Research Cloud. Adapted from the [eWaterCycle lab infrastructure](https://github.com/eWaterCycle/infra).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

```yaml
# Location where conda installer is downloaded to
conda_installer_root: /opt
# Location where conda will be installed
conda_root: /opt/conda
# Name of conda environment to use
conda_environment: jupyterdask
# URL to environment file
environment_url: https://raw.githubusercontent.com/RS-DAT/JupyterDaskOnSRC/environment-from-link/environment.yml
```

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache-2.0

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
