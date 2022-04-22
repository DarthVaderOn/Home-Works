# __База данных__ 
___

## __Работа в *DBeaver & Postgres*__
___


### 
__Домашка до понедельника:__<br/>
- *Реализовать в базе данных SQLite, Postgres, MySQL или MariaDB таблички, которые на картинке. И также необходимо связать их внешними ключами.*<br/>

- *id в каждой таблице — первичный ключ, autoincrement.<br/>
   user_id, post_id — внешние ключи.*<br/>

- *Заполнить все таблицы, создав минимум по 5 записей: 5 пользователей, у каждого пользователя хотя бы по одному посту. А лучше — по несколько. У каждого пользователя есть лайки других постов, а так же комментарии.*<br/>

- *Загрузить на гитхаб dump базы данных (.sql или .SQLite файл), сделать скрин похожей диаграммы в ваших программах с вашей БД и тоже загрузить в гитхаб эту картинку. Добавить ее в readme.md в папке с уроком №12.*<br/>

***Важное замечание:***
*Во вторичном ключе должны быть существующие id из первичного ключа соответствующей таблицы. Например, если есть только один пользователь с id=1, то во вторичном ключе не может быть user_id=2 — только user_id=1. Если есть 2 пользователя, то возможны 2 варианта в user_id, и так далее.*<br/>
<br/>

~~~sql
CREATE TABLE public."sm_app users" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	name varchar NOT NULL,
	age int4 NOT NULL,
	gender varchar NOT NULL,
	nationality varchar NOT NULL,
	CONSTRAINT sm_app_users_pk PRIMARY KEY (id)
);

CREATE TABLE public."sm_app comments" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	"text" varchar NOT NULL,
	user_id int4 NOT NULL,
	post_id int4 NOT NULL,
	CONSTRAINT sm_app_comments_pk PRIMARY KEY (id),
	CONSTRAINT sm_app_comments_fk FOREIGN KEY (user_id) REFERENCES public."sm_app users"(id),
	CONSTRAINT sm_app_comments_fk_1 FOREIGN KEY (post_id) REFERENCES public."sm_app posts"(id)
);

CREATE TABLE public."sm_app likes" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	user_id int4 NOT NULL,
	post_id int4 NOT NULL,
	CONSTRAINT sm_app_likes_pk PRIMARY KEY (id),
	CONSTRAINT sm_app_likes_fk FOREIGN KEY (user_id) REFERENCES public."sm_app users"(id),
	CONSTRAINT sm_app_likes_fk_1 FOREIGN KEY (post_id) REFERENCES public."sm_app posts"(id)
);

CREATE TABLE public."sm_app posts" (
	id int4 NOT NULL GENERATED ALWAYS AS IDENTITY,
	title varchar NOT NULL,
	description varchar NOT NULL,
	used_id int4 NOT NULL,
	CONSTRAINT sm_app_post_pk PRIMARY KEY (id),
	CONSTRAINT sm_app_post_fk FOREIGN KEY (used_id) REFERENCES public."sm_app users"(id)
);
~~~
**Полный код программы в** *sql* **формате находится по ссылке** [**сlick me.**](https://github.com/DarthVaderOn/Home-Works/blob/master/10/Home%20Work%2010%20dump.sql)

## **Диаграмма связи таблиц**
___
### 
![diagrams](https://raw.githubusercontent.com/DarthVaderOn/Home-Works/master/10/Home%20Work%20%2310.png)<br/>
**Фото диаграммы в** *png* **формате находится по ссылке** [**click me.**](https://github.com/DarthVaderOn/Home-Works/blob/master/10/Home%20Work%20%2310.png)<br/>
