Dask
====

[Dask](https://dask.org) role for the JupyterDask deployment on SURF Research Cloud. Adapted from [Emma](https://github.com/nlesc-sherlock/emma).

Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

```yaml
# Location where conda will be installed
conda_root: /opt/conda
# Name of conda environment to use
conda_environment: jupyterdask
# Path to conda environments bin directory
conda_environment_bin: '{{ conda_root }}/envs/{{ conda_environment }}/bin'
# Port on which dask scheduler is running
dask_scheduler_port: 3389
# Port on which dask dashboard is running
dask_dashboard_port: 8787
# Port on which dask workers are running
dask_worker_port: 5986
# Workers' scratch directory
dask_worker_dir: "/scratch"
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
