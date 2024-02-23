# Web Infrastructure README
![Alt Text](Image URL)

## Load Balancer (HAProxy):

- **Addition**: HAProxy is added to distribute incoming traffic across multiple servers.
- **Reason**: HAProxy enhances the scalability, fault tolerance, and performance of the infrastructure by efficiently distributing incoming requests among the available servers.
- **Distribution Algorithm**: HAProxy can be configured with various distribution algorithms, such as round-robin, least connections, source IP hash, etc.

### Active-Active vs. Active-Passive:

- **Active-Active**: All servers actively handle incoming requests simultaneously. This setup improves scalability and fault tolerance.
- **Active-Passive**: Only one server actively handles incoming requests, while the others remain on standby. This setup provides redundancy and failover capabilities.
- **Configuration**: HAProxy can be configured in either Active-Active or Active-Passive mode based on the specific requirements of the infrastructure.

## Database Primary-Replica (Master-Slave) Cluster:

- **Addition**: Implementing a primary-replica database cluster (Master-Slave) provides data redundancy, high availability, and read scalability.
- **Reason**: Having a database cluster ensures data durability and availability, even in the event of hardware failures or maintenance activities.
- **How It Works**:
  - The primary node (Master) handles both read and write operations.
  - Replica nodes (Slaves) replicate data from the primary node asynchronously and handle read-only queries.
  - Write operations are performed on the primary node and then replicated to the replica nodes.
- **Difference Between Primary and Replica Nodes**:
  - **Primary Node**: Handles both read and write operations. It's the authoritative source for data updates.
  - **Replica Node**: Replicates data from the primary node and handles read-only queries. It's used for scaling read operations and providing redundancy.

## Reasons for Adding Each Element:

- **Load Balancer**: Efficiently distributes incoming traffic and enhances scalability and fault tolerance.
- **Application Server**: Hosts the application logic and processes dynamic content.
- **Web Server (Nginx)**: Acts as a reverse proxy, serves static content, and forwards dynamic requests to the application server.
- **Database (MySQL)**: Stores and retrieves data for the website, ensuring data durability and availability.

## Issues With This Infrastructure

### Single Points of Failure (SPOF):
- **Load Balancer (HAProxy)**: If the load balancer fails, all incoming traffic will be disrupted, leading to downtime.
- **Database (MySQL)**: If the primary node fails and there is no automatic failover mechanism in place, the entire database becomes inaccessible until manual intervention.
- **Application Servers**: If one of the application servers fails, the load balancer might still route traffic to the failed instance, resulting in service degradation for users accessing that particular server.

### Security Issues:
- **Lack of Firewall**: Without a firewall, the infrastructure is vulnerable to unauthorized access, DDoS attacks, and other security threats.
- **Lack of HTTPS**: Transmitting data over HTTP exposes it to interception and manipulation by malicious actors. Without HTTPS, sensitive information, such as user credentials and payment details, is at risk of being compromised.

### No Monitoring:
- Without monitoring tools and processes in place, it becomes challenging to detect and address performance issues, resource utilization spikes, security breaches, or system failures promptly.
- Monitoring is crucial for maintaining the health and performance of the infrastructure, identifying potential security vulnerabilities, and ensuring the availability of services to users.

### Addressing these issues would involve implementing the following measures:

#### High Availability and Redundancy:
- Implement redundant load balancers to eliminate the single point of failure.
- Configure automatic failover mechanisms for the database cluster to ensure continuous availability in case of node failures.
- Deploy multiple application servers and distribute traffic evenly among them to prevent service disruptions due to server failures.

#### Security Enhancements:
- Set up a firewall to control incoming and outgoing traffic, filter malicious requests, and protect the infrastructure from various security threats.
- Enable HTTPS by installing SSL certificates on the web servers to encrypt data in transit and ensure secure communication between clients and servers.

#### Monitoring and Alerting:
- Implement monitoring tools to track system performance, resource usage, and network traffic in real-time.
- Set up alerts to notify administrators about any anomalies, security breaches, or service disruptions, allowing them to respond promptly and mitigate potential issues.


