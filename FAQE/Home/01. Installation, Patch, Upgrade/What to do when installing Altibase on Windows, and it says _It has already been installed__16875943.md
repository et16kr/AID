---
title: "What to do when installing Altibase on Windows, and it says \"It has already been installed\""
page_id: "16875943"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875943"
updated_at: "2021-03-03T11:08:43.000+0900"
version: 1
ancestors: ["Home", "01. Installation, Patch, Upgrade"]
labels: []
---

# What to do when installing Altibase on Windows, and it says "It has already been installed"
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875943
Updated: 2021-03-03T11:08:43.000+0900

---

# Situation

If the user repeats Altibase installation and uninstallation on Windows, it may not install normally.

As for the error, if the user tries to install the full package, the user will get an error saying that it is already installed. In addition, if the user tries to patch it, it will get an error saying that it cannot be done.

# Solution

The above situation is because the Altibase program registered in the registry has not been deleted normally.

So, the user has to delete the entry from the registry.

Here is how to run the registry: (Windows Start -> Run -> Run regedit.exe)

Below is the item to be deleted.

| Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Altibase Corp., |
| --- |

![altibase_registry.png](https://docs.altibase.com/download/attachments/embedded-page/FAQE/What%20to%20do%20when%20installing%20Altibase%20on%20Windows,%20and%20it%20says%20%22It%20has%20already%20been%20installed%22/altibase_registry.png?api=v2)

After deleting the above item, the registry is cleaned up and the user can proceed with the Altibase installation normally.
