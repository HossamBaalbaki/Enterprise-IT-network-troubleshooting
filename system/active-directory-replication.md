# System Incident – Active Directory Replication Failure

## Incident ID
SYS-001

## Title
AD Replication Failure Between Domain Controllers

## Severity
High

## Environment
- Windows Server 2019
- Domain: CORP.LOCAL
- Domain Controllers: DC01, DC02
- Users Affected: ~100 users
- Services Impacted: Authentication, File Access, Email

## Description
Changes made on DC01 were not replicating to DC02.
New users and password changes were not applied across domain.

## Impact
- Users could not log in using updated credentials
- New accounts unavailable on DC02
- Group Policy changes not applied

## Detection Method
- Event Viewer: 1311 & 2042 errors
- repadmin /showrepl confirmed replication failures

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 08:30 | Checked Event Viewer | Replication errors detected |
| 08:45 | Ran dcdiag | DC02 shows connectivity warning |
| 09:00 | Verified network connectivity | Ping successful |
| 09:15 | Checked DNS settings | Correct |
| 09:30 | Forced replication repadmin /syncall /AdeP | Errors cleared |
| 09:45 | Verified replication | Success on all DCs |

## Root Cause Analysis
Replication failed due to lingering metadata and outdated Kerberos tickets.

## Resolution
1. Cleared lingering objects using repadmin /removelingeringobjects  
2. Forced AD replication repadmin /syncall /AdeP  
3. Verified replication on all DCs  
4. Communicated resolution to IT team

## Recovery Verification
- repadmin /replsummary shows no errors  
- Group Policies applied correctly  
- New users and password changes active

## Preventive Actions
- Schedule AD health checks  
- Monitor replication errors  
- Document all changes to AD

## Lessons Learned
- AD replication issues silently affect authentication  
- Regular monitoring avoids user impact
