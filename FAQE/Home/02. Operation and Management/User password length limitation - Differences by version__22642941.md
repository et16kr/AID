---
title: "User password length limitation - Differences by version"
page_id: "22642941"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/User+password+length+limitation+-+Differences+by+version"
updated_at: "2025-10-20T15:22:10.000+0900"
version: 1
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# User password length limitation - Differences by version
Source: https://docs.altibase.com/display/FAQE/User+password+length+limitation+-+Differences+by+version
Updated: 2025-10-20T15:22:10.000+0900

- [Overview](#Userpasswordlengthlimitation-Differencesbyversion-Overview) - [Version changed from no limit to 8 digits](#Userpasswordlengthlimitation-Differencesbyversion-Versionchangedfromnolimitto8digits) - [Password length changed from 8 digits to 16 digits](#Userpasswordlengthlimitation-Differencesbyversion-Passwordlengthchangedfrom8digitsto16digits) - [Password length changed from 16 digits to 40 digits](#Userpasswordlengthlimitation-Differencesbyversion-Passwordlengthchangedfrom16digitsto40digits)

# Overview

---

This section summarizes the restrictions on the length of database user passwords that differ depending on the ALTIBASE HDB server version.

## Version changed from no limit to 8 digits

---

There is no length limit when setting a user password, but in ALTIBASE HDB, only 8 digits of the entered password are cut and saved.

This part was confusing to the users, so from the version below it has been changed to limit the password length to fit the actual structure.

- **Applied versions**
  ALTIBASE HDB 4.3.9.200
  ALTIBASE HDB 5.1.5.98
  ALTIBASE HDB 5.3.3.62
  ALTIBASE HDB 5.3.5.25
  ALTIBASE HDB 5.5.1.2.10
  ALTIBASE HDB 6.1.1.0.0
- Difference in password length by platform
  Windows, Solaris(sparc, x86) : 11byte
  Other platforms: 8byte

## Password length changed from 8 digits to 16 digits

---

As the length of the password is limited to 8 digits, the length of the password has been doubled to reflect the opinion that the length is short.

- **Applied versions**
  ALTIBASE HDB 4.3.9.221
  ALTIBASE HDB 5.3.3.89
  ALTIBASE HDB 5.5.1.5.1
  ALTIBASE HDB 6.1.1.1.5
  ALTIBASE HDB 6.3.1

- **Difference in password length by platform**
  Windows, solaris(sparc, x86) : 22byte
  Other platforms: 8byte

## Password length changed from 16 digits to 40 digits

---

To meet higher security requirements from customers and to encourage the use of strong passwords, the password length has been increased from the previous 16 characters to 40 characters.

- **Applied versions**
  ALTIBASE HDB 6.5.1
  ALTIBASE HDB 7.1
  ALTIBASE HDB 7.3
- **Difference in password length by platform**
  Windows : 40byte

The increase in password length was reflected by the addition of the 'Password Policy Function'. **ALTIBASE HDB versions 5.1.5 and 5.3.5** do not reflect this function, so there is no change in the password length. (No change after change to 8 digits)

Password Policy Function

- When login fails for the set number of times, the account is set to LOCK.
- Function to set the period when the account is changed to the OPEN state after the account is locked
- Function to set the Account password expiration date
- Function to set a grace period for a certain period after the account expires
- Function to set the password reuse number and date
- Function to verify the password

**Version with password policy function applied**

- ALTIBASE HDB 4.3.9.211
- ALTIBASE HDB 5.3.3.89
- ALTIBASE HDB 5.5.1.5.1
- ALTIBASE HDB 6.1.1.2.1
- ALTIBASE HDB 6.3.1
- ALTIBASE HDB 6.5.1
- ALTIBASE HDB 7.1
- ALTIBASE HDB 7.3
