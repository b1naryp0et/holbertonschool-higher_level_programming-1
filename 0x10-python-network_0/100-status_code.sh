#!/bin/bash
#display status code
curl -sLI $1 -o /dev/null -w '%(http_code)'
