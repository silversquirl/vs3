#!/bin/bash
# An example CGI script designed to be used with Python3's http.server
# module. To test it out, run `python3 -m http.server --cgi` in the
# example directory (NOT cgi-bin) and navigate to the following URL:
# http://localhost:8000/cgi-bin/example.cgi/index
# You should see the rendered version of pages/index.md

notfound() {
  echo "Status: 404"
  echo "Content-type: text/plain"
  echo
  echo "404 Not Found"
  exit
}

[[ -z "$PATH_INFO" ]] && notfound
[[ -f "pages/$PATH_INFO.md" ]] || notfound

echo "Content-type: text/html"
echo

# Python's CGI implementation is weird. Normally this would be
# ../../vs3 "../pages/$PATH_INFO.md"
../vs3 "pages/$PATH_INFO.md"
