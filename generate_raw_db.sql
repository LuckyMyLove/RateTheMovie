create table Actors
(
    id        int auto_increment
        primary key,
    firstname text not null,
    surname   text not null,
    birthday  date not null,
    photo     text null
);

create table Categories
(
    id   int auto_increment
        primary key,
    name text not null,
    constraint Categories_name_uindex
        unique (name) using hash
);

create table Directors
(
    id        int auto_increment
        primary key,
    firstname char(50) not null,
    surname   char(50) not null,
    birthday  date     not null,
    photo     text     null
);

create table Movies
(
    id           int auto_increment
        primary key,
    title        text not null,
    description  text not null,
    premier_date date not null,
    category_id  int  not null,
    picture      text null,
    constraint Movies_Categories_id_fk
        foreign key (category_id) references Categories (id)
);

create table Movies_actors
(
    movie_id int not null,
    actor_id int not null,
    constraint Movies_actors_Actors_id_fk
        foreign key (actor_id) references Actors (id),
    constraint Movies_actors_Movies_id_fk
        foreign key (movie_id) references Movies (id)
);

create table Movies_directors
(
    movie_id    int not null,
    director_id int not null,
    constraint Movies_directors_Directors_id_fk
        foreign key (director_id) references Directors (id),
    constraint Movies_directors_Movies_id_fk
        foreign key (movie_id) references Movies (id)
);

create table Roles
(
    id   int auto_increment
        primary key,
    name text not null,
    constraint Roles_name_uindex
        unique (name) using hash
);

create table Users
(
    id        int auto_increment
        primary key,
    username  text not null,
    password  text not null,
    firstname text not null,
    surname   text not null,
    role_id   int  not null,
    constraint Users_Roles_id_fk
        foreign key (role_id) references Roles (id)
);

create table Actors_rates
(
    actors_id   int  not null,
    user_id     int  not null,
    rate        int  not null,
    description text null,
    constraint Actors_rates_Actors_id_fk
        foreign key (actors_id) references Actors (id),
    constraint Actors_rates_Users_id_fk
        foreign key (user_id) references Users (id)
);

create table Directors_rates
(
    director_id int  not null,
    user_id     int  not null,
    rate        int  not null,
    description text null,
    constraint Directors_rates_Directors_id_fk
        foreign key (director_id) references Directors (id),
    constraint Directors_rates_Users_id_fk
        foreign key (user_id) references Users (id)
);

create table Movies_rates
(
    movie_id    int  not null,
    user_id     int  not null,
    rate        int  not null,
    description text null,
    constraint Movies_rates_Movies_id_fk
        foreign key (movie_id) references Movies (id),
    constraint Movies_rates_Users_id_fk
        foreign key (user_id) references Users (id)
);

