# Network Incident – VLAN Misconfiguration

## Incident ID
NET-001

## Title
VLAN Misconfiguration Causing Inter-Office Connectivity Loss

## Severity
High

## Environment
- Network: 3 switches (Cisco Catalyst 2960)
- VLANs: 10 (Sales), 20 (HR), 30 (IT)
- Users Affected: ~60 users
- Services: File Server, Email, ERP system

## Description
Users in Sales VLAN unable to communicate with internal resources in IT VLAN.
Ping between VLANs failing, while intra-VLAN communication works.

## Impact
- ERP system inaccessible for Sales department
- Delay in business operations

## Detection Method
- User reports of connectivity issues
- Network monitoring alert for VLAN 10 traffic

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 09:00 | Checked switch VLAN configuration | VLAN 10 not assigned on Switch 2 |
| 09:15 | Verified trunk ports | Allowed VLAN 10 missing on trunk to Switch 2 |
| 09:30 | Reconfigured VLAN assignment & trunk | Communication restored |
| 09:40 | Tested ping between VLANs | Successful |

## Root Cause Analysis
Misconfiguration on Switch 2:  
- VLAN 10 missing from VLAN assignment  
- Trunk ports did not allow VLAN 10

## Resolution
1. Add VLAN 10 to Switch 2 VLAN database  
2. Configure trunk ports to allow VLAN 10  
3. Verified connectivity for all affected users

## Recovery Verification
- Ping test successful across VLANs  
- Users confirmed access to ERP system

## Preventive Actions
- Document VLAN assignments per switch  
- Implement configuration templates for new VLANs  
- Enable monitoring alerts for VLAN connectivity

## Lessons Learned
- VLAN misconfiguration can silently block critical services  
- Standardized configuration reduces human errors
