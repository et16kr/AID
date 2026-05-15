---
title: "ERR-01002 Invalid character in use"
page_id: "7340276"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-01002+Invalid+character+in+use"
updated_at: "2014-11-20T15:11:31.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-01002 Invalid character in use
Source: https://docs.altibase.com/display/FAQE/ERR-01002+Invalid+character+in+use
Updated: 2014-11-20T15:11:31.000+0900

- [Version](#ERR-01002Invalidcharacterinuse-Version)
- [Explanation](#ERR-01002Invalidcharacterinuse-Explanation)
- [Cause](#ERR-01002Invalidcharacterinuse-Cause)
- [Action](#ERR-01002Invalidcharacterinuse-Action)
- [Reference](#ERR-01002Invalidcharacterinuse-Reference)

## Version

All versions.

## Explanation

This error is occurs when searching Korean with the LIKE clause.

## Cause

A character beyond the range of the character set is also stored.

## Action

The user is advised to take the following steps:

1. Download the table data using iLoader.

2. Shut down the Altibase server.

3. Change NLS_USE to MS940 from $ALTIBASE_HOME/conf/altibase.properties

4. Start the Altibase server.

5. Truncate the table that has a problem (not DELETE)

6. Upload the data downloaded from (1) using iLoader.

The user is advised to use the same character set that matches the server. For example, use MS949/UTF8 for Korean, rather than KSC5601.

## Reference

N/A
