# Network Incident – Routing Loop

## Incident ID
NET-004

## Title
Intermittent Network Outages Due to Routing Loop

## Severity
Critical

## Environment
- Network: 3 Cisco Layer 3 Switches, 2 Routers
- Routing Protocol: OSPF
- Users Affected: Entire office (~80 users)
- Services: File Server, Email, ERP, Internet Access

## Description
Users reported intermittent network outages and slow connectivity.
Ping to default gateway sometimes succeeded, sometimes failed.

## Impact
- Users experienced packet loss and high latency  
- Critical applications disrupted intermittently  
- Monitoring systems alerted multiple network faults

## Detection Method
- Network monitoring tool: abnormal routing table changes  
- Packet capture showed looping packets between routers

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 09:00 | Checked routing tables | Duplicate routes detected |
| 09:15 | Reviewed OSPF neighbors | Misconfigured router advertising wrong network |
| 09:30 | Isolated problematic router | Loop stopped temporarily |
| 09:40 | Corrected OSPF configuration | Stable routing restored |
| 09:50 | Monitored network | No further routing loops |

## Root Cause Analysis
A router was misconfigured to advertise a network it should not, causing OSPF to form a routing loop.

## Resolution
1. Corrected OSPF advertisement on misconfigured router  
2. Verified routing tables on all routers  
3. Monitored network for stability  
4. Documented incident for future reference

## Recovery Verification
- Packet loss resolved  
- Routing tables stable  
- Users confirmed normal network performance

## Preventive Actions
- Implement change control for router configuration  
- Regularly audit OSPF advertisements  
- Enable alerts for routing inconsistencies

## Lessons Learned
- Misconfigurations in routing protocols can cause severe network outages  
- Monitoring and documentation are critical for early detection
