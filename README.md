
### Command for starting tests
    "pytest"

### if u need see browser
    "pytest -s --headed --slowmo 500"

### if u need start only 1 case

    pytest -s --headed --slowmo 500 -k {name_method}

or

    pytest -k {name_method} 
#### alert: name_method use without {}

### if u need have more info when cases start 
    pytest -vv

or

    pytest -v
