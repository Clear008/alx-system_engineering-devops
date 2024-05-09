# Postmortem: File Storage System Outage

## Issue Summary:
- **Duration:** The outage occurred from 8:00 PM to 1:00 AM on June 12th, 2024 (UTC timezone).
- **Impact:** The service affected was our file storage system, leading to users experiencing difficulties uploading and accessing files. Approximately 46% of users were unable to utilize file storage services during the outage.
- **Root Cause:** The root cause of the issue was identified as a misconfiguration in the network routing tables, causing traffic to be routed to an incorrect destination.

## Timeline:
- **8:00 PM:** The issue was detected through an increase in error rates and user complaints related to file uploads.
- **8:15 PM:** Engineering team initiated investigation into the root cause of the issue.
- **8:30 PM:** Initial focus was on analyzing network traffic patterns and server logs.
- **9:00 PM:** Assumptions were made about potential server overload issues.
- **9:30 PM:** Misleading investigation efforts led to temporary server restarts, which did not resolve the issue.
- **10:00 PM:** The incident was escalated to the network infrastructure team for further analysis.
- **11:00 PM:** Network administrators identified the misconfigured routing tables causing traffic redirection.
- **12:00 AM:** The routing tables were corrected, restoring normal functionality to the file storage system.

## Root Cause and Resolution:
- The issue stemmed from a misconfiguration in the network routing tables, causing traffic to be directed to an incorrect destination.
- To resolve the issue, the misconfigured routing tables were corrected, ensuring proper routing of network traffic to the file storage system.

## Corrective and Preventative Measures:
- **Improvements/Fixes:** 
  - Implement regular audits of network configurations to identify and address potential misconfigurations.
  - Enhance communication and coordination between network and infrastructure teams to expedite issue resolution.
- **Tasks to Address the Issue:** 
  - Develop automated checks to monitor network routing table configurations and alert for any discrepancies.
  - Conduct training sessions for network administrators to ensure awareness of best practices for network configuration management.
  - Review incident response procedures to streamline escalation and resolution processes for similar issues in the future.

In summary, the outage was caused by a misconfiguration in the network routing tables, which was promptly resolved by correcting the routing table settings. Implementing automated monitoring and enhancing communication between teams will help prevent similar issues and ensure uninterrupted service delivery to our users.

