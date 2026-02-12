# Network Incident – VPN Connection Failure

## Incident ID
NET-003

## Title
Remote Users Unable to Connect via VPN

## Severity
Critical

## Environment
- VPN Type: Cisco AnyConnect SSL VPN
- VPN Server: ASA 5506-X
- Users Affected: ~30 remote users
- Network: Internal LAN, Active Directory, File Servers
- Services Impacted: Remote access, Email, ERP system

## Description
Remote users reported failure to establish VPN connection.
Error: “Authentication Failed” despite correct credentials.

## Impact
- Remote workforce could not access critical resources
- Business operations delayed for 30+ users

## Detection Method
- Helpdesk tickets from remote employees
- VPN server monitoring alerts

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 08:00 | Checked VPN server logs | Multiple failed login attempts |
| 08:15 | Verified user accounts in AD | Accounts active |
| 08:30 | Checked VPN licensing | Licenses exhausted |
| 08:40 | Cleared inactive VPN sessions | Some users able to connect |
| 08:50 | Verified VPN group policies | Correct |
| 09:00 | Monitored connection | All remote users connected successfully |

## Root Cause Analysis
- VPN server licenses were fully utilized due to inactive sessions  
- Remote users could not connect until old sessions were cleared

## Resolution
1. Cleared inactive VPN sessions  
2. Verified active connections did not exceed license limit  
3. Communicated resolution to remote users  
4. Implemented monitoring to prevent future license exhaustion

## Recovery Verification
- All affected users successfully connected  
- Monitoring system confirms VPN sessions within limit  
- Tickets closed

## Preventive Actions
- Monitor active VPN sessions and license usage  
- Increase VPN license capacity as company grows  
- Educate users to properly disconnect sessions after use

## Lessons Learned
- VPN license limits can silently block users  
- Proactive monitoring prevents service disruption.
