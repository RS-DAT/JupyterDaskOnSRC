# JupyterDask on SRC

Deploy Dask on a cluster of virtual machines (VMs) on SURF Research Cloud. Access the cluster via JupyterHub, deployed on the head node.

TODO: current limitations:
  * the SURF HCP cloud cluster subscription is only available in the development Research Cloud environment;

## Register Application

A member of the CO [with "developer" privileges](https://servicedesk.surfsara.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer) can register the current application on SURF Research Cloud following [these instructions](https://servicedesk.surfsara.nl/wiki/display/WIKI/Create+your+own+applications).

The following steps create a catalog item with two paraters:
* the number of worker nodes in the cluster of VMs;
* (optional) the URL to a conda environment file - it should be based on the [`environmnent.yml` file provided in this repository](./environment.yml).

When setting up the **plugin**:
* Set "Script type" to "Ansible PlayBook";
* In the "Script source" tab:
  * Set "Source type" as "git";
  * Paste the link to this repository as "Repository";
  * Set "Path" as `research-cloud-plugin.yml`;
  * Set "Tag" to target "branch", if needed;
* Add two "Plugin parameters":
  * Set "key" as `environment_url`, "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable";
  * Set "key" as `worker_ip_addresses`, "Source type" as "Resource" and "Data type" as "string".

When setting up the **application**:
* Set "Access format" as `https://==REVERSE_PROXY==`;
* Select the following application plugins (in this order): "RSC-OS", "RSC-CO", "RSC-Nginx", "RSC-External plugin", and the plugin just created;
* Add the following "Application parameters":
  * Choose "environment_url" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable";
  * Choose "co_passwordless_sudo" from the menu, then set "Source type" as "Fixed", "Default value" as `true`, "Data type" as "string", and tick "Overwritable";
  * Choose "num_nodes" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable" and "Required".

When setting up the **application offer**:
* Set "Application" as the application just created;
* Set "Subscription" as "SURF HPC Cloud cluster";
* Add the following "Application offer parameters":
  * Choose "environment_url" from the menu, then set "Source type" as "Fixed", "Default value" as `default`, "Data type" as "string", and tick "Overwritable";
  * Choose "num_nodes" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable" and "Required".


## Credits

Most of the playbooks in this repository have been taken, inspired or adapted from the ones in the [eWaterCycle infrastructure](https://github.com/eWaterCycle/infra) and the [Emma](https://github.com/nlesc-sherlock/emma) projects. 
