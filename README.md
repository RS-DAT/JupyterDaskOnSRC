# JupyterDask on SURF Research Cloud

Deploy Dask on a cluster of virtual machines (VMs) on SURF Research Cloud (SRC). Access the cluster via JupyterHub, deployed on the head node.

## Create the SRC Catalog Item

A member of the CO [with "developer" privileges](https://servicedesk.surfsara.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer) can register the current application as a Catalog Item on SURF Research Cloud following [these instructions](https://servicedesk.surf.nl/wiki/display/WIKI/Create+your+own+catalog+items).

The following steps create a catalog item with the following three paraters:
* the number of worker nodes in the cluster of VMs;
* (optional) the URL to a conda environment file, employed to configure both the head node and the workers with the same Python environment;
* (optional) a macaroon to authenticate access to [the SURF dCache starage](http://doc.grid.surfsara.nl/en/latest/Pages/Advanced/storage_clients/webdav.html#sharing-data-with-macaroons) via [dCacheFS](https://github.com/NLeSC-GO-common-infrastructure/dcachefs).

Note that setting up the "Catalog Item" requires first to create a "Component" based on the Ansible playbook that is part of this repository.

### Create the Component

Follow the ["Create a
component"](https://servicedesk.surf.nl/wiki/display/WIKI/Create+a+component)
instructions, using the following parameters:

* Set "Component script type" to "Ansible Playbook".
* In the "Script source" tab:
  * Set "Repository URL" as `https://github.com/RS-DAT/JupyterDaskOnSRC.git`;
  * Set "Path" as `research-cloud-plugin.yml`;
  * *(if neededed)* Set "Tag" as target "branch" or "tag";
  * Set "Script availability" as "Script is publicly available through Git". 
* Add three "Component parameters":
  * Set "Parameter key" as `environment_url`, "Source type" as "Fixed", and tick "Overwritable";
  * Set "key" as `dcache_token`, "Source type" as "Fixed", and tick "Overwritable";
  * Set "key" as `worker_ip_addresses`, "Source type" as "Resource".

### Create the Catalog Item

Follow the ["Create a catalog item"](https://servicedesk.surf.nl/wiki/display/WIKI/Create+a+catalog+item) instructions, using the following parameters:

* In the "Available components" tab, choose the following components (in this order):
  * SRC-OS
  * SRC-CO
  * SRC-Ngnix
  * SRC-External plugin
  * the component created in the previous step
* In the "Cloud providers" tab, add "SURF HPC Cloud cluster" with "Ubuntu 20.04" as OS and tick all available sizes.
* In the "Ovewritable parameters" tab:
  * For `co_passwordless_sudo`, set "Actions" to "Overwrite" and set "New parameter value" to `true`.
  * For `num_nodes`, set "Actions" to "Make interactive", set "Label or question for workspace creator" to "Number of worker nodes", and set "Default parameter value" to `0`.
  * For `dcache_token`, set "Actions" to "Make interactive", set "Label or question for workspace creator" to "dCache token: provide the macaroon to authenticate on the dCache storage", and set "Default parameter value" to `null`.
  * For `environment_url`, set "Actions" to "Make interactive", set "Label or question for workspace creator" to "Conda environment file: provide the URL to a custom environment.yml (blank for default environment)", and set "Default parameter value" to `default`.

## Credits

Most of the playbooks in this repository have been taken, inspired or adapted from the ones in the [eWaterCycle infrastructure](https://github.com/eWaterCycle/infra) and the [Emma](https://github.com/nlesc-sherlock/emma) projects. 
