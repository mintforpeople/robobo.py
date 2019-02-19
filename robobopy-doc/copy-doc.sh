#!/bin/bash

rsync --archive --delete --progress --verbose -e 'ssh' ./build/html/* ../doc-html/