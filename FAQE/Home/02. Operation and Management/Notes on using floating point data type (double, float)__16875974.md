---
title: "Notes on using floating point data type (double, float)"
page_id: "16875974"
space_key: "FAQE"
space_name: "FAQ(English)"
source_url: "https://docs.altibase.com/pages/viewpage.action?pageId=16875974"
updated_at: "2021-04-02T11:24:53.000+0900"
version: 2
ancestors: ["Home", "02. Operation and Management"]
labels: []
---

# Notes on using floating point data type (double, float)
Source: https://docs.altibase.com/pages/viewpage.action?pageId=16875974
Updated: 2021-04-02T11:24:53.000+0900

- [Notes when using double or float data types](#Notesonusingfloatingpointdatatype(double,float)-Noteswhenusingdoubleorfloatdatatypes) - [Version](#Notesonusingfloatingpointdatatype(double,float)-Version) - [Example of truncated double numeric value](#Notesonusingfloatingpointdatatype(double,float)-Exampleoftruncateddoublenumericvalue) - [Phenomenon that the value is truncated in iSQL](#Notesonusingfloatingpointdatatype(double,float)-PhenomenonthatthevalueistruncatediniSQL) - [When data is exported from iLoader](#Notesonusingfloatingpointdatatype(double,float)-WhendataisexportedfromiLoader) - [When it comes to a double type host variable from a program, it is normally retrieved.](#Notesonusingfloatingpointdatatype(double,float)-Whenitcomestoadoubletypehostvariablefromaprogram,itisnormallyretrieved.) - [Same phenomenon in Oracle sqlplus](#Notesonusingfloatingpointdatatype(double,float)-SamephenomenoninOraclesqlplus) - [Solution](#Notesonusingfloatingpointdatatype(double,float)-Solution)

# Notes when using double or float data types

---

Altibase's double data type is the same as the C language's double data type. While the double data type can represent a wider range of numbers than the fixed-point method, the value may be inaccurate because it is expressed as an approximate value, and meaningless values after the decimal point may be too long.

In addition, when double/float type values are retrieved with iSQL or exported with iloader, the values after the decimal point may be truncated.

Therefore, in order to accurately retrieve or store values below the decimal point, a fixed-point number type such as numeric must be used.

# Version

---

This is the same for all Altibase versions.

# Example of truncated double numeric value

### Phenomenon that the value is truncated in iSQL

iSQL> create table t1 ( c1 double ); Create success.

iSQL> desc t1; [ TABLESPACE : SYS_TBS_MEM_DATA ] [ ATTRIBUTE ] ------------------------------------------------------------------------------ NAME TYPE IS NULL ------------------------------------------------------------------------------ C1 DOUBLE FIXED

iSQL> insert into t1 values ( double'100.00000000000001421085471520200372'); <-- Enter the number with the long decimal point of the double type in the double column. 1 row inserted.

iSQL> select c1, to_char(c1) from t1; C1 TO_CHAR(C1) -------------------------------------------------------------------------------------------- 100 100 <--- Retrieve because the value below the decimal point is truncated

iSQL>

iSQL> select * from t1 where c1 = 100.00000000000001421085471520200372; <-- The retrieve condition value may not be retrieved because it is truncated. C1 ------------------------- No rows selected.

iSQL> select c1, to_char(c1) from t1 where c1 = double'100.00000000000001421085471520200372'; <-- By casting the retrieve condition value, the desired value can be found. C1 TO_CHAR(C1) -------------------------------------------------------------------------------------------- 100 100 <--- However, the value that is retrieved and output is truncated and expressed. 1 row selected.

### When data is exported from iLoader

$ iloader -s localhost -u SYS -p MANAGER out -f SYS_T1.fmt -d SYS_T1.dat -log SYS_T1.log $ cat SYS_T1.dat 100 <--- The value after the decimal point is truncated in the exported data.

### When it comes to a double type host variable from a program, it is normally retrieved.

/* select.c */ ................... ................... EXEC SQL BEGIN DECLARE SECTION; double c1; // double host variable for select output double ins_c1; // double host variable for insert EXEC SQL END DECLARE SECTION;

ins_c1 = 100.00000000000001421085471520200372;

EXEC SQL INSERT INTO T1 values ( :ins_c1 ); if (sqlca.sqlcode != SQL_SUCCESS) { printf("Error : [%d] %s\n\n", SQLCODE, sqlca.sqlerrm.sqlerrmc);

}

EXEC SQL SELECT C1 INTO :c1 FROM T1 limit1; /* check sqlca.sqlcode */ if (sqlca.sqlcode == SQL_SUCCESS) { printf("c1 = %.32f \n", c1); } ................. ................. shell> ./select ( Execute the program) <SELECT> c1 = 100.00000000000001421085471520200372 <-- Normal value is output.

### Same phenomenon in Oracle sqlplus

As a result of checking, there is a phenomenon that the same value is truncated in the Oracle sqlplus.

[SCOTT@orcl](mailto:SCOTT@orcl)> create table t1 ( c1 binary_double );

Table created.

[SCOTT@orcl](mailto:SCOTT@orcl)> insert into t1 values ( 100.00000000000001421085471520200372 );

1 row created.

[SCOTT@orcl](mailto:SCOTT@orcl)> select c1, to_char(c1) from t1;

C1 TO_CHAR(C1) ---------- ---------------------------------------- 1.0E+002 1.0000000000000001E+002

# Solution

---

In order to accurately retrieve or store values below the decimal point, a fixed-point number type such as numeric(scale, precision) must be used.

The following execution example shows that values are retrieved normally in iSQL when the numeric type is used.

iSQL> create table t2 ( c1 numeric(35, 32 ) ); Create success. iSQL> desc t2; [ TABLESPACE : SYS_TBS_MEM_DATA ] [ ATTRIBUTE ] ------------------------------------------------------------------------------ NAME TYPE IS NULL ------------------------------------------------------------------------------ C1 NUMERIC(35, 32) FIXED

iSQL> insert into t2 values ( 100.00000000000001421085471520200372 ); iSQL> insert into t2 values ( 123.00000000000001421085471520200372 ); iSQL> insert into t2 values ( 100.12345 );

iSQL> select c1, to_char(c1) from t2; <-- In iSQL, to express the value after the decimal point as it is, convert it to char type using the to_char function. C1 TO_CHAR(C1) --------------------------------------------------------------------------------- 100 100.00000000000001421085471520200372 123 123.00000000000001421085471520200372 100.12345 100.12345

iSQL> select c1, to_char(c1) from t2 where c1 = 100.00000000000001421085471520200372; <-- When retrieving by condition value, it can be used without the need for a separate cast. C1 TO_CHAR(C1) --------------------------------------------------------------------------------- 100 100.00000000000001421085471520200372 1 row selected.
