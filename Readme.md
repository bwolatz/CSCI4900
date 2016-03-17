# CSCI4900 One-Shot DoSOCS

## Introduction.
The members of our team are Brian and Nikhit. We will be creating software that uses DoSOCS we will send a program's JAR files and dependency tree and it will return relevent information such as licensing information and SPDX documentation. It will accomplish this by integrating many programs together but ultimately it will require only one input from the developer using it.

## Copyright.
Brian and Nikhit

## License(s).
Creative Commons Attribution 4.0 International License.<br />
GNU GENERAL PUBLIC LICENSE

## Install Directions.

#### Plugin Install
[Grab the source from the latest
release](https://github.com/bwolatz/CSCI4900/releases) and use `pip` to install
it as a package. Replace `0.x.x` with the latest release version number.

#### Obtain Source Files and install inforamtion from DoSOCS<br />
DoSOCS - https://github.com/DoSOCSv2/DoSOCSv2<br />

#### Install the correct dependencies/libraries for Python 2.7 and for DoSOCS<br />
Ensure Python is version 2.7, if it is 3.0 it will not work<br />
1. To check, run python --version

#### To add libraries for DoSOCS<br />
| File(s) | Commands |
| --- | --- |
|SQLAlchemy|pip install sqlalchemy|
|python-mysqldb|sudo apt-get build-dep python-mysqldb|
|libpq-dev|sudo apt-get install libpq-dev|
|posstgreSQL|pip install psycopg2|
|libglib2.0-dev|sudo apt-get install libglib2.0-dev|

#### Install Maven in your environment<br/>
For Maven<br />
1. Type sudo apt-get install maven.<br/>
2. To verify Type mvn -version.

## Environment.

The enviornment should be in a Windows Virtual Box and Unix 14.04 using the Python programming languange for any programs and scripts 

## Usage.

Used to generate a list of dependecies given a pom.xml and one command. This will be a "one-shot" method of genertaing said list, and it uses the program DoSOCS and the specification SPDX.
