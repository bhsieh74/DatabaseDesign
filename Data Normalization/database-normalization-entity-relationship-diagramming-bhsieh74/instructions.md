# Data Normalization and Entity-Relationship Diagramming

The following table, representing students in a course, is already in [first normal form](https://knowledge.kitchen/A_Simple_Guide_to_Five_Normal_Forms_in_Relational_Database_Theory#FIRST_NORMAL_FORM) (1NF) - all records have the same number of fields, and there is only one value per field.

| assignment_id | student_id | due_date | professor | assignment_topic                | classroom | grade | textbook | professor_email  |
| :------------ | :--------- | :------- | :-------- | :------------------------------ | :-------- | :---- | :------- | :--------------- |
| 1             | 1          | 23.02.18 | Bloomberg | Data normalization              | WWH 101   | 80    | Deumlich | bloo@foo.edu     |
| 2             | 1          | 18.11.18 | Engel     | Single table queries            | 60FA 314  | 25    | Dümmlers | d.e.1234@foo.edu |
| 1             | 4          | 23.02.18 | Bloomberg | Data normalization              | WWH 101   | 75    | Deumlich | bloo@foo.edu     |
| 5             | 2          | 05.05.18 | Engel     | Python and pandas               | 60FA 314  | 92    | Dümmlers | d.e.1234@foo.edu |
| 4             | 2          | 04.07.18 | Clayton   | Spreadsheet aggregate functions | WWH 201   | 65    | Zehnder  | j.c.3@foo.edu    |

## Requirements

### Convert to 3NF

Convert this table to the [third normal form](https://knowledge.kitchen/A_Simple_Guide_to_Five_Normal_Forms_in_Relational_Database_Theory#Third_Normal_Form) (3NF) using the techniques we have learned in this class.

### Draw an ER diagram

Draw an Entity-Relationship Diagram of your 3NF-compliant data tables. You do not need to use any particular software to do this, and can simply draw on paper and post a photo (appropriately sized for a web page, of course).

### Write a report

Write a short report about your solution explaining what about the original data set was not 3NF compliant and what changes you made to make it 3NF-compliant. Be specific.

### Post to web

Write a wonderfully-formatted Markdown report in `README.md` a nicely designed web page, with clear headings, sub-headings, and text that includes:

- a table containing the original data set
- your description of what makes this data set not compliant with 3NF
- tables containing the 3NF-compliant version of the data set
- the ER diagram(s) you created of your 3NF-compliant version of the data set (this diagram must be visible on the `README.md` document, not simply linked from there)
- your description of what changes you made and how these changes make the data 3NF-compliant

## Submit your work

Each student must submit this assignment individually. Use Visual Studio Code to perform git `stage`, `commit` and `push` actions to submit. These actions are all available as menu items in Visual Studio Code's Source Control panel.

1. Type a short note about what you have done to the files in the `Message` area, and then type `Command-Enter` (Mac) or `Control-Enter` (Windows) to perform git `stage` and `commit` actions.
1. Click the `...` icon next to the words, "Source Control" and select "Push" to perform the git `push` action. This will upload your work to your repository on GitHub.com.

![Pushing work in Visual Studio Code](./images/vscode_stage_commit_push.png)
