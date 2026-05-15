---
title: "Detailed procedure for changing character set"
page_id: "16876045"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/display/FAQE/Detailed+procedure+for+changing+character+set"
updated_at: "2021-03-15T16:07:20.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Detailed procedure for changing character set
Source: https://docs.altibase.com/display/FAQE/Detailed+procedure+for+changing+character+set
Updated: 2021-03-15T16:07:20.000+0900

### - [Overview](#Detailedprocedureforchangingcharacterset-Overview) - [Version](#Detailedprocedureforchangingcharacterset-Version) - [Change procedure](#Detailedprocedureforchangingcharacterset-Changeprocedure) - [Summary of change procedure](#Detailedprocedureforchangingcharacterset-Summaryofchangeprocedure) - [Details of change procedure](#Detailedprocedureforchangingcharacterset-Detailsofchangeprocedure) - [STEP 1: Download the entire schema of the database using the database export tool.](#Detailedprocedureforchangingcharacterset-STEP1:Downloadtheentireschemaofthedatabaseusingthedatabaseexporttool.) - [STEP 2: Download the database data in the current DB character set. Example) KSC5601](#Detailedprocedureforchangingcharacterset-STEP2:DownloadthedatabasedatainthecurrentDBcharacterset.Example)KSC5601) - [STEP 3: Delete the database and create a new database with the character set setting the user wants to change. Example) UTF8](#Detailedprocedureforchangingcharacterset-STEP3:Deletethedatabaseandcreateanewdatabasewiththecharactersetsettingtheuserwantstochange.Example)UTF8) - [STEP 4: Use the schema information downloaded from STEP1 to configure the schema in the newly created DB.](#Detailedprocedureforchangingcharacterset-STEP4:UsetheschemainformationdownloadedfromSTEP1toconfiguretheschemainthenewlycreatedDB.) - [STEP 5: Use the data import tool to upload the data downloaded in STEP2 using the changed character set. Example) UTF8](#Detailedprocedureforchangingcharacterset-STEP5:UsethedataimporttooltouploadthedatadownloadedinSTEP2usingthechangedcharacterset.Example)UTF8)

# Overview

---

The character set of the database is determined by the setting value at database creation time and cannot be changed later. To change it, delete the database and create a new one.

When the database is deleted, all objects and data disappear. Therefore, the necessary data must be backed up and re-imported after recreating the database.

This document assumes and describes a situation where the database character set is changed while preserving the necessary data.

# Version

---

This document applies to ALTIBASE HDB version 5.3.1 or later, which supports multiple languages.

# Change procedure

---

## Summary of change procedure

---

In summary, the change procedure proceeds in the following steps.

- STEP 1: Download the entire schema of the database using the database export tool.
- STEP 2: Download the database data in the current DB character set. Example) KSC5601
- STEP 3: Delete the database and create a new database with the character set setting the user wants to change. Example) UTF8
- STEP 4: Use the schema information downloaded from STEP1 to configure the schema in the newly created DB.
- STEP 5: Use the data import tool to upload the data downloaded in STEP2 using the changed character set. Example) UTF8

## Details of change procedure

---

The detailed change procedure proceeds in the following steps. This is an explanation of the procedure for changing the character set of the DB whose current DB character set is US7ASCII to MS949.

### STEP 1: Download the entire schema of the database using the database export tool.

#1.1 Set the same client character set as the current DB as an environment variable.

$ export ALTIBASE_NLS_USE=US7ASCII

#1.2 Check the current DB character set and client character set.

iSQL> set vertical on;

iSQL> select * from v$nls_parameters;

SESSION_ID : 1

**NLS_USE : US7ASCII <--- client character set**

**NLS_CHARACTERSET : ASCII <--- database character set**

NLS_NCHAR_CHARACTERSET : UTF16

NLS_COMP : BINARY

NLS_NCHAR_CONV_EXCP : FALSE

NLS_NCHAR_LITERAL_REPLACE : FALSE

#1.3 Download the schema using the aexport tool.

$ aexport

### STEP 2: Download the database data in the current DB character set. Example) KSC5601

#2.1 Set the same client character set as the current DB in an environment variable.

$ export ALTIBASE_NLS_USE=US7ASCII

#2.2 Create formout script and data export script in run_il_out.sh created by aexport in STEP1.

iSQL> create table hangul_t (c1 char(500));

iSQL> insert into hangul_t values('US7ASII_한글테스트합니다');

iSQL> select * from hangul_t;

C1 : US7ASII_한글테스트합니다

$ cat run_il_out.sh | grep formout > formout.sh

$ cat run_il_out.sh | grep 'out -f' > dataout.sh

#2.3 Create a formout script and check whether `NLS_USE` in the form script uses the same character set as the DB.

$ sh formout.sh

$ cat *.fmt

table HANGUL_T

{

"C1" char (500);

}

**DATA_NLS_USE=US7ASCII**

#2.4 Execute the script created in step 2.2 to download the data as a file and check the Hangul data to see if Hangul is normally included.

$ sh dataout.sh

$ cat *.dat

"한글 데이터입니다"

### STEP 3: Delete the database and create a new database with the character set setting the user wants to change. Example) UTF8

#3.1 Delete the database.

$ server stop

$ cd $ALTIBASE_HOME

$ rm dbs/*

$ rm logs/*

#3.2 Create a DB with a new character set.

$ export ALTIBASE_NLS_USE=MS949

$ server create MS949 UTF16

#3.3 Check the DB character set.

iSQL> set vertical on;

iSQL> select * from v$nls_parameters;

SESSION_ID : 1

**NLS_USE : MS949**

**NLS_CHARACTERSET : MS949**

NLS_NCHAR_CHARACTERSET : UTF16

NLS_COMP : BINARY

NLS_NCHAR_CONV_EXCP : FALSE

NLS_NCHAR_LITERAL_REPLACE : FALSE

### STEP 4: Use the schema information downloaded from STEP1 to configure the schema in the newly created DB.

#4.1 Execute the schema creation shell script created by aexport and check whether the schema has been successfully created.

$ sh run_is.sh

iSQL> select * from tab;

### STEP 5: Use the data import tool to upload the data downloaded in STEP2 using the changed character set. Example) UTF8

#5.1 Change the NLS_USE setting in the form file created in STEP 2.2 to a new character set.

$ export ALTIBASE_NLS_USE=MS949

$ cat *.fmt

table HANGUL_T

{

"C1" char (500);

}

**DATA_NLS_USE=MS949**

#5.2 Execute a shell script that imports the data created by aexport and upload the data to the table.

$ sh run_il_in.sh

#5.3 Check the table containing Korean characters to see if the data has been uploaded normally.

iSQL> select * from v$nls_parameters;

SESSION_ID : 1

**NLS_USE : MS949**

**NLS_CHARACTERSET : MS949**

NLS_NCHAR_CHARACTERSET : UTF16

NLS_COMP : BINARY

NLS_NCHAR_CONV_EXCP : FALSE

NLS_NCHAR_LITERAL_REPLACE : FALSE

iSQL> select * from hangul_t;

C1 : US7ASII_한글테스트합니다 .
