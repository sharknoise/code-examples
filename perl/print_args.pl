#!/usr/bin/perl
@elems = ('default1', 'default2', 'default3');
if (@ARGV){
    @elems = @ARGV;  # user input from terminal
}
foreach (@elems) {
    print;
}
