# SQL Injection

SQL injection is a prevalent vulnerability and has long been a hot topic in
cyber security. To understand this vulnerability, we must first learn what a
database is and how websites interact with a database.

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

-D database_name -T table_name --dump

f you see any web application using GET parameters in the URLs to retrieve data,
you can test that URL with the -u flag in the SQLMap tool. This is considered to
be HTTP GET-based testing. This approach is followed when the application uses
GET parameters in the URL to retrieve data from the searches.

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
sqlmap -u http://sqlmaptesting.thmsearch/cat=1 -D users -T thomas --dump
```

unlike the URL used for testing above, you can also use POST-based testing,
where the application sends data in the request's body instead of the URL.
Examples of this could be login forms, registration forms, etc. To follow this
approach, you must intercept a POST request on the login or registration page
and save it as a text file. You can use the following command to input that
request saved in the text file to the SQLMap tool: sqlmap -r
intercepted_request.txt

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
