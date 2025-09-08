
To list all available cmdlets, functions, aliases, and scripts that can be executed in the current PowerShell session, we can use Get-Command. It’s an essential tool for discovering what commands one can use.

Similar to the dir command in Command Prompt (or ls in Unix-like systems), Get-ChildItem lists the files and directories in a location specified with the -Path parameter. It can be used to explore directories and view their contents. If no Path is specified, the cmdlet will display the content of the current working directory.

Another essential cmdlet to keep in our tool belt is Get-Help: it provides detailed information about cmdlets, including usage, parameters, and examples.

To navigate to a different directory, we can use the Set-Location cmdlet. It changes the current directory, bringing us to the specified path, akin to the cd command in Command Prompt.

To navigate to a different directory, we can use the Set-Location cmdlet. It changes the current directory, bringing us to the specified path, akin to the cd command in Command Prompt.


We can copy or move files and directories alike, using respectively Copy-Item (equivalent to copy) and Move-Item (equivalent to move).

Finally, to read and display the contents of a file, we can use the Get-Content cmdlet, which works similarly to the type command in Command Prompt (or cat in Unix-like systems).

Piping is a technique used in command-line environments that allows the output of one command to be used as the input for another. This creates a sequence of operations where the data flows from one command to the next. Represented by the | symbol, piping is widely used in the Windows CLI, as introduced earlier in this module, as well as in Unix-based shells.

The Get-ComputerInfo cmdlet retrieves comprehensive system information, including operating system information, hardware specifications, BIOS details, and more. It provides a snapshot of the entire system configuration in a single command. Its traditional counterpart systeminfo retrieves only a small set of the same details.

- Get-LocalUser lists all the local user accounts on the system

- Get-NetIPConfiguration provides detailed information about the network interfaces on the system, including IP addresses, DNS servers, and gateway configurations.

- In case we need specific details about the IP addresses assigned to the network interfaces, the Get-NetIPAddress cmdlet will show details for all IP addresses configured on the system, including those that are not currently active.


- In PowerShell, you need to change the directory to the “C:\Users” folder where user profiles are located. You can do this by using the Set-Location cmdlet (or its alias cd)


- To gather more advanced system information, especially concerning dynamic aspects like running processes, services, and active network connections, we can leverage a set of cmdlets that go beyond static machine details.

- Get-Process provides a detailed view of all currently running processes, including CPU and memory usage, making it a powerful tool for monitoring and troubleshooting.

- Similarly, Get-Service allows the retrieval of information about the status of services on the machine, such as which services are running, stopped, or paused.

- To monitor active network connections, Get-NetTCPConnection displays current TCP connections

- Additionally, we are going to mention Get-FileHash as a useful cmdlet for generating file hashes, which is particularly valuable in incident response, threat hunting, and malware analysis, as it helps verify file integrity and detect potential tampering.


The OwningProcess property indicates the Process ID (PID) of the process that owns or created the TCP connection. Each active connection is associated with a specific process running on the machine, and this property helps you identify which process that is.


What is the syntax to execute the command Get-Service on a remote computer named "RoyalFortune"? Assume you don't need to provide credentials to establish the connection. [for the sake of this question, avoid the use of quotes (" or ') in your answer]
Answer :

``` bash
Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }
```

Invoke-Command is essential for executing commands on remote systems, making it fundamental for system administrators, security engineers and penetration testers. Invoke-Command enables efficient remote management and—combining it with scripting—automation of tasks across multiple machines. It can also be used to execute payloads or commands on target systems during an engagement by penetration testers—or attackers alike.

