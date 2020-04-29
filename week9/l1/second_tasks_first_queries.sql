#first task
SELECT address 
FROM STUDIO
where name == 'MGM';

#second task
SELECT birthdate 
FROM MOVIESTAR
WHERE name == 'Kim Basinger';

#third task
SELECT name 
FROM MOVIEEXEC
WHERE networth > 10000000;

#fourth task
SELECT name 
FROM MOVIESTAR
WHERE gender == 'M' or address == 'Prefect Rd.';

#fifth task
INSERT INTO MOVIESTAR
VALUES ('Zahari Baharov', 'Studentski Grad', 'M', '1980-29-02')

#sixth task
DELETE FROM STUDIO
WHERE CHARINDEX('5', address)>0

#seventh task
UPDATE MOVIE
  SET studioname = 'FOX'
    WHERE CHARINDEX('Star', title) > 0;

#Relations
#task 1
SELECT starname
From STARSIN
INNER JOIN MOVIESTAR on MOVIESTAR.NAME == STARSIN.STARNAME
WHERE STARSIN.MOVIETITLE == 'Terms of Endearment' and MOVIESTAR.GENDER == 'M';

#task2
SELECT starname
FROM STARSIN
INNER JOIN MOVIE on MOVIE.TITLE == STARSIN.MOVIETITLE
WHERE MOVIE.year == 1995 and MOVIE.studioname == 'MGM';

#task 3
ALTER TABLE STUDIO
ADD PresidentName VARCHAR(50);

UPDATE STUDIO
SET presidentname = 'Piotur Petrovic'
WHERE name == 'MGM'

UPDATE STUDIO
SET presidentname = 'Sancho Pansa'
WHERE name == 'USA Entertainm.'

SELECT presidentname 
FROM STUDIO
WHERE name == 'MGM';