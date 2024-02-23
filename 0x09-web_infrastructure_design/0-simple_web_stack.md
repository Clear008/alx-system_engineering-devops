# Server Overview

## What is a server?
A server is a powerful computer dedicated to providing resources and services to other devices (clients) over a network. It can be hardware, software, or both. Servers come in various types, each specializing in specific tasks like web hosting, email, file storage, etc.

## What is the role of the domain name?
A domain name acts like a website's address on the internet. Users type it into their browser to access the website. It translates to an IP address (a numerical identifier) that servers use to locate and connect to the website's actual location.

## What type of DNS record is "www" in www.foobar.com?
The "www" subdomain often points to a "CNAME" DNS record, which aliases it to the main domain. This is done for historical reasons and user preference, but it doesn't affect functionality.

## Web Server
The web server receives requests from your browser when you enter a website's address. It processes these requests, retrieves the website's content (HTML, CSS, images, etc.), and sends it back to your browser for display. Common web servers include Apache and Nginx.

## Application Server
While not always present, an application server sits behind the web server, handling complex tasks. It interacts with databases, processes user data, and generates dynamic content, like personalized recommendations or shopping carts. Examples include Java EE servers like Tomcat or WildFly.

## What is the role of the database
The database stores website data like product information, user accounts, and website content. This data is organized and easily accessible for the web server or application server to retrieve and use when building the website you see. Popular database systems include MySQL, PostgreSQL, and MongoDB.

## What is the server using to communicate with the computer of the user requesting the website
Communication happens through a protocol called HTTP (Hypertext Transfer Protocol). This protocol defines how messages are formatted and exchanged between the server and your browser. When you request a website, your browser sends an HTTP request to the server, and the server responds with an HTTP response containing the website's data.

