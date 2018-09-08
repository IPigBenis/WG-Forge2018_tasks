# WG-Forge2018_tasks

## INSTALL

```bash
$ git clone https://github.com/igorxxl8/WG-Forge2018_tasks.git
$ cd WG-Forge2018_tasks
$ pip install . --user
```

## UNINSTALL
```bash
$ pip uninstall wgforge2018_igorxxl8
```

# TASK 1

### PROBLEM: Внимательность  
Для начала тебе следует найти адрес, на который необходимо отправить ответы на тестовое задание и заявку.

### SOLUTION:  
wg_forge@wargaming.net

# TASK 2 
### PROBLEM: Анализ  
Какой IP-адрес является вторым по частоте появления в этом log-файле?

### SOLUTION:
```bash
$ task2 wgforge.wargaming.com_access.log 2
```

### RESULT: 176.0.0.70


# TASK 3  
### PROBLEM: SQL
У тебя есть две таблицы в базе данных MySQL:
	Employees
+---------------+-------+
|DEPARTMENT_ID	|INT	|
+---------------+-------+
|NAME		|STRING	|
+---------------+-------+
|SALARY		|FLOAT	|
+---------------+-------+
|LEAD		|BOOL	|
+---------------+-------+
	Departments
+---------------+-------+	
|DEPARTMENT_ID	|INT	|
+---------------+-------+
|DEPARTMENT_NAME|STRING	|
+---------------+-------+
Напиши запрос, который выведет имя департамента и список сотрудников, получающих большую заработную плату, чем их непосредственный руководитель. 


