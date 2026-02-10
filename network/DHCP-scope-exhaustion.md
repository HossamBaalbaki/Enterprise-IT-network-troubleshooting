# Network Incident – DHCP Scope Exhaustion

## Incident ID
NET-002

## Title
DHCP Scope Exhaustion Causing Network IP Assignment Failures

## Severity
High

## Environment
- Network: 2 Cisco Layer 3 Switches + Windows Server 2019 DHCP
- Scope: 192.168.10.100 - 192.168.10.199
- Users Affected: 50+ users
- Services: Email, File Server, ERP system

## Description
New devices could not obtain IP addresses from DHCP.
Users reported network connectivity issues intermittently.

## Impact
- New devices could not access network resources
- Temporary downtime for 20+ users connecting with new machines
- Productivity slowed for departments onboarding new devices

## Detection Method
- Helpdesk tickets reporting network failure
- DHCP server event log: “No available IP addresses”

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 09:00 | Checked DHCP server scope | Scope fully allocated |
| 09:10 | Ping existing IP addresses | IPs in use |
| 09:15 | Identified inactive leases | 10 expired but not cleared |
| 09:20 | Cleared inactive leases | 5 IPs freed |
| 09:25 | Added additional DHCP range | Users received IPs |
| 09:30 | Verified connectivity | All new devices online |

## Root Cause Analysis
The DHCP scope was too small for the number of devices.
Inactive leases remained in the server, reducing available IPs.

## Resolution
1. Cleared inactive leases  
2. Expanded DHCP scope to accommodate growth  
3. Configured lease duration to 8 hours for guest devices  
4. Verified all devices could obtain IP addresses

## Recovery Verification
- New devices successfully obtained IPs  
- Users confirmed network access  
- Event logs showed no DHCP errors

## Preventive Actions
- Monitor DHCP lease utilization regularly  
- Adjust scope dynamically as network grows  
- Set up alerts for high IP utilization

## Lessons Learned
- Plan DHCP scopes with growth in mind  
- Shorter lease times for temporary devices prevent scope exhaustion
