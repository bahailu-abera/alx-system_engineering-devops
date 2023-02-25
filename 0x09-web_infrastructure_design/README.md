# Web infrastructure design

## Resources:books:
Read or watch:
* [Network basics](https://intranet.hbtn.io/rltoken/Sn9ZSSHjyEW5aRfKvNiZCg)
* [Server](https://intranet.hbtn.io/rltoken/83joH7-HzuV9gBNe16iTrA)
* [Web server](https://intranet.hbtn.io/rltoken/7moqhXcFOXP6zNMWdsjWjQ)
* [DNS](https://intranet.hbtn.io/rltoken/G0a1v98rwb2RHA8VHxo36A)
* [Load balancer](https://intranet.hbtn.io/rltoken/H6TVgGaqt13JhXKzJ2rVAA)
* [Monitoring](https://intranet.hbtn.io/rltoken/JY6524JCvX9dREoNgnQUFw)
* [What is a database](https://intranet.hbtn.io/rltoken/XLIOfzfuaxPQu39VQ0TLtw)
* [What’s the difference between a web server and an app server?](https://intranet.hbtn.io/rltoken/Nb8B47Y2D8SLqQMOKVoQyQ)
* [DNS record types](https://intranet.hbtn.io/rltoken/pSGVxlKznxONwGEHIXLSwA)
* [Single point of failure](https://intranet.hbtn.io/rltoken/wYpewVpIp9PSqqL27RPafg)
* [How to avoid downtime when deploying new code](https://intranet.hbtn.io/rltoken/Mlvynt0OgLQXrxjrC5Wlnw)
* [High availability cluster (active-active/active-passive)](https://intranet.hbtn.io/rltoken/POX3jE0S6TChQHSYQraYeQ)
* [What is HTTPS](https://intranet.hbtn.io/rltoken/N4BwU4wYDNW02kdzMiekFw)
* [What is a firewall](https://intranet.hbtn.io/rltoken/HrYI70d_nxUPZeufjUYzIw)

---
## Learning Objectives:bulb:
What you should learn from this project:

* You must be able to draw a diagram covering the web stack you built with the sysadmin/devops track projects
* You must be able to explain what each component is doing
* You must be able to explain system redundancy
* Know all the mentioned acronyms: LAMP, SPOF, QPS

---

### [0. Simple web stack](./0-simple_web_stack)
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a LAMP stack.

-   What is a server?
	-  Is a piece of computer hardware or software that provides functionality for other programs or devices, called "clients".
-   What is the role of the domain name?
	- **Domain names** serve to identify Internet resources, such as computers, networks, and services, with a text-based label that is easier to memorize than the numerical addresses
-   What type of DNS record  `www`  is in  `www.foobar.com`
	- The use of _www_ is not required by any technical or policy standard and many web sites do not use it,  a CNAME record that points to a cluster of web servers.
-   What is the role of the web server
	- A **[web server](https://www.nginx.com/resources/glossary/web-server/)**‘s fundamental job is to accept and fulfill requests from clients for static content from a website (HTML pages, files, images, video, and so on). The client is almost always a browser or mobile application and the request takes the form of a Hypertext Transfer Protocol ([HTTP](https://www.nginx.com/resources/glossary/http/)) message, as does the web server’s response.
-   What is the role of the application server
	- An **application server**’s fundamental job is to provide its clients with access to what is commonly called _business logic_, which generates dynamic content; that is, it’s code that transforms data to provide the specialized functionality offered by a business, service, or application.
-   What is the role of the database
	- A database is a way of storing information in an organised, logical way. Databases can store very large numbers of records efficiently (they take up little space). It is very quick and easy to find information. It is easy to add new data and to edit or delete old data.
-   What is the server using to communicate with the computer of the user requesting the website
	- HTTP
-   SPOF
	- If anything fails the system stops being available
-   Downtime when maintenance needed (like deploying new code web server needs to be restarted)
	- There's no way to have backup when updating the web server, and tests can't be perform while having the service online.
-   Cannot scale if too much incoming traffic
	- There's no way to give more resources to the server if it needs it.
### [1. Distributed web infrastructure](./1-distributed_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com.
-   What distribution algorithm your load balancer is configured with and how it works
	- **Round robin**: (sometimes called "Next in Loop"). It is the oldest, simplest scheduling algorithm, which is mostly used for multitasking. In Round-robin scheduling, each ready task runs turn by turn only in a cyclic queue for a limited time slice.
-   Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
	- Active - Active setup, when our setup is Active - Passive we have one server as backup (standby) waiting for the other to get damage, but here bot are working at the same time.
-   How a database Primary-Replica (Master-Slave) cluster works
	- **Master**-**slave** replication enables data from one **database** server (the **master**) to be replicated to one or more other **database** servers (the slaves). The **master** logs the updates
-   What is the difference between the Primary node and the Replica node in regard to the application
	- **Scale-out solutions —** spreading the load among multiple slaves to improve performance. In this environment, all writes and updates must take place on the master server. Reads, however, may take place on one or more slaves. This model can improve the performance of writes (since the master is dedicated to updates), while dramatically increasing read speed across an increasing number of slaves.


### [2. Secured and monitored web infrastructure](./2-secured_and_monitored_web_infrastructure)
* On a whiteboard, design a three server web infrastructure that hosts the website www.foobar.com, it must be secured, serve encrypted traffic, and be monitored.
-   What are firewalls for?
	- Firewalls can either be software or hardware, though it’s best to have both. A software firewall is a program installed on each computer and regulates traffic through port numbers and applications, while a physical firewall is a piece of equipment installed between your network and gateway.
	- Packet-filtering firewalls, the most common type of firewall, examine packets and prohibit them from passing through if they don’t match an established security rule set.
	- **Proxy firewalls** filter network traffic at the application level. Unlike basic firewalls, the proxy acts an intermediary between two end systems. The client must send a request to the firewall, where it is then evaluated against a set of security rules and then permitted or blocked.
-   Why is the traffic served over HTTPS?
	- A site **served over https** is more secure. Since **https** uses the secure port 443, which encrypts outgoing information, it is much more difficult for people to spy on your site's information. Regular http, on the other hand, uses port 80, which sends information via plain text.
-   What monitoring is used for?
	- Server Monitoring is the process of monitoring all the system resources associated with the server in order to understand their resource usage patterns and optimize them accordingly to provide a better end-user experience. It ensures that your server is capable of hosting your applications by providing sufficient data relating to the performance of your system and helps you understand the system operations.
-   How the monitoring tool is collecting data?
	- Collector is an application that runs on a server within your infrastructure and uses standard monitoring protocols to intelligently monitor devices within your infrastructure.
-   Explain what to do if you want to monitor your web server QPS?
	- Once you’ve completed a series of benchmarks, take a step back and think about what the data is telling you about the system you’re benchmarking. Document your insights and how the data backs them up.


### [3. Scale up](./3-scale_up)
-   1 load-balancer (HAproxy) configured as cluster with the other one
-   Split components (web server, application server, database) with their own server
---

## Author
* **Bahailu Abera** - [bahailu-abera](https://github.com/bahailu-abera)