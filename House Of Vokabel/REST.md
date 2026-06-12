# REST

Status: Done

[REST](../House%20Of%20Vokabel/REST.md)

## Representational State Transfer

REST is an architectural style for designing networked applications.
It uses standard HTTP methods and is stateless by design.

## Key Principles

- **Stateless** — each request contains all the information needed; the server holds no session state.
- **Client-Server** — the client and server are separated, each able to evolve independently.
- **Uniform Interface** — resources are identified by URLs; responses return representations (JSON, XML).
- **Cacheable** — responses can be cached to improve performance.
- **Layered System** — clients do not need to know whether they are talking directly to the server.

## HTTP Methods

| Method | Purpose |
|--------|---------|
| GET    | Retrieve a resource |
| POST   | Create a resource |
| PUT    | Update a resource |
| DELETE | Delete a resource |

## REST vs SOAP

- REST is lightweight and uses JSON or XML; [[SOAP]] is XML-only and more rigid.
- REST is typically preferred for public-facing APIs and microservices.
- SOAP is more common in enterprise and legacy systems where strict contracts are required.
