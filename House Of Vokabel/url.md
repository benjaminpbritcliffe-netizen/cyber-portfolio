# Defining a URL

Think of a URL as being made up of several parts, each playing a different role
in helping you find the right resource. Understanding how these parts fit
together is important for browsing the web, developing web applications, and
even troubleshooting problems.

Here’s a breakdown of the key components:

## Scheme

The scheme is the protocol used to access the website. The most common are HTTP
(HyperText Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure).
HTTPS is more secure because it encrypts the connection, which is why browsers
and cyber security experts recommend it. Websites often enforce HTTPS for added
protection.

## User

Some URLs can include a user’s login details (usually a username) for sites that
require authentication. This happens mostly in URLs that need credentials to
access certain resources. However, it’s rare nowadays because putting login
details in the URL isn’t very safe—it can expose sensitive information, which is
a security risk.

## Host/Domain

The host or domain is the most important part of the URL because it tells you
which website you’re accessing. Every domain name has to be unique and is
registered through domain registrars. From a security standpoint, look for
domain names that appear almost like real ones but have small differences (this
is called typosquatting). These fake domains are often used in phishing attacks
to trick people into giving up sensitive info.

## Port

The port number helps direct your browser to the right service on the web
server. It’s like telling the server which doorway to use for communication.
Port numbers range from 1 to 65,535, but the most common are 80 for HTTP and 443
for HTTPS.

## Path

The path points to the specific file or page on the server that you’re trying to
access. It’s like a roadmap that shows the browser where to go. Websites need to
secure these paths to make sure only authorised users can access sensitive
resources.

## Query String

The query string is the part of the URL that starts with a question mark (?).
It’s often used for things like search terms or form inputs. Since users can
modify these query strings, it’s important to handle them securely to prevent
attacks like injections, where malicious code could be added.

## Fragment

The fragment starts with a hash symbol (#) and helps point to a specific section
of a webpage—like jumping directly to a particular heading or table. Users can
modify this too, so like with query strings, it’s important to check and clean
up any data here to avoid issues like injection attacks.

## HTTP

Each message follows a specific format that helps both the user and the server
communicate smoothly.

### Start Line

The start line is like the introduction of the message. It tells you what kind
of message is being sent—whether it's a request from the user or a response from
the server. This line also gives important details about how the message should
be handled.

### Headers

Headers are made up of key-value pairs that provide extra information about the
HTTP message. They give instructions to both the client and the server handling
the request or response. These headers cover all sorts of things, like security,
content types, and more, making sure everything goes smoothly in the
communication.

### Empty Line

The empty line is a little divider that separates the header from the body. It’s
essential because it shows where the headers stop and where the actual content
of the message begins. Without this empty line, the message might get messed up,
and the client or server could misinterpret it, causing errors.

### Body

The body is where the actual data is stored. In a request, the body might
include data the user wants to send to the server (like form data). In a
response, it’s where the server puts the content that the user requested (like a
webpage or API data).

### Request Line

Request Line The request line (or start line) is the first part of an HTTP
request and tells the server what kind of request it’s dealing with. It has
three main parts: the HTTP method, the URL path, and the HTTP version.

Example: METHOD /path HTTP/version

HTTP Methods The HTTP method tells the server what action the user wants to
perform on the resource identified by the URL path. Here are some of the most
common methods and their possible security issue:

GET Used to fetch data from the server without making any changes. Reminder!
Make sure you’re only exposing data the user is allowed to see. Avoid putting
sensitive info like tokens or passwords in GET requests since they can show up
as plaintext.

POST Sends data to the server, usually to create or update something. Reminder!
Always validate and clean the input to avoid attacks like SQL injection or XSS.

PUT Replaces or updates something on the server. Reminder! Make sure the user is
authorised to make changes before accepting the request.

DELETE Removes something from the server. Reminder! Just like with PUT, make
sure only authorised users can delete resources.

Besides these common methods, there are a few others used in specific cases:

PATCH Updates part of a resource. It’s useful for making small changes without
replacing the whole thing, but always validate the data to avoid
inconsistencies.

HEAD Works like GET but only retrieves headers, not the full content. It’s handy
for checking metadata without downloading the full response.

OPTIONS Tells you what methods are available for a specific resource, helping
clients understand what they can do with the server.

TRACE Similar to OPTIONS, it shows which methods are allowed, often for
debugging. Many servers disable it for security reasons.

CONNECT Used to create a secure connection, like for HTTPS. It’s not as common
but is critical for encrypted communication.

Each of these methods has its own set of security rules. For example, PATCH
requests should be validated to avoid inconsistencies, and OPTIONS and TRACE
should be turned off if not needed to avoid possible security risks.
