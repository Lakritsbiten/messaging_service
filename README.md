Test assignment
==========================

Build a service for sending and retrieving text messages. The service should 
support the following functions.

1. Submit a message to a defined recipient, identified with some identifier, e.g. email-address, phone-number, user name or similar.
2. Fetch previously not fetched messages. This implies that the service should be aware about what messages that has been previously fetched.
3. Delete one or more messages
4. Fetch messages (including previously fetched) ordered by time, according to start and stop index.

The service must be implemented with a REST-API

Assumptions/delimitations
----------------------------
The service does not need to include a client (curl or similar must be supported 
as a client) or other client interfaces. The implementation does not need to handle authorization or authentication. The implementation does not need to be "ready for production", however it should reflect your regular level of work. It is ok to make assumptions as longs as they are clearly communicated and motivated.

Implementation
----------------------------
Preferably Python should be used. Most other languages are ok, but needs to be 
approved by TriOptima first, in order to ensure that we can evaluate the 
solution.

The implementation should preferably be executable on a Unix-like 
environment, e.g. Linux or OSX. Exceptions from this can be agreed when 
motivated/needed.

If curl is the only client, or if the client is not self-explanatory, there must be 
documentation for how to use the service.
Usage of 3rd party open source components are encouraged.
The implementation should consider, but not necessarily include.
-Redundancy
-Scalability

Delivery
----------------------------
The service should be made available to TriOptima with clear instructions on 
how to build/compile/run the service. Usage of common techniques for building 
the service and managing dependencies is encouraged. E.g. Maven in Java or pip 
in Python.