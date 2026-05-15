---
title: "ERR-9102B utERR_ABORT_Token_Value_Range_Error Token value length overflow. Maximum token length=0%d. Column =1%s, Value=2%s"
page_id: "7340231"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=7340231"
updated_at: "2014-10-28T10:16:56.000+0900"
version: 3
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-9102B utERR_ABORT_Token_Value_Range_Error Token value length overflow. Maximum token length=0%d. Column =1%s, Value=2%s
Source: https://docs.altibase.com/pages/viewpage.action?pageId=7340231
Updated: 2014-10-28T10:16:56.000+0900

- [Version](#ERR-9102ButERR_ABORT_Token_Value_Range_ErrorTokenvaluelengthoverflow.Maximumtokenlength=0%d.Column=1%s,Value=2%s-Version)
- [Explanation](#ERR-9102ButERR_ABORT_Token_Value_Range_ErrorTokenvaluelengthoverflow.Maximumtokenlength=0%d.Column=1%s,Value=2%s-Explanation)
- [Cause](#ERR-9102ButERR_ABORT_Token_Value_Range_ErrorTokenvaluelengthoverflow.Maximumtokenlength=0%d.Column=1%s,Value=2%s-Cause)
- [Action](#ERR-9102ButERR_ABORT_Token_Value_Range_ErrorTokenvaluelengthoverflow.Maximumtokenlength=0%d.Column=1%s,Value=2%s-Action)
- [Reference](#ERR-9102ButERR_ABORT_Token_Value_Range_ErrorTokenvaluelengthoverflow.Maximumtokenlength=0%d.Column=1%s,Value=2%s-Reference)

## Version

All versions

## Explanation

Unable to execute iLoader.

## Cause

This error occurs when the uploaded data length in iLoader is bigger than the table column size.

## Action

1. Check the datafile that the iLoader reads and check whether there is data bigger than the table column which is about to be uploaded.

2. Check whether the delimiter of the row and column are configured properly.

## Reference

N/A
