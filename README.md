# CSCI4900 Plugin

##Introduction.
The members of our team are Brian and Nikhit. We will be creating a software that uses a plugin to send pom.xml coordinates to maven to get all the jars and the dependency tree. Using the dependency tree we will gather relationship info on the other hand we will also use DoSOCS to scan the JAR files to get relevent information such as licensing information and SPDX documentation. Finally all the san information and the relationship information is stored in the database.

## Copyright.
Nikhit Adusumilli<br/>
Brian Wolatz

## License(s).
####Source License<br/>
MIT © Nikhit Adusumilli, Brian Wolatz<br/>
####Document License<br/>
CC-BY-SA-4.0 © Nikhit Adusumilli, Brian Wolatz<br/>

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

## Communication Management

Brian and Nikhit will use GitHub as the main source of communication and open issues in GitHub for all problems, even if the issue creator plans on solving the issue himself, as it is important to keep the other team member up-to-date on the progress of the project. It is essential that this communication plan is employed, for it will keep all relevant project work documented and the other mediums of communicated will be either in-person or over email, both of which are very effective. Technical Issues with the project should be handled by submitting GitHub issues, other issues should be solved using email and in-person communication.

In review of this communication plan, there does appear to be a few flaws. First, it is not easy to request simple resources from one another as we do not have a dedicated email chain for that nor are the requested items necessary to submit a whole issue over. To combat this, we have opened an email chain dedicated to asking each other questions and for resources.

### Contributing to CSCI4900

Nikhit and Brian are working on this project for school, for academic integrity reasons, we are not accepting pull requests or commits from the community at this point in time. However, you can feel free to leave us any comments/feedback or post issues for us to look at.

##System Description.

We are creating a system that will communicate with DoSOCS and maven central to retrieve the project-level dependency and vulnerability information relating to the package or file that has been sent to them (using the nomos portion of DoSOCS). To create the connection we will be using python scripts and all the information that is retrieved will be stored into a database which uses the SPDX schema provided in class. The SPDX document is generated and saved by DoSOCS as well.

##Use Cases
####Use Case 1
**Title**: Creating Dependency Relationship in SPDX.<br/>
**Primary Actor**: Developer. <br/>
**Goal in context**: Discover the relationships of a project using the pom.xml file and store in spdx database.<br/>
**Stakeholders and Interests**: Developers looking to capture dependency relationships for a given project. <br/>
**Preconditions**: Install instructions located above, all these installations are needed. A POM.xml file to scan is also necessary. <br/>
**Main success scenario**: succesfully Created dependency tree and stored relationship information in the SPDX schema. <br/>
**Failed end conditions**: Dependency relationship not created and not stored.<br/>
**Trigger**: running "dosmav pom-file" on cmd.<br/>

##Data Flow Diagram

![image](https://cloud.githubusercontent.com/assets/11622664/14574510/ba34028a-0321-11e6-8355-6b2faddd92e3.png)

