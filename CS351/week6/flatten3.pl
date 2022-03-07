        # Exported functions
        use Hash::Flatten qw(:all);

        $nested = {
                'x' => 1,
                'y' => {
                        'a' => 2,
                        'b' => 3
                },
                'z' => [
                        'a', 'b', 'c'
                ]
        };

        $flat = flatten($nested);
        use Data::Dumper;
        print Dumper($flat);

        #$flat_hash = flatten($nested_hash);
        $nested_hash = unflatten($flat);
        
        # OO interface
        my $o = new Hash::Flatten({
                HashDelimiter => '->', 
                ArrayDelimiter => '=>',
                OnRefScalar => 'warn',
        });
        $flat_hash = $o->flatten($nested_hash);
        $nested_hash = $o->unflatten($flat_hash);


        $VAR1 = {
                'y.a' => 2,
                'x' => 1,
                'y.b' => 3,
                'z:0' => 'a',
                'z:1' => 'b',
                'z:2' => 'c'
        };
