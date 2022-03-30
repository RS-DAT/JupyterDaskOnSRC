# JupyterDask on SRC

Deploy a Dask cluster and JupyterHub on SURF Research Cloud.

## Register Application

A member of the CO [with "developer" privileges](https://servicedesk.surfsara.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer) can register the current application on SURF Research Cloud following [these instructions](https://servicedesk.surfsara.nl/wiki/display/WIKI/Create+your+own+applications).

When setting up the **plugin**:
* Set "Script type" to "Ansible PlayBook";
* In the "Script source" tab:
  * Set "Source type" as "git";
  * Paste the link to this repository as "Repository";
  * Set "Path" as `research-cloud-plugin.yml`
* Add two "Plugin parameters":
  * Set "key" as `environment_url`, "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable";
  * Set "key" as `worker_ip_addresses`, "Source type" as "Resource" and "Data type" as "string".

When setting up the **application**:
* Set "Access format" as `https://==REVERSE_PROXY==`;
* Select the following application plugins (in this order): "RSC-OS", "RSC-CO", "RSC-External plugin", and the plugin just created; (TODO: add NGINX plugin when fixed)
* Add the following "Application parameters":
  * Choose "environment_url" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable";
  * Choose "co_passwordless_sudo" from the menu, then set "Source type" as "Fixed", "Default value" as `true`, "Data type" as "string", and tick "Overwritable";
  * Choose "num_nodes" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable" and "Required";

When setting up the **application offer**:
* Set "Application" as the application just created;
* Set "Subscription" as "SURF HPC Cloud cluster";
* Add the following "Application offer parameters":
  * Choose "environment_url" from the menu, then set "Source type" as "Fixed", "Default value" as `https://raw.githubusercontent.com/RS-DAT/JupyterDaskOnSRC/main/environment.yml`, "Data type" as "string", and tick "Overwritable";
  * Choose "num_nodes" from the menu, then set "Source type" as "Fixed", "Data type" as "string", and tick "Overwritable" and "Required";
