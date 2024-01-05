#!/bin/bash
# Script that sends a request to URL, and displays the size of the body of the response
curl -s "$1" | wc -c
