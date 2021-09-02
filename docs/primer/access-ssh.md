# Access workspace using Secure Shell
[back to index](../primer-for-users.md)

SURF ResearchCloud supports key-based access. 


### Preparation
Your SSH public key needs to be uploaded to 
[SURF Research Access Management (SRAM)](https://sbs.sram.surf.nl).
Login to SRAM, then access and update your "profile".

Make a note of the ***Username*** listed in your SRAM profile. This is the
username you will need to use for SHH access.


### Accessing a running Workspace
Login to [SURF ResearchCloud portal](https://portal.live.surfresearchcloud.nl).

The dashboard page shows the workspaces that you have access to. Unfold the
workspace to find its ***IP address*** (requires state = running).

Now access the workspace from a local shell using `ssh <username>@<ip>`.

