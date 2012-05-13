#!/usr/bin/perl
use strict;

use CGI;

my $VERSION = '6.5';

my $cgi = new CGI;

my $url = $cgi->param('url') || '';
my $virus = $cgi->param('virus') || '';
my $source = $cgi->param('source') || '';
$source =~ s/\/-//;
my $user = $cgi->param('user') || '';


my $TITLE_VIRUS = "SquidClamAv $VERSION: Virus detection";
my $subtitle = 'contains the virus';
if ($virus =~ /Safebrowsing/) {
	$TITLE_VIRUS = "SquidClamAv $VERSION: Unsafe Browsing detected";
	$subtitle = 'Safe Browsing message';
}

# Remove clamd infos
$virus =~ s/stream: //;
$virus =~ s/ FOUND//;


print $cgi->header();

print $cgi->start_html(-title => $TITLE_VIRUS);
print qq{
<h2 style="color: #FF0000">$TITLE_VIRUS</h2>
<hr>
<p>
};
print qq{
The requested URL $url <br>
$subtitle: $virus
};

print qq{
<p>
This URL can not be downloaded.
<p>
Origin: $source / $user
<p>
<hr>
Powered by <a href="http://squidclamav.darold.net/">SquidClamAv $VERSION</a>.
};

print $cgi->end_html();

exit 0;
