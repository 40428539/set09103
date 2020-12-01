drop table if exists RoomList;
	create table RoomList (
	RoomName text unique primary key,
	RoomPass text not null
);
