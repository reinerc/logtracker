#!/bin/bash

#
# Count the hours, the computer is on
#

first=$(date +%s --date="$(zcat /var/log/syslog.7.gz | head -1 | awk '{print $1, $2, $3}')")
now=$(date +%s)
(
(for i in /var/log/syslog*.gz; do zcat $i | grep 'CRON\[' | grep hourly | wc -l ; done
cat /var/log/syslog | grep 'CRON\[' | grep hourly | wc -l
cat /var/log/syslog.1 | grep 'CRON\[' | grep hourly | wc -l) | awk '{s+=$1} END {print s}'
(echo $now $first - p  q | dc
 echo '(24 * 3600)') | paste -sd'/' | bc -l  
) | paste -sd'/' | bc -l  
