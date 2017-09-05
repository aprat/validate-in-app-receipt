# Validate in-app receipt
> Validate Apple in-app receipts

A command line Python program to validate Apple in-app receipts using [itunes-iap](https://github.com/youknowone/itunes-iap) from [youknowone](https://github.com/youknowone).

## Installation

OS X & Linux:

```sh
virtualenv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

## Usage example

```sh
source ENV/bin/activate
python validate.py receipt.txt
deactivate
```

## Release History

* 0.1 (2017-09-17)
    * Initial release

## Meta

Adrià Prat – [@adria_prat](https://twitter.com/adria_prat) – adria@adriaprat.com

Distributed under the MIT license. See ``LICENSE`` for more information.

[https://github.com/aprat/validate-in-app-receipt](https://github.com/aprat/validate-in-app-receipt)

## Contributing

1. Fork it (<https://github.com/aprat/validate-in-app-receipt/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
