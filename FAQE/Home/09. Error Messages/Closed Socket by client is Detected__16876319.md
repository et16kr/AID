---
title: "Closed Socket by client is Detected"
page_id: "16876319"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Closed+Socket+by+client+is+Detected"
updated_at: "2021-03-25T09:15:00.000+0900"
version: 1
ancestors: ["Home", "09. Error Messages"]
labels: []
---

# Closed Socket by client is Detected
Source: https://docs.altibase.com/display/FAQE/Closed+Socket+by+client+is+Detected
Updated: 2021-03-25T09:15:00.000+0900

- [Version](#ClosedSocketbyclientisDetected-Version) - [Symptom](#ClosedSocketbyclientisDetected-Symptom) - [Cause](#ClosedSocketbyclientisDetected-Cause) - [Solution](#ClosedSocketbyclientisDetected-Solution) - [Note/Consideration](#ClosedSocketbyclientisDetected-Note/Consideration)

# Version

---

All the versions

# Symptom

---

The following error message is recorded in altibase_boot.log.

[Notify : Detect] Closed Socket by client is Detected. : Session ID = 7687977

# Cause

---

When the client calls disconnect, the connection (session) is normally terminated between the server and the client.

In addition, if the client terminates the program or the server detects that the connection with the client is disconnected due to a network problem, etc., the above error message is recorded and the session is cleaned up.

# Solution

---

This is not an error message because there is a problem with the server because it records a log and cleans the session for the session that has already been disconnected.

Therefore, it is not necessary to take any action on the Altibase server.

However, check if there was any work such as restarting the application during the time period. If not, please check if there is any problem on the network side.

# Note/Consideration

---

If there was no problem with the service, this error message can be ignored.
