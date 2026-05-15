---
title: "ERR-51067 Neither PORT_NO in the connection string or ALTIBASE_PORT_NO environment variable are set"
page_id: "7340767"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-51067+Neither+PORT_NO+in+the+connection+string+or+ALTIBASE_PORT_NO+environment+variable+are+set"
updated_at: "2014-11-27T17:51:23.000+0900"
version: 4
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-51067 Neither PORT_NO in the connection string or ALTIBASE_PORT_NO environment variable are set
Source: https://docs.altibase.com/display/FAQE/ERR-51067+Neither+PORT_NO+in+the+connection+string+or+ALTIBASE_PORT_NO+environment+variable+are+set
Updated: 2014-11-27T17:51:23.000+0900

- [Version](#ERR-51067NeitherPORT_NOintheconnectionstringorALTIBASE_PORT_NOenvironmentvariableareset-Version)
- [Explanation](#ERR-51067NeitherPORT_NOintheconnectionstringorALTIBASE_PORT_NOenvironmentvariableareset-Explanation)
- [Cause](#ERR-51067NeitherPORT_NOintheconnectionstringorALTIBASE_PORT_NOenvironmentvariableareset-Cause)
- [Action](#ERR-51067NeitherPORT_NOintheconnectionstringorALTIBASE_PORT_NOenvironmentvariableareset-Action)
- [Reference](#ERR-51067NeitherPORT_NOintheconnectionstringorALTIBASE_PORT_NOenvironmentvariableareset-Reference)

## Version

All versions

## Explanation

Unable to connect to the server.

## Cause

This error message is output if ALTIBASE_PORT_NO was not set at installation or the altibase.properties file cannot be opened.

## Action

1. Check whether ALTIBASE_PORT_NO is properly set within the altibase.properties file.

2. Check the permissions of the altibase.properties file or the directory in which the file exists.

## Reference

N/A
