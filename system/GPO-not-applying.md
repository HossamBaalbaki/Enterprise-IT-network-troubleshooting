# System Incident – GPO Not Applying

## Incident ID
SYS-002

## Title
Group Policy Not Applying on Multiple Workstations

## Severity
High

## Environment
- Windows Server 2019 Domain Controller
- Domain: CORP.LOCAL
- Workstations: 50 Windows 10 machines
- Users Affected: Entire Sales Department
- Service Impacted: Security settings, mapped drives, software deployment

## Description
Newly created GPO for password policy and mapped drives was not applying on several workstations.
Affected users could log in, but policies were not enforced.

## Impact
- Security policies not applied  
- Mapped network drives unavailable  
- Software deployment via GPO failed

## Detection Method
- User reports of missing drives and settings  
- gpresult /r command showed GPO not applied  
- Event Viewer logged Group Policy errors (Event ID 1058, 1030)

## Troubleshooting Timeline
| Time | Action | Result |
|------|--------|--------|
| 08:00 | Checked GPO status on DC | GPO exists and linked correctly |
| 08:15 | Ran gpupdate /force on affected machines | No change |
| 08:30 | Checked network connectivity | Machines connected to domain |
| 08:40 | Verified DNS configuration | Correct |
| 08:50 | Checked SYSVOL and NTFRS replication | Missing GPO on some DCs |
| 09:10 | Forced replication | GPO now visible on all DCs |
| 09:20 | Users ran gpupdate /force | Policies applied successfully |

## Root Cause Analysis
- GPO not replicated to all Domain Controllers due to SYSVOL replication delay
- Resulted in some workstations unable to retrieve the policy

## Resolution
1. Verified SYSVOL replication using dfsrdiag and ntfrsutl  
2. Forced replication and verified GPO presence on all DCs  
3. Confirmed successful application on client machines  
4. Communicated resolution to affected users

## Recovery Verification
- gpresult /r confirmed GPO applied on all machines  
- Mapped drives and security policies enforced  
- Event Viewer showed no further errors

## Preventive Actions
- Monitor SYSVOL replication regularly  
- Test GPOs in a staging OU before full deployment  
- Set alerts for replication failures

## Lessons Learned
- GPO failures often relate to replication issues  
- Monitoring replication and testing in small scope avoids business disruption
