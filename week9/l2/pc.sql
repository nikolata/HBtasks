#task 1
SELECT avg(speed)
  FROM pc;

#task 2
select avg(screen), maker 
from laptop 
join product 
on product.model = laptop.model 
group by maker;

#task 3
select avg(price) 
from laptop 
where price > 1000;

#task 4
select abs(price), hd  
from pc 
group by hd;

#task 5
select avg(price) 
from pc 
where speed>500 
group by speed;

#task 6
select avg(price) 
from pc 
join product 
on product.model = pc.model
where maker == 'A';

#task 7
select avg(price), type 
from laptop 
join product 
on product.model = laptop.model 
where product.maker = 'B' 
union 
select avg(price), type 
from pc 
join product 
on product.model = pc.model 
where product.maker = 'B'

#task 8 
select maker 
from pc 
join product 
on product.model = pc.model 
group by maker 
having count(maker)>3;

#task 9
select maker 
from pc 
join product 
on product.model = pc.model 
order by price desc 
limit 1;

#task 10
select avg(cd) 
from pc 
join product 
on product.model = pc.model 
where product.maker IN (
	SELECT maker FROM   product WHERE  type 
       = 'Printer') 
group by maker