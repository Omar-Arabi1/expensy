# expensy
an expense tracker to track your expenses automatically by you inserting your expenses with a price and they will be saved with a date and id once you call the `calculate` command you will see how much you have spent and how much you still have left

install the app with `pipx install expensy`

***NOTE:*** *this app isn't available on windows*

## table of contents:
- [add command](#add-command)
- [calculate command](#calculate-command)
- [export command](#export-command)
- [remove command](#remove-command)
- [update command](#update-command)
- [view command](#view-command)

## add command:
adds an expense to the database, the expense will be added with a name, price and a creation date

both the name and price will be given by you, but the creation date (Y-M-D, AKA: 2025-6-18) will be saved automatically
by the tool, something to note is that the creation date doesn't change and it is always set to the date when you created the
expense

the name must be string or TEXT type, while the price must be a float type or a REAL type

the price must also be greater than 0

#### example:
`>>> expensy add 'car repairs' 49.99`

## calculate command:
calculates the amount of money you have left from your balance based on all the expenses inside the list

the balance will be entered by you and it must be *bigger than or equal to the sum of all the expenses inside the list and a float type REAL type*
the program will subtract that balance that you have entered with the sum of all the expenses inside the list and tells
you how much you lost and how much you kept

#### example:
`>>> expensy calculate 100`

## export command:
exports the list as a csv file

it takes in nothing or an optional `--output` option or `-o` for short this option will take a path to export the csv into
you could give it a path and a name ***NOTE:*** *you must enter the FULL PATH not a relative path*
it should *have a parent directory already exists and the extension '.csv' and it shouldn't already exist (e.g the file name provided and path already exist)*

by default the application exports the file at your current working directory with the name "expenses.db"

#### bad example:
`>>> expensy export -o /this/path/does/not/exist.csv`
its bad because the provided file's parent directory (e.g /this/path/does/not/) doesn't exist

#### good example:
`>>> expensy export -o /home/<user>/expenses.csv`
its good because this file's parent directory (e.g /home/<user>) exists and the file name (e.g expenses.csv) doesn't already exists

## remove command:
removes an expense from the list

it takes in a required expense_name which it will query and remove, but it could also take an optional option `--remove-date` or `-d` which takes in a creation date (AKA 2025-6-18)
and it will remove all the expenses with the date given or you could use the optional option `--all` or `-a` which takes in nothing and removes ***all*** the expenses so be careful

also note that if you use the options you must put "_" as the expense name it is not neccessary to put that symbol exactly but it is encouraged, you can't just leave it empty because 
click (the library I used for argument parsing) still takes it as a required argument

#### example:
`>>> expensy remove _ --all`

## update command:
updates the price of an existing expense

it takes in two required arguments an expense_name and a new_price the expense_name must already exist in the list and the price at that name will be updated
with the new_price argument, 

the new_price argument must be a float and it must be greater than 0

#### example:
`>>> expensy update 'car wash' 83.99`

## view command:
use this command to view all the expenses saved

it takes in nothing and once ran it will show you the expense name, price and creation date

#### example:
`>>> expensy view`