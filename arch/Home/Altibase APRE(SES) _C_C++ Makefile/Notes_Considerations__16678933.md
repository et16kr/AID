---
title: "Notes/Considerations"
page_id: "16678933"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16678933"
updated_at: "2021-02-22T16:11:13.000+0900"
version: 3
ancestors: ["Home", "Altibase APRE(SES) *C/C++ Makefile"]
labels: []
---

# Notes/Considerations
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16678933
Updated: 2021-02-22T16:11:13.000+0900

---

For the sake of understanding, we have looked at some errors that may occur during the make-process of simple .sc source and how to fix the errors with the Makefile modification. For compile-related problems, it is important to understand what type of problem it is.

When a problem related to compilation occurs, the following items are the items to be checked:

1. Is the correct library being used for the compiler?
2. Are there any errors in the Makefile? (Path, specification, type, variable name use, etc.)
3. Are the compile bits different between libraries or objects?
4. Are you correctly linking the required vendor's library?
5. Are you specifying the required system library?
6. Do you specify a library for compatibility between C/C++?
