---
title: "Altibase ODBC Development Guide in Windows Environment"
page_id: "15138911"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+ODBC+Development+Guide+in+Windows+Environment"
updated_at: "2021-02-22T14:27:06.000+0900"
version: 5
ancestors: ["Home"]
labels: []
---

# Altibase ODBC Development Guide in Windows Environment
Source: https://docs.altibase.com/display/arch/Altibase+ODBC+Development+Guide+in+Windows+Environment
Updated: 2021-02-22T14:27:06.000+0900

---

- [Overview](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-Overview) - [Altibase ODBC Driver Configuration](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-AltibaseODBCDriverConfiguration) - [Downloading ODBC](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-DownloadingODBC) - [Installing ODBC Driver](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-InstallingODBCDriver) - [ODBC settings in Control Panel](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-ODBCsettingsinControlPanel) - [ODBC Driver Development Guide](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-ODBCDriverDevelopmentGuide) - [ODBC connection string](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-ODBCconnectionstring) - [Visual C++ example source](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-VisualC++examplesource) - [Visual C# example source](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-VisualC#examplesource) - [Visual Basic example source](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-VisualBasicexamplesource) - [Considerations when using LOB](#AltibaseODBCDevelopmentGuideinWindowsEnvironment-ConsiderationswhenusingLOB)

# Overview

---

This document describes how to set up various development tools using the ODBC Driver in Altibase development in the Windows environment.

This document is based on Altibase version 6.5.1 and Windows 10.

**ODBC for Windows is provided only up to Altibase version 6.5.1 and is not provided starting from Altibase version 7.1.0.**

For errors and improvements related to this document, contact the technical support portal or technical support center.

- Technical support portal: [http://support.altibase.com](http://support.altibase.com/) -> Technical Knowledge -> Q&A
- Technical support center: 02-2082-1114

# Altibase ODBC Driver Configuration

---

Before development, the ODBC Driver provided by Altibase must be installed. It can be downloaded from [http://support.altibase.com](http://support.altibase.com/).

## Downloading ODBC

---

Go to [http://support.altibase.com](http://support.altibase.com/), then "Downloads" -> "Products" to download Windows ODBC files for each version. Windows ODBC is supported up to Altibase version 6.5.1.

For older versions that are not available on the website, contact [support@altibase.com](mailto:support@altibase.com).

![odbc1_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc1_eng.png?api=v2)

![odbc2_eng.png](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc2_eng.png?api=v2)

## Installing ODBC Driver

---

When installing for the first time, download and install the Windows Client package.

Since there is no complicated process when installing the Windows Client package, this document does not describe it separately. The Altibase ODBC installation process is also not complicated.

When installing Windows Client, the ODBC installation screen appears as shown below.

![odbc3.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc3.jpg?api=v2)

## ODBC settings in Control Panel

---

To register Altibase ODBC Driver, click “Start” → “Control Panel” → “Management Tools” → “ODBC Data Source (64-bit)” → “Add”.

![odbc4.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc4.jpg?api=v2)

After clicking "Add", select ALTIBASE_HDB_ODBC_64bit and click "Finish".

![odbc5.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc5.jpg?api=v2)

When the following DB connection setting screen appears, enter the setting value for the connection.

![odbc6.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc6.jpg?api=v2)

| Items | Description | Example |
| --- | --- | --- |
| Windows DSN Name | Name that distinguishes it from other DSN names | SERVER1 |
| Host (name or IP) | IP information where Altibase DB Server is located | 192.168.1.35 |
| Port (default 20300) | Altibase DB Server connection port information | 20300 |
| User | Account on DB | sys |
| Password | DB account password | manager |
| DB Name | DB_NAME created at the time of DB creation | mydb |
| NLS_USE | DB character set | MS949 |

Click the "Test Connection" button after entering each item to check the connection to Altibase through the ODBC Driver. The Altibase DB Server must be running.

If this is properly set, the user can check the newly added ODBC items as follows.

![odbc7.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20ODBC%20Development%20Guide%20in%20Windows%20Environment/odbc7.jpg?api=v2)

# ODBC Driver Development Guide

---

When connecting to the Altibase DB server with ODBC driver, separate source conversion is not required, and ODBC connection strings need to be changed in the connection part.

Compile by using the appropriate header files (for example, `windows.h`, `sql.h`, `sqlext.h`, `afxdb.h`) and libraries (for example, `odbc32.lib`) required to integrate the ODBC driver on Windows.

## ODBC connection string

---

In a program using the ODBC Driver, the connection string is used as follows.

The keyword parts of the connection string are fixed, and the connection values should be changed according to the target Altibase DB Server connection information and ODBC version.

|  |  |
| --- | --- |
| **DRIVER=ALTIBASE_HDB_ODBC_64bit;user=sys;password=manager; Server=127.0.0.1;PORT=20300;NLS_USE=MS949;LongDataCompat=on** |  |
| Driver | Altibase Driver name checked in ODBC management tool |
| User | User account on DB |
| Password | DB account password |
| Server | IP information where Altibase DB Server is located. |
| Port | Altibase DB Server connection port information |
| NLS_USE | DB character set |
| LongDataCompat | ON / OFF (Set to ON when using large data such as BLOB) |

## Visual C++ example source

---

A simple connection example in Visual C++ is as follows.

**Visual C++ example source**

```
#include <Afx.h>
#include <Afxdb.h>
#include "stdafx.h"
int _tmain(int argc, _TCHAR* argv[])
{
    CDatabase db;

    try
    {
        db.OpenEx(_T("ODBC connection string”), CDatabase::noOdbcDialog);
        AfxMessageBox (_T("Connect OK"));
    }catch (CDBException *e)
    {
        AfxMessageBox(e->m_strError);
    }
    return 0;
}
```

## Visual C# example source

---

A simple connection example in Visual C# is as follows.

**Visual C# example source**

```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Data.Odbc;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            OdbcConnection cn = new OdbcConnection();

            try
                cn.ConnectionString = “ODBC connection string”;
                cn.Open();
                Console.WriteLine("connect ok");
            }
            catch (OdbcException ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.ReadLine();
        }
    }
}
```

## Visual Basic example source

---

A simple connection example in Visual Basic is as follows. In the example below, it is implemented as a source that connects to a DB and gets the current date and time. (The same applies when using ADO objects).

**Visual Basic example source**

```
Sub Main()
    Dim cn As Odbc.OdbcConnection
    Dim cmd As Odbc.OdbcCommand
    Dim dr As Odbc.OdbcDataReader

    cn = New Odbc.OdbcConnection
    cmd = New Odbc.OdbcCommand

    cn.ConnectionString = “ODBC connection string”

    Try
        cn.Open()
        Console.WriteLine("Successfully connected.")
        cmd.Connection = cn

        cmd.CommandText = "SELECT TO_CHAR(SYSDATE,'YYYY-MM-DD HH:MI:SS')FROM DUAL"

        dr = cmd.ExecuteReader()
        While (dr.Read())
            Console.WriteLine(dr.GetString(0))
        End While
    Catch ex As Odbc.OdbcException
        Console.WriteLine("Error in the connection" + ex.Message)
    End Try

    Console.ReadLine()
End Sub
```

## Considerations when using LOB

---

In the case of Altibase, if LOB data type is used, it can be used after changing the connection information to Non-AutoCommit.

If not, NULL for LOB data type is brought when retrieving, or the following error occurs when insert/update time.

```
Connection is in autocommit mode. One can not operate on LOB datas with autocommit mode on.
```

With the following example of C# source, the user can see the process of inserting/selecting a BLOB data type into a table.

The example of BLOB insert is an example of changing the connection information to Non-AutoCommit and inserting data as described above while the DB is connected.

The used “blob” variable is declared as Byte[] type.

The example of BLOB select is an example that declares a Byte[] variable through a function called BINARY_LENGTH provided by Altibase to find out the length of a BLOB data type, saves data in the variable, and creates a file.

**Example of BLOB insert**

```
// BLOB INSERT
FileStream fs = new FileStream("c:\\test.dat", FileMode.Open, FileAccess.Read);

Byte[] blob = new byte[fs.Length];
fs.Read(blob, 0, System.Convert.ToInt32(fs.Length));
fs.Close();
OdbcTransaction tx = cn.BeginTransaction();
cmd.Transaction = tx;
cmd.CommandText = "INSERT INTO T1 (C1, C2) VALUES (?, ?)";
cmd.Parameters.Add("C1", OdbcType.Int);
cmd.Parameters.Add("C2", OdbcType.Binary);
cmd.Parameters[0].Value = 1;
cmd.Parameters[1].Value = blob;
cmd.ExecuteNonQuery();
tx.Commit();
```

**Example of BLOB select**

```
// BLOB SELECT
cmd.CommandText = "SELECT binary_length(C2), C2 FROM T1";
tx = cn.BeginTransaction();
cmd.Transaction = tx;
OdbcDataReader dr = cmd.ExecuteReader();
int len;
while (dr.Read())
{
    len = dr.GetInt32(0);
    Byte[] ff = new Byte[len];
    dr.GetBytes(1, 0, ff, 0, len);

    fs = new FileStream("c:\\test.dat", FileMode.CreateNew, FileAccess.Write);
    fs.Write(ff, 0, len);
    fs.Close();
}
```

# Korean Source Attachments

The Korean source page also references these downloadable source attachments. They are preserved here so the English document set does not lose those references.

- [Korean source attachment 1 (PDF)](https://docs.altibase.com/download/attachments/13436856/ALTIBASE_Windows_ODBC_%EA%B0%9C%EB%B0%9C%EA%B0%80%EC%9D%B4%EB%93%9C.pdf?version=1&modificationDate=1698199482000&api=v2)
