---
title: "ERR-11136 The LogAnchor file already exists"
page_id: "7340099"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-11136+The+LogAnchor+file+already+exists"
updated_at: "2014-11-20T15:38:00.000+0900"
version: 6
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-11136 The LogAnchor file already exists
Source: https://docs.altibase.com/display/FAQE/ERR-11136+The+LogAnchor+file+already+exists
Updated: 2014-11-20T15:38:00.000+0900

- [Version](#ERR-11136TheLogAnchorfilealreadyexists-Version)
- [Explanation](#ERR-11136TheLogAnchorfilealreadyexists-Explanation)
- [Cause](#ERR-11136TheLogAnchorfilealreadyexists-Cause)
- [Action](#ERR-11136TheLogAnchorfilealreadyexists-Action)
- [Reference](#ERR-11136TheLogAnchorfilealreadyexists-Reference)

## Version

All versions

## Explanation

Unable to start server.

## Cause

This error occurs if a database is recreated or recovery is executed on a path that has previously stored a database.This is because the server tries to create duplicate log anchor files from the /logs directory.

## Action

This error message is output when the server is unable to start due to duplicate loganchor files while recreating the database or executing recovery. Check the loganchor files directory and delete unnecessary loganchor files.

## Reference

N/A
