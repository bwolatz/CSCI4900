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
[Grab the source from the latest
release](https://github.com/nadusumilli/DoSOCSv2/releases) and use `pip` to install
it as a package. Replace `0.x.x` with the latest release version number.

` $ tar xf 0.x.x.tar.gz`<br/>
` $ pip install ./DoSOCSv2-0.x.x`

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

Brian and Nikhit will use GitHub as the main source of communication and open issues in GitHub for all problems, even if the issue creator plans on solving the issue himself, as it is important to keep the other team member up-to-date on the progress of the project. It is essential that this communication plan is employed, for it will keep all relevant project work documented and the other mediums of communicated will be either in-person or over github by creating issues and commits, both of which are very effective. Technical Issues with the project should be handled by submitting GitHub issues, other issues should be solved by in-person communication.

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

![image](https://cloud.githubusercontent.com/assets/11622664/14574580/243bf868-0322-11e6-86c3-68a74aa23fbe.png)

##Unit Test Cases Document

These tests were performed using the broken up functions in the udependency.py and umain.py files.

|Test Case ID|Action Tested|Expected Result|Verify|Actual Result|
| -----------|---------------|-------------|------|-------------|<br/>
|1|Create Dependency Object|Initializes Dependency Object. Creates Temp Directory.|I call the method from the test class and print the location of the temp directory and dependency object|Pass|<br/>
|2|Copy POM|Takes in file name from command line. Copies it into the Temp Directory. Switches working directory to temp directory|Call the method from the test case and check if the pom is being copied to the temp directory by listing all files in the temp directory. I also print the current working directory to make sure we are in the temp directory|Pass|
|3|Get Dependencies|Run a Maven command that copies dependencies into the temp directory|We Call the method from the test case program and list all the files in the temp directory.|Pass|
|4|Get Tree|Run a Maven command that creates a text document that lays out the dependencies and their relationships|Call the method from the test case and read the document form the temp folder.|Pass|
|5|Scan Tree For Levels|Scan the tree document to gather the parent-child relationships for the first three levels of dependencies|We call this method from the test case and pass it a tree file. It prints out the level of dependencies by parsinf through the tree file.|Pass|
|6|Scan Dependencies by Level|Use dosocs to scan a dependency into the SPDX database. Use for the first three levels of dependencies|After the tree file is parsed above and the level of dependencies are printed we just scan them through dosocs.|Pass|
|7|Create Relationship Document|Adds each parent-child relationship into the SPDX databse using custom-made dosocs functionality|we Call the method from the test case and pass it a tree file. the method parses through the file and scans the dependencies based on that. After that we parse for the relationships and send the parent and child dependencies to dosocs where it gets the parent and child identifiers and prints them. Then i send the information into the database table.|Pass|
|8|Print Relationship Tree|Print out the relationship document from the database.|We are still working on creating the method.|Fail|
|9|Delete the Temp Directory|Removes the temporary directory from the system.|we call the method from the test case where it just calls the shutil.rmtree and deletes all the temp file. We list all documents to make sure the temp file is deleted|Pass|

