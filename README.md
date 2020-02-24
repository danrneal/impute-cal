# Impute Cal for TDEE

A script to parse a TDEE spreadsheet and impute the calories for a missed day
of calorie tracking. Total Daily Energy Expenditure (TDEE) is the measure of
the amount of calories burned in a day. The included spreadsheet (created by
reddit user /u/3-suns) calculates a persons TDEE from daily weigh-ins and
through daily calorie tracking. If a day of calorie tracking is missed, this
script can provide a best guess given past data contained in the spreadsheet.

## Set-up

Set-up a virtual environment and activate it:
```
python3 -m venv venv
source venv/bin/activate
```
You should see (venv) before your command prompt now. (You can type `deactivate`
to exit the virtual environment any time.)

Install the requirements:
```
pip install -r requirements.txt
```

## Usage

Make sure you are in the virtual environment (you should see (venv) before your
command prompt). If not `source /venv/bin/activate` to enter it.

```
Usage: impute_cal.py
```

## Testing Suite

This repository contains a test suite consisting of unit tests.

#### Unit Tests

These test the program from the inside, from developer's point of view. You
can run them with the following command:

```
python3 -m unittest discover tests/
```

## A comment on TDD

This project was done following Test-Driven Development principles where the
starting point is a failing test. My process was to write a unit test to define how I wanted to the code to behave. That is the point where I wrote the "actual" code to get the unit tests to pass.

While this may seem unnecessary for a program of such a small size and may
seem like overdoing, TDD principles help to create quality, maintainable code
and as such I believe are good habits to foster even on a small project such as
this.

## Credit

Reddit user /u/3-suns for their [adaptive TDEE spreadsheet](https://drive.google.com/open?id=0B8EbfzFB0mBrMGJ6V2N5QWNfeTg)

## License

Impute Cal for TDEE is licensed under the [MIT license](https://github.com/danrneal/impute-cal-for-tdee/blob/master/LICENSE).
