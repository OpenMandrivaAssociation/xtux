#!/bin/sh
curl -s https://xtux.sourceforge.net/download.html |grep xtux-src- |sed -e 's,.*xtux-src-,,;s,\.tar.*,,'
