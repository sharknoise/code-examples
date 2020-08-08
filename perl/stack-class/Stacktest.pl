use strict;
use warnings;

# Perl 5.26 removed having the current working directory
# in @INC as a security measure.
# We do it with the following 3 lines instead.
use Cwd qw( abs_path );
use File::Basename qw( dirname );
use lib dirname(abs_path($0));

use Stack;

my $testnote = 'created by Stacktest.pl';
my @testitems = ('default1', 'default2', 'default3');

if (@ARGV){
    @testitems = @ARGV;
}

my $teststack = Stack->new({
                note => $testnote,
                contents => \@testitems,  # '\' makes reference to array
            });


my $output_ref = $teststack->{contents};
print "initial stack: @$output_ref\n";

my $popped_element = $teststack->pop;
print "popped element: $popped_element\n";

# this time we get array instead of array reference
my @output = $teststack->get_contents;
print "stack after popping: @output\n";

$teststack->push('test_item');
@output = $teststack->get_contents;
print "stack after pushing test_item: @output\n";

my @number_of_items = $teststack->count_items;
print "current number of items = @number_of_items\n";