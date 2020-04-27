#task 1
CREATE TABLE Languages(
  id INTEGER PRIMARY KEY,
  language VARCHAR(50),
  answer VARCHAR(100),
  answers INTEGER,
  guide TEXT
);

#task 2
INSERT into Languages
  VALUES
    (1, 'Python', 'google', 0, 'A folder named Python was created. Go there and fight with program.py!'),
    (2, 'Go', '200 OK', 0, 'A folder named Go was created. Go there and try to make Google Go run.'),
    (3, 'Java', 'object oriented programming', 0, 'A folder named Java was created. Can you handle the class?'),
    (4, 'Haskell', 'Lambda', 0, 'Something pure has landed. Go to Haskell folder and see it!'),
    (5, 'C#', 'NDI=', 0, 'Do you see sharp? Go to the C# folder and check out.')

#task 3
ALTER TABLE Languages
  add rating INTEGER rating(1,9)

#mistake
INSERT into Languages(Rating)
values 
	(9),
    (3),
    (8),
    (5),
    (1);
#fix the mistake
DELETE from Languages
Where id>5

UPDATE Languages
Set rating = 9
where id = 1

UPDATE Languages
Set rating = 6
where id = 2

UPDATE Languages
Set rating = 8
where id = 3

UPDATE Languages
Set rating = 4
where id = 4

UPDATE Languages
Set rating = 2
where id = 5

#task 4

UPDATE Languages
Set answers = 1
where language = 'Python'

UPDATE Languages
Set answers = 1
where language = 'Go'

#task 5
SELECT language 
 from Languages
  where answer like "%200 OK%" or answer like '%Lambda%'