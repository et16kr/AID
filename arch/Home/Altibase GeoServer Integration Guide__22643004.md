---
title: "Altibase GeoServer Integration Guide"
page_id: "22643004"
space_key: "arch"
space_name: "Technical Documents(English)"
source_url: "https://docs.altibase.com/display/arch/Altibase+GeoServer+Integration+Guide"
updated_at: "2025-10-21T09:04:57.000+0900"
version: 1
ancestors: ["Home"]
labels: []
---

# Altibase GeoServer Integration Guide
Source: https://docs.altibase.com/display/arch/Altibase+GeoServer+Integration+Guide
Updated: 2025-10-21T09:04:57.000+0900

- [Overview](#AltibaseGeoServerIntegrationGuide-Overview) - [GeoServer](#AltibaseGeoServerIntegrationGuide-GeoServer) - [GeoServer Installation and Setup](#AltibaseGeoServerIntegrationGuide-GeoServerInstallationandSetup) - [Integrating GeoServer with Altibase](#AltibaseGeoServerIntegrationGuide-IntegratingGeoServerwithAltibase) - [Spatial Data Import](#AltibaseGeoServerIntegrationGuide-SpatialDataImport) - [Check the registered layer.](#AltibaseGeoServerIntegrationGuide-Checktheregisteredlayer.) - [Reference materials](#AltibaseGeoServerIntegrationGuide-Referencematerials)

# Overview

---

This document provides a guide for integrating GeoServer with Altibase.

This document is based on the following versions:

- Altibase 7.1.0 or higher
- GeoServer 2.16.2 or higher

# GeoServer

---

GeoServer is an open-source GIS software server developed in Java that allows sharing and editing of geospatial data.

As a community-based project, GeoServer is developed, tested, and supported by diverse groups of individuals and organizations worldwide.

GeoServer serves as a reference implementation not only for Web Map Service (WMS) but also for Open Geospatial Consortium (OGC) standards such as Web Feature Service (WFS), Web Coverage Service (WCS), and Web Processing Service (WPS).

GeoServer forms a core component of the Geospatial Web.

## GeoServer Installation and Setup

---

This document is based on installing GeoServer on Windows 10.

1. To install GeoServer, JRE (Java Runtime Environment) must be installed:

- JRE version 8 or higher is recommended.
- You can download and install it from [OpenJDK](https://adoptopenjdk.net/) or [Oracle JRE](https://www.oracle.com/java/technologies/javase-downloads.html).
- After installation, verify the JAVA environment settings.

2. Installing GeoServer:

- Download a stable version from the [GeoServer download site](http://geoserver.org/download/). This document uses version 2.16.2 as the reference.
- Extract the downloaded Zip file to the installation path and configure the environment. Here, GeoServer is installed at `C:\Program Files\GeoServer`. Set the environment variables as follows:

    - `GEOSERVER_HOME = C:\Program Files\GeoServer`
    - `GEOSERVER_DATA_DIR = C:\Program Files\GeoServer\data_dir`

3. To integrate with Altibase, additional libraries need to be installed. Copy the required libraries to `C:\Program Files\GeoServer\webapps\geoserver\WEB-INF\lib`:

- Altibase-specific spatial DBMS driver: [`gt-jdbc-altibase-21-SNAPSHOT.jar`](https://sourceforge.net/projects/gt-jdbc-korean/files/Altibase/)
- JTS Topology Suite: [`jts-1.14.jar`](https://sourceforge.net/projects/jts-topo-suite/files/jts/)
- Altibase JDBC driver: The `Altibase.jar` file can be found in the `lib` directory of your Altibase installation folder.

4. Altibase Spatial module installation and coordinate system setup:

- The spatial module is not installed by default during Altibase installation. Use the following commands to install the spatial module.

```
$ is -f $ALTIBASE_HOME/thirdparty/ArcGIS/geometry_columns.sql
```

- Insert the coordinate system to be used when creating layers into the `spatial_ref_sys` table.

```
$isql
iSQL> INSERT into spatial_ref_sys (srid, auth_name, auth_srid, proj4text, srtext) values ( 4326, 'EPSG', 4326, '+proj=longlat +datum=WGS84 +no_defs ', 'GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0,AUTHORITY["EPSG","8901"]],UNIT["degree",0.0174532925199433,AUTHORITY["EPSG","9122"]],AUTHORITY["EPSG","4326"]]');
```

* More coordinate system information is available in the [`altibase_spatial_ref_sys.sql`](https://github.com/mangosystem/geotools-jdbc-korean/blob/master/jdbc-altibase/altibase_spatial_ref_sys.sql) reference script.

5. Starting GeoServer

- Run the startup.bat file located in the GEOSERVER_HOME directory to start GeoServer.

## Integrating GeoServer with Altibase

---

1. Accessing GeoServer

- Open a browser and go to [http://localhost:8080/geoserver](http://localhost:8080/geoserver)
- Username: admin
- Password: geoserver

![1.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/1.JPG?api=v2)

2. Adding a Store

- Add Altibase as a data store.

![1.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/1.JPG?api=v2)
![2.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/2.JPG?api=v2)
![3.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/3.JPG?api=v2)
![4.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/4.JPG?api=v2)

The required input fields are as follows:

| Item | Description |
| --- | --- |
| Workspace | To publish or register a layer, you must add a workspace. Here, the default workspace "cite" was selected. |
| Data Store Name | Enter the name of the data store. |
| dbtype | Set to "altibase". |
| host | Enter the address of the Altibase server. |
| port | Enter the service port configured in Altibase. The default value is 20300. |
| database | Enter the database name configured in Altibase. The default value is "mydb". |
| schema | Altibase does not manage schemas. |
| user | Enter the Altibase DB account name. |
| password | Enter the Altibase DB account password. |
| preparedStatements | Optional. Not checked for Altibase. |

3. Registering a Layer

- Register a layer in the data store.
- The registered layer is managed as a Table in Altibase.
- Select a layer from the left tree and click “Add New Layer.”

![5.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/5.JPG?api=v2)

- Select the data store where the layer will be created. Here, the data store called ALTIBASE_SPATIAL in the workspace cite was selected.

![6.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/6.JPG?api=v2)

- Click "Create New Feature Type" to create the layer.

![7.jpg](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/7.jpg?api=v2)

- Enter the type name. This name will be used as the table name.
- Click "Add New Attribute Field" to add attribute fields. These attribute fields are defined as columns.

![8.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/8.JPG?api=v2)

- Enter the name. This will be the column name.
- Enter the type. This will be the data type of the column.
- If the data type requires a length, specify the size.
- For geometry types, specify the coordinate system and click the save button.

![9.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/9.JPG?api=v2)

- Review the attribute information and enter the layer’s minimum bounding area. Clicking "Calculate from Data," "Calculate from SRS Extent," or "Calculate from Source Extent" will automatically fill it in.
- Click "Save" to save.

![10.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/10.JPG?api=v2)

## Spatial Data Import

---

You can import a layer using a shapefile.

1. Install the extension plug-in. [Download the importer plug-in](https://sourceforge.net/projects/geoserver/files/GeoServer/2.16.2/extensions/geoserver-2.16.2-importer-plugin.zip/download), unzip it, and copy it to `C:\Program Files\GeoServer\webapps\geoserver\WEB-INF\lib`. Restart GeoServer for the change to take effect.

2. When you access GeoServer, the "Import Data" option will be added.

![11.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/11.JPG?api=v2)

3. Select the spatial file from the data source to import. Currently, Altibase only supports importing spatial files. Click the browse button to select the spatial file.

![12.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/12.JPG?api=v2)

4. Select the directory where the spatial file is located.

![13.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/13.JPG?api=v2)

- Select the workspace and data store, then click the Next button.

![14.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/14.JPG?api=v2)

- Select the spatial data file to import, then click the Import button to complete the import.

![15.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/15.JPG?api=v2)

## Check the registered layer

---

The registered layer can be viewed in the layer preview.

- Click Layer Preview, and then click OpenLayers for the layer to check.

  ![17.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/17.JPG?api=v2)
  ![18.JPG](https://docs.altibase.com/download/attachments/embedded-page/arch/Altibase%20GeoServer%20Integration%20Guide/18.JPG?api=v2)
- In Altibase, verify the registered layer as follows.

  ```
  $isql
  iSQL> SELECT "fid", "emd_cd", "emd_eng_nm", ASTEXT("the_geom") FROM "SEOUL_43260" LIMIT 3;
  fid         emd_cd                          emd_eng_nm                      ASTEXT("THE_GEOM")
  -----------------------------------------------------------------------------------------------------------------
  1           11110152                        Bongik-dong                     MULTIPOLYGON(((126.9925 37.573
                                                                              85, 126.9941 37.57206, 126.994
                                                                              3 37.571, 126.9929 37.57085, 1
                                                                              26.9923 37.57203, 126.9916 37.
                                                                              57389, 126.9925 37.57385)))
  2           11110153                        Donui-dong                      MULTIPOLYGON(((126.991 37.5733
                                                                              6, 126.9918 37.5708, 126.9905
                                                                              37.5707, 126.9902 37.57189, 12
                                                                              6.9899 37.5729, 126.991 37.573
                                                                              36)))
  3           11560123                        Mullae-dong 5(o)-ga             MULTIPOLYGON( ... )
  3 rows selected.
  ```

  - At Atlibase, table names and column names are case-sensitive.
       When querying table and column names that contain lowercase letters, use double quotes ("").

# Reference materials

---

### Altibase Manual

- [Altibase 7.3 Getting Started Guide manuals](https://manual.altibase.com/7.3/en/start-here/getting-started/copyright/)
- [Altibase 7.3 Spatial SQL manuals](https://manual.altibase.com/7.3/en/ref/spatial-sql/copyright/)

### GeoServer

- [GeoServer download site](http://geoserver.org/download/)

### Open Geospatial

- [Open Geospatial Consortium (OGC)](https://www.ogc.org/)
- [Open Source Geospatial Foundation (OSGeo)](https://www.osgeo.org/)
- [Open Source Geospatial Foundation Korean chapter](https://www.osgeo.kr/)
