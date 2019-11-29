* Using a single hostile Tor node they have located hidden servers within minutes. 

* First intersection attacks performed on a public network, confirming theory and expectation. 

* Hidden services resistant against DoS, and to bring them down, would need to DDoS entire Tor. 

*  Hidden servers have also been recommended for preserving the anonymity of the service offerer and to resist censorship.

* The attacks provided in the paper focus on locating hidden services, the results and the principles can be applied to "normal" Tor servers, and outside Tor as well. 

* They should apply to the hidden service design even if run on another underlying anonymity network and should apply to other
clients using an anonymity network, not just to hidden servers.

* One of the major vulnerabilities for a hidden service in Tor is the server’s selection of the first and last node in the communication path

* First the Hidden Server connects (1) to a node in the Tor network and asks if it is OK for the node to act as an Introduction Point for his service. If the node accepts, we keep the circuit open and continue; otherwise HS tries another node until successful.
Next, the Hidden Server contacts (2) the Directory Server and asks it to publish the contact information of its hidden service. The hidden service is now ready to receive connection requests from clients. In order to retrieve data from the service the
Client connects (3) to DS and asks for the contact information of the identified service and retrieves it if it exists (including the addresses of Introduction Points). There can be several Introduction Points per service. The Client then selects a node
in the network to act as a Rendezvous Point, connects (4) to it and asks it to listen for connections from a hidden service on C’s behalf. The Client repeats this until a Rendezvous Point has accepted, and then contacts (5) the Introduction Point and asks it to forward the information about the selected RP.2 The Introduction Point forwards (6) this message to the Hidden Server who determines whether to connect to the Rendezvous Point or not.3 If OK, the Hidden Server connects (7) to RP and asks to be connected to the waiting rendezvous circuit, and RP then forwards (8) this connection request to the Client. Now RP can start passing data between the two
connections and the result is an anonymous data tunnel (9) from C to HS through RP

* Observations: The Client does not know the location(IP Address) of the Hidden service, but does know the location of the Rendezvous point. In turn, the Hidden service does not know the location of the Client, but does know the location of the Rendezvous point. 

The Rendezvous point does not know the location of either the Client or the Hidden service. Furthermore, the Rendezvous point does not know the service he's serving, nor the content of the message sent through him.

There are multiple nodes between the Rendezvous point and the Hidden service, and two nodes between the Client and the Rendezvous point, to hide traffic and create anonymity. 

Any member of the network who offers stability can be used by the Hidden service to create a tunnel to the Rendezvous point, including the Client if it's a node in the anonymization network, which the attacks are based on. 


* The attacks can be carried out by an adversary that controls merely a single node in the network. In fact the adversary need only run
a “middleman” node, which never lets circuits exit the anonymization network.  At the end we describe an accelerated attack using two compromised nodes. Alice = Attacker. Alice controls the Client and one node. Her goal is to control Node 1 of the circuit.
Certain circuits will yield a match of traffic pattern with what is expected given when C sends to and receives from HS. Alice will look for such pattern matches among all active circuits through the node
she owns. If she finds a match, then her node has been made part of the circuit between the Hidden Server and the Rendezvous Point as Node 1, 2 or 3.


1. -

2. 
First she will know when she has the node closest to
RP (Node 3) since she knows RP’s IP address, and
she can easily abandon the circuit and attack again.
Second, if her node has an unknown IP address on
both sides of the matching circuit, she knows she is
either Node 1 connected directly to HS or Node 2
in the circuit. This enables her to use timing or statistical methods to determine her position as will be
described later.
We will continue sampling data until we have
enough to determine when Alice is connecting to
the hidden service as Node 1 in the circuit towards RP, at which point we will know the Hidden
Server’s IP address