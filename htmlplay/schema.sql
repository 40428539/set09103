drop table if exists Users;
	create table Users (
	Username text unique primary key,
	Email text not null,
	password text not null
	
);

