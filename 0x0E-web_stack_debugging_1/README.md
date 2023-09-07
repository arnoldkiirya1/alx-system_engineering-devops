# Web Stack Debugging #1

In this project, you'll demonstrate your debugging skills by troubleshooting and fixing issues related to an Nginx web server not listening on port 80. The goal is to ensure that Nginx is running and properly configured to listen on port 80 of all the server's active IPv4 IPs.

## Tasks

### 0. Nginx likes port 80

**File:** [0-nginx_likes_port_80](0-nginx_likes_port_80)

To complete this task, you need to find out what's preventing Nginx from listening on port 80 and write a Bash script that configures a server to meet the following requirements:

- Nginx must be running.
- Nginx must be listening on port 80 of all the server's active IPv4 IPs.

You can use whatever debugging tools and techniques you need to solve this issue. The script should automate the fix with the minimum number of commands.

### Usage

```bash
./0-nginx_likes_port_80

