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

        $VAR1 = {
                'y.a' => 2,
                'x' => 1,
                'y.b' => 3,
                'z:0' => 'a',
                'z:1' => 'b',
                'z:2' => 'c'
        };
