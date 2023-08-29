# Web Server Configuration and Automation Project

This project involves configuring a web server (Ubuntu 16.04) and automating tasks using a Bash script. The primary goal is to learn about web server configuration, automation, and related concepts.

## Table of Contents

- [Introduction](#introduction)
- [Project Tasks](#project-tasks)
- [Usage](#usage)
- [Resources](#resources)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [Quiz Questions](#quiz-questions)

## Introduction

In this project, we will configure a web server (Nginx) according to specific requirements and create a Bash script to automate the configuration process. The automation script will perform tasks such as transferring files to the server using `scp`.

## Project Tasks

0. **Transfer a File to Your Server:**
   - Write a Bash script to transfer a file from a client to a server using `scp`.
   - The script should accept parameters for file path, server IP, username, and SSH private key path.
   - Strict host key checking must be disabled when using `scp`.

## Usage

To use the script for transferring a file to the server:

```bash
./0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY

