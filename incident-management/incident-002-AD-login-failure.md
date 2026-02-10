# Incident Report

## Incident ID
INC-002

## Title
Active Directory User Login Failure

## Severity
High

## Environment
- Operating System: Windows Server 2019
- Domain: CORP.LOCAL
- Users Affected: 50+ users
- Services: AD-integrated authentication, Exchange, File Server

## Description
Multiple users reported inability to log in to domain accounts.
Some users could authenticate on cached credentials, but domain resources were inaccessible.

## Impact
- Users could not access email or shared drives
- Workflow disruption for ~50 users
- Potential delay in critical business operations

## Detection Method
- User reports via ticket system
- Monitoring tool alert: AD replication errors

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 08:30 | Checked AD Event Viewer | Multiple replication errors (Event ID 1311) |
| 08:40 | Pinged Domain Controllers | All reachable |
| 08:50 | Checked SYSVOL & NTDS directories | Permissions intact, disk space OK |
| 09:00 | Reviewed recent changes | Group Policy update applied 1 hour before |
| 09:10 | Forced AD replication | Errors cleared |
| 09:20 | Users tested login | Successful login restored |

## Root Cause Analysis
A recent Group Policy update caused replication delay between Domain Controllers,
resulting in temporary authentication failures.

## Resolution
1. Forced replication using repadmin /syncall /AdeP  
2. Verified replication status with repadmin /showrepl  
3. Ensured all Domain Controllers were synchronized  
4. Communicated resolution to affected users

## Recovery Verification
- AD replication healthy (repadmin /replsummary)  
- All affected users able to log in  
- Ticket system confirmed incident closure

## Preventive Actions
- Schedule AD replication health check scripts  
- Test Group Policy changes in a staging environment before production  
- Enable monitoring alerts for replication failures

## Lessons Learned
- Always validate AD replication after major changes  
- Replication issues can silently block authentication
