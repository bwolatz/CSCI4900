##Unit Test Cases Document

These tests were performed using the broken up functions in the udependency.py and umain.py files.

|Test Case ID|Action Tested|Expected Result|Actual Result|
| -----------|---------------|-------------|-------------|<br/>
|1|Create Dependency Object|Initializes Dependency Object. Creates Temp Directory.|Pass|<br/>
|2|Copy POM|Takes in file name from command line. Copies it into the Temp Directory. Switches working directory to temp directory|Pass|
|3|Get Dependencies|Run a Maven command that copies dependencies into the temp directory|Pass|
|4|Get Tree|Run a Maven command that creates a text document that lays out the dependencies and their relationships|Pass|
|5|Scan Tree For Levels|Scan the tree document to gather the parent-child relationships for the first three levels of dependencies|Pass|
|6|Scan Dependencies by Level|Use dosocs to scan a dependency into the SPDX database. Use for the first three levels of dependencies|Pass|
|7|Create Relationship Document|Adds each parent-child relationship into the SPDX databse using custom-made dosocs functionality|Pass|
|8|Print Relationship Tree|Print out the relationship document from the database|Fail|
|9|Delete the Temp Directory|Removes the temporary directory from the system|Pass|
