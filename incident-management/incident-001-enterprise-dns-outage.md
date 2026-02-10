# Incident Report

## Incident ID
INC-001

## Title
Enterprise DNS Service Outage

## Severity
Critical

## Environment
- Operating System: Windows Server 2019
- Servers / Devices: Domain Controller (DC01)
- Network: Internal LAN, AD-integrated DNS
- Users Affected: ~120 users

## Description
Users were unable to access internal and external resources using
hostnames. Direct IP access was functioning normally.

## Impact
- Users could not access email, intranet, or shared resources
- Business operations disrupted for approximately 35 minutes

## Detection Method
- Multiple user reports
- Monitoring system DNS health alert

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 09:05 | Ping internal IP | Successful |
| 09:07 | Ping hostname | Failed |
| 09:10 | nslookup test | Timeout |
| 09:12 | Checked DNS service status | Service stopped |
| 09:15 | Event Viewer review | DNS database corruption detected |

## Root Cause Analysis
An unexpected server reboot caused corruption of the DNS database,
resulting in DNS service failure.

## Resolution
1. Restarted DNS Server service
2. Restored DNS database from last known backup
3. Cleared DNS cache on server
4. Verified name resolution internally and externally

## Recovery Verification
- Successful nslookup queries
- Users confirmed service restoration
- Monitoring system status returned to normal

## Preventive Actions
- Schedule automated DNS backups
- Implement secondary DNS server
- Enable DNS service monitoring alerts

## Lessons Learned
DNS is a critical service and must be protected with redundancy
and proactive monitoring.
