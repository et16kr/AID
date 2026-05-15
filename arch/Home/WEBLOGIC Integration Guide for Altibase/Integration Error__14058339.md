---
title: "Integration Error"
page_id: "14058339"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Integration+Error"
updated_at: "2025-09-24T09:11:18.000+0900"
version: 4
ancestors: ["Home", "WEBLOGIC Integration Guide for Altibase"]
labels: []
---

# Integration Error
Source: https://docs.altibase.com/display/arch/Integration+Error
Updated: 2025-09-24T09:11:18.000+0900

- [Cannot load driver](#IntegrationError-Cannotloaddriver) - [Can not make a database connection to the given URL / Invalid Altibase URL (No suitable driver)](#IntegrationError-CannotmakeadatabaseconnectiontothegivenURL/InvalidAltibaseURL(Nosuitabledriver)) - [Could not create pool connection](#IntegrationError-Couldnotcreatepoolconnection) - [Client unable to establish connection / Communication link failure](#IntegrationError-Clientunabletoestablishconnection/Communicationlinkfailure) - [Hang phenomenon](#IntegrationError-Hangphenomenon)

## Cannot load driver

This occurs when attempting to connect without the JDBC driver set up normally.

Refer to "How to set the JDBC Driver to be used in WebLogic."

## Can not make a database connection to the given URL / Invalid Altibase URL (No suitable driver)

If there is an error in the connection URL as below, an error occurs.

- Incorrect format, typo
- When JDBC item is set to a name other than "Altibase" (In this case, no suitable driver may occur depending on the version.)

```
jdbc:otherDBMS://127.0.0.1:20300/mydb
```

## Could not create pool connection

This occurs when there is an error in the connection pool configuration when creating a JDBC data source. There are various cases, but typical cases are as follows.

- When the connection target is ALTIBASE 4, the user to access in the form of "user=sys" must be entered in the property.

## Client unable to establish connection / Communication link failure

In the following cases, a client unable to establish a connection error occurs. (Communication link failure may occur depending on the version.)

- ALTIBASE server is not running
- If the connection is impossible because the IP address or port number of the ALTIBASE server is incorrectly set in the connection URL

The following is an example of the case where the IP address of the ALTIBASE server to be integrated is 192.168.1.81 and the port number is 20300, and it is incorrectly specified as a different value.

```
jdbc:Altibase://192.168.1.80:20800/mydb
```

## Hang phenomenon

If the user tries to connect while the ALTIBASE JDBC driver and the CM protocol version of the ALTIBASE server are different, a phenomenon such as hang may occur depending on the WebLogic version.

When this happens, most of the WebLogic server instances have to be restarted, so caution is required in advance.

For related information, refer to How to Check the ALTIBASE JDBC Driver Version.
