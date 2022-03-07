        # Exported functions
        use Hash::Flatten qw(:all);
        $flat_hash = flatten($nested_hash);
        $nested_hash = unflatten($flat_hash);
        
        # OO interface
        my $o = new Hash::Flatten({
                HashDelimiter => '->', 
                ArrayDelimiter => '=>',
                OnRefScalar => 'warn',
        });
        $flat_hash = $o->flatten($nested_hash);
        $nested_hash = $o->unflatten($flat_hash);

