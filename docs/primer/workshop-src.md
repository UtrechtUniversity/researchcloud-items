# ResearchCloud workshop
[back to index](../primer-for-users.md)

Below are some suggestions for Research-IT support staff to assist new users 
during their first use of SURF ResearchCloud. 
While most users will be able to find their bearings using available 
documentation, you can make the difference to make this a much faster and more
gentle learning curve.   

The below steps build upon either other. They minimize the roundtrips that you
and users need to wait for SURF ResearchCloud and SRAM services to complete
a procedure.


## 1. (WITH USER) Intake
First, make sure that SURF ResearchCloud is indeed the right solution
to the needs of the new user. Will the user benefit from any of the 
existing workspace configurations? Or are more preparations required?
 
Give the new user a heads-up: soon they will receive an invitation 
email from the SRAM system asking them to join a collaboration.

## 2. Create Collaboration
In SRAM, create a collaboration named after the research project of the user.
Add SURF ResearchCloud to the services of the collaboration.
Decide if the user should be added as admin of the collaboration or that
you will manage collaboration membership for the moment.
Invite the user to the collaboration.

Allow 5-10 minutes for SURF ResearchCloud to synchronize with SRAM and 
pick up the new collaboration information.   

## 3. Create an example workspace with desktop
In SURF ResearchCloud portal, check in your profile that the new
collaboration exists. Then create an arbitrary workspace with desktop
graphical user interface using this collaboration. This workspace will be
used only to allow the new user to experience how to access a workspace.

Creation of a desktop workspace could take 20-30 minutes. Initiate the next
steps while the workspace is being created.

## 4. (WITH USER) Explain SRC and setup user account
Check that the user has been able to join the collaboration. 
Explain that the user needs a time-based token to login to workspaces.
Ask the user to login into the 
[SURF ResearchCloud portal](https://portal.live.surfresearchcloud.nl/).
Explain the dashboard page and show them how they will be able to create
a new workspace (catalog) and how they can find and access running workspaces
(the access button).
Assist them to configure the time-based token
as part of their profile.  

Test that the user is able to use the time-based token to access the
workspace created in step 3. If the workspace is not yet ready for use, then 
execute step 5 in parallel.

## 5. (WITH USER) Request wallet
Next guide the user through the portal to request a wallet for use with
their project. Explain the purpose of a wallet. To ensure that the
wallet is linked to the user account, the user herself needs to 
request the wallet via the SURF ResearchCloud portal.

Prompt the user for the information needed to make the request
(the fields in the request are: subtitle, existing contract, remarks). 
The subtitle should ideally
be an abbrevation of the research project name and the surname of the user.
Existing contract field is left empty and in remarks field the user should
reference "contact UU for approval".

Explain the user that at may take a few working days for the wallet request
to be processed.  Meanwhile they can use the workspace created in step 3 to 
familiarize themselves with SURF ResearchCloud.

## 6. (WITH USER) Show how data can be staged into a workspace.
Explain that data in the workspace is not persistent, it will only
be available for the duration of the lifetime of the workspace. 
Hence data needs to be *staged* to a workspace from a persistent storage
location. Likewise the results of analysis need to be transfered to a
persistent storage location. 

Assist them to load some sample data from a persistent location. This
may involve setting up a data transfer connection.
Proceed with one of the steps below in line
with needs of the user.

## 6a. Setup network drive connection to Yoda
(the same procedure can be used to connect a SURF Researchdrive)   
Show the user how to use the SURF ResearchCloud portal to link 
Yoda or SURF Researchdrive as an option in the collaboration attributes.

Important: For security reasons, the user should generate a Yoda data 
access password and use this access token for linking Yoda with a workspace.
This feature is available per Yoda 1.8. 

## 6b. Setup data transfer with Yoda using iCommands
Make sure the workspace type includes iRODS icommands. Show the user
how to acces a shell terminal window from within the workspace. Assist
them to use the command `iselect` to connect with a Yoda server.
Explain how they can use the `iget` and `iput` iRODS commands to transfer
data.

## 6c. Setup ftp or scp commandline data transfer
Assist the user to create a public/private key pair 
for use with SSH related commands on her own laptop.  
Have the user upload the public key and added to her profile 
in the SRAM web portal.   
NB: Allow 5-10 minutes for synchronization of the public key information
between SRAM and SURF ResearchCloud.

Test that the user can use the keypair to login to a workspace using the
SSH protocol.  Alternatively check that the user is able to use another
SSH protocol based command, such as `ftp`.

## 7. (WITH USER, AFTER WALLET APPROVAL) User creates a workspace
Assist the user to create a new workspace using the SURF ResearchCloud catalog.
Explain how pause and resume buttons can be used to stop and restart
the workspace during its lifecycle.

[back to index](../primer-for-users.md)
