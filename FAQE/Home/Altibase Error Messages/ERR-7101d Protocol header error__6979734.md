---
title: "ERR-7101d Protocol header error"
page_id: "6979734"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/ERR-7101d+Protocol+header+error"
updated_at: "2014-11-20T15:40:12.000+0900"
version: 25
ancestors: ["Home", "Altibase Error Messages"]
labels: []
---

# ERR-7101d Protocol header error
Source: https://docs.altibase.com/display/FAQE/ERR-7101d+Protocol+header+error
Updated: 2014-11-20T15:40:12.000+0900

- [Version](#ERR-7101dProtocolheadererror-Version)
- [Explanation](#ERR-7101dProtocolheadererror-Explanation)
- [Cause](#ERR-7101dProtocolheadererror-Cause)
- [Action](#ERR-7101dProtocolheadererror-Action)
- [Reference](#ERR-7101dProtocolheadererror-Reference)

## Version

All versions

## Explanation

The client is unable to establish a connection.

The following error message is output to $ALTIBASE_HOME/trc/altibase_boot.log.

ERR-7101d(errno=11) Protocol header error.(TCP 127.0.0.1:60264) Protocol processing failed. Close connection...

## Cause

The following error description can be viewed with the AltiErr utility:

$ altierr 0x7101D 0x7101D ( 462877) cmERR_ABORT_PROTOCOL_HEADER_ERROR Protocol header error.(<0%s>)

# *Cause: Protocol header error

# *Action: Please send a bug report to the vendor.

This error message is written to altibase_boot.log when a client of a version incompatible with the server tried to establish a connection.

This error keeps a message history and does not adversely affect the Altibase server.

## Action

If this error persists, find the client that is attempting to connect, then reinstall it with a version compatible with the server.

## Reference

If this error persists, find the client that is attempting to connect and reinstall it with a version compatible with the server.

- For ALTIBASE HDB 5.3.1 or below, the cm protocol version of the server and client must be identical for the client to connect to the server.
- For ALTIBASE HDB 5.3.3 or above, backward compatibility for the server and client is supported. The client can connect to a server of the same or newer version regardless of its cm protocol version whereas, connection fails if the client is of a newer version than the server.
- In this context, the first three numbers of a product version are denoted as the version (the fourth and succeeding numbers which indicate the patch versions are irrelevant).

# How to check the server/client version

- Server version
- $ altibase -v version 5.1.5.68 XEON_LINUX_redhat_Enterprise_AS4-64bit-5.1.5.68-release-GCC3.4.6 (xeon-redhat-linux-gnu) Jan 5 2010 21:17:22, binary db version 5.1.2, meta version 5.3.3, cm protocol version 5.4.5, replication protocol version 5.2.1

- Client version
- **5.3.1 or below**

  $ sesc -v SES C/C++ Precompiler 3 Ver 5.1.5.68 XEON_LINUX_redhat_Enterprise_AS4-64bit-5.1.5.68-release-GCC3.4.6 (xeon-redhat-linux-gnu) Jan 5 2010 21:17:22 **5.3.3 or above** $ apre -v Altibase Precompiler2(APRE) Ver.1 6.3.1.0.9 X86_64_LINUX_redhat_Enterprise_ES4-64bit-6.3.1.0.9-release-GCC3.4.6 (x86_64-unknown-linux-gnu) Mar 20 2014 18:19:25

- Using the JDBC driver
- $ java -jar $ALTIBASE_HOME/lib/Altibase.jar JDBC Driver Info : Altibase Ver = 6.3.1.0.9 for JavaVM v1.4, CMP:7.1.1, Mar 20 2014 17:07:25
- Using the ODBC library on Windows
- Altibase Installation Directory (e.g., C:\Program Files (x86)\Altibase\altibase-server-6.3.1) -> lib Directory altiodbc.dll -> Properties -> Details -> Product Version

# Examples of server and client compatibility for different versions

|  | Server Version | Client Version | Result | Remarks |
| --- | --- | --- | --- | --- |
| Server Version > Client Version (5.3.3 or above) | 6.3.1 | 5.3.3 | Succeeds | Backward compatibility is supported for 5.3.3 or above. |
| Server Version > Client Version (5.3.1 or below) | 6.3.1 | 4.3.9 | Fails | Backward compatibility is supported only if the version of both the server and client is 5.3.3 or above. Since the client version is older than 5.3.3, backward compatibility is not supported. For 4.3.9, connection succeeds only if the cm protocol versions are the same. |
| ServerVersion < Client Version | 6.1.1 | 6.3.1 | Fails | If the version of the client is newer than the server, connection fails regardless of the Altibase version. The version of the client must be the same or older than the server. |
