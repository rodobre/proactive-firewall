# Threathunter

![Threathunter](/resources/threathunter.png)

### DISCLAIMER: The project is in a Minimal Viable Product stage (MVP). As such, users/customers/integrators of this project may encounter bugs. The feature set is incomplete but the project is being actively developed.

### Introduction

Threathunter is a platform which enables automatic detection of malware/suspicious activity within enterprise networks.
The purpose of the program is to act as a passive firewall, performing consistent detection on the traffic proxied by the platform.

The goals for this project were to enable sustainable detection on even the most basic hardware, few levels under common consumer grade specifications. Thus, to prove our commitment to performance and optimization, the platform runs on a Raspberry Pi 4GB running a Ubuntu Server x64 distribution.

A demo of the project can be found at https://www.youtube.com/watch?v=W0trfWDBApM.

### Endpoint structure and diagram

![UML Diagram](/resources/uml.png)

The project is structured as such:

1. **Lightweight native proxy** - A lightweight proxy located inbetween the enterprise users (acts as a router) and the platform, performs SSL stripping and is implemented via mitmdump (https://mitmproxy.org/)
1. **Anomaly detection endpoint** - An anomaly detection endpoint is a primitive implemented via Isolation Forests in order to sift through the large amount of traffic that is incoming at large speeds and perform basic detection.
1. **Traffic classifiying endpoint** - The traffic classifying endpoint is the next detection layer. Packets that are labeled as suspicious by the anomaly detection endpoint end up being classified. Upon certain confidence scores, those classifications are reported.
1. **Flask backend** - The Flask (python web route framework) powers the dashboard and serves the needed Javascript/CSS for the React application
1. **Realtime dashboard** - The React dashboard combines a modern, pleasing, self-made design with the user-friendly UX that allows sifting with ease through notification logs, as well as observing shifts of attack frequencies.
1. **Data pipeline** - The pipeline used for this project is represented by a redis message queue, which enables the proxy to efficiently communicate with the detection endpoints.

### Technology stack

For the frontend, the following technologies were used:

1. React (w/ Apex Charts, Material UI, Bootstrap)
1. JavaScript
1. CSS

The backend is comprised of the following technology stack:

1. MITMProxy
1. Docker
1. Redis (Message Queue daemon)
1. sklearn (Machine Learning framework)
1. Python 3.8.2

### Feature set

The project implements the following feature set:

1. **Active detection** - Research-backed threat detection using novel algorithms for maximum efficiency
1. **Performance driven** - The project is designed to run on even the most feeble of setups, maximizing efficiency and performance. The most significant bottleneck is the I/O.
1. **User-friendly monitoring** - The real time dashboard allows administrators to track the safety of the enterprise network instantly, while also showcasing a modern theme, designed around the user.
1. **State-of-the-art technologies** - The project employs the best tools for the job, no compromises. The target is the safety of the users, the goal is performance, efficiency and usability.
1. **Meaningful detections, no noise** - We took extra steps to ensure that only the entries with the highest confidence are considered attacks. This narrows the surface area for the administratos and enables them to only focus on the important feed.
1. **Replicable results** - The dataset is constructed based on actual attacks, fed from tools such as 'gobuster', 'dirb', 'BurpSuite', etc. These tools are used by security professionals to perform audits / penetration tests. Therefore, the scenario is as real life as could be.
1. **Layered design** - The platform is designed on layers which help minimize false positives while maintaining high levels of efficiency and speed.
1. **Reliable pipelines** - The core of the I/O: the database and the message queue. Those two components are implemented using industry proven technologies such as Redis and MySQL, toolsets which have been used in Top 500 companies for over a decade.
1. **Inside-out approach** - The product offers a novel approach to protecting enterprise networks. Instead of filtering incoming traffic, our focus is to filter outgoing traffic, because data is exfiltrated from within the network to outside hosts.
1. **Sandboxing** - The product relies on components which can exist on separate hosts, separate machines, even separate networks if a complex infrastructure requires so. The components exist in their own environment without interfering with the host machine.


### Roadmap

1. Implement a more diversified range of attacks.
1. Add support for multiple protocols.
1. Add more statistics related to the confidence of the detection, as well as True Positive/False Positive indicators.
1. Implement automatic retraining to enable the model to learn during the lifetime of the product.
1. Synchronize multiple datasets from multiple deployments to aggregate information and construct a better model, similar to the inner workings of genetic algorithms.
