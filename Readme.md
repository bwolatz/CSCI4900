# CSCI4900 One-Shot DoSOCS

##Introduction.
The members of our team are Brian and Nikhit. We will be creating a software that uses a plugin to send pom.xml coordinates to maven to get all the jars and the dependency tree. Using the dependency tree we will gather relationship info. we will also use DoSOCS to scan the JAR files and which will return relevent information such as licensing information and SPDX documentation. Finally all the san information and the relationship information is stored in the database.

## Copyright.
Brian and Nikhit

## License(s).
MIT © Nikhit Adusumilli, Brain<br/>
CC-BY-SA-4.0 © Nikhit Adusumilli, Brain<br/>

## Install Directions.

##### Plugin Install
[Grab the source from the latest
release](https://github.com/bwolatz/CSCI4900/releases) and use `pip` to install
it as a package. Replace `0.x.x` with the latest release version number.

` $ tar xf 0.x.x.tar.gz`<br/>
` $ pip install ./CSCI4900-0.x.x`

##### Obtain Source Files and install inforamtion from DoSOCS<br />
DoSOCS - https://github.com/DoSOCSv2/DoSOCSv2<br />

##### Install the correct dependencies/libraries for Python 2.7 and for DoSOCS<br />
Ensure Python is version 2.7, if it is 3.0 it will not work<br />
1. To check, run `python --version`

##### To add libraries for DoSOCS<br />
| File(s) | Commands |
| --- | --- |
|SQLAlchemy|`pip install sqlalchemy`|
|python-mysqldb|`sudo apt-get build-dep python-mysqldb`|
|libpq-dev|`sudo apt-get install libpq-dev`|
|posstgreSQL|`pip install psycopg2`|
|libglib2.0-dev|`sudo apt-get install libglib2.0-dev`|

##### Install Maven in your environment<br/>
For Maven<br />
1. Type `sudo apt-get install maven`.<br/>
2. To verify Type `mvn -version`.

## Environment.

The enviornment should be in a Windows Virtual Box and Ubuntu 14.04 using the Python 2.7 programming languange for any programs and scripts and DoSOCSv2 for scanning of files.

## Usage.

The Usage of this program to get the coordinates and jars to get the relationships and scan is <br/>
`dosmav /path/to/pom.xml`

