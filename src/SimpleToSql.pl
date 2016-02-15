#!/usr/bin/perl
use strict;
use DBI;
use DBD::mysql;

use warnings;

my $driver = "mysql"; 
my $database = "myDB2";
my $dsn = "DBI:$driver:database=$database";
my $userid =  "newuser";
my $password = "password";
my $dbh = DBI->connect($dsn, $userid, $password ) or die $DBI::errstr;

my $cmi  = "./nomos -d openssl-1.1.0-pre2" ;
my @output = `$cmi`;

# group all entries that contain the word "contains", all file/license arrangements
my @capture = grep /contains/, @output;

my $j = 0; my $pos = 0; my $hold = 0; my $i = 0; my $filename = ""; my $licenses = "";
foreach my $line (@capture)
{
    for ($j = 6; $j < length($line); $j++) {
	if ((substr $line, $j, 1) =~ / /) { $filename = substr $line, 5, $j - 5; last; }
    } 
    for ($pos = 26; $pos < length($line); $pos++) {
        if ((substr $line, $pos, 1) =~ /\)/) { $licenses = substr $line, $pos+1, length($line) - $pos - 1; }
    }
    $licenses =~ s/\s//g;
    my $sth = $dbh -> prepare("INSERT INTO simpleSql (id, FILENAME, LICENSES) values (default, '$filename', '$licenses')");
    $sth->execute() or die $DBI::errstr;
    $sth->finish();
}

if (! $dbh->{'AutoCommit'}) {
    $dbh->commit;
}
