# __База данных__ 

## __Работа в *DBeaver & Postgres*__



### 
- **CREATE TABLE** __public."sm_app users" (__ <br/>
    *id* __int4__ **NOT NULL GENERATED ALWAYS AS IDENTITY,** <br/>
    *"name"* __varchar__ **NOT NULL,**<br/>
    *age* __int4__ **NOT NULL,**<br/>
    *gender* __varchar__ **NOT NULL**,<br/>
    *nationality* __varchar__ **NOT NULL,**<br/>
    **CONSTRAINT** __sm_app_users_pk__ **PRIMARY KEY** __(id)__<br/>
    __);__<br/>
<br/>

- **CREATE TABLE** __public."sm_app comments" (__ <br/>
    *id* __int4__ **NOT NULL GENERATED ALWAYS AS IDENTITY,**<br/>
    *"text"* __varchar__ **NOT NULL,**<br/>
    *user_id* __int4__ **NOT NULL,**<br/>
    *post_id* __int4__ **NOT NULL,**<br/>
    **CONSTRAINT** __sm_app_comments_pk__ **PRIMARY KEY** __(id),__<br/>
    **CONSTRAINT** __sm_app_comments_fk__ **FOREIGN KEY** __(user_id)__ **REFERENCES** __public."sm_app users"(id),__<br/>
    **CONSTRAINT** __sm_app_comments_fk_1__ **FOREIGN KEY**__(post_id)__ **REFERENCES** __public."sm_app posts"(id)__<br/>
    __);__<br/>
<br/>

- **CREATE TABLE** __public."sm_app likes" (__<br/>
    *id* __int4__ **NOT NULL GENERATED ALWAYS AS IDENTITY,**<br/>
    *user_id* __int4__ **NOT NULL,**<br/>
    *post_id* __int4__ **NOT NULL,**<br/>
    **CONSTRAINT** __sm_app_likes_pk__ **PRIMARY KEY** __(id),__<br/>
    **CONSTRAINT** __sm_app_likes_fk__ **FOREIGN KEY** __(user_id)__ **REFERENCES** __public."sm_app users"(id)__,<br/>
    **CONSTRAINT** __sm_app_likes_fk_1__ **FOREIGN KEY** __(__post_id__)__ **REFERENCES** __public."sm_app posts"(id)__<br/>
    __);__<br/>
<br/>

- **CREATE TABLE** __public."sm_app posts" (__<br/>
    *id* __int4__ **NOT NULL GENERATED ALWAYS AS IDENTITY,**<br/>
    *title* __varchar__ **NOT NULL,**<br/>
    *description* __varchar__ **NOT NULL,**<br/>
    *used_id* __int4__ **NOT NULL,**<br/>
    **CONSTRAINT** __sm_app_post_pk__ **PRIMARY KEY** __(id),__<br/>
    **CONSTRAINT** __sm_app_post_fk__ **FOREIGN KEY** __(used_id)__ **REFERENCES** __public."sm_app users"(id)__<br/>
    __);__<br/>

**Код программы в** *sql* **формате находится по ссылке** [**сlick me.**](https://github.com/DarthVaderOn/Home-Works/blob/master/10/Home%20Work%2010%20dump.sql)

## **Диаграмма связи таблиц**
### 
![diagrams](https://raw.githubusercontent.com/DarthVaderOn/Home-Works/master/10/Home%20Work%20%2310.png)<br/>
**Фото диаграммы в** *png* **формате находится по ссылке** [**click me.**](https://github.com/DarthVaderOn/Home-Works/blob/master/10/Home%20Work%20%2310.png)<br/>
