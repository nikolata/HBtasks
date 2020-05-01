#task 1
select `NAME`, `COUNTRY`, `NUMGUNS`, `LAUNCHED` 
from `SHIPS` 
join `CLASSES` 
on `CLASSES`.`CLASS` = `SHIPS`.`CLASS` 
order by launched

#task 2



#task 3
select `NAME` 
from `SHIPS` 
join `OUTCOMES` 
on `OUTCOMES`.`SHIP` = `SHIPS`.`NAME` 
where `OUTCOMES`.`BATTLE` 
in (select `NAME` from `BATTLES` 
	where `BATTLES`.`DATE` like '%1942%')

#task 4
select `NAME`
from `CLASSES` 
join `SHIPS` 
on `CLASSES`.`CLASS` = `SHIPS`.`CLASS` 
where `SHIPS`.`NAME` not in (select `SHIP` 
	from `OUTCOMES` 
	join `BATTLES` 
	on `OUTCOMES`.`BATTLE` = `BATTLES`.`NAME` ) 
ORDER by `COUNTRY`