# JupyterDask on SURF Research Cloud

This is an instruction about how to set up a Jupyter interface including
[Dask](https://www.dask.org/) on [SURF Research Cloud
(SRC)](https://www.surf.nl/en/surf-research-cloud-collaboration-portal-for-research).

## For the user

### Access the existing workspace

To access an existing workspace, first ask administrators to invite you to a collaborative organization (CO). After
receiving the invitation link, you will be directed to the [log in
page](https://portal.live.surfresearchcloud.nl/). Follow the instructions in
[Workspace Access with TOTP](https://servicedesk.surf.nl/wiki/display/WIKI/Log+in+to+your+workspace#Logintoyourworkspace-WorkspaceAccesswithTOTP)
to setup a time-based one time password and 
to access your workspace.

### Create a new workspace

See the instructions ["Create the workspace"](#3-create-the-workspace) below to create a
new workspace.

## For the administrator

To get access to SRC, you need to apply for the compute services via the
[request
portal](https://www.surf.nl/en/research-it/apply-for-access-to-compute-services).
When your application is approved, SURF will send you an invitation with the
login to SRC. To get familiar with the SRC, have a look at the [SRC First
Steps](https://servicedesk.surf.nl/wiki/display/WIKI/First+Steps).

A member of the CO [with "developer"
privileges](https://servicedesk.surfsara.nl/wiki/display/WIKI/Appoint+a+CO-member+a+developer)
can register the current application as a `Catalog Item` and setting up these
three parameters:

* the number of worker nodes in the cluster of VMs;
* (optional) the URL to a conda environment file, employed to configure both the
  head node and the workers with the same Python environment;
* (optional) a macaroon to authenticate access to [the SURF dCache
  starage](http://doc.grid.surfsara.nl/en/latest/Pages/Advanced/storage_clients/webdav.html#sharing-data-with-macaroons)
  via [dCacheFS](https://github.com/NLeSC-GO-common-infrastructure/dcachefs).

### 1. Create the component

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
  * Set "Parameter key" as `dcache_token`, "Source type" as "Fixed", and tick "Overwritable";
  * Set "Parameter key" as `worker_ip_addresses`, "Source type" as "Resource".

### 2. Create the catalog item

Follow the ["Create a catalog
item"](https://servicedesk.surf.nl/wiki/display/WIKI/Create+a+catalog+item)
instructions, using the following parameters:

* In the "Available components" tab, choose the following components (in this order):
  * SRC-OS
  * SRC-CO
  * SRC-Ngnix
  * SRC-External plugin
  * the component created in the previous step
* In the "Cloud providers" tab, add "SURF HPC Cloud cluster" with "Ubuntu 20.04"
  as OS and tick all available sizes.
* In the "Ovewritable parameters" tab:
  * For `co_passwordless_sudo`, set "Actions" to "Overwrite" and set "New
    parameter value" to `true`.
  * For `num_nodes`, set "Actions" to "Make interactive", set "Label or question
    for workspace creator" to "Number of worker nodes", and set "Default
    parameter value" to `0`.
  * For `dcache_token`, set "Actions" to "Make interactive", set "Label or
    question for workspace creator" to "dCache token: provide the macaroon to
    authenticate on the dCache storage", and set "Default parameter value" to
    `null`.
  * For `environment_url`, set "Actions" to "Make interactive", set "Label or
    question for workspace creator" to "Conda environment file: provide the URL
    to a custom environment.yml (blank for default environment)", and set
    "Default parameter value" to `default`.

### 3. Create the workspace

To create a workspace, you need to first create a storage, see [External storage
volumes](https://servicedesk.surf.nl/wiki/display/WIKI/External+storage+volumes).
Then, you can create a new workspace by following [Start a simple
workspace](https://servicedesk.surf.nl/wiki/display/WIKI/Start+a+simple+workspace)
and attach your storage to it. For the application, select the catalog item
created in the previous steps.

> Note: There are multiple pre-defiend set of virtual machines/working
> environments (which are called
> [<strong><em>flavours</em></strong>](https://servicedesk.surf.nl/wiki/display/WIKI/SRC+Available+Flavours))
> available on SRC.

### 4. Invite users

Administrators can invite users to access the created workspace on SRC via the
[SURF Research Access Management system](https://sram.surf.nl/). As an
administrator, you can send invitations to users following [Invite colleagues to
a CO](https://servicedesk.surf.nl/wiki/display/WIKI/Invite+colleagues+to+a+CO).

## Acknowledgments

Most of the playbooks in this repository have been taken, inspired or adapted
from the ones in the [eWaterCycle
infrastructure](https://github.com/eWaterCycle/infra) and the
[Emma](https://github.com/nlesc-sherlock/emma) projects.
