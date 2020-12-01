drop table if exists Users;
	create table Users (
	Username text unique primary key,
	Email text not null,
	password text not null
	
);

drop table if exists Messages;
	create table Messages (
	ID integer primary key autoincrement,
	Username text not null,
	Message text,
	Time timestamp,
	Important boolean,
	Roomname text not null
	
);

