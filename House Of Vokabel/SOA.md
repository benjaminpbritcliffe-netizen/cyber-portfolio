# SOA

Status: Done

[SOA](../House%20Of%20Vokabel/SOA.md)

## Service Oriented Architecture

SOA comprises multiple modules that communicate over a network
to provide application functionality.
It is mostly used in enterprise applications.

**Enterprise Service Bus** — the backbone that connects services in an SOA.

Each module is self-contained and promotes code reusability.

SOA services:

- Are independent of each other.
- Are easier to maintain than interdependent services.
- Can be reused in many applications.
- Reduce development costs.

## Microservices

Microservices are a type of SOA, but the services are more granular.

- Expose functionality via specific business-need APIs (HTTP or Thrift).
- Each microservice is independent, providing fault tolerance and scalability.
- If one service fails, the application can keep working.
- Scale easily because each service is independent.
- Allow large complex applications to be quickly deployed.
