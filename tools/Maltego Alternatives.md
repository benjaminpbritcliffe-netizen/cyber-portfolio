# Maltego Alternatives

## SpiderFoot

What it is: The closest free equivalent to Maltego in terms of automated OSINT reconnaissance.
It has a free open-source version (SpiderFoot OSS)
and a paid hosted version (SpiderFoot HX).

Why it's a good fit:

Over 200 modules that pull data from search engines, DNS, WHOIS, breach databases,
social media, threat intel feeds, etc.
Produces a similar node/graph visualization of relationships between entities
(domains, IPs, emails, usernames).
Has both a web UI and a CLI, plus a REST API.
Runs locally on Windows/Linux/macOS or via Docker.

Limitation:
The graphing/visualization is less polished than Maltego's "transform" interface,
and it's more automated/scanner-like rather than the manual,
exploratory pivoting style Maltego is known for.

## Recon-ng

What it is:
A modular, CLI-based reconnaissance framework, sort of the "Metasploit of OSINT."

Why it's a good fit:

Modular architecture very similar conceptually to Maltego's transforms —
each module pulls specific data (subdomains, contacts, breach data, etc.)
and feeds it into a workspace database.
Free and fully open source.
Good for scripted, repeatable recon workflows.

Limitation: No visual graph interface out of the box — it's terminal-based.
You'd need to export data and visualize it separately (e.g., with Gephi, see below).

## OSINT Framework (not a tool, but a map of tools)

This is a website (osintframework.com) that organizes free OSINT tools by category
(username search, email search, geolocation, etc.).
It doesn't do the graphing/pivoting itself,
but it's an excellent companion for finding the right free tool
for each specific transform you'd normally run in Maltego.

## Gephi (for the visualization side)

What it is: A free, open-source graph/network visualization tool.

Why it's relevant: Maltego's core value is really two things —
(1) data gathering via transforms,
and (2) visualizing those relationships as a graph.
Gephi doesn't do the data gathering,
but it's the best free tool for the visualization half.
A common workflow is: gather data with SpiderFoot/Recon-ng/theHarvester
→ export as CSV/GEXF → import into Gephi → build the link-analysis graph manually.

## theHarvester

What it is:
A free tool focused specifically on gathering emails, subdomains, hosts,
employee names, and open ports from public sources.

Why it's useful:
Great as a data-gathering module to feed into Gephi for graphing,
similar to running a single Maltego transform.

## Datasploit

An OSINT framework that aggregates data on domains, emails, usernames,
and phone numbers, and can output structured/graphable data.
Less actively maintained than SpiderFoot but still usable.
