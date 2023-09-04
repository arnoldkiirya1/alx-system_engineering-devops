# Load Balancer Project

## Overview
This project focuses on setting up a load balancer and configuring web servers for redundancy and load balancing. The goal is to distribute incoming traffic across multiple web servers and add a custom HTTP header to the Nginx response to track which server is serving the request.

## Table of Contents
- [Project Tasks](#project-tasks)
- [Requirements](#requirements)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Testing](#testing)
- [Author](#author)
- [License](#license)

## Project Tasks
1. **Double the number of webservers**
   - Configure `web-02` to match the configuration of `web-01`.
   - Add a custom HTTP header to the Nginx response with the server's hostname.
   - Write a Bash script to automate the configuration.
   - Ensure proper hostnames.
   - Example usage and script: [0-custom_http_response_header](0-custom_http_response_header).

2. **Install your load balancer**
   - Install and configure HAProxy on `lb-01` server.
   - Configure HAProxy to send traffic to `web-01` and `web-02`.
   - Distribute requests using a round-robin algorithm.
   - Ensure HAProxy can be managed via an init script.
   - Ensure proper hostnames.
   - Example usage and script: [1-install_load_balancer](1-install_load_balancer).

3. **Add a custom HTTP header with Puppet**
   - Automate the task of creating a custom HTTP header response using Puppet.
   - The header name must be `X-Served-By`, and the value should be the server's hostname.
   - Example usage and Puppet manifest: [2-puppet_custom_http_response_header.pp](2-puppet_custom_http_response_header.pp).

## Requirements
- Ubuntu 16.04 LTS
- Bash scripts must be executable.
- Puppet for task 3.
- Proper server hostnames: `[STUDENT_ID]-web-01` and `[STUDENT_ID]-web-02`.

## Getting Started
1. Clone this repository to your local machine.
2. SSH into the provided servers (`web-01`, `web-02`, and `lb-01`) using your SSH key.
3. Navigate to the project directory.

## Usage
- Execute the Bash scripts and Puppet manifest provided in each task to configure the servers as per the project requirements.
- Ensure you replace `[STUDENT_ID]` with your actual student ID.

## Project Structure
- `0-custom_http_response_header`: Bash script for task 1.
- `1-install_load_balancer`: Bash script for task 2.
- `2-puppet_custom_http_response_header.pp`: Puppet manifest for task 3.
- `README.md`: Project documentation.

## Testing
- After running the scripts, test the configuration to ensure HAProxy load balancing and custom HTTP headers are working as expected.

## Author
- Kiirya Arnold

## License
This project is licensed under [License Name] - see the [LICENSE.md](LICENSE.md) file for details.

