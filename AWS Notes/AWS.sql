create table toys (
  toy_name varchar2(100),
  weight   number
);

insert into toys values ('Car',80)

select * from toys;

select * from user_constraints where table_name='TOYS'

select * from all_tables where owner = 'SYS'

select * from user_tables

create table bricks (
  colour varchar2(100),
  shape varchar2(100)
);

create table toys_heap (
  toy_name varchar2(100)
) organization heap;

create table toys_iot (
  toy_id   integer primary key,
  toy_name varchar2(100)
) organization index;

create table bricks_iot (
  bricks_id integer primary key
) organization index;

select * from user_clusters

desc emp

select * from user_tables

select * from toys

select * from bricks

select ename, nvl(mgr,1000) from emp;

select * from user_tables


delete from toys_iot where 