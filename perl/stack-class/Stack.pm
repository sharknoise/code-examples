package Stack;

sub new {
    my ($class, $args) = @_;
    my $self = {
        note => $args->{note} || 'no note was provided',
        contents => $args->{contents},
    };
    return bless $self, $class;
}

sub get_contents {
    my $self = shift;
    # return dereferenced array
    return @{ $self->{contents} };
};

sub pop {
    my $self = shift;
    return pop @{ $self->{contents} };
};

sub push {
    my ($self, $new_item)  = @_;
    push @{ $self->{contents} }, $new_item;
};

sub count_items {
    my $self = shift;
    return scalar(@{ $self->{contents} })
}

1;