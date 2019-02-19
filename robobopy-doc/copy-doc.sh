#!/bin/bash

rsync --archive --delete --progress --verbose ./build/html/* ../docs/
rsync --archive --delete --progress --verbose  ./build/html/.nojekyll ../docs/