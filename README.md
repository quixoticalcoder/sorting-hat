# sorting-hat

A Python command-line simulation that assigns fictional school houses from character traits and calculates a grade from a birth year. It supports batch CSV processing and an interactive prompt using only the Python standard library.

## Run locally

Requires Python 3; no external packages are needed.

```bash
git clone https://github.com/quixoticalcoder/sorting-hat.git
cd sorting-hat
python3 sorting_hat/project.py sorting_hat/student.csv sorted_students.csv
```

The batch command reads the included ten-row example and writes `sorted_students.csv`. To answer prompts instead:

```bash
python3 sorting_hat/project.py
```

Enter `yes`, then provide a name, a characteristic, and a birth year.

## Input and output

Input requires the exact headers `name,characteristic,birthdate`. Despite its name, `birthdate` contains an integer year rather than a full date:

```csv
name,characteristic,birthdate
Student 01,patience,2005
Student 02,courage,2008
```

Output uses `name,house,Grade`:

```csv
name,house,Grade
Student 01,Hufflepuff,Grade 12
Student 02,Griffindor,Grade 9
```

The script overwrites the output path if it already exists. Use a separate destination to preserve the input.

## Assignment rules

| Characteristics | Returned house |
| --- | --- |
| courage, loyalty, adventure, confidence | `Griffindor` |
| patience, dedication, honesty, smartness | `Hufflepuff` |
| wisdom, creativity, perfectionism | `Ravenclaw` |
| ambition, competitive, leadership, knowledge | `Slytherin` |
| Any other value | `No House` |

`Griffindor` is the spelling currently returned by the implementation. Interactive characteristics are trimmed and case-normalized; CSV values are matched exactly.

Grades use the fixed formula `2022 - birth_year - 5`, returned as `Grade N`. The calculation does not use the current year. Interactive mode rejects birth years before 2005; batch mode applies no equivalent admission check.

## Structure and limitations

- `sorting_hat/project.py` contains argument handling, CSV processing, house assignment, grade calculation, and interactive prompts.
- `sorting_hat/student.csv` contains ten anonymized example records.
- `sorting_hat/Hogwarts.png` is a preserved image asset; the CLI does not load it.

The program checks argument count and whether path strings contain `.csv`, and catches missing-file errors. It does not validate required headers, year ranges, numeric input, or all filesystem errors. Interactive completion calls `sys.exit` with a message, producing a nonzero exit status even after displaying a result. Batch processing buffers all records in memory, so memory use grows linearly with input size.

This is an unofficial fan-themed programming exercise with no affiliation to the Harry Potter franchise.
