# connectNcopy
Connects to a server and copy files in local drive. Useful for unattended copying files (e.g. Krios movies) from beamline server.
1. connects to server using user provided domain name and password.
2. User needs to provide a mother path/tree where the program will look for files.
3. User needs to provide file extension the program needs to look for (e.g. *_fractions.tiff).
4. Enjoy your life while your data is rushing to you.

NOTE: Paramiko libraries needed to connect to a doamin using ssh protocol. Install using: `pip install paramiko`    

NOTE II: Please report issues, if encountered.  

Cheers  
Abhisek
