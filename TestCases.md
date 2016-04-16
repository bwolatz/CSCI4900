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
|8|Print Relationship Tree|Print out the relationship document from the database.||Fail|
|9|Delete the Temp Directory|Removes the temporary directory from the system.|we call the method from the test case where it just calls the shutil.rmtree and deletes all the temp file. We list all documents to make sure the temp file is deleted|Pass|
