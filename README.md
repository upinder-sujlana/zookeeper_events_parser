### zookeeper_events_parser

```
Quick script to parse and print out each hyperflex zookeeper event. 
The script just picks up the relevant messages & prints the time in a human readable format along with the description & ID.

e.g.
root@SpringpathControllerXXXXXXX:/tmp# python readzkEvents_ver2.py
Timestamp   :- 2020-01-18 12:17:45
Description :- License is in EVAL mode
Id          :- SmartLicenseEvalEvent
******************************************************************************************

Timestamp   :- 2020-01-18 12:19:09
Description :- Rotational Disk /dev/sdk added to node 192.168.5.143
Id          :- DiskAddedEvent
******************************************************************************************

<snip>
```
